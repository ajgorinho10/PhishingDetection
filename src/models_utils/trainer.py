import numpy as np
import matplotlib.pyplot as plt

import torch
from torch.utils.data import TensorDataset, DataLoader
import torch.nn as nn
import torch.nn.functional as F

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    classification_report, 
    confusion_matrix, 
    f1_score, 
    accuracy_score, 
    recall_score)


from .tokenization import CharTokenizer
from .early_stopping import EarlyStopping


class Trainer:
    
    def __init__(self, model, cfg, data_sets = None):
        self.model = model
        self.model.to(cfg.DEVICE)
        self.data = data_sets
        self.cfg = cfg
        
        self.optimizer = torch.optim.AdamW(self.model.parameters(), lr=cfg.LR)
        self.loss_f = nn.BCEWithLogitsLoss()
        self.early_stopping = EarlyStopping(patience=cfg.PATIENCE, min_delta=0.001, path = cfg.PATH)
        self.tokenizer = CharTokenizer()
        
        self.history = {'train_loss': [], 'val_loss': [], 'f1': [], 'acc': [], 'recal': []}
         
     
    @torch.no_grad()
    def evaluate(self, valDataLoader):
        self.model.load_state_dict(torch.load(self.cfg.PATH))
        print("Załadowano optymalne wagi do modelu.")
        
        wszystkie_predykcje = []
        wszystkie_etykiety = []
        
        self.model.to(self.cfg.DEVICE)
        self.model.eval()

        for batch_X, batch_y in valDataLoader:
            batch_X, batch_y = batch_X.to(self.cfg.DEVICE), batch_y.to(self.cfg.DEVICE)
            output_raw = self.model(batch_X)
            output = torch.sigmoid(output_raw).round().cpu().numpy()
                
            wszystkie_predykcje.extend(output)
            wszystkie_etykiety.extend(batch_y.cpu().numpy())
                
        print("\nRaport końcowy:")
        print(classification_report(wszystkie_etykiety, wszystkie_predykcje))
        print(confusion_matrix(wszystkie_etykiety, wszystkie_predykcje))
              
              
    def get_tokenized_tensors(self, X_data, y_data):   
        X_tensor = torch.tensor(self.tokenizer.encode_dataset(X_data), dtype=torch.long)
        y_tensor = torch.tensor(y_data.values,dtype=torch.float32).view(-1,1)
        
        return X_tensor, y_tensor
    
    
    def get_data_loaders(self, X_data, y_data, shuffled = False):
        dataset = TensorDataset(X_data, y_data)
        dataloader = DataLoader(dataset, batch_size=self.cfg.BATCH_SIZE, shuffle = shuffled)
        
        return dataloader
    
    
    def splits_data_to_Train_Val_Test(self):
        X, y = self.data[0], self.data[1]
        
        #   len(data) = 6 000 000
        #        test = 3 000 000 
        #       train = 1 500 000
        #         val = 1 500 000
        
        X_train, X_test_val, y_train, y_test_val = train_test_split(X, y, test_size=0.3, random_state=42)
        X_test, X_val, y_test, y_val           = train_test_split(X_test_val, y_test_val, test_size=0.5, random_state=42)
         
        train_loader    = self.get_data_loaders(*self.get_tokenized_tensors(X_train, y_train), shuffled = True)
        val_loader      = self.get_data_loaders(*self.get_tokenized_tensors(X_val, y_val))
        test_loader     = self.get_data_loaders(*self.get_tokenized_tensors(X_test, y_test))
        
        return train_loader, val_loader, test_loader
    
    
    def _train_epoch(self, data_loader):    
        self.model.train()
        running_train_loss = 0.0
            
        for batch_X, batch_y in data_loader:
            batch_X, batch_y = batch_X.to(self.cfg.DEVICE), batch_y.to(self.cfg.DEVICE)
                
            self.optimizer.zero_grad(set_to_none=True)
            output = self.model(batch_X)
            loss = self.loss_f(output, batch_y)
            loss.backward()
            self.optimizer.step()
                
            running_train_loss += loss.item()
                
        return running_train_loss / len(data_loader)

            
    def _val_epoch(self, data_loader):
        self.model.eval()
        running_val_loss = 0.0
            
        running_labels = []
        running_predicts = []
        metrics = {}
                
        with torch.no_grad():
            for batch_X, batch_y in data_loader:
                batch_X, batch_y = batch_X.to(self.cfg.DEVICE), batch_y.to(self.cfg.DEVICE)
                output = self.model(batch_X)
                loss = self.loss_f(output, batch_y)
                running_val_loss += loss.item()

                running_labels.extend(batch_y.cpu().numpy().flatten())
                running_predicts.extend(torch.sigmoid(output).squeeze(-1).round().cpu().numpy())
                        
            metrics['val_loss'] = running_val_loss / len(data_loader)
            metrics['f1']       = f1_score      (running_labels,running_predicts, zero_division = 0)
            metrics['acc']      = accuracy_score(running_labels,running_predicts)
            metrics['recal']    = recall_score  (running_labels,running_predicts, zero_division = 0)
                
            return metrics
        
      
    def train(self): 
        train_loader, val_loader, test_loader = self.splits_data_to_Train_Val_Test()

        for epoch in range(self.cfg.EPOCHS):
            avg_train_loss  = self._train_epoch(train_loader)
            metrics         = self._val_epoch(val_loader)
            
            avg_val_loss = metrics['val_loss']
            
            self.history['train_loss'].append(avg_train_loss)
            self.history['val_loss'].append(avg_val_loss)
            self.history['f1'].append(metrics['f1'])
            self.history['acc'].append(metrics['acc'])
            self.history['recal'].append(metrics['recal'])
            
            print(
                          f"Epoka: [{epoch+1}/{self.cfg.EPOCHS}]",
                  f" | Train Loss: {avg_train_loss  :.4f}",
                    f" | Val Loss: {avg_val_loss    :.4f}",
                      f" | Val F1: {metrics['f1']   :.4f}",
                     f" | Val Acc: {metrics['acc']  :.4f}",
                   f" | Val Recal: {metrics['recal']:.4f}"
            )
            
            self.early_stopping(avg_val_loss, self.model)
            if self.early_stopping.early_stop:
                print(f"Zatrzymano trening wcześnie w epoce {epoch+1}. Brak poprawy funkcji straty.")
                break
                
        self.evaluate(test_loader)
        #self.plot_history()
        
        
    def plot_history(self):
        epoki = range(1, len(self.history['train_loss']) + 1)
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        
        # Wykres 1: Funkcja straty (Loss)
        ax1.plot(epoki, self.history['train_loss'], label='Train Loss', marker='o')
        ax1.plot(epoki, self.history['val_loss'], label='Val Loss', marker='o')
        ax1.set_title('Zmiana funkcji straty')
        ax1.set_xlabel('Epoka')
        ax1.set_ylabel('Loss')
        ax1.grid(True, linestyle='--', alpha=0.7)
        ax1.legend()
        
        # Wykres 2: Metryki klasyfikacji
        ax2.plot(epoki, self.history['f1'], label='Val F1', marker='s')
        ax2.plot(epoki, self.history['acc'], label='Val Acc', marker='s')
        ax2.plot(epoki, self.history['recal'], label='Val Recall', marker='s')
        ax2.set_title('Metryki walidacyjne')
        ax2.set_xlabel('Epoka')
        ax2.set_ylabel('Wartość')
        ax2.grid(True, linestyle='--', alpha=0.7)
        ax2.legend()
        
        plt.tight_layout()
        plt.show() 
