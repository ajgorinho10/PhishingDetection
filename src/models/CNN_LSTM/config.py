import torch

#CNN + LSTM
class Config:
    # Tokenizacja
    MAX_LEN       = 200          
    VOCAB_SIZE    = 102          
    PAD_IDX       = 0
    UNK_IDX       = 1

    # Model
    EMBED_DIM     = 64
    CNN_FILTERS   = 256
    CNN_KERNELS   = [3, 5]       
    LSTM_UNITS    = 128          
    ATTN_DIM      = 128
    DENSE_DIM     = 256
    DROPOUT       = 0.4

    # Trening
    BATCH_SIZE    = 1024
    EPOCHS        = 20
    LR            = 1e-3
    PATIENCE      = 3            

    DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
    PATH = 'models/CNN_LSTM/best.pth'


cfg = Config()