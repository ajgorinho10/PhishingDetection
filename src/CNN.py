import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import numpy as np
import time

from Set_Processor import ImportData


class CNN(nn.Module):
    def __init__(self, vocab_size, embed_dim=64, max_len=100):
        super(CNN, self).__init__()
        # Warstwa osadzeń - zamienia numery liter na wielowymiarowe wektory
        self.embedding = nn.Embedding(num_embeddings=vocab_size, embedding_dim=embed_dim)

        # Skaner konwolucyjny (Skanuje zbitki po 3 litery naraz)
        self.conv1 = nn.Conv1d(in_channels=embed_dim, out_channels=128, kernel_size=3, padding=1)
        self.relu = nn.ReLU()
        # Zmniejszanie wymiarowości (wyciąganie najważniejszych cech)
        self.pool = nn.MaxPool1d(kernel_size=2)

        # Ochrona przed przeuczeniem
        self.dropout = nn.Dropout(0.3)

        # Klasyfikator końcowy (MLP na końcu sieci)
        self.fc = nn.Linear(128 * (max_len // 2), 1)

    def forward(self, x):
        x = self.embedding(x)  # Kształt: [batch, max_len, embed_dim]
        x = x.permute(0, 2, 1)  # Wymagane przez Conv1d: [batch, kanały, max_len]

        x = self.conv1(x)
        x = self.relu(x)
        x = self.pool(x)

        x = torch.flatten(x, 1)  # Spłaszczanie danych przed warstwą liniową
        x = self.dropout(x)
        x = self.fc(x)
        return x


# ==========================================
# 2. FUNKCJA TRENUJĄCA I PRZYGOTOWUJĄCA DANE
# ==========================================
def train_CNN_sequence(X_data, y_data):
    print("\n" + "=" * 60)
    print("🚀 TRENOWANIE SIECI KONWOLUCYJNEJ (CNN 1D) NA SEKWENCJACH ZNAKÓW")
    print("=" * 60)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"🔥 PyTorch używa akceleratora: {device}")

    # --- KROK 1: Tokenizacja Znakowa i Padding ---
    print("\nBudowanie słownika znaków i tokenizacja linków...")

    # Kuloodporne tworzenie słownika (set() usuwa ewentualne duplikaty znaków)
    surowe_znaki = "abcdefghijklmnopqrstuvwxyz0123456789-,;.!?:'\"/\\|_@#$%^&*~`+-=<>()[]{}"
    unikalne_znaki = list(set(surowe_znaki))  # Pozbywamy się duplikatów

    char_to_int = {c: i + 1 for i, c in enumerate(unikalne_znaki)}
    vocab_size = len(char_to_int) + 1
    max_len = 300

    X_sequences = []
    for url in X_data:
        seq = [char_to_int.get(c.lower(), 0) for c in str(url)]
        seq = seq[:max_len]
        if len(seq) < max_len:
            seq += [0] * (max_len - len(seq))
        X_sequences.append(seq)

    X_seq_array = np.array(X_sequences)

    # --- KROK 2: Podział danych ---
    X_train, X_test, y_train, y_test = train_test_split(X_seq_array, y_data, test_size=0.3, random_state=42)

    # --- KROK 3: Zamiana na Tensory PyTorch ---
    print("Wysyłanie danych na kartę graficzną...")
    X_train_tensor = torch.tensor(X_train, dtype=torch.long)  # Zauważ dtype=torch.long! Wymagane dla Embeddingów
    y_train_tensor = torch.tensor(y_train.values, dtype=torch.float32).view(-1, 1)

    X_test_tensor = torch.tensor(X_test, dtype=torch.long).to(device)
    y_test_tensor = torch.tensor(y_test.values, dtype=torch.float32).view(-1, 1).to(device)

    train_dataset = TensorDataset(X_train_tensor, y_train_tensor)
    train_loader = DataLoader(train_dataset, batch_size=128, shuffle=True)

    # --- KROK 4: Inicjalizacja modelu ---
    model = CNN(vocab_size=vocab_size, max_len=max_len).to(device)
    criterion = nn.BCEWithLogitsLoss()
    #optimizer = optim.Adam(model.parameters(), lr=0.002)
    optimizer = optim.SGD(model.parameters(),lr=0.01,momentum=0.9)

    # --- KROK 5: Pętla ucząca ---
    epochs = 10
    print("\nRozpoczynamy trening sieci CNN...")
    start_time = time.time()

    for epoch in range(epochs):
        model.train()
        running_loss = 0.0

        for batch_X, batch_y in train_loader:
            batch_X, batch_y = batch_X.to(device), batch_y.to(device)

            optimizer.zero_grad()
            outputs = model(batch_X)
            loss = criterion(outputs, batch_y)
            loss.backward()
            optimizer.step()

            running_loss += loss.item()

        print(f"Epoka [{epoch + 1}/{epochs}] | Błąd (Loss): {running_loss / len(train_loader):.4f}")

    czas = time.time() - start_time
    print(f"✅ Trening zakończony w {czas:.2f} sekund!")

    # --- KROK 6: Ewaluacja ---
    print("\nTestowanie modelu CNN w paczkach (ochrona VRAM)...")
    model.eval()

    # 1. Tworzymy DataLoader również dla zbioru testowego!
    # Używamy większego batch_size (np. 512), bo w fazie testów nie liczymy gradientów, więc zużywa mniej pamięci
    test_dataset = TensorDataset(X_test_tensor, y_test_tensor)
    test_loader = DataLoader(test_dataset, batch_size=512, shuffle=False)

    wszystkie_predykcje = []
    wszystkie_etykiety = []

    with torch.no_grad():
        for batch_X, batch_y in test_loader:
            # Wysyłamy TYLKO paczkę 512 linków na kartę graficzną
            batch_X = batch_X.to(device)

            # Predykcja dla małej paczki
            predictions_raw = model(batch_X)
            predictions = torch.sigmoid(predictions_raw).round().cpu().numpy()

            # Zbieramy wyniki do wspólnej listy
            wszystkie_predykcje.extend(predictions)
            wszystkie_etykiety.extend(batch_y.cpu().numpy())

    print("\n" + "=" * 50)
    print("RAPORT: PyTorch CNN 1D (Znakowa tokenizacja)")
    print("=" * 50)
    print(classification_report(wszystkie_etykiety, wszystkie_predykcje))
    print("Macierz Pomyłek:")
    print(confusion_matrix(wszystkie_etykiety, wszystkie_predykcje))


if __name__ == "__main__":
    d = ImportData()
    d.Import_set_3()
    X, y = d.Get_NLP()
    train_CNN_sequence(X, y)