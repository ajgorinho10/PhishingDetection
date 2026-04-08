import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import joblib
import numpy as np
import torch
from sklearn.preprocessing import StandardScaler

from collections import Counter
from urllib.parse import urlparse

from Set_Processor import ImportData
from models_utils import CharTokenizer, Trainer

from models.CNN_LSTM.model import CnnLstm2 as modelxd
from models.CNN_LSTM.config import cfg

import torch
import numpy as np
from urllib.parse import urlparse
from collections import Counter

import pandas as pd

def diagnose(trainer, new_urls, new_labels, threshold=0.5):
    """
    Zewnętrzna funkcja diagnostyczna.
    Wymaga podania instancji klasy Trainer, która przetrenowała model.
    """
    model = trainer.model
    cfg = trainer.cfg
    
    model.eval()
    all_probs, all_preds = [], []
    
    # Korzystamy z metod przekazanego trainera
    x_tensor, y_tensor = trainer.get_tokenized_tensors(new_urls, new_labels)
    
    with torch.no_grad():
        if trainer.use_features:
            trainer.scaler = joblib.load(cfg.SCALER_PATH)
            # 1. Pobieramy cechy przez trainera
            X_features = trainer.get_data_features(new_urls)
            
            # 2. KLUCZOWE: Używamy scalera zapisanego w trainerze (tylko transform!)
            X_features = torch.tensor(
                trainer.scaler.transform(X_features.numpy()), 
                dtype=torch.float32
            )
            
            dataloader = trainer.get_data_loaders(x_tensor, y_tensor, X_features, shuffled=False)
            
            for batch_X, batch_features, batch_y in dataloader:
                batch_X = batch_X.to(cfg.DEVICE)
                batch_features = batch_features.to(cfg.DEVICE)
                
                output_raw = model(batch_X, batch_features)
                probs = torch.sigmoid(output_raw).squeeze(-1).cpu().numpy()
                
                # Zabezpieczenie wymiarów
                if probs.ndim == 0:
                    probs = np.array([probs])
                    
                all_probs.extend(probs)
                all_preds.extend((probs >= threshold).astype(int))
                
        else:
            dataloader = trainer.get_data_loaders(x_tensor, y_tensor, shuffled=False)  
               
            for batch_X, batch_y in dataloader:
                batch_X = batch_X.to(cfg.DEVICE)
                
                output_raw = model(batch_X)
                probs = torch.sigmoid(output_raw).squeeze(-1).cpu().numpy()
                
                if probs.ndim == 0:
                    probs = np.array([probs])
            
                all_probs.extend(probs)
                all_preds.extend((probs >= threshold).astype(int))
                
    all_probs  = np.array(all_probs).flatten()
    all_preds  = np.array(all_preds).flatten()
    
    if hasattr(new_labels, 'values'):
        all_labels = new_labels.values.flatten()
    else:
        all_labels = np.array(new_labels).flatten()

    # ── 1. Precision / Recall rozdzielnie ──────────────────────────
    tp = ((all_preds==1) & (all_labels==1)).sum()
    fp = ((all_preds==1) & (all_labels==0)).sum()
    fn = ((all_preds==0) & (all_labels==1)).sum()
    tn = ((all_preds==0) & (all_labels==0)).sum()

    precision = tp / (tp + fp + 1e-9)
    recall    = tp / (tp + fn + 1e-9)
    f1        = 2 * precision * recall / (precision + recall + 1e-9)
    fpr       = fp / (fp + tn + 1e-9)

    print("── Metryki ─────────────────────────────────")
    print(f"  Precision : {precision:.4f}   (ile z 'phishing' to naprawdę phishing)")
    print(f"  Recall    : {recall:.4f}   (ile phishingów zostało wykrytych)")
    print(f"  F1        : {f1:.4f}")
    print(f"  FPR       : {fpr:.4f}   (ile legit URL-i fałszywie oznaczono jako phishing)\n")

    # ── 2. Gdzie model jest pewny a się myli ──────────────────────
    errors = all_preds != all_labels
    high_conf_errors = errors & (np.abs(all_probs - 0.5) > 0.4)
    print(f"── Błędy wysokiej pewności (|prob−0.5|>0.4) ──")
    print(f"  Liczba: {high_conf_errors.sum()} / {errors.sum()} błędów ogółem")
    print(f"  → Im więcej, tym poważniejszy distribution shift\n")

    # ── 3. Analiza długości URL ────────────────────────────────────
    lengths = np.array([len(u) for u in new_urls])
    print("── F1 według długości URL ──────────────────")
    for lo, hi in [(0,50),(50,100),(100,150),(150,200),(200,999)]:
        mask = (lengths >= lo) & (lengths < hi)
        if mask.sum() < 100:
            continue
        tp_ = ((all_preds[mask]==1) & (all_labels[mask]==1)).sum()
        fp_ = ((all_preds[mask]==1) & (all_labels[mask]==0)).sum()
        fn_ = ((all_preds[mask]==0) & (all_labels[mask]==1)).sum()
        p_  = tp_ / (tp_ + fp_ + 1e-9)
        r_  = tp_ / (tp_ + fn_ + 1e-9)
        f_  = 2*p_*r_ / (p_+r_+1e-9)
        print(f"  [{lo:3d}–{hi:3d} znaków]  n={mask.sum():7,}  F1={f_:.4f}")
    print()

    # ── 4. Rozkład prawdopodobieństw ──────────────────────────────
    print("── Rozkład predykcji ───────────────────────")
    buckets = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.01]
    for lo, hi in zip(buckets, buckets[1:]):
        mask = (all_probs >= lo) & (all_probs < hi)
        n = mask.sum()
        if n == 0: continue
        acc = (all_preds[mask] == all_labels[mask]).mean()
        bar = '█' * int(n / len(all_probs) * 40)
        print(f"  [{lo:.1f}–{hi:.1f}]  n={n:8,}  acc={acc:.3f}  {bar}")
    print()

    # ── 5. Najczęstsze domeny w błędach ──────────────────────────
    def get_domain(url):
        url_str = str(url)
        if not url_str.startswith(("http://", "https://")):
            url_str = "https://" + url_str
        try: 
            return urlparse(url_str).netloc
        except: 
            return 'unknown'

    # Zabezpieczenie przed różnymi formatami wejściowymi
    new_urls_list = new_urls.tolist() if hasattr(new_urls, 'tolist') else list(new_urls)
    
    # Wyciągamy URL-e, Predykcje i Etykiety tylko dla błędów
    error_urls = [url for url, is_err in zip(new_urls_list, errors) if is_err]
    error_preds = all_preds[errors]
    error_labels = all_labels[errors]
    
    # Tworzymy listę krotek: (domena, predykcja, prawdziwa_klasa)
    error_details = []
    for u, p, l in zip(error_urls, error_preds, error_labels):
        error_details.append((get_domain(u), p, l))
    
    # Zliczamy te kombinacje
    error_counts = Counter(error_details)
    
    print("── Top 10 domen w błędach (Domena | Model | Prawda) ──")
    for (dom, pred, label), cnt in error_counts.most_common(10):
        # Mapowanie cyfr na czytelne nazwy dla łatwiejszej analizy
        pred_nazwa = "Phishing (1)" if pred == 1 else "Legit (0)"
        label_nazwa = "Phishing (1)" if label == 1 else "Legit (0)"
        
        print(f"  {cnt:6,}×  {dom:<35} | Model: {pred_nazwa:<12} | Prawda: {label_nazwa}")

    return dict(precision=precision, recall=recall, f1=f1, fpr=fpr,
                n_errors=errors.sum(), n_high_conf_errors=high_conf_errors.sum())
    

