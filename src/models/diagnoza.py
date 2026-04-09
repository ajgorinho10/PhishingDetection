import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import joblib
import numpy as np
import pandas as pd
from collections import Counter
from urllib.parse import urlparse

import torch
from Set_Processor import ImportData

def _prepare_universal_dataloader(trainer, new_urls, new_labels):
    """
    Funkcja pomocnicza: Automatycznie wykrywa typ Trainera 
    (Tokens, TF-IDF, lub Hybrid) i generuje odpowiedni DataLoader.
    """
    # 1. Przygotowanie etykiet wspólnie dla wszystkich
    y_tensor = torch.tensor(
        new_labels.values if hasattr(new_labels, 'values') else new_labels, 
        dtype=torch.float32
    ).view(-1, 1)

    # 2. Przygotowanie cech statycznych (jeśli aktywne)
    X_features = None
    if trainer.use_features:
        # Zakładamy, że scaler został załadowany z dysku w funkcji testującej
        X_features_raw = trainer.get_data_features(new_urls)
        X_features = torch.tensor(
            trainer.scaler.transform(X_features_raw.numpy()), 
            dtype=torch.float32
        )

    # 3. Wykrywanie architektury modelu na podstawie obiektów w Trainerze
    is_hybrid      = hasattr(trainer, 'ftidfVectorizer') and hasattr(trainer, 'tokenizer')
    is_tfidf_only  = hasattr(trainer, 'ftidfVectorizer') and not hasattr(trainer, 'tokenizer')
    is_tokens_only = hasattr(trainer, 'tokenizer') and not hasattr(trainer, 'ftidfVectorizer')

    # 4. Generowanie DataLoadera
    if is_hybrid:
        X_tokens = torch.tensor(trainer.tokenizer.encode_dataset(new_urls), dtype=torch.long)
        X_tfidf = trainer.ftidfVectorizer.transform(new_urls)
        return trainer.get_data_loaders(X_tokens, X_tfidf, y_tensor, X_features, shuffled=False)
        
    elif is_tfidf_only:
        X_tfidf = trainer.ftidfVectorizer.transform(new_urls)
        return trainer.get_data_loaders(X_tfidf, y_tensor, X_features, shuffled=False)
        
    elif is_tokens_only:
        # Pamiętamy, że get_tokenized_tensors zwracało (X, y)
        X_tokens, _ = trainer.get_tokenized_tensors(new_urls, new_labels)
        return trainer.get_data_loaders(X_tokens, y_tensor, X_features, shuffled=False)
        
    else:
        raise ValueError("Nie rozpoznano struktury Trainera (Brak Tokenizera i TF-IDF).")


