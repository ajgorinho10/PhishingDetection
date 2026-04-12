import torch

class Config:
    # Parametry ogólne i danych
    USE_FEATURES = False
    FEATURES_LEN = 8
    VOCAB_SIZE   = 102   # Twój CharTokenizer ma słownik około 70-100 znaków
    MAX_LEN      = 200   # Maksymalna długość URL po paddingu
    PADIDX       = 0
    UNKIDX       = 1

    # Parametry Transformera
    EMBED_DIM     = 128          # d_model — musi być podzielne przez N_HEADS
    N_HEADS       = 8            # liczba głowic attention; dim_head = 128/8 = 16
    N_LAYERS      = 4            # liczba warstw encodera
    DIM_FF        = 512          # wymiar feed-forward (typowo 4 × EMBED_DIM)
    DROPOUT       = 0.1          # dropout w attention i FFN
    MAX_SEQ_LEN   = MAX_LEN + 1  # +1 dla tokenu [CLS]
    CLS_IDX = VOCAB_SIZE

    # Klasyfikator
    DENSE_DIM     = 128
    CLF_DROPOUT   = 0.3

    # Trening
    BATCH_SIZE   = 1024   
    EPOCHS       = 40
    LR           = 5e-4  
    PATIENCE     = 5
    WARMUP_STEPS = 1000
    WARNUP       = True

    DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
    PATH = 'models/transformers/best.pth'
    SCALER_PATH = 'models/transformers/scaler.pkl'

cfg = Config()