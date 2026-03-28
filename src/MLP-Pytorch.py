import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset

from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import StandardScaler

import time

from Set_Processor import ImportData



class PhishingMLP(nn.Module):
    def __init__(self, input_size):
        super(PhishingMLP, self).__init__()
        self.network = nn.Sequential(
            nn.Linear(input_size, 256),
            nn.ReLU(),
            nn.Dropout(0.3),

            nn.Linear(256, 64),
            nn.ReLU(),
            nn.Dropout(0.3),

            nn.Linear(64, 1),
        )

    def forward(self, x):
        return self.network(x)



class PyTorchTrainer:
    def __init__(self, X, y):
        self.X = X
        self.y = y

        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        print(f"PyTorch będzie trenował na: {self.device}")

    def NLP_train(self):
        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=0.3, random_state=42)

        vectorizer = TfidfVectorizer(analyzer='char', ngram_range=(3, 5), max_features=3000)
        X_train_nlp = vectorizer.fit_transform(X_train)
        X_test_nlp = vectorizer.transform(X_test)

        X_train_tensor = torch.tensor(X_train_nlp.toarray(), dtype=torch.float32)
        y_train_tensor = torch.tensor(y_train.values, dtype=torch.float32).view(-1, 1)

        X_test_tensor = torch.tensor(X_test_nlp.toarray(), dtype=torch.float32).to(self.device)
        y_test_tensor = torch.tensor(y_test.values, dtype=torch.float32).view(-1, 1).to(self.device)

        train_dataset = TensorDataset(X_train_tensor, y_train_tensor)
        train_loader = DataLoader(train_dataset, batch_size=128, shuffle=True)

        model = PhishingMLP(input_size=3000).to(self.device)

        criterion = nn.BCEWithLogitsLoss()
        optimizer = optim.Adam(model.parameters(), lr=0.001)

        epochs = 100
        print("\n START-TRENING")

        start_time = time.time()
        for epoch in range(epochs):
            model.train()
            running_loss = 0.0

            for batch_X, batch_y in train_loader:
                batch_X, batch_y = batch_X.to(self.device), batch_y.to(self.device)

                optimizer.zero_grad()

                outputs = model(batch_X)

                loss = criterion(outputs, batch_y)

                loss.backward()
                optimizer.step()

                running_loss += loss.item()

            print(f"Epoka [{epoch + 1}/{epochs}] | Błąd (Loss): {running_loss / len(train_loader):.4f}")

        czas = time.time() - start_time
        print(f"Trening zakończony w {czas:.2f}")


        model.eval()

        with torch.no_grad():
            predictions_raw = model(X_test_tensor)
            predictions = torch.sigmoid(predictions_raw).round().cpu().numpy()
            y_test_numpy = y_test_tensor.cpu().numpy()

        print("\n" + "=" * 50)
        print("RAPORT: PyTorch MLP + NLP (TF-IDF)")
        print("=" * 50)
        print(classification_report(y_test_numpy, predictions))
        print("Macierz Pomyłek:")
        print(confusion_matrix(y_test_numpy, predictions))

    def CECHY_train(self):
        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=0.3, random_state=42)

        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)

        X_train_tensor = torch.tensor(X_train_scaled, dtype=torch.float32)
        y_train_tensor = torch.tensor(y_train.values, dtype=torch.float32).view(-1, 1)

        X_test_tensor = torch.tensor(X_test_scaled, dtype=torch.float32).to(self.device)
        y_test_tensor = torch.tensor(y_test.values, dtype=torch.float32).view(-1, 1).to(self.device)

        train_dataset = TensorDataset(X_train_tensor, y_train_tensor)
        train_loader = DataLoader(train_dataset, batch_size=128, shuffle=True)

        liczba_cech = X_train_scaled.shape[1]

        model = PhishingMLP(input_size=liczba_cech).to(self.device)

        criterion = nn.BCEWithLogitsLoss()
        optimizer = optim.Adam(model.parameters(), lr=0.001)

        epochs = 15
        print("\n START-TRENING")

        start_time = time.time()
        for epoch in range(epochs):
            model.train()
            running_loss = 0.0

            for batch_X, batch_y in train_loader:
                batch_X, batch_y = batch_X.to(self.device), batch_y.to(self.device)

                optimizer.zero_grad()
                outputs = model(batch_X)
                loss = criterion(outputs, batch_y)
                loss.backward()
                optimizer.step()

                running_loss += loss.item()

            print(f"Epoka [{epoch + 1}/{epochs}] | Błąd (Loss): {running_loss / len(train_loader):.4f}")

        czas = time.time() - start_time
        print(f"Trening zakończony w {czas:.2f}")

        model.eval()

        with torch.no_grad():
            predictions_raw = model(X_test_tensor)
            predictions = torch.sigmoid(predictions_raw).round().cpu().numpy()
            y_test_numpy = y_test_tensor.cpu().numpy()

        print("\n" + "=" * 50)
        print("RAPORT: PyTorch MLP + CECHY RĘCZNE")
        print("=" * 50)
        print(classification_report(y_test_numpy, predictions))
        print("Macierz Pomyłek:")
        print(confusion_matrix(y_test_numpy, predictions))


if __name__ == "__main__":
    dane = ImportData()
    #df, X, y = dane.scal_sets()
    X, y = dane.Get_Scalet_sets()

    trener_pt = PyTorchTrainer(X, y)
    trener_pt.NLP_train()
    #trener_pt.CECHY_train()