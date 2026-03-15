import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
from sklearn.metrics import classification_report, confusion_matrix, f1_score
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import time

from importData import ImportData


# 1. DEFINICJA ARCHITEKTURY SIECI NEURONOWEJ
class PhishingMLP(nn.Module):
    def __init__(self, input_size):
        super(PhishingMLP, self).__init__()
        # ZASADA LEJKA: input -> 256 -> 64 -> 1
        self.network = nn.Sequential(
            nn.Linear(input_size, 256),
            nn.ReLU(),
            nn.Dropout(0.3),  # Wyłączamy losowo 30% neuronów (ochrona przed przeuczeniem!)

            nn.Linear(256, 64),
            nn.ReLU(),
            nn.Dropout(0.3),

            nn.Linear(64, 1)  # 1 wyjście (0 lub 1)
        )

    def forward(self, x):
        return self.network(x)


# 2. GŁÓWNA KLASA TRENUJĄCA
class PyTorchTrainer:
    def __init__(self, X, y):
        self.X = X
        self.y = y
        # Sprawdzamy, czy masz dostępną kartę NVIDIA (CUDA)
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        print(f"🔥 PyTorch będzie trenował na: {self.device}")

    def train_and_evaluate(self):
        print("\nPrzygotowywanie danych (TF-IDF)...")
        # 1. Podział i Wektoryzacja
        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=0.3, random_state=42)

        vectorizer = TfidfVectorizer(analyzer='char', ngram_range=(3, 5), max_features=3000)
        X_train_nlp = vectorizer.fit_transform(X_train)
        X_test_nlp = vectorizer.transform(X_test)

        print("Zamiana macierzy rzadkiej na tensory PyTorch...")
        # PyTorch potrzebuje gęstych tensorów. Zamieniamy z TF-IDF i wysyłamy na GPU!
        X_train_tensor = torch.tensor(X_train_nlp.toarray(), dtype=torch.float32)
        y_train_tensor = torch.tensor(y_train.values, dtype=torch.float32).view(-1, 1)

        X_test_tensor = torch.tensor(X_test_nlp.toarray(), dtype=torch.float32).to(self.device)
        y_test_tensor = torch.tensor(y_test.values, dtype=torch.float32).view(-1, 1).to(self.device)

        # DataLoader - pakuje dane w "paczki" (batche) po 128 sztuk, żeby nie zapchać RAMu karty
        train_dataset = TensorDataset(X_train_tensor, y_train_tensor)
        train_loader = DataLoader(train_dataset, batch_size=128, shuffle=True)

        # 2. Inicjalizacja Modelu, Funkcji Straty i Optymalizatora
        model = PhishingMLP(input_size=3000).to(self.device)

        # BCEWithLogitsLoss to idealna funkcja dla klasyfikacji 0/1 (zawiera wbudowanego Sigmoida)
        criterion = nn.BCEWithLogitsLoss()
        # Adam to nasz optymalizator (odpowiednik 'adam' ze sklearn)
        optimizer = optim.Adam(model.parameters(), lr=0.001)

        # 3. PĘTLA UCZĄCA (Training Loop)
        epochs = 15  # W PyTorchu 15-20 epok z reguły wystarcza dla takich danych
        print("\n🚀 Rozpoczynamy trening na GPU (PyTorch)!")

        start_time = time.time()
        for epoch in range(epochs):
            model.train()  # Tryb uczenia (włącza Dropout)
            running_loss = 0.0

            for batch_X, batch_y in train_loader:
                # Wysłanie paczki na GPU
                batch_X, batch_y = batch_X.to(self.device), batch_y.to(self.device)

                # Czyszczenie starych gradientów
                optimizer.zero_grad()

                # Predykcja (Forward pass)
                outputs = model(batch_X)

                # Obliczenie błędu (Loss)
                loss = criterion(outputs, batch_y)

                # Poprawa wag (Backward pass)
                loss.backward()
                optimizer.step()

                running_loss += loss.item()

            # Co epokę wypisujemy średni błąd
            print(f"Epoka [{epoch + 1}/{epochs}] | Błąd (Loss): {running_loss / len(train_loader):.4f}")

        czas = time.time() - start_time
        print(f"✅ Trening zakończony w {czas:.2f} sekund!")

        # 4. OCENA MODELU
        print("\nTestowanie modelu na zbiorze testowym...")
        model.eval()  # Tryb testowy (WYŁĄCZA Dropout, bo teraz chcemy pewnych odpowiedzi)

        with torch.no_grad():  # Wyłączamy śledzenie gradientów na czas testów (oszczędza pamięć)
            predictions_raw = model(X_test_tensor)
            # Zamiana wyników na 0 lub 1 (Sigmoid i próg 0.5)
            predictions = torch.sigmoid(predictions_raw).round().cpu().numpy()
            y_test_numpy = y_test_tensor.cpu().numpy()

        print("\n" + "=" * 50)
        print("RAPORT: PyTorch Custom MLP + NLP (TF-IDF)")
        print("=" * 50)
        print(classification_report(y_test_numpy, predictions))
        print("Macierz Pomyłek:")
        print(confusion_matrix(y_test_numpy, predictions))

if __name__ == "__main__":
    # 1. Pobieramy dane (z Twojej już napisanej, świetnej klasy)
    dane = ImportData()
    dane.Import_set_2()
    X, y = dane.Get_NLP()

    # 2. Odpalamy PyTorcha!
    trener_pt = PyTorchTrainer(X, y)
    trener_pt.train_and_evaluate()