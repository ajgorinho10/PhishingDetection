"""
Klasyfikator URL phishingowych — CNN + Bi-LSTM + Attention
PyTorch | Char-level tokenizacja | Cechy ręczne (hand-crafted)

Autor: wygenerowano automatycznie
Wymagania: torch, numpy, scikit-learn, pandas, tqdm
    pip install torch numpy scikit-learn pandas tqdm
"""

import re
import math
import string
from collections import Counter
from typing import List, Tuple, Dict, Optional

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader
from sklearn.metrics import (
    accuracy_score, f1_score, roc_auc_score,
    classification_report, confusion_matrix
)
from sklearn.model_selection import train_test_split


# ─────────────────────────────────────────────
#  1. KONFIGURACJA
# ─────────────────────────────────────────────

class Config:
    # Tokenizacja
    MAX_LEN       = 200          # max długość URL (znaki)
    VOCAB_SIZE    = 100          # 96 ASCII + padding + unk + special
    PAD_IDX       = 0
    UNK_IDX       = 1

    # Model
    EMBED_DIM     = 128
    CNN_FILTERS   = 256
    CNN_KERNELS   = [3, 5]       # rozmiary filtrów
    LSTM_UNITS    = 128          # wyjście = 128*2 (bi-directional)
    ATTN_DIM      = 128
    DENSE_DIM     = 256
    DROPOUT       = 0.4

    # Cechy ręczne (hand-crafted features)
    N_HAND_FEATS  = 10

    # Trening
    BATCH_SIZE    = 512
    EPOCHS        = 1
    LR            = 1e-3
    LR_MIN        = 1e-5
    WEIGHT_DECAY  = 1e-4
    PATIENCE      = 5            # early stopping
    LABEL_SMOOTH  = 0.05

    DEVICE = "cuda" if torch.cuda.is_available() else "cpu"


cfg = Config()


# ─────────────────────────────────────────────
#  2. TOKENIZACJA NA POZIOMIE ZNAKÓW
# ─────────────────────────────────────────────

class CharTokenizer:
    """
    Mapuje każdy znak URL-a na indeks.
    Alfabet: ASCII printable (32-127) + PAD + UNK.
    """
    def __init__(self, max_len: int = cfg.MAX_LEN):
        self.max_len = max_len
        # Indeksy 0 i 1 zarezerwowane dla PAD i UNK
        chars = list(string.printable)  # 100 znaków
        self.char2idx: Dict[str, int] = {
            c: i + 2 for i, c in enumerate(chars)
        }
        self.vocab_size = len(chars) + 2  # +PAD +UNK

    def encode(self, url: str) -> List[int]:
        """URL → lista indeksów, obcięta/dopełniona do max_len."""
        url = url[:self.max_len]
        ids = [self.char2idx.get(c, cfg.UNK_IDX) for c in url]
        # padding po prawej
        ids += [cfg.PAD_IDX] * (self.max_len - len(ids))
        return ids


# ─────────────────────────────────────────────
#  3. CECHY RĘCZNE (HAND-CRAFTED FEATURES)
# ─────────────────────────────────────────────

# Popularne marki, wobec których liczmy podobieństwo
BRAND_NAMES = [
    "paypal", "google", "amazon", "microsoft", "apple",
    "facebook", "netflix", "instagram", "twitter", "linkedin",
]

def levenshtein(a: str, b: str) -> int:
    """Odległość edycyjna Levenshteina."""
    if len(a) < len(b):
        return levenshtein(b, a)
    if len(b) == 0:
        return len(a)
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a):
        curr = [i + 1]
        for j, cb in enumerate(b):
            curr.append(min(prev[j+1]+1, curr[j]+1, prev[j]+(ca != cb)))
        prev = curr
    return prev[-1]

def shannon_entropy(s: str) -> float:
    """Entropia Shannona ciągu znaków (mierzy chaotyczność)."""
    if not s:
        return 0.0
    counts = Counter(s)
    n = len(s)
    return -sum((c/n) * math.log2(c/n) for c in counts.values())

