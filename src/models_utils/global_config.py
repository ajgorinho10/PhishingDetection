import torch

class Config:
    # Tokenizacja
    MAX_LEN       = 200          
    VOCAB_SIZE    = 102          
    PAD_IDX       = 0
    UNK_IDX       = 1

    # Trening
    BATCH_SIZE    = 1024
    EPOCHS        = 20
    LR            = 1e-3
    PATIENCE      = 3

    DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

cfg = Config()