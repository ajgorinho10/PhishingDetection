import joblib
import numpy as np

import torch
from torch.utils.data import TensorDataset, DataLoader

from sklearn.model_selection import train_test_split

from models_utils import CharTokenizer
from .trainer import Trainer


class Trainer_Tokens(Trainer):
    
    def __init__(self, model, cfg, data_sets = None):
        super().__init__(model, cfg)

        self.data = data_sets
        self.tokenizer = CharTokenizer()
        
    def load_scaler(self):
        self.scaler = joblib.load(self.cfg.SCALER_PATH)       
              
    def get_tokenized_tensors(self, X_data, y_data):   
        X_tensor = torch.tensor(self.tokenizer.encode_dataset(X_data), dtype=torch.long)
        
        if isinstance(y_data, torch.Tensor):
            y_tensor = y_data.clone().detach().to(torch.float32).view(-1, 1)
        else:
            y_arr = y_data.to_numpy() if hasattr(y_data, 'to_numpy') else np.array(y_data)
            y_tensor = torch.tensor(y_arr, dtype=torch.float32).view(-1, 1)
            
        return X_tensor, y_tensor
    
    
    def get_data_loaders(self, X_data, y_data, X_features = None, shuffled = False):
        dataset = None
        
        if self.use_features and X_features is not None:
            dataset = TensorDataset(X_data, X_features, y_data)
        else:
            dataset = TensorDataset(X_data, y_data)
            
        dataloader = DataLoader(dataset, batch_size=self.cfg.BATCH_SIZE, shuffle = shuffled)
        
        return dataloader
    
    
    def splits_data_to_Train_Val_Test(self):
        X, y = self.data[0], self.data[1]
        
        X_train, X_test_val, y_train, y_test_val = train_test_split(X, y, test_size=0.3, random_state=42)
        X_test, X_val, y_test, y_val             = train_test_split(X_test_val, y_test_val, test_size=0.5, random_state=42)
                    
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
         
        train_loader    = self.get_data_loaders(*self.get_tokenized_tensors(X_train, y_train),  X_train_features, shuffled = True)
        val_loader      = self.get_data_loaders(*self.get_tokenized_tensors(X_val, y_val),      X_val_features  )
        test_loader     = self.get_data_loaders(*self.get_tokenized_tensors(X_test, y_test),    X_test_features )
        
        return train_loader, val_loader, test_loader
    
