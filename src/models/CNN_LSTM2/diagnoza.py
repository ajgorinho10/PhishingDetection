import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import numpy as np
import torch
from collections import Counter
from urllib.parse import urlparse

from Set_Processor import ImportData
from model import CnnLstm2
from models_utils import CharTokenizer, Trainer
from config import cfg

def diagnose(model, tokenizer, new_urls, new_labels, device='cpu', threshold=0.5):
    model.eval()
    all_probs, all_preds = [], []
    
    trainer = Trainer(model,cfg)

    x_tensor,y_tensor = trainer.get_tokenized_tensors(new_urls,new_labels)
    dataloader = trainer.get_data_loaders(x_tensor,y_tensor,shuffled=False)
    
    with torch.no_grad():
        for batch_X, batch_y in dataloader:
            batch_X, batch_y = batch_X.to(cfg.DEVICE), batch_y.to(cfg.DEVICE)
            output_raw = model(batch_X)
            
            # Poprawka: usunięto round() i dodano squeeze()
            probs = torch.sigmoid(output_raw).squeeze().cpu().numpy()
            
            all_probs.extend(probs)
            all_preds.extend((probs >= threshold).astype(int))

    all_probs  = np.array(all_probs).flatten()
    all_preds  = np.array(all_preds).flatten()
    all_labels = np.array(new_labels).flatten()

    # ── 1. Precision / Recall rozdzielnie ──────────────────────────
    tp = ((all_preds==1) & (all_labels==1)).sum()
    fp = ((all_preds==1) & (all_labels==0)).sum()
    fn = ((all_preds==0) & (all_labels==1)).sum()
    tn = ((all_preds==0) & (all_labels==0)).sum()

    precision = tp / (tp + fp + 1e-9)
    recall    = tp / (tp + fn + 1e-9)
    f1        = 2 * precision * recall / (precision + recall + 1e-9)
    fpr       = fp / (fp + tn + 1e-9)  # false positive rate

    print("── Metryki ─────────────────────────────────")
    print(f"  Precision : {precision:.4f}   (ile z 'phishing' to naprawdę phishing)")
    print(f"  Recall    : {recall:.4f}   (ile phishingów zostało wykrytych)")
    print(f"  F1        : {f1:.4f}")
    print(f"  FPR       : {fpr:.4f}   (ile legit URL-i fałszywie oznaczono jako phishing)")
    print()

    # ── 2. Gdzie model jest pewny a się myli ──────────────────────
    errors = all_preds != all_labels
    high_conf_errors = errors & (np.abs(all_probs - 0.5) > 0.4)
    print(f"── Błędy wysokiej pewności (|prob−0.5|>0.4) ──")
    print(f"  Liczba: {high_conf_errors.sum()} / {errors.sum()} błędów ogółem")
    print(f"  → Im więcej, tym poważniejszy distribution shift")
    print()

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
        url = "https://"+url
        try: return urlparse(url).netloc
        except: return 'unknown'

    error_urls = np.array(new_urls)[errors].tolist()
    error_domains = Counter(get_domain(u) for u in error_urls)
    print("── Top 10 domen w błędach ──────────────────")
    for dom, cnt in error_domains.most_common(10):
        print(f"  {cnt:6,}×  {dom}")

    return dict(precision=precision, recall=recall, f1=f1, fpr=fpr,
                n_errors=errors.sum(), n_high_conf_errors=high_conf_errors.sum())
    
    
    

tokenizer = CharTokenizer()
data = ImportData()
models = CnnLstm2(cfg)
models.load_state_dict(torch.load(cfg.PATH))



data.Import_set_3()
X, y = data.Get_NLP()
print("-"*50)
print("set treningowy")
diagnose(models, tokenizer, X, y, cfg.DEVICE)


data.Import_set_2()
X, y = data.Get_NLP()
print("-"*50)
print("Inny set")
diagnose(models, tokenizer, X, y, cfg.DEVICE)

#data.Import_set_5()
#X, y = data.Get_NLP()
#print("-"*50)
#print("Inny set 6 000 000 url")
#diagnose(models, tokenizer, X, y, cfg.DEVICE)