import torch

#LSTM
class Config:
    # Tokenizacja
    MAX_LEN       = 200          # max długość URL (znaki)
    VOCAB_SIZE    = 102          # 96 ASCII + padding + unk + special
    PAD_IDX       = 0
    UNK_IDX       = 1

    # Model
    EMBED_DIM     = 64
    CNN_FILTERS   = 128
    CNN_KERNELS   = [3, 5]       # rozmiary filtrów
    LSTM_UNITS    = 128          # wyjście = 128*2 (bi-directional)
    ATTN_DIM      = 128
    DENSE_DIM     = 256
    DROPOUT       = 0.3

    # Cechy ręczne (hand-crafted features)
    N_HAND_FEATS  = 10

    # Trening
    BATCH_SIZE    = 1024
    EPOCHS        = 20
    LR            = 1e-3
    LR_MIN        = 1e-5
    WEIGHT_DECAY  = 1e-4
    PATIENCE      = 3            # early stopping
    LABEL_SMOOTH  = 0.05

    DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
    PATH = 'models/LSTM/best.pth'


cfg = Config()