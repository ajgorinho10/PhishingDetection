"""
diagnoza_distilbert.py — odpowiednik diagnoza.py dla DistilBERT_Model.

Różnice względem diagnoza.py:
  - DataLoader zwraca (input_ids, attention_mask, [features,] y)
  - model.forward(input_ids, attention_mask, [features]) — dwa/trzy argumenty
  - Tokenizacja przez DistilBertTokenizerFast zamiast CharTokenizer
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
import torch
from collections import Counter
from urllib.parse import urlparse

from Set_Processor import ImportData


def _build_eval_loader(trainer, urls, labels):
    """Tokenizuje URLs i buduje DataLoader dla ewaluacji."""
    input_ids, attention_mask, y = trainer.get_tokenized_tensors(urls, labels)

    X_features = None
    if trainer.use_features:
        import torch
        X_features = torch.tensor(
            trainer.scaler.transform(trainer.get_data_features(urls).numpy()),
            dtype=torch.float32
        )

    return trainer.get_data_loaders(input_ids, attention_mask, y, X_features, shuffled=False)


def diagnose(trainer, new_urls, new_labels, threshold=0.5):
    model = trainer.model
    cfg   = trainer.cfg

    model.eval()
    all_probs, all_preds = [], []

    dataloader = _build_eval_loader(trainer, new_urls, new_labels)

    with torch.no_grad():
        for batch in dataloader:
            if trainer.use_features:
                input_ids, attention_mask, features, y = batch
                logit = model(
                    input_ids.to(cfg.DEVICE),
                    attention_mask.to(cfg.DEVICE),
                    features.to(cfg.DEVICE)
                )
            else:
                input_ids, attention_mask, y = batch
                logit = model(
                    input_ids.to(cfg.DEVICE),
                    attention_mask.to(cfg.DEVICE)
                )

            probs = torch.sigmoid(logit).squeeze(-1).cpu().numpy()
            if probs.ndim == 0:
                probs = np.array([probs])
            all_probs.extend(probs)
            all_preds.extend((probs >= threshold).astype(int))

    all_probs  = np.array(all_probs).flatten()
    all_preds  = np.array(all_preds).flatten()
    all_labels = (new_labels.values if hasattr(new_labels, 'values') else np.array(new_labels)).flatten()

    tp = ((all_preds == 1) & (all_labels == 1)).sum()
    fp = ((all_preds == 1) & (all_labels == 0)).sum()
    fn = ((all_preds == 0) & (all_labels == 1)).sum()
    tn = ((all_preds == 0) & (all_labels == 0)).sum()

    precision = tp / (tp + fp + 1e-9)
    recall    = tp / (tp + fn + 1e-9)
    f1        = 2 * precision * recall / (precision + recall + 1e-9)
    fpr       = fp / (fp + tn + 1e-9)

    print("### Metryki")
    print(f"-  Precision : {precision:.4f}   (ile z 'phishing' to naprawdę phishing)")
    print(f"-  Recall    : {recall:.4f}   (ile phishingów zostało wykrytych)")
    print(f"-  F1        : {f1:.4f}")
    print(f"-  FPR       : {fpr:.4f}   (ile legit URL-i fałszywie oznaczono jako phishing)\n")

    errors = all_preds != all_labels
    high_conf_errors = errors & (np.abs(all_probs - 0.5) > 0.4)
    print(f"### Błędy wysokiej pewności (|prob−0.5|>0.4)")
    print(f"-  Liczba: {high_conf_errors.sum()} / {errors.sum()} błędów ogółem\n")

    lengths = np.array([len(str(u)) for u in new_urls])
    print("### F1 według długości URL")
    for lo, hi in [(0, 50), (50, 100), (100, 150), (150, 200), (200, 999)]:
        mask = (lengths >= lo) & (lengths < hi)
        if mask.sum() < 100:
            continue
        tp_ = ((all_preds[mask] == 1) & (all_labels[mask] == 1)).sum()
        fp_ = ((all_preds[mask] == 1) & (all_labels[mask] == 0)).sum()
        fn_ = ((all_preds[mask] == 0) & (all_labels[mask] == 1)).sum()
        p_  = tp_ / (tp_ + fp_ + 1e-9)
        r_  = tp_ / (tp_ + fn_ + 1e-9)
        f_  = 2 * p_ * r_ / (p_ + r_ + 1e-9)
        print(f"-  [{lo:3d}–{hi:3d} znaków]  n={mask.sum():7,}  F1={f_:.4f}")
    print()

    print("### Rozkład predykcji")
    buckets = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.01]
    for lo, hi in zip(buckets, buckets[1:]):
        mask = (all_probs >= lo) & (all_probs < hi)
        n = mask.sum()
        if n == 0:
            continue
        acc = (all_preds[mask] == all_labels[mask]).mean()
        bar = '█' * int(n / len(all_probs) * 40)
        print(f"-  [{lo:.1f}–{hi:.1f}]  n={n:8,}  acc={acc:.3f}  {bar}")
    print()

    def get_domain(url):
        s = str(url)
        if not s.startswith(("http://", "https://")):
            s = "https://" + s
        try:
            return urlparse(s).netloc
        except Exception:
            return 'unknown'

    urls_list    = new_urls.tolist() if hasattr(new_urls, 'tolist') else list(new_urls)
    error_urls   = [u for u, e in zip(urls_list, errors) if e]
    error_preds  = all_preds[errors]
    error_labels = all_labels[errors]

    error_details = [(get_domain(u), p, l) for u, p, l in zip(error_urls, error_preds, error_labels)]
    error_counts  = Counter(error_details)

    print("### Top 10 domen w błędach (Domena | Model | Prawda)")
    for (dom, pred, label), cnt in error_counts.most_common(10):
        print(f"  {cnt:6,}×  {dom:<35} | Model: {'Phishing (1)' if pred==1 else 'Legit (0)':<12} | Prawda: {'Phishing (1)' if label==1 else 'Legit (0)'}")

    return dict(precision=precision, recall=recall, f1=f1, fpr=fpr,
                n_errors=errors.sum(), n_high_conf_errors=high_conf_errors.sum())


def export_hard_negatives_to_csv(trainer, urls, true_labels, output_filename="hard_negatives_distilbert.csv"):
    import pandas as pd
    trainer.model.eval()
    all_preds = []

    dataloader = _build_eval_loader(trainer, urls, true_labels)

    with torch.no_grad():
        for batch in dataloader:
            if trainer.use_features:
                input_ids, attention_mask, features, y = batch
                logit = trainer.model(input_ids.to(trainer.cfg.DEVICE),
                                      attention_mask.to(trainer.cfg.DEVICE),
                                      features.to(trainer.cfg.DEVICE))
            else:
                input_ids, attention_mask, y = batch
                logit = trainer.model(input_ids.to(trainer.cfg.DEVICE),
                                      attention_mask.to(trainer.cfg.DEVICE))
            probs = torch.sigmoid(logit).squeeze(-1).cpu().numpy()
            if probs.ndim == 0:
                probs = np.array([probs])
            all_preds.extend((probs >= 0.5).astype(int))

    all_preds  = np.array(all_preds).flatten()
    all_labels = (true_labels.values if hasattr(true_labels, 'values') else np.array(true_labels)).flatten()
    urls_list  = urls.tolist() if hasattr(urls, 'tolist') else list(urls)

    df = pd.DataFrame({'url': urls_list, 'true_label': all_labels, 'prediction': all_preds})
    df_errors = df[df['true_label'] != df['prediction']][['url', 'true_label']].rename(columns={'true_label': 'label'})
    df_errors.to_csv(output_filename, index=False)
    print(f"Zapisano {len(df_errors)} hard negatives do '{output_filename}'.")


# ── Funkcje testowe ──────────────────────────────────────────────────────────

data = ImportData()


def diagnoze_at_all_sets(trainer):
    for num, fn in [(1, data.Import_set_1), (2, data.Import_set_2),
                    (3, data.Import_set_3), (4, data.Import_set_4)]:
        fn()
        X, y = data.Get_NLP()
        print(f"## SET - {num}")
        diagnose(trainer, X, y)
        print()


def test_model_DistilBERT():
    from models.transformers.model import DistilBERT_Model
    from models.transformers.config import cfg
    from trainer import Trainer_DistilBERT

    model = DistilBERT_Model(cfg)
    model.load_state_dict(torch.load(cfg.PATH, weights_only=True))

    trainer = Trainer_DistilBERT(model, cfg)
    if cfg.USE_FEATURES:
        trainer.load_scaler()

    diagnoze_at_all_sets(trainer)


if __name__ == "__main__":
    test_model_DistilBERT()