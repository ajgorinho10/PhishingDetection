import joblib
import numpy as np

import torch
from torch.utils.data import DataLoader, Dataset

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

from .trainer import Trainer


class SparseDataset(Dataset):
    def __init__(self, X_sparse, y_data, X_features=None):
        self.X_sparse = X_sparse
        self.X_features = X_features
        
        # Bepieczna konwersja (omija kolizję nazwy .values)
        if isinstance(y_data, torch.Tensor):
            self.y_data = y_data.clone().detach().to(torch.float32).view(-1, 1)
        else:
            y_arr = y_data.to_numpy() if hasattr(y_data, 'to_numpy') else np.array(y_data)
            self.y_data = torch.tensor(y_arr, dtype=torch.float32).view(-1, 1)

    def __len__(self):
        return self.X_sparse.shape[0]

    def __getitem__(self, idx):
        x_dense = torch.tensor(self.X_sparse[idx].toarray().squeeze(), dtype=torch.float32)
        
        if self.X_features is not None:
            return x_dense, self.X_features[idx], self.y_data[idx]
        return x_dense, self.y_data[idx]


class Trainer_TfIDF(Trainer):
    def __init__(self, model, cfg, dataset = None):
        
        super().__init__(model, cfg)
        
        self.dataset = dataset
        self.ftidfVectorizer = TfidfVectorizer(analyzer='char', ngram_range=(3, 5), max_features=cfg.TFIDF_FEATURES)
     
    def load_scaler_tfidf(self):
        self.scaler = joblib.load(self.cfg.SCALER_PATH)
        self.ftidfVectorizer = joblib.load(self.cfg.FTIDF_PATH)
    
    def get_data_loaders(self, X_sparse, y, X_features=None, shuffled=False):
        # Używamy naszej nowej, chroniącej RAM klasy SparseDataset
        train_dataset = SparseDataset(X_sparse, y, X_features)
        train_loader = DataLoader(train_dataset, batch_size=self.cfg.BATCH_SIZE, shuffle=shuffled)
        return train_loader
        
    def splits_data_to_Train_Val_Test(self):
        X, y = self.dataset[0], self.dataset[1]
        
        X_train, X_test_val, y_train, y_test_val = train_test_split(X, y, test_size=0.3, random_state=42)
        X_test, X_val, y_test, y_val             = train_test_split(X_test_val, y_test_val, test_size=0.5, random_state=42)
        
        X_train_tfidf = self.ftidfVectorizer.fit_transform(X_train)
        X_val_tfidf   = self.ftidfVectorizer.transform(X_val)
        X_test_tfidf  = self.ftidfVectorizer.transform(X_test)
        
        joblib.dump(self.ftidfVectorizer, self.cfg.FTIDF_PATH)
        
        X_train_features, X_val_features, X_test_features  = None, None, None
        if self.use_features:
            X_train_features = self.get_data_features(X_train)
            X_val_features   = self.get_data_features(X_val)
            X_test_features  = self.get_data_features(X_test)
            
            X_train_features = torch.tensor(
                self.scaler.fit_transform(X_train_features.numpy()), 
                dtype=torch.float32
            )
            
            X_val_features = torch.tensor(
                self.scaler.transform(X_val_features.numpy()), 
                dtype=torch.float32
            )
            
            X_test_features = torch.tensor(
                self.scaler.transform(X_test_features.numpy()), 
                dtype=torch.float32
            )
            
            joblib.dump(self.scaler, self.cfg.SCALER_PATH)
            

        train_loader    = self.get_data_loaders(X_train_tfidf, y_train,  X_train_features, shuffled = True)
        val_loader      = self.get_data_loaders(X_val_tfidf, y_val,      X_val_features  )
        test_loader     = self.get_data_loaders(X_test_tfidf, y_test,    X_test_features )
        
        return train_loader, val_loader, test_loader