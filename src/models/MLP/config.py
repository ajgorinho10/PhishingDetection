import torch

class Config:
    # Tokenizacja (Dla modeli sekwencyjnych)
    MAX_LEN       = 200          
    VOCAB_SIZE    = 102          
    PAD_IDX       = 0
    UNK_IDX       = 1

    # Model
    TFIDF_FEATURES= 3000         # NOWE: Maksymalna liczba cech z TF-IDF
    DENSE_DIM     = 512          # Rozmiar warstwy ukrytej (po redukcji)
    DROPOUT       = 0.4
    USE_FEATURES  = True
    FEATURES_LEN  = 8

    # Trening
    BATCH_SIZE    = 1024
    EPOCHS        = 20
    LR            = 1e-3
    PATIENCE      = 2            

    DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
    PATH = 'models/MLP/best.pth'
    SCALER_PATH = 'models/MLP/scaler.pkl'
    FTIDF_PATH = 'models/MLP/ftidf.pkl'

cfg = Config()