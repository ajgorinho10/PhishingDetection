import torch

class Config:

    TFIDF_FEATURES = 3000
    USE_FEATURES   = False
    FEATURES_LEN   = 8


    MAX_DEPTH        = 6
    LEARNING_RATE    = 0.1
    N_ESTIMATORS     = 1000
    SUBSAMPLE        = 0.8
    COLSAMPLE_BYTREE = 0.8
    PATIENCE         = 10 


    DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
    PATH = 'models/XGBoost/best.json'
    SCALER_PATH = 'models/XGBoost/scaler.pkl'
    FTIDF_PATH = 'models/XGBoost/ftidf.pkl'

    BATCH_SIZE = 1024

cfg = Config()