import pandas as pd
import numpy as np
import torch

def export_hard_negatives_to_csv(trainer, urls, true_labels, output_filename="hard_negatives.csv"):
    """
    Uruchamia model na podanym zbiorze, znajduje błędy i zapisuje 
    błędne adresy URL wraz z ich poprawnymi etykietami do pliku CSV.
    Wersja zoptymalizowana pod kątem zużycia pamięci RAM (Pandas-first).
    """
    trainer.model.eval()
    all_preds = []
    
    # 1. Przygotowanie danych
    x_tensor, y_tensor = trainer.get_tokenized_tensors(urls, true_labels)
    
    with torch.no_grad():
        if trainer.use_features:
            X_features = trainer.get_data_features(urls)
            X_features = torch.tensor(
                trainer.scaler.transform(X_features.numpy()), 
                dtype=torch.float32
            )
            dataloader = trainer.get_data_loaders(x_tensor, y_tensor, X_features, shuffled=False)
            
            for batch_X, batch_features, batch_y in dataloader:
                batch_X = batch_X.to(trainer.cfg.DEVICE)
                batch_features = batch_features.to(trainer.cfg.DEVICE)
                
                output_raw = trainer.model(batch_X, batch_features)
                probs = torch.sigmoid(output_raw).squeeze(-1).cpu().numpy()
                
                if probs.ndim == 0: probs = np.array([probs])
                all_preds.extend((probs >= 0.5).astype(int))
                
        else:
            dataloader = trainer.get_data_loaders(x_tensor, y_tensor, shuffled=False)
            for batch_X, batch_y in dataloader:
                batch_X = batch_X.to(trainer.cfg.DEVICE)
                
                output_raw = trainer.model(batch_X)
                probs = torch.sigmoid(output_raw).squeeze(-1).cpu().numpy()
                
                if probs.ndim == 0: probs = np.array([probs])
                all_preds.extend((probs >= 0.5).astype(int))

    # 2. Spłaszczenie predykcji i etykiet
    all_preds = np.array(all_preds).flatten()
    
    if hasattr(true_labels, 'values'):
        all_labels = true_labels.values.flatten()
    else:
        all_labels = np.array(true_labels).flatten()

    # ZABEZPIECZENIE PAMIĘCI (Zamiast NumPy, używamy bezpośrednio Pandas DataFrame)
    # Pandas przechowuje stringi jako referencje do obiektów, ignorując ich maksymalną długość.
    urls_list = urls.tolist() if hasattr(urls, 'tolist') else list(urls)

    # 3. Tworzymy tabelę zbiorczą
    df_results = pd.DataFrame({
        'url': urls_list,
        'true_label': all_labels,
        'prediction': all_preds
    })

    # 4. Odfiltrowujemy tylko te wiersze, gdzie model się pomylił (Hard Negatives)
    df_errors = df_results[df_results['true_label'] != df_results['prediction']].copy()

    # 5. Formatujemy kolumny pod standardowy trening i zapisujemy do pliku
    df_errors = df_errors[['url', 'true_label']]
    df_errors.rename(columns={'true_label': 'label'}, inplace=True)
    
    df_errors.to_csv(output_filename, index=False)
    print(f"Zakończono! Zapisano {len(df_errors)} trudnych przypadków (Hard Negatives) do pliku '{output_filename}'.")


data = ImportData()
models = modelxd(cfg)
models.load_state_dict(torch.load(cfg.PATH))
trainer = Trainer(models, cfg)
trainer.scaler = joblib.load(cfg.SCALER_PATH)


data.Import_set_4()
X, y = data.Get_NLP()
print("-"*50)
print("set - 4")
diagnose(trainer, X, y)
#export_hard_negatives_to_csv(trainer, X, y)


data.Import_set_1()
X, y = data.Get_NLP()
print("-"*50)
print("set - 1")
diagnose(trainer, X, y)


data.Import_set_2()
X, y = data.Get_NLP()
print("-"*50)
print("set - 2")
diagnose(trainer, X, y)


data.Import_set_3()
X, y = data.Get_NLP()
print("-"*50)
print("set - 3")
diagnose(trainer, X, y)

