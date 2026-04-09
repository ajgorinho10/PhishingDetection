import torch

#CNN
class Config:
    # Tokenizacja
    MAX_LEN       = 200          
    VOCAB_SIZE    = 102          
    PAD_IDX       = 0
    UNK_IDX       = 1

    # Model
    EMBED_DIM     = 64
    CNN_FILTERS   = 256
    CNN_KERNELS   = [3, 5, 7]
    DROPOUT       = 0.4
    USE_FEATURES  = False
    FEATURES_LEN  = 8


    # Trening
    BATCH_SIZE    = 1024
    EPOCHS        = 20
    LR            = 1e-3
    PATIENCE      = 2            

    DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
    PATH = 'models/CNN/best.pth'
    SCALER_PATH = 'models/CNN/scaler.pkl'


cfg = Config()