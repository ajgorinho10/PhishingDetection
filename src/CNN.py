import time

import torch
from sklearn.metrics import classification_report, confusion_matrix
from torch import nn
import torch.nn.functional as F
import torchvision

import numpy as np

from sklearn.model_selection import train_test_split
from torch.utils.data import TensorDataset, DataLoader

from Set_Processor import ImportSet1, ImportData


class CNN(nn.Module):
    def __init__(self, embed_dim=16, max_len=100, epoch = 5):
        super(CNN, self).__init__()

        self.vocab_size = None
        self.embed_dim = embed_dim
        self.max_len = max_len
        self.slownik = None
        self.epoch = epoch

        self.embed = None

        self.conv1 = nn.Conv1d(in_channels=embed_dim, out_channels=embed_dim * 2, kernel_size=2, padding='same')
        self.conv2 = nn.Conv1d(in_channels=embed_dim * 2, out_channels=embed_dim * 4, kernel_size=3, padding='same')
        self.conv3 = nn.Conv1d(in_channels=embed_dim * 4, out_channels=embed_dim * 8, kernel_size=5, padding='same')
        self.conv4 = nn.Conv1d(in_channels=embed_dim * 8, out_channels=embed_dim * 16, kernel_size=7, padding='same')

        self.pool = nn.MaxPool1d(kernel_size=2)
        self.dropout = nn.Dropout(p=0.3)
        self.relu = nn.ReLU()
        self.gelu = nn.GELU()

        linearInput = embed_dim * 16 * (self.max_len//4)
        self.linear1 = nn.Linear(in_features=linearInput, out_features=linearInput//8)
        self.linear2 = nn.Linear(in_features=linearInput//8, out_features=1)


        self.sigmoid = nn.Sigmoid()

    def forward(self,x):
        x = self.embed(x)
        x = x.permute(0,2,1)

        #KONWULENCYJNA - 1
        x = self.conv1(x)
        #x = self.relu(x)
        x = self.gelu(x)

        #KONWULENCYJNA - 2 po niej dropout i pool
        x = self.conv2(x)
        #x = self.relu(x)
        x = self.gelu(x)

        x = self.pool(x)
        x = self.dropout(x)

        #KONWULENCYJNA - 3
        x = self.conv3(x)
        #x = self.relu(x)
        x = self.gelu(x)

        #KONWULENCYJNA - 4 po niej dropout i pool
        x = self.conv4(x)
        #x = self.relu(x)
        x = self.gelu(x)

        x = self.pool(x)
        x = self.dropout(x)

        #MLP - dwie warstwy po pierwszej dropout
        x = torch.flatten(x, 1)
        x = self.linear1(x)
        #x = self.relu(x)
        x = self.gelu(x)
        x = self.dropout(x)

        x = self.linear2(x)



        x = self.sigmoid(x)
        return x


    def tokenize(self, data):
        surowe_znaki = "abcdefghijklmnopqrstuvwxyz0123456789-,;.!?:'\"/\\|_@#$%^&*~`+-=<>()[]{}"
        unikalne_znaki = list(set(surowe_znaki))

        char_to_int = {c: i+1 for i, c in enumerate(sorted(unikalne_znaki))} if self.slownik is None else self.slownik
        self.slownik = char_to_int

        self.vocab_size = len(unikalne_znaki) + 1
        self.embed = nn.Embedding(self.vocab_size, self.embed_dim)

        X_sequences = []
        for url in data:
            seq = [char_to_int.get(c.lower(),0) for c in url]

            seq = seq[:self.max_len]

            if len(seq) < self.max_len:
                seq += [0]* (self.max_len - len(seq))
            X_sequences.append(seq)

        return X_sequences

    def train_model(self, X_data, y_data):
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        print("[Device]:", device)

        print("[Przygotowywanie danych]: Tokenizacja, podział danych")
        X_tokenized = self.tokenize(X_data)

        X_train, X_test, y_train, y_test = train_test_split(X_tokenized, y_data, test_size=0.3, random_state=42)

        print("[Przygotowywanie danych]: Zamiana danych na tensory PyTorch")

        X_train_tensor = torch.tensor(X_train,dtype=torch.long)
        X_test_tensor = torch.tensor(X_test,dtype=torch.long).to(device)

        y_train_tensor = torch.tensor(y_train.values, dtype=torch.float32).view(-1,1)
        y_test_tensor = torch.tensor(y_test.values, dtype=torch.float32).view(-1,1).to(device)

        train_dataset = TensorDataset(X_train_tensor, y_train_tensor)
        train_loader = DataLoader(train_dataset, batch_size=128, shuffle=True)

        print("[Przygotowywanie danych]: Zakończone !")

        print("[Trening modelu]: Inicjalizacja modelu")
        self.to(device)
        #optimizer = torch.optim.Adam(self.parameters(), lr=0.001)
        optimizer = torch.optim.AdamW(self.parameters(), lr=0.001)
        criterion = nn.BCELoss()

        start_time = time.time()
        print("[Trening modelu]: Rozpoczynanie treningu")
        for epoch in range(self.epoch):
            self.train()
            running_loss = 0.0

            for batch_X, batch_y in train_loader:
                batch_X, batch_y = batch_X.to(device), batch_y.to(device)

                optimizer.zero_grad()
                output = self(batch_X)
                loss = criterion(output, batch_y)
                loss.backward()
                optimizer.step()

                running_loss += loss.item()

            print(f"Epoch {epoch+1}/{self.epoch} || loss: {running_loss/len(train_loader):.4f}")

        czas = time.time() - start_time
        print(f"[Trening modelu]: Trening zakończony w {czas:.2f}s")

        print(f"[Wyniki]: ...")
        self.eval()
        test_dataset = TensorDataset(X_test_tensor, y_test_tensor)
        test_loader = DataLoader(test_dataset, batch_size=512, shuffle=False)

        wszystkie_predykcje = []
        wszystkie_etykiety = []

        with torch.no_grad():
            for batch_X, batch_y in test_loader:
                batch_X = batch_X.to(device)

                pred_raw = self(batch_X)
                pred = pred_raw.round().cpu().numpy()

                wszystkie_predykcje.extend(pred)
                wszystkie_etykiety.extend(batch_y.cpu().numpy())

        print("\n" + "=" * 50)
        print("RAPORT: PyTorch CNN 1D (Znakowa tokenizacja)")
        print("=" * 50)
        print(classification_report(wszystkie_etykiety, wszystkie_predykcje))
        print("Macierz Pomyłek:")
        print(confusion_matrix(wszystkie_etykiety, wszystkie_predykcje))




if __name__ == "__main__":
    data = ImportData()
    data.Import_set_3()
    X, y = data.Get_NLP()

    CNN = CNN(embed_dim=64, max_len=100,epoch=10)
    CNN.train_model(X,y)