def diagnose(trainer, new_urls, new_labels, threshold=0.5):
    """
    Uniwersalna funkcja diagnostyczna.
    """
    model = trainer.model
    cfg = trainer.cfg
    
    model.eval()
    all_probs, all_preds = [], []
    
    # Korzystamy z uniwersalnego generatora
    dataloader = _prepare_universal_dataloader(trainer, new_urls, new_labels)
    
    with torch.no_grad():
        for batch_data in dataloader:
            # Przenosimy wszystkie tensory (np. Tokeny, TFIDF, Cechy, Etykiety) na GPU
            batch_data = [d.to(cfg.DEVICE) for d in batch_data]
            
            # Magia Pythona: batch_data[:-1] to wszystkie wejścia (bez ostatniego, czyli etykiet y).
            # Dzięki '* ' automatycznie podajemy je jako osobne argumenty do metody forward() modelu.
            output_raw = model(*batch_data[:-1])
            probs = torch.sigmoid(output_raw).squeeze(-1).cpu().numpy()
            
            # Zabezpieczenie wymiarów
            if probs.ndim == 0: probs = np.array([probs])
                
            all_probs.extend(probs)
            all_preds.extend((probs >= threshold).astype(int))
                
    all_probs  = np.array(all_probs).flatten()
    all_preds  = np.array(all_preds).flatten()
    
    if hasattr(new_labels, 'values'):
        all_labels = new_labels.values.flatten()
    else:
        all_labels = np.array(new_labels).flatten()

    # ── 1. Precision / Recall ──────────────────────────
    tp = ((all_preds==1) & (all_labels==1)).sum()
    fp = ((all_preds==1) & (all_labels==0)).sum()
    fn = ((all_preds==0) & (all_labels==1)).sum()
    tn = ((all_preds==0) & (all_labels==0)).sum()

    precision = tp / (tp + fp + 1e-9)
    recall    = tp / (tp + fn + 1e-9)
    f1        = 2 * precision * recall / (precision + recall + 1e-9)
    fpr       = fp / (fp + tn + 1e-9)

    print("### Metryki")
    print(f"-  Precision : {precision:.4f}   (ile z 'phishing' to naprawdę phishing)")
    print(f"-  Recall    : {recall:.4f}   (ile phishingów zostało wykrytych)")
    print(f"-  F1        : {f1:.4f}")
    print(f"-  FPR       : {fpr:.4f}   (ile legit URL-i fałszywie oznaczono jako phishing)\n")

    # ── 2. Błędy ──────────────────────
    errors = all_preds != all_labels
    high_conf_errors = errors & (np.abs(all_probs - 0.5) > 0.4)
    print(f"###  Błędy wysokiej pewności (|prob−0.5|>0.4)")
    print(f"-  Liczba: {high_conf_errors.sum()} / {errors.sum()} błędów ogółem")

    # ── 3. Analiza długości URL ────────────────────────────────────
    lengths = np.array([len(str(u)) for u in new_urls])
    print("### F1 według długości URL")
    for lo, hi in [(0,50),(50,100),(100,150),(150,200),(200,999)]:
        mask = (lengths >= lo) & (lengths < hi)
        if mask.sum() < 100: continue
        tp_ = ((all_preds[mask]==1) & (all_labels[mask]==1)).sum()
        fp_ = ((all_preds[mask]==1) & (all_labels[mask]==0)).sum()
        fn_ = ((all_preds[mask]==0) & (all_labels[mask]==1)).sum()
        p_  = tp_ / (tp_ + fp_ + 1e-9)
        r_  = tp_ / (tp_ + fn_ + 1e-9)
        f_  = 2*p_*r_ / (p_+r_+1e-9)
        print(f"-  [{lo:3d}–{hi:3d} znaków]  n={mask.sum():7,}  F1={f_:.4f}")
    print()

    # ── 4. Rozkład prawdopodobieństw ──────────────────────────────
    print("### Rozkład predykcji")
    buckets = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.01]
    for lo, hi in zip(buckets, buckets[1:]):
        mask = (all_probs >= lo) & (all_probs < hi)
        n = mask.sum()
        if n == 0: continue
        acc = (all_preds[mask] == all_labels[mask]).mean()
        bar = '█' * int(n / len(all_probs) * 40)
        print(f"-  [{lo:.1f}–{hi:.1f}]  n={n:8,}  acc={acc:.3f}  {bar}")
    print()

    # ── 5. Najczęstsze domeny w błędach ──────────────────────────
    def get_domain(url):
        url_str = str(url)
        if not url_str.startswith(("http://", "https://")):
            url_str = "https://" + url_str
        try: return urlparse(url_str).netloc
        except: return 'unknown'

    new_urls_list = new_urls.tolist() if hasattr(new_urls, 'tolist') else list(new_urls)
    error_urls = [url for url, is_err in zip(new_urls_list, errors) if is_err]
    error_preds = all_preds[errors]
    error_labels = all_labels[errors]
    
    error_details = [(get_domain(u), p, l) for u, p, l in zip(error_urls, error_preds, error_labels)]
    error_counts = Counter(error_details)
    
    print("### Top 10 domen w błędach (Domena | Model | Prawda)")
    for (dom, pred, label), cnt in error_counts.most_common(10):
        pred_nazwa = "Phishing (1)" if pred == 1 else "Legit (0)"
        label_nazwa = "Phishing (1)" if label == 1 else "Legit (0)"
        print(f"  {cnt:6,}×  {dom:<35} | Model: {pred_nazwa:<12} | Prawda: {label_nazwa}")

    return dict(precision=precision, recall=recall, f1=f1, fpr=fpr,
                n_errors=errors.sum(), n_high_conf_errors=high_conf_errors.sum())
    

