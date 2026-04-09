import joblib
import scipy.sparse as sp
import numpy as np
from sklearn.model_selection import train_test_split
from .trainer_tfidf import Trainer_TfIDF

class Trainer_XGB(Trainer_TfIDF):
    def __init__(self, model_wrapper, cfg, dataset=None):
        super().__init__(model_wrapper, cfg, dataset)
        self.model_wrapper = model_wrapper
        
    def train(self):
        X, y = self.dataset[0], self.dataset[1]
        
        X_train, X_test_val, y_train, y_test_val = train_test_split(X, y, test_size=0.3, random_state=42)
        X_test, X_val, y_test, y_val             = train_test_split(X_test_val, y_test_val, test_size=0.5, random_state=42)
        
        X_train_tfidf = self.ftidfVectorizer.fit_transform(X_train)
        X_val_tfidf   = self.ftidfVectorizer.transform(X_val)
        joblib.dump(self.ftidfVectorizer, self.cfg.FTIDF_PATH)
        
        if self.use_features:
            X_train_feat = self.get_data_features(X_train).numpy()
            X_val_feat   = self.get_data_features(X_val).numpy()
            
            X_train_feat = self.scaler.fit_transform(X_train_feat)
            X_val_feat   = self.scaler.transform(X_val_feat)
            joblib.dump(self.scaler, self.cfg.SCALER_PATH)
            
            X_train_final = sp.hstack([X_train_tfidf, X_train_feat])
            X_val_final   = sp.hstack([X_val_tfidf, X_val_feat])
        else:
            X_train_final = X_train_tfidf
            X_val_final   = X_val_tfidf
        

        X_train_final = X_train_final.tocsr().astype(np.float32)
        X_val_final   = X_val_final.tocsr().astype(np.float32)


        y_train_np = (y_train.values if hasattr(y_train, 'values') else np.array(y_train)).flatten().astype(np.float32)
        y_val_np   = (y_val.values if hasattr(y_val, 'values') else np.array(y_val)).flatten().astype(np.float32)
        
        self.model_wrapper.model.fit(
            X_train_final, y_train_np,
            eval_set=[(X_val_final, y_val_np)],
            verbose=50 
        )
        
        self.model_wrapper.save(self.cfg.PATH)