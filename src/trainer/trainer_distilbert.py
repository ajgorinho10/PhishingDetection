import torch
import joblib
import numpy as np
from torch.utils.data import TensorDataset, DataLoader
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score, accuracy_score, recall_score
from sklearn.metrics import classification_report, confusion_matrix
import torch.nn as nn

# POPRAWKA: Fast zamiast zwykłego Tokenizer — 3-10x szybszy
from transformers import DistilBertTokenizerFast

from trainer import Trainer


class Trainer_DistilBERT(Trainer):
    def __init__(self, model, cfg, data_sets=None):
        super().__init__(model, cfg)
        self.data = data_sets
        self.tokenizer = DistilBertTokenizerFast.from_pretrained(cfg.MODEL_NAME)

    def load_scaler(self):
        self.scaler = joblib.load(self.cfg.SCALER_PATH)

    def get_tokenized_tensors(self, X_data, y_data):
        X_list = X_data.tolist() if hasattr(X_data, 'tolist') else list(X_data)
        encoded = self.tokenizer(
            X_list,
            padding='max_length',
            truncation=True,
            max_length=self.cfg.MAX_LEN,
            return_tensors='pt'
        )
        input_ids      = encoded['input_ids']
        # POPRAWKA: attention_mask musi być zwracana i używana
        attention_mask = encoded['attention_mask']

        if isinstance(y_data, torch.Tensor):
            y_tensor = y_data.clone().detach().to(torch.float32).view(-1, 1)
        else:
            y_arr = y_data.to_numpy() if hasattr(y_data, 'to_numpy') else np.array(y_data)
            y_tensor = torch.tensor(y_arr, dtype=torch.float32).view(-1, 1)

        # POPRAWKA: zwracamy trzy wartości — input_ids, attention_mask, y
        return input_ids, attention_mask, y_tensor

    def get_data_loaders(self, input_ids, attention_mask, y_data, X_features=None, shuffled=False):
        # POPRAWKA: DataLoader teraz zawiera attention_mask jako osobny tensor
        if self.use_features and X_features is not None:
            dataset = TensorDataset(input_ids, attention_mask, X_features, y_data)
        else:
            dataset = TensorDataset(input_ids, attention_mask, y_data)

        return DataLoader(dataset, batch_size=self.cfg.BATCH_SIZE, shuffle=shuffled, drop_last=shuffled)

    # Klasa bazowa Trainer.train() wywołuje _train_epoch_with_features gdy use_features=True.
    # Musimy nadpisać OBE pary metod — bazowe wersje nie znają attention_mask.
    # Dla DistilBERT obie pary robią identycznie (features są obsługiwane wewnątrz
    # pętli przez if self.use_features), więc _with_features deleguje do zwykłej wersji.
    def _train_epoch_with_features(self, data_loader):
        return self._train_epoch(data_loader)

    def _val_epoch_with_features(self, data_loader):
        return self._val_epoch(data_loader)

    # POPRAWKA: nadpisujemy _train_epoch — bazowa wersja nie zna attention_mask
    def _train_epoch(self, data_loader):
        self.model.train()
        running_loss = 0.0

        for batch in data_loader:
            if self.use_features:
                input_ids, attention_mask, features, y = batch
                input_ids      = input_ids.to(self.cfg.DEVICE)
                attention_mask = attention_mask.to(self.cfg.DEVICE)
                features       = features.to(self.cfg.DEVICE)
                y              = y.to(self.cfg.DEVICE)
                output = self.model(input_ids, attention_mask, features)
            else:
                input_ids, attention_mask, y = batch
                input_ids      = input_ids.to(self.cfg.DEVICE)
                attention_mask = attention_mask.to(self.cfg.DEVICE)
                y              = y.to(self.cfg.DEVICE)
                output = self.model(input_ids, attention_mask)

            self.optimizer.zero_grad(set_to_none=True)
            loss = self.loss_f(output.view(-1), y.float().view(-1))
            loss.backward()
            nn.utils.clip_grad_norm_(self.model.parameters(), max_norm=1.0)
            self.optimizer.step()

            if hasattr(self.cfg, 'WARMUP_STEPS'):
                self.scheduler.step()

            running_loss += loss.item()

        return running_loss / len(data_loader)

    # POPRAWKA: nadpisujemy _val_epoch — bazowa wersja nie zna attention_mask
    def _val_epoch(self, data_loader):
        self.model.eval()
        running_loss = 0.0
        all_labels, all_preds = [], []

        with torch.no_grad():
            for batch in data_loader:
                if self.use_features:
                    input_ids, attention_mask, features, y = batch
                    input_ids      = input_ids.to(self.cfg.DEVICE)
                    attention_mask = attention_mask.to(self.cfg.DEVICE)
                    features       = features.to(self.cfg.DEVICE)
                    y              = y.to(self.cfg.DEVICE)
                    output = self.model(input_ids, attention_mask, features)
                else:
                    input_ids, attention_mask, y = batch
                    input_ids      = input_ids.to(self.cfg.DEVICE)
                    attention_mask = attention_mask.to(self.cfg.DEVICE)
                    y              = y.to(self.cfg.DEVICE)
                    output = self.model(input_ids, attention_mask)

                loss = self.loss_f(output.view(-1), y.float().view(-1))
                running_loss += loss.item()
                all_labels.extend(y.cpu().numpy().flatten())
                all_preds.extend(torch.sigmoid(output).squeeze(-1).round().cpu().numpy())

        return {
            'val_loss': running_loss / len(data_loader),
            'f1'      : f1_score      (all_labels, all_preds, zero_division=0),
            'acc'     : accuracy_score(all_labels, all_preds),
            'recal'   : recall_score  (all_labels, all_preds, zero_division=0),
        }

    # POPRAWKA: nadpisujemy evaluate — bazowa wersja nie zna attention_mask
    def evaluate(self, data_loader):
        self.model.load_state_dict(torch.load(self.cfg.PATH, weights_only=True))
        print("Załadowano optymalne wagi do modelu.")
        self.model.to(self.cfg.DEVICE)
        self.model.eval()
        all_preds, all_labels = [], []

        with torch.no_grad():
            for batch in data_loader:
                if self.use_features:
                    input_ids, attention_mask, features, y = batch
                    output = self.model(
                        input_ids.to(self.cfg.DEVICE),
                        attention_mask.to(self.cfg.DEVICE),
                        features.to(self.cfg.DEVICE)
                    )
                else:
                    input_ids, attention_mask, y = batch
                    output = self.model(
                        input_ids.to(self.cfg.DEVICE),
                        attention_mask.to(self.cfg.DEVICE)
                    )
                all_preds.extend(torch.sigmoid(output).squeeze(-1).round().cpu().numpy())
                all_labels.extend(y.numpy().flatten())

        print("\nRaport końcowy:")
        print(classification_report(all_labels, all_preds))
        print(confusion_matrix(all_labels, all_preds))

    def splits_data_to_Train_Val_Test(self):
        X, y = self.data[0], self.data[1]
        X_train, X_tv, y_train, y_tv = train_test_split(X, y, test_size=0.3, random_state=42)
        X_test, X_val, y_test, y_val = train_test_split(X_tv, y_tv, test_size=0.5, random_state=42)

        X_train_features = X_val_features = X_test_features = None

        if self.use_features:
            X_train_features = torch.tensor(
                self.scaler.fit_transform(self.get_data_features(X_train).numpy()), dtype=torch.float32)
            X_val_features   = torch.tensor(
                self.scaler.transform(self.get_data_features(X_val).numpy()),   dtype=torch.float32)
            X_test_features  = torch.tensor(
                self.scaler.transform(self.get_data_features(X_test).numpy()),  dtype=torch.float32)
            joblib.dump(self.scaler, self.cfg.SCALER_PATH)

        train_loader = self.get_data_loaders(*self.get_tokenized_tensors(X_train, y_train), X_train_features, shuffled=True)
        val_loader   = self.get_data_loaders(*self.get_tokenized_tensors(X_val,   y_val),   X_val_features)
        test_loader  = self.get_data_loaders(*self.get_tokenized_tensors(X_test,  y_test),  X_test_features)

        return train_loader, val_loader, test_loader