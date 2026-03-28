import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import numpy as np
import time

from Set_Processor import ImportData


# ==========================================
# 1. ARCHITEKTURA SIECI Z PAMIĘCIĄ (Bi-LSTM)
# ==========================================
class LSTM(nn.Module):
    def __init__(self, vocab_size, embed_dim=64, hidden_dim=128):
        super(LSTM, self).__init__()
        # 1. Zamiana numerów liter na wektory
        self.embedding = nn.Embedding(num_embeddings=vocab_size, embedding_dim=embed_dim)

        # 2. Główny silnik rekurencyjny (Dwukierunkowy)
        # batch_first=True jest kluczowe, by kształty tensorów się zgadzały
        self.lstm = nn.LSTM(input_size=embed_dim, hidden_size=hidden_dim,
                            num_layers=1, batch_first=True, bidirectional=True)

        # Ochrona przed przeuczeniem (Dropout)
        self.dropout = nn.Dropout(0.5)

        # 3. Klasyfikator
        # Mnożymy hidden_dim * 2, ponieważ używamy Bidirectional (mamy dwa stany ukryte do połączenia)
        self.fc = nn.Linear(hidden_dim * 2, 1)

    def forward(self, x):
        # x: [batch, max_len]
        x = self.embedding(x)  # [batch, max_len, embed_dim]

        # Wyjście LSTM składa się z pełnej sekwencji (lstm_out) oraz stanów końcowych (hn, cn)
        lstm_out, (hn, cn) = self.lstm(x)

        # Bierzemy "pamięć" z samego końca czytania (z obu kierunków naraz)
        # hn ma kształt [2, batch, hidden_dim] -> wyciągamy kierunek w przód i w tył
        hidden_last = torch.cat((hn[-2, :, :], hn[-1, :, :]), dim=1)

        x = self.dropout(hidden_last)
        x = self.fc(x)
        return x


# ==========================================
# 2. FUNKCJA TRENUJĄCA
# ==========================================
def train_LSTM_sequence(X_data, y_data):
    print("\n" + "=" * 60)
    print("🚀 TRENOWANIE SIECI REKURENCYJNEJ (Bi-LSTM) NA ZNAKACH")
    print("=" * 60)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"🔥 PyTorch używa akceleratora: {device}")

    # --- KROK 1: Tokenizacja Znakowa i Padding (Zabezpieczona przed duplikatami) ---
    print("\nTokenizacja linków...")
    surowe_znaki = "abcdefghijklmnopqrstuvwxyz0123456789-,;.!?:'\"/\\|_@#$%^&*~`+-=<>()[]{}"
    unikalne_znaki = list(set(surowe_znaki))

    char_to_int = {c: i + 1 for i, c in enumerate(unikalne_znaki)}
    vocab_size = len(char_to_int) + 1
    max_len = 100

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

    # --- KROK 3: Tensory i DataLoaders ---
    print("Ładowanie danych na GPU...")
    X_train_tensor = torch.tensor(X_train, dtype=torch.long)
    y_train_tensor = torch.tensor(y_train.values, dtype=torch.float32).view(-1, 1)

    X_test_tensor = torch.tensor(X_test, dtype=torch.long)
    y_test_tensor = torch.tensor(y_test.values, dtype=torch.float32).view(-1, 1)

    train_dataset = TensorDataset(X_train_tensor, y_train_tensor)
    train_loader = DataLoader(train_dataset, batch_size=128, shuffle=True)

    test_dataset = TensorDataset(X_test_tensor, y_test_tensor)
    test_loader = DataLoader(test_dataset, batch_size=512, shuffle=False)  # Większy batch dla testów!

    # --- KROK 4: Inicjalizacja modelu ---
    model = LSTM(vocab_size=vocab_size).to(device)
    criterion = nn.BCEWithLogitsLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    # --- KROK 5: Pętla ucząca ---
    epochs = 15
    print("\nRozpoczynamy trening sieci LSTM...")
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

    # --- KROK 6: Ewaluacja chroniąca VRAM ---
    print("\nTestowanie modelu LSTM w paczkach...")
    model.eval()

    wszystkie_predykcje = []
    wszystkie_etykiety = []

    with torch.no_grad():
        for batch_X, batch_y in test_loader:
            batch_X = batch_X.to(device)

            predictions_raw = model(batch_X)
            predictions = torch.sigmoid(predictions_raw).round().cpu().numpy()

            wszystkie_predykcje.extend(predictions)
            wszystkie_etykiety.extend(batch_y.numpy())

    print("\n" + "=" * 50)
    print("RAPORT: PyTorch Bi-LSTM (Znakowa tokenizacja)")
    print("=" * 50)
    print(classification_report(wszystkie_etykiety, wszystkie_predykcje))
    print("Macierz Pomyłek:")
    print(confusion_matrix(wszystkie_etykiety, wszystkie_predykcje))

# Wywołanie:
if __name__ == "__main__":
    X, y = ImportData().Get_Scalet_sets()
    train_LSTM_sequence(X, y)