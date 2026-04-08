
from models_utils import Trainer

from sklearn.preprocessing import StandardScaler

import torch
import joblib

class BaseModel:
    def __init__(self, cfg):
        self.cfg = cfg
                

    def run_training(self, X, y):
        data_to_trainer = [X, y]
        trainer = Trainer(
            self, 
            data_sets=data_to_trainer, 
            cfg=self.cfg
        )
        trainer.train()
        
    def evaluate(self, X, y):
        trainer = Trainer(self, cfg=self.cfg, data_sets=None)
        
        if self.cfg.USE_FEATURES:
            trainer.scaler = joblib.load(self.cfg.SCALER_PATH)
            X_features = trainer.get_data_features(X)
            
            scaler = StandardScaler()
            
            X_features = torch.tensor(
                scaler.fit_transform(X_features.numpy()), 
                dtype=torch.float32
            )

            
            data_loader = trainer.get_data_loaders(*trainer.get_tokenized_tensors(X, y), X_features, shuffled=False)
        else:
            data_loader = trainer.get_data_loaders(*trainer.get_tokenized_tensors(X, y), shuffled=False)
            
        trainer.evaluate(data_loader)