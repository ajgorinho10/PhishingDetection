import torch
import joblib

class ModelTokens:
    def __init__(self, cfg):
        self.cfg = cfg

    def run_training(self, X, y):
        from trainer import Trainer_Tokens
        data_to_trainer = [X, y]
        trainer = Trainer_Tokens(
            self, 
            data_sets=data_to_trainer, 
            cfg=self.cfg
        )
        trainer.train()
        
    def evaluate(self, X, y):
        from trainer import Trainer_Tokens
        trainer = Trainer_Tokens(self, cfg=self.cfg, data_sets=None)
        
        if self.cfg.USE_FEATURES:
            trainer.scaler = joblib.load(self.cfg.SCALER_PATH)
            X_features = trainer.get_data_features(X)
            
            X_features = torch.tensor(
                trainer.scaler.transform(X_features.numpy()), 
                dtype=torch.float32
            )
            
            data_loader = trainer.get_data_loaders(*trainer.get_tokenized_tensors(X, y), X_features, shuffled=False)
        else:
            data_loader = trainer.get_data_loaders(*trainer.get_tokenized_tensors(X, y), shuffled=False)
            
        trainer.evaluate(data_loader)
               
        
        
class ModelTfIDF:
    def __init__(self, cfg):
        self.cfg = cfg

    def run_training(self, X, y):
        from trainer import Trainer_TfIDF
        data_to_trainer = [X, y]
        trainer = Trainer_TfIDF(
            self, 
            dataset=data_to_trainer, 
            cfg=self.cfg
        )
        trainer.train()
        
    def evaluate(self, X, y):
        from trainer import Trainer_TfIDF
        trainer = Trainer_TfIDF(self, cfg=self.cfg, dataset=None)
        
        trainer.ftidfVectorizer = joblib.load(self.cfg.FTIDF_PATH)
        X_tfidf = trainer.ftidfVectorizer.transform(X)
        
        if self.cfg.USE_FEATURES:
            trainer.scaler = joblib.load(self.cfg.SCALER_PATH)
            X_features = trainer.get_data_features(X)
            
            X_features = torch.tensor(
                trainer.scaler.transform(X_features.numpy()), 
                dtype=torch.float32
            )
            
            data_loader = trainer.get_data_loaders(X_tfidf, y, X_features, shuffled=False)
        else:
            data_loader = trainer.get_data_loaders(X_tfidf, y, shuffled=False)
            
        trainer.evaluate(data_loader)