def extract_features(url: str) -> List[float]:
    """
    Zwraca wektor 10 cech numerycznych dla pojedynczego URL-a.

    Cechy:
        0  długość URL (znormalizowana przez max_len)
        1  liczba subdomen (kropki w hostname)
        2  flaga: IP zamiast domeny (0/1)
        3  entropia Shannona całego URL-a
        4  udział cyfr w URL-u
        5  udział znaków specjalnych (@, -, _, ~, %, =, &, ?)
        6  liczba tokenów ścieżki (/)
        7  flaga: HTTPS (0/1)
        8  min. odległość Levenshteina do listy marek (znorm.)
        9  długość domeny głównej (znorm.)
    """
    url_lower = url.lower().strip()

    # Wyciągnij hostname i ścieżkę
    try:
        proto_split = url_lower.split("://", 1)
        is_https = float(proto_split[0] == "https")
        rest = proto_split[1] if len(proto_split) > 1 else url_lower
        hostname = rest.split("/")[0].split("?")[0]
        path_tokens = len(rest.split("/"))
    except Exception:
        is_https = 0.0
        hostname = url_lower
        path_tokens = 1

    # IP
    ip_pattern = re.compile(
        r"^(\d{1,3}\.){3}\d{1,3}(:\d+)?$"
    )
    has_ip = float(bool(ip_pattern.match(hostname)))

    # Domena główna (ostatnie 2 segmenty po kropce)
    parts = hostname.split(".")
    domain = parts[-2] if len(parts) >= 2 else hostname
    num_subdomains = max(0, len(parts) - 2)

    # Min Levenshtein do brand names
    min_lev = min(levenshtein(domain, b) for b in BRAND_NAMES)
    min_lev_norm = min_lev / max(len(domain), 1)

    # Udział cyfr
    digit_ratio = sum(c.isdigit() for c in url_lower) / max(len(url_lower), 1)

    # Udział znaków specjalnych
    special_chars = set("@-_~%=&?")
    special_ratio = sum(c in special_chars for c in url_lower) / max(len(url_lower), 1)

    return [
        len(url_lower) / cfg.MAX_LEN,            # 0
        num_subdomains / 10.0,                    # 1
        has_ip,                                   # 2
        shannon_entropy(url_lower) / 6.0,         # 3 (max ~6 bit)
        digit_ratio,                              # 4
        special_ratio,                            # 5
        min(path_tokens, 20) / 20.0,              # 6
        is_https,                                 # 7
        min_lev_norm,                             # 8
        len(domain) / 50.0,                       # 9
    ]


# ─────────────────────────────────────────────
#  4. DATASET
# ─────────────────────────────────────────────

class URLDataset(Dataset):
    """
    Dataset przyjmujący listy URL-i i etykiet.

    Args:
        urls:    lista ciągów URL
        labels:  lista 0/1 (0=bezpieczny, 1=phishing)
        tokenizer: instancja CharTokenizer
    """
    def __init__(
        self,
        urls: List[str],
        labels: List[int],
        tokenizer: CharTokenizer,
    ):
        self.tokenizer = tokenizer
        self.urls = urls
        self.labels = labels

    def __len__(self) -> int:
        return len(self.urls)

    def __getitem__(self, idx: int) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
        url = self.urls[idx]
        ids      = torch.tensor(self.tokenizer.encode(url), dtype=torch.long)
        feats    = torch.tensor(extract_features(url), dtype=torch.float32)
        label    = torch.tensor(self.labels[idx], dtype=torch.float32)
        return ids, feats, label


# ─────────────────────────────────────────────
#  5. MODEL: CNN + Bi-LSTM + ATTENTION
# ─────────────────────────────────────────────

class ScaledDotAttention(nn.Module):
    """
    Self-attention: ważone sumowanie ukrytych stanów LSTM.

    Wejście: (B, T, H)  — batch, czas, wymiar
    Wyjście: (B, H)     — kontekstowy wektor dla całego URL-a
    """
    def __init__(self, hidden_dim: int, attn_dim: int):
        super().__init__()
        self.W = nn.Linear(hidden_dim, attn_dim, bias=False)
        self.v = nn.Linear(attn_dim, 1, bias=False)

    def forward(
        self,
        hidden: torch.Tensor,                    # (B, T, H)
        mask: Optional[torch.Tensor] = None      # (B, T) bool
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        # Wylicz energię
        energy = self.v(torch.tanh(self.W(hidden)))  # (B, T, 1)
        energy = energy.squeeze(-1)                  # (B, T)
        if mask is not None:
            energy = energy.masked_fill(mask, float("-inf"))
        weights = F.softmax(energy, dim=-1)          # (B, T)
        context = torch.bmm(weights.unsqueeze(1), hidden).squeeze(1)  # (B, H)
        return context, weights


class PhishingClassifier(nn.Module):
    """
    Główna architektura: CNN 1D → Bi-LSTM → Attention → Dense → Sigmoid

    Dodatkowo do gęstej warstwy doklejane są cechy hand-crafted.
    """
    def __init__(self, vocab_size: int = cfg.VOCAB_SIZE, cfg: Config = cfg):
        super().__init__()

        # ── Embedding ──────────────────────────────────────────
        self.embedding = nn.Embedding(
            num_embeddings=vocab_size,
            embedding_dim=cfg.EMBED_DIM,
            padding_idx=cfg.PAD_IDX,
        )
        nn.init.uniform_(self.embedding.weight, -0.1, 0.1)
        self.embedding.weight.data[cfg.PAD_IDX].zero_()

        # ── Blok CNN (wieloskalowy) ─────────────────────────────
        # Wiele równoległych Conv1D z różnymi kernelami
        self.conv_blocks = nn.ModuleList([
            nn.Sequential(
                nn.Conv1d(
                    in_channels=cfg.EMBED_DIM,
                    out_channels=cfg.CNN_FILTERS,
                    kernel_size=k,
                    padding=k // 2,
                ),
                nn.BatchNorm1d(cfg.CNN_FILTERS),
                nn.ReLU(),
                nn.MaxPool1d(kernel_size=2, stride=2),
            )
            for k in cfg.CNN_KERNELS
        ])
        cnn_out_dim = cfg.CNN_FILTERS * len(cfg.CNN_KERNELS)

        # Projekcja przed LSTM
        self.cnn_proj = nn.Sequential(
            nn.Linear(cnn_out_dim, cfg.EMBED_DIM),
            nn.ReLU(),
            nn.Dropout(cfg.DROPOUT * 0.5),
        )

        # ── Bi-LSTM ────────────────────────────────────────────
        self.lstm = nn.LSTM(
            input_size=cfg.EMBED_DIM,
            hidden_size=cfg.LSTM_UNITS,
            num_layers=1,
            batch_first=True,
            bidirectional=True,
            dropout=0.0,
        )
        lstm_out_dim = cfg.LSTM_UNITS * 2  # bi-directional

        # ── Attention ──────────────────────────────────────────
        self.attention = ScaledDotAttention(lstm_out_dim, cfg.ATTN_DIM)

        # ── Klasyfikator ───────────────────────────────────────
        #   wejście: context (lstm_out) + cechy hand-crafted
        clf_in = lstm_out_dim + cfg.N_HAND_FEATS
        self.classifier = nn.Sequential(
            nn.Linear(clf_in, cfg.DENSE_DIM),
            nn.ReLU(),
            nn.Dropout(cfg.DROPOUT),
            
            nn.Linear(cfg.DENSE_DIM, 64),
            nn.ReLU(),
            nn.Dropout(cfg.DROPOUT * 0.5),
            
            nn.Linear(64, 1),
        )

        self._init_weights()

    def _init_weights(self):
        """Inicjalizacja Kaiming dla warstw liniowych."""
        for m in self.modules():
            if isinstance(m, nn.Linear):
                nn.init.kaiming_normal_(m.weight, nonlinearity="relu")
                if m.bias is not None:
                    nn.init.zeros_(m.bias)
            elif isinstance(m, nn.Conv1d):
                nn.init.kaiming_normal_(m.weight, nonlinearity="relu")
                if m.bias is not None:
                    nn.init.zeros_(m.bias)

    def forward(
        self,
        ids: torch.Tensor,        # (B, T) — indeksy znaków
        hand_feats: torch.Tensor,  # (B, N_HAND_FEATS)
        return_attention: bool = False,
    ) -> torch.Tensor:

        # 1) Embedding  →  (B, T, E)
        x = self.embedding(ids)

        # 2) CNN block  →  (B, T', F*n_kernels)
        #    Conv1d oczekuje (B, C, L), więc permutujemy
        x_conv = x.permute(0, 2, 1)       # (B, E, T)
        conv_outs = [block(x_conv) for block in self.conv_blocks]
        # każdy blok: (B, CNN_FILTERS, T')
        # T' może się różnić przy parzystych kernelach, bierzemy min
        min_len = min(c.size(-1) for c in conv_outs)
        conv_outs = [c[:, :, :min_len] for c in conv_outs]
        x_cnn = torch.cat(conv_outs, dim=1)   # (B, F*n, T')
        x_cnn = x_cnn.permute(0, 2, 1)        # (B, T', F*n)

        # 3) Projekcja CNN → EMBED_DIM
        x_cnn = self.cnn_proj(x_cnn)           # (B, T', E)

        # 4) Bi-LSTM  →  (B, T', 2*LSTM_UNITS)
        lstm_out, _ = self.lstm(x_cnn)

        # 5) Attention  →  (B, 2*LSTM_UNITS)
        context, attn_weights = self.attention(lstm_out)

        # 6) Konkatenacja z cechami ręcznymi
        combined = torch.cat([context, hand_feats], dim=-1)  # (B, D+N)

        # 7) Klasyfikator  →  logit (B, 1)
        logit = self.classifier(combined).squeeze(-1)         # (B,)

        if return_attention:
            return logit, attn_weights
        return logit


# ─────────────────────────────────────────────
#  6. LABEL SMOOTHING LOSS
# ─────────────────────────────────────────────

class LabelSmoothingBCE(nn.Module):
    """
    Binary cross-entropy z wygładzaniem etykiet.
    Zapobiega nadmiernemu upewnieniu modelu.
    """
    def __init__(self, smoothing: float = 0.05):
        super().__init__()
        self.smoothing = smoothing

    def forward(self, logits: torch.Tensor, targets: torch.Tensor) -> torch.Tensor:
        targets_smooth = targets * (1 - self.smoothing) + 0.5 * self.smoothing
        return F.binary_cross_entropy_with_logits(logits, targets_smooth)


# ─────────────────────────────────────────────
#  7. TRENER
# ─────────────────────────────────────────────

class Trainer:
    def __init__(
        self,
        model: PhishingClassifier,
        train_loader: DataLoader,
        val_loader: DataLoader,
        cfg: Config,
    ):
        self.model = model.to(cfg.DEVICE)
        self.train_loader = train_loader
        self.val_loader   = val_loader
        self.cfg = cfg

        self.optimizer = torch.optim.Adam(
            model.parameters(),
            lr=cfg.LR,
            weight_decay=cfg.WEIGHT_DECAY,
        )
        self.scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(
            self.optimizer,
            T_max=cfg.EPOCHS,
            eta_min=cfg.LR_MIN,
        )
        self.criterion = LabelSmoothingBCE(smoothing=cfg.LABEL_SMOOTH)

        self.best_val_f1  = 0.0
        self.best_state   = None
        self.patience_cnt = 0
        self.history      = {
            "train_loss": [], "val_loss": [],
            "val_acc": [], "val_f1": [], "val_auc": []
        }

    def _run_epoch(self, loader: DataLoader, train: bool) -> Tuple[float, Dict]:
        self.model.train(train)
        total_loss = 0.0
        all_preds, all_probs, all_labels = [], [], []

        with torch.set_grad_enabled(train):
            for ids, feats, labels in loader:
                ids    = ids.to(self.cfg.DEVICE)
                feats  = feats.to(self.cfg.DEVICE)
                labels = labels.to(self.cfg.DEVICE)

                logits = self.model(ids, feats)
                loss   = self.criterion(logits, labels)

                if train:
                    self.optimizer.zero_grad()
                    loss.backward()
                    nn.utils.clip_grad_norm_(self.model.parameters(), max_norm=1.0)
                    self.optimizer.step()

                probs = torch.sigmoid(logits).detach().cpu().numpy()
                preds = (probs >= 0.5).astype(int)
                total_loss += loss.item() * len(labels)
                all_probs.extend(probs.tolist())
                all_preds.extend(preds.tolist())
                all_labels.extend(labels.cpu().numpy().tolist())

        avg_loss = total_loss / len(all_labels)
        metrics  = {}
        if not train:
            metrics["acc"] = accuracy_score(all_labels, all_preds)
            metrics["f1"]  = f1_score(all_labels, all_preds, zero_division=0)
            try:
                metrics["auc"] = roc_auc_score(all_labels, all_probs)
            except ValueError:
                metrics["auc"] = 0.0
        return avg_loss, metrics

    def train(self) -> Dict:
        print(f"\n{'='*60}")
        print(f"  Trening na urządzeniu: {self.cfg.DEVICE.upper()}")
        print(f"  Epoki: {self.cfg.EPOCHS}  |  Batch: {self.cfg.BATCH_SIZE}")
        print(f"{'='*60}\n")

        for epoch in range(1, self.cfg.EPOCHS + 1):
            train_loss, _         = self._run_epoch(self.train_loader, train=True)
            val_loss, val_metrics = self._run_epoch(self.val_loader, train=False)
            self.scheduler.step()

            val_f1  = val_metrics["f1"]
            val_acc = val_metrics["acc"]
            val_auc = val_metrics["auc"]
            lr_now  = self.optimizer.param_groups[0]["lr"]

            self.history["train_loss"].append(train_loss)
            self.history["val_loss"].append(val_loss)
            self.history["val_acc"].append(val_acc)
            self.history["val_f1"].append(val_f1)
            self.history["val_auc"].append(val_auc)

            print(
                f"Epoka {epoch:3d}/{self.cfg.EPOCHS}"
                f"  loss: {train_loss:.4f} -> {val_loss:.4f}"
                f"  acc: {val_acc:.4f}"
                f"  F1: {val_f1:.4f}"
                f"  AUC: {val_auc:.4f}"
                f"  lr: {lr_now:.2e}"
            )

            # Zapis najlepszego modelu
            if val_f1 > self.best_val_f1:
                self.best_val_f1 = val_f1
                self.best_state  = {
                    k: v.clone() for k, v in self.model.state_dict().items()
                }
                self.patience_cnt = 0
                print(f"  -> Nowy najlepszy model  (F1={val_f1:.4f})")
            else:
                self.patience_cnt += 1
                if self.patience_cnt >= self.cfg.PATIENCE:
                    print(f"\n  Early stopping po {epoch} epokach.")
                    break

        # Przywróć najlepszy stan
        if self.best_state:
            self.model.load_state_dict(self.best_state)
        return self.history

    def evaluate(self, loader: DataLoader, split_name: str = "Test") -> None:
        self.model.eval()
        all_preds, all_probs, all_labels = [], [], []

        with torch.no_grad():
            for ids, feats, labels in loader:
                ids   = ids.to(self.cfg.DEVICE)
                feats = feats.to(self.cfg.DEVICE)
                probs = torch.sigmoid(self.model(ids, feats)).cpu().numpy()
                preds = (probs >= 0.5).astype(int)
                all_probs.extend(probs.tolist())
                all_preds.extend(preds.tolist())
                all_labels.extend(labels.numpy().tolist())

        print(f"\n{'='*60}")
        print(f"  Ewaluacja — {split_name}")
        print(f"{'='*60}")
        print(classification_report(
            all_labels, all_preds,
            target_names=["Bezpieczny", "Phishing"],
            digits=4
        ))
        cm = confusion_matrix(all_labels, all_preds)
        print(f"Macierz pomylek:\n{cm}")
        try:
            auc = roc_auc_score(all_labels, all_probs)
            print(f"ROC-AUC: {auc:.4f}")
        except ValueError:
            pass

    def save(self, path: str = "phishing_model.pt") -> None:
        torch.save({
            "model_state": self.model.state_dict(),
            "vocab_size":  self.model.embedding.num_embeddings,
            "best_val_f1": self.best_val_f1,
            "history":     self.history,
        }, path)
        print(f"\nModel zapisany -> {path}")

    @staticmethod
    def load(path: str, cfg: Config = cfg) -> "PhishingClassifier":
        checkpoint = torch.load(path, map_location=cfg.DEVICE)
        model = PhishingClassifier(vocab_size=checkpoint["vocab_size"], cfg=cfg)
        model.load_state_dict(checkpoint["model_state"])
        model.eval()
        return model.to(cfg.DEVICE)


# ─────────────────────────────────────────────
#  8. PREDYKCJA NA NOWYCH URL-ach
# ─────────────────────────────────────────────

class Predictor:
    """Klasa do inferencji na pojedynczych URL-ach lub listach."""
    def __init__(
        self,
        model: PhishingClassifier,
        tokenizer: CharTokenizer,
        cfg: Config = cfg
    ):
        self.model     = model.eval()
        self.tokenizer = tokenizer
        self.cfg       = cfg

    @torch.no_grad()
    def predict(self, urls: List[str]) -> List[Dict]:
        results = []
        for url in urls:
            ids   = torch.tensor(
                [self.tokenizer.encode(url)], dtype=torch.long
            ).to(self.cfg.DEVICE)
            feats = torch.tensor(
                [extract_features(url)], dtype=torch.float32
            ).to(self.cfg.DEVICE)
            logit, attn = self.model(ids, feats, return_attention=True)
            prob = torch.sigmoid(logit).item()
            results.append({
                "url":           url,
                "phishing_prob": round(prob, 4),
                "label":         "PHISHING" if prob >= 0.5 else "BEZPIECZNY",
                "confidence":    round(max(prob, 1 - prob), 4),
                # wagi attention nad sekwencją CNN (T' tokenów)
                "attention":     attn.squeeze(0).cpu().numpy(),
            })
        return results


# ─────────────────────────────────────────────
#  9. FUNKCJE POMOCNICZE DO DANYCH
# ─────────────────────────────────────────────

def load_data_from_csv(
    path: str,
    url_col: str = "url",
    label_col: str = "label"
) -> Tuple[List[str], List[int]]:
    """
    Wczytuje dane z CSV.
    Etykiety: 1 = phishing, 0 = bezpieczny.
    Zastąp tę funkcję własnym źródłem danych (PhishTank, Kaggle itd.).
    """
    import pandas as pd
    df = pd.read_csv(path)
    urls   = df[url_col].astype(str).tolist()
    labels = df[label_col].astype(int).tolist()
    return urls, labels


def generate_demo_data(n: int = 2000) -> Tuple[List[str], List[int]]:
    """
    Generuje syntetyczne dane demo do testowania kodu.
    NIE nadaje się do prawdziwego treningu — tylko do weryfikacji pipeline'u.
    """
    safe_templates = [
        "https://www.google.com/search?q={}",
        "https://github.com/user/{}",
        "https://wikipedia.org/wiki/{}",
        "https://amazon.com/product/{}",
        "https://stackoverflow.com/questions/{}",
    ]
    phish_templates = [
        "http://paypa1-secure.{}.xyz/login",
        "http://192.168.1.{}/verify/account",
        "http://google-security-alert.{}.tk/confirm",
        "http://amaz0n-account-update.com/verify?id={}",
        "http://{}.free-prize.click/claim",
    ]
    rng = np.random.default_rng(42)
    urls, labels = [], []
    words = ["test", "abc", "foo", "bar", "data", "info", "web", "net", "srv"]
    for _ in range(n // 2):
        tmpl = safe_templates[rng.integers(len(safe_templates))]
        urls.append(tmpl.format(rng.choice(words)))
        labels.append(0)
    for _ in range(n // 2):
        tmpl = phish_templates[rng.integers(len(phish_templates))]
        urls.append(tmpl.format(int(rng.integers(100, 999))))
        labels.append(1)
    idx = rng.permutation(len(urls))
    return [urls[i] for i in idx], [labels[i] for i in idx]


# ─────────────────────────────────────────────
#  10. MAIN
# ─────────────────────────────────────────────

def main():
    print("Klasyfikator URL phishingowych — CNN + Bi-LSTM + Attention")
    print(f"Urzadzenie: {cfg.DEVICE}\n")

    # ── Dane ────────────────────────────────────────────────────
    # Opcja A: własny plik CSV
    urls, labels = load_data_from_csv(
           "data/set_2/processed/set2.csv", url_col="url", label_col="label"
       )
    
    #from Set_Processor import ImportData
    #data = ImportData()
    #data.Import_set_3()
    #urls, labels = data.Get_NLP()
    # Opcja B: dane syntetyczne (demo)
    #print("Generowanie danych demo (2000 przykladow)...")
    #urls, labels = generate_demo_data(n=2000)
    #print(
    #    f"Lacznie: {len(urls)} URL"
    #    f"  |  phishing: {sum(labels)}"
    #    f"  |  safe: {len(labels)-sum(labels)}\n"
    #)

    # ── Podział train / val / test ───────────────────────────────
    X_train, X_temp, y_train, y_temp = train_test_split(
        urls, labels, test_size=0.3, stratify=labels, random_state=42
    )
    X_val, X_test, y_val, y_test = train_test_split(
        X_temp, y_temp, test_size=0.5, stratify=y_temp, random_state=42
    )
    print(f"Train: {len(X_train)}  Val: {len(X_val)}  Test: {len(X_test)}\n")

    # ── Tokenizator ─────────────────────────────────────────────
    tokenizer = CharTokenizer(max_len=cfg.MAX_LEN)
    vocab_size = tokenizer.vocab_size
    print(f"Rozmiar slownika: {vocab_size}\n")

    # ── DataLoadery ─────────────────────────────────────────────
    def make_loader(x, y, shuffle=False) -> DataLoader:
        ds = URLDataset(x, y, tokenizer)
        return DataLoader(
            ds, batch_size=cfg.BATCH_SIZE, shuffle=shuffle, num_workers=0
        )

    train_loader = make_loader(X_train, y_train, shuffle=True)
    val_loader   = make_loader(X_val,   y_val)
    test_loader  = make_loader(X_test,  y_test)

    # ── Model ───────────────────────────────────────────────────
    model = PhishingClassifier(vocab_size=vocab_size, cfg=cfg)
    n_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
    print(f"Parametry modelu: {n_params:,}\n")
    print(model)

    # ── Trening ─────────────────────────────────────────────────
    trainer = Trainer(model, train_loader, val_loader, cfg)
    history = trainer.train()

    # ── Ewaluacja na zbiorze testowym ───────────────────────────
    trainer.evaluate(test_loader, split_name="Test")

    # ── Zapis modelu ────────────────────────────────────────────
    trainer.save("phishing_model.pt")
    
    
    urls_set5, labels_set5 = load_data_from_csv(
           "data/set_1/processed/set1.csv", url_col="url", label_col="label"
    )
    
    # Przekazanie całego nowego zbioru do loadera testowego
    test_loader_set5 = make_loader(urls_set5, labels_set5, shuffle=False)
    
    trainer.evaluate(test_loader_set5, split_name="Test-Set-5")



if __name__ == "__main__":
    main()
