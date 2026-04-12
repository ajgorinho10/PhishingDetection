import torch
import numpy as np
import scipy.sparse as sp
import xgboost as xgb
from Set_Processor import ImportData
from .config import cfg

class XGBoostWrapper:
    def __init__(self, cfg):
        self.cfg = cfg
        
        tree_method = "hist"
        device = "cuda" if self.cfg.DEVICE == "cuda" else "cpu"
        
        self.model = xgb.XGBClassifier(
            max_depth=self.cfg.MAX_DEPTH,
            learning_rate=self.cfg.LEARNING_RATE,
            n_estimators=self.cfg.N_ESTIMATORS,
            subsample=self.cfg.SUBSAMPLE,
            colsample_bytree=self.cfg.COLSAMPLE_BYTREE,
            tree_method=tree_method,
            device=device,
            objective='binary:logistic',
            eval_metric='logloss',
            early_stopping_rounds=self.cfg.PATIENCE
        )

    def eval(self):
        pass
        
    def to(self, device):
        return self
        
    def __call__(self, x_tfidf, features=None):
        x_np = x_tfidf.cpu().numpy()
        
        if self.cfg.USE_FEATURES and features is not None:
            feat_np = features.cpu().numpy()
            x_combined = np.hstack([x_np, feat_np])
        else:
            x_combined = x_np
            
        x_sparse = sp.csr_matrix(x_combined, dtype=np.float32)
        dmat = xgb.DMatrix(x_sparse)
        
        margins = self.model.get_booster().predict(dmat, output_margin=True)
        return torch.tensor(margins, dtype=torch.float32).to(self.cfg.DEVICE)
        
    def save(self, path):
        self.model.save_model(path)
        
    def load(self, path):
        self.model.load_model(path)
        
    def run_training(self, X, y):
        from trainer import Trainer_XGB
        trainer = Trainer_XGB(self, self.cfg, dataset=[X, y])
        trainer.train()

if __name__ == "__main__":
    dane = ImportData()
    dane.Import_set_4()
    X, y = dane.Get_NLP()

    xgb_model = XGBoostWrapper(cfg)
    xgb_model.run_training(X, y)