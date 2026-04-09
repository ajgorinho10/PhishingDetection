import torch
import torch.nn as nn

from Set_Processor import ImportData
from models_utils import ModelTfIDF
from .config import cfg

class MLP(nn.Module, ModelTfIDF):
    def __init__(self, cfg):
        super().__init__()
        
        self.cfg = cfg
        

        self.dense_in_dim = self.cfg.TFIDF_FEATURES + (self.cfg.FEATURES_LEN if self.cfg.USE_FEATURES else 0)
        
        self.dense = nn.Sequential(
            nn.Linear(self.dense_in_dim, self.cfg.DENSE_DIM),
            nn.ReLU(),
            nn.Dropout(self.cfg.DROPOUT),

            nn.Linear(self.cfg.DENSE_DIM, self.cfg.DENSE_DIM // 2),
            nn.ReLU(),
            nn.Dropout(self.cfg.DROPOUT),
            
            nn.Linear(self.cfg.DENSE_DIM // 2, self.cfg.DENSE_DIM // 4),
            nn.ReLU(),
            nn.Dropout(self.cfg.DROPOUT),

            nn.Linear(self.cfg.DENSE_DIM // 4, 1),
        )

    def forward(self, x, features=None):
        if self.cfg.USE_FEATURES and features is not None:
            x = torch.cat([x, features], dim = -1)
        
        return self.dense(x)
    
    def run_training(self, X, y):
        from trainer import Trainer_TfIDF
        trainer = Trainer_TfIDF(self, self.cfg, [X, y])
        trainer.train()

if __name__ == "__main__":
    dane = ImportData()
    dane.read_set_1()
    X, y = dane.Get_NLP()

    mlp = MLP(cfg)
    mlp.run_training(X, y)