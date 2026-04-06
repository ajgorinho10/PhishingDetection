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
    #DENSE_DIM     = 256
    DROPOUT       = 0.4


    # Trening
    BATCH_SIZE    = 1024
    EPOCHS        = 20
    LR            = 1e-3
    #LR_MIN        = 1e-5
    #WEIGHT_DECAY  = 1e-4
    PATIENCE      = 5            
    #LABEL_SMOOTH  = 0.05

    DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
    PATH = 'CNN/best.pth'


cfg = Config()