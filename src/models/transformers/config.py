import torch

class Config:
    USE_FEATURES = True
    FEATURES_LEN = 8

    # POPRAWKA: 128 zamiast 200 — WordPiece tokenizuje URL do ~10-30 tokenów,
    # nie 200 znaków. MAX_LEN=200 to ~85% padding na typowym URL.
    MAX_LEN      = 128

    # DistilBERT nie używa PAD_IDX=0 bezpośrednio — padding obsługuje attention_mask.
    # Zostaje dla zgodności z konfiguracją projektu.
    PADIDX       = 0

    MODEL_NAME   = "distilbert-base-uncased"
    DENSE_DIM    = 128
    CLF_DROPOUT  = 0.3

    BATCH_SIZE   = 64
    EPOCHS       = 5
    LR           = 2e-5
    PATIENCE     = 3
    WARMUP_STEPS = 100

    DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
    PATH        = 'models/transformers/best.pth'
    SCALER_PATH = 'models/transformers/scaler.pkl'

cfg = Config()