def export_hard_negatives_to_csv(trainer, urls, true_labels, output_filename="hard_negatives.csv"):
    """
    Uniwersalny eksport błędów (wspiera Hybrydę, TF-IDF i Tokeny).
    """
    trainer.model.eval()
    all_preds = []
    
    dataloader = _prepare_universal_dataloader(trainer, urls, true_labels)
    
    with torch.no_grad():
        for batch_data in dataloader:
            batch_data = [d.to(trainer.cfg.DEVICE) for d in batch_data]
            output_raw = trainer.model(*batch_data[:-1])
            probs = torch.sigmoid(output_raw).squeeze(-1).cpu().numpy()
            
            if probs.ndim == 0: probs = np.array([probs])
            all_preds.extend((probs >= 0.5).astype(int))

    all_preds = np.array(all_preds).flatten()
    all_labels = true_labels.values.flatten() if hasattr(true_labels, 'values') else np.array(true_labels).flatten()
    urls_list = urls.tolist() if hasattr(urls, 'tolist') else list(urls)

    df_results = pd.DataFrame({'url': urls_list, 'true_label': all_labels, 'prediction': all_preds})
    df_errors = df_results[df_results['true_label'] != df_results['prediction']].copy()
    
    df_errors = df_errors[['url', 'true_label']].rename(columns={'true_label': 'label'})
    df_errors.to_csv(output_filename, index=False)
    print(f"Zakończono! Zapisano {len(df_errors)} trudnych przypadków (Hard Negatives) do pliku '{output_filename}'.")


# ==========================================
# METODY TESTOWE
# ==========================================
data = ImportData()

def diagnoze_at_all_sets(trainer):
    
    data.Import_set_1()
    X, y = data.Get_NLP()
    print(f"## SET - 1")
    diagnose(trainer, X, y)
    print("\n")
    
    data.Import_set_2()
    X, y = data.Get_NLP()
    print(f"## SET - 2")
    diagnose(trainer, X, y)
    print("\n")
    
    data.Import_set_3()
    X, y = data.Get_NLP()
    print(f"## SET - 3")
    diagnose(trainer, X, y)
    print("\n")
    
    data.Import_set_4()
    X, y = data.Get_NLP()
    print(f"## SET - 4")
    diagnose(trainer, X, y)
    print("\n")
        
        
def test_model_CNN():
    from models.CNN.model import CNN
    from models.CNN.config import cfg
    from trainer import Trainer_Tokens
    
    cnn = CNN(cfg)
    cnn.load_state_dict(torch.load(cfg.PATH, weights_only=True))
    
    trainer = Trainer_Tokens(cnn, cfg)
    trainer.load_scaler()
    
    if cfg.USE_FEATURES:
        trainer.load_scaler()
    
    diagnoze_at_all_sets(trainer)


def test_model_LSTM():
    from models.LSTM.model import LSTM
    from models.LSTM.config import cfg
    from trainer import Trainer_Tokens
    
    lstm = LSTM(cfg)
    lstm.load_state_dict(torch.load(cfg.PATH, weights_only=True))
    
    trainer = Trainer_Tokens(lstm, cfg)
    if cfg.USE_FEATURES:
        trainer.load_scaler()
    
    diagnoze_at_all_sets(trainer)


def test_model_CNN_LSTM():
    from models.CNN_LSTM.model import CnnLstm2
    from models.CNN_LSTM.config import cfg
    from trainer import Trainer_Tokens
    
    cnnlstm = CnnLstm2(cfg)
    cnnlstm.load_state_dict(torch.load(cfg.PATH, weights_only=True))
    
    trainer = Trainer_Tokens(cnnlstm, cfg)
    if cfg.USE_FEATURES:
        trainer.load_scaler()
    
    diagnoze_at_all_sets(trainer)


def test_model_MLP():
    from models.MLP.model import MLP
    from models.MLP.config import cfg
    from trainer import Trainer_TfIDF
    
    mlp = MLP(cfg)
    mlp.load_state_dict(torch.load(cfg.PATH, weights_only=True))
    
    trainer = Trainer_TfIDF(mlp, cfg, dataset=None)
    trainer.load_scaler_tfidf()
    
    if cfg.USE_FEATURES:
        trainer.scaler = joblib.load(cfg.SCALER_PATH)
    
    diagnoze_at_all_sets(trainer)


#test_model_CNN_LSTM()
test_model_CNN()
#test_model_MLP()
#test_model_LSTM()