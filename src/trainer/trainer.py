import matplotlib.pyplot as plt
import math

import torch
import torch.nn as nn
import torch.nn.functional as F

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    classification_report, 
    confusion_matrix, 
    f1_score, 
    accuracy_score, 
    recall_score)


from models_utils import EarlyStopping

from Set_Processor import FeaturesExtraction

def get_scheduler(optimizer, warmup_steps: int, total_steps: int):
    def lr_lambda(step: int) -> float:
        if step < warmup_steps:
            return float(step) / max(1, warmup_steps)
        progress = (step - warmup_steps) / max(1, total_steps - warmup_steps)
        return max(0.0, 0.5 * (1.0 + math.cos(math.pi * progress)))
    
    return torch.optim.lr_scheduler.LambdaLR(optimizer, lr_lambda)

class FocalLoss(nn.Module):
    def __init__(self, alpha=0.25, gamma=2.0):
        super().__init__()
        self.alpha = alpha
        self.gamma = gamma

    def forward(self, inputs, targets):
        bce_loss = F.binary_cross_entropy_with_logits(inputs, targets, reduction='none')
        pt = torch.exp(-bce_loss) 
        focal_loss = self.alpha * (1 - pt) ** self.gamma * bce_loss
        return focal_loss.mean()

class Trainer:
    
    def __init__(self, model, cfg):
        self.model = model
        self.model.to(cfg.DEVICE)
        self.cfg = cfg
        self.use_features = cfg.USE_FEATURES
        self.scaler = StandardScaler()
        
        if hasattr(self.model, 'parameters'):
            self.optimizer  = torch.optim.AdamW(self.model.parameters(), lr=cfg.LR, weight_decay=1e-4)
            self.scheduler  = torch.optim.lr_scheduler.CosineAnnealingLR(
                self.optimizer, T_max=cfg.EPOCHS, eta_min=1e-5
            )
        else:
            self.optimizer = None
            self.scheduler = None
            
        self.loss_f = FocalLoss(alpha=0.25, gamma=2.0)
        self.early_stopping = EarlyStopping(patience=cfg.PATIENCE, min_delta=0.001, path = cfg.PATH)
        
        self.history = {'train_loss': [], 'val_loss': [], 'f1': [], 'acc': [], 'recal': []}
         
    
    def get_data_features(self, X_data):
        features = FeaturesExtraction()
        
        extracted_features = []
        for url in X_data:
            tmp = []
            tmp.append(features.count_subdomains(url))
            tmp.append(features.has_redirect_pattern(url))
            tmp.append(features.get_path_depth(url))
            tmp.append(features.has_ip_domain(url))
            tmp.append(features.is_shortener(url))
            tmp.append(features.is_risky_tld(url))
            tmp.append(features.has_punycode(url))
            tmp.append(features.special_char_ratio(url))
            extracted_features.append(tmp)
            
        return torch.tensor(extracted_features, dtype=torch.float32)
    
    @torch.no_grad()
    def evaluate(self, valDataLoader):
        self.model.load_state_dict(torch.load(self.cfg.PATH))
        print("Załadowano optymalne wagi do modelu.")
        
        wszystkie_predykcje = []
        wszystkie_etykiety = []
        
        self.model.to(self.cfg.DEVICE)
        self.model.eval()

        if self.use_features:
            for batch_X, batch_features, batch_y in valDataLoader:
                batch_X, batch_features, batch_y = batch_X.to(self.cfg.DEVICE), batch_features.to(self.cfg.DEVICE), batch_y.to(self.cfg.DEVICE)
                output_raw = self.model(batch_X, batch_features)
                output = torch.sigmoid(output_raw).squeeze(-1).round().cpu().numpy()
                
                wszystkie_predykcje.extend(output)
                wszystkie_etykiety.extend(batch_y.cpu().numpy().flatten())
        else:
            for batch_X, batch_y in valDataLoader:
                batch_X, batch_y = batch_X.to(self.cfg.DEVICE), batch_y.to(self.cfg.DEVICE)
                output_raw = self.model(batch_X)
                output = torch.sigmoid(output_raw).squeeze(-1).round().cpu().numpy()
                
                wszystkie_predykcje.extend(output)
                wszystkie_etykiety.extend(batch_y.cpu().numpy().flatten())
                
        print("\nRaport końcowy:")
        print(classification_report(wszystkie_etykiety, wszystkie_predykcje))
        print(confusion_matrix(wszystkie_etykiety, wszystkie_predykcje))
              
              
    def splits_data_to_Train_Val_Test(self):
        pass
    
    
    def _train_epoch(self, data_loader):    
        self.model.train()
        running_train_loss = 0.0
            
        for batch_X, batch_y in data_loader:
            batch_X, batch_y = batch_X.to(self.cfg.DEVICE), batch_y.to(self.cfg.DEVICE)
                
            self.optimizer.zero_grad(set_to_none=True)
            output = self.model(batch_X)
            loss = self.loss_f(output, batch_y)
            loss.backward()
                
            nn.utils.clip_grad_norm_(self.model.parameters(), max_norm=1.0)
            self.optimizer.step()
                
            if hasattr(self.cfg, 'WARMUP_STEPS') is True:
                self.scheduler.step()
                
            running_train_loss += loss.item()
                
        return running_train_loss / len(data_loader)

    def _train_epoch_with_features(self, data_loader):
        self.model.train()
        running_train_loss = 0.0
            
        for batch_X, batch_features, batch_y in data_loader:
            batch_X, batch_features, batch_y = batch_X.to(self.cfg.DEVICE), batch_features.to(self.cfg.DEVICE), batch_y.to(self.cfg.DEVICE)
                
            self.optimizer.zero_grad(set_to_none=True)
            output = self.model(batch_X, batch_features)
            loss = self.loss_f(output, batch_y)
            loss.backward()
                
            
            nn.utils.clip_grad_norm_(self.model.parameters(), max_norm=1.0)
            self.optimizer.step()
            
            if hasattr(self.cfg, 'WARMUP_STEPS') is True:
                self.scheduler.step()
            
            running_train_loss += loss.item()
                
        return running_train_loss / len(data_loader)
            
    def _val_epoch(self, data_loader):
        self.model.eval()
        running_val_loss = 0.0
            
        running_labels = []
        running_predicts = []
        metrics = {}
                
        with torch.no_grad():
            for batch_X, batch_y in data_loader:
                batch_X, batch_y = batch_X.to(self.cfg.DEVICE), batch_y.to(self.cfg.DEVICE)
                output = self.model(batch_X)
                loss = self.loss_f(output, batch_y)
                running_val_loss += loss.item()

                running_labels.extend(batch_y.cpu().numpy().flatten())
                running_predicts.extend(torch.sigmoid(output).squeeze(-1).round().cpu().numpy())
                        
            metrics['val_loss'] = running_val_loss / len(data_loader)
            metrics['f1']       = f1_score      (running_labels,running_predicts, zero_division = 0)
            metrics['acc']      = accuracy_score(running_labels,running_predicts)
            metrics['recal']    = recall_score  (running_labels,running_predicts, zero_division = 0)
                
            return metrics
        
        
    def _val_epoch_with_features(self, data_loader):
        self.model.eval()
        running_val_loss = 0.0
            
        running_labels = []
        running_predicts = []
        metrics = {}
                
        with torch.no_grad():
            for batch_X, batch_features, batch_y in data_loader:
                batch_X, batch_features, batch_y = batch_X.to(self.cfg.DEVICE), batch_features.to(self.cfg.DEVICE), batch_y.to(self.cfg.DEVICE)
                output = self.model(batch_X, batch_features)
                loss = self.loss_f(output, batch_y)
                running_val_loss += loss.item()

                running_labels.extend(batch_y.cpu().numpy().flatten())
                running_predicts.extend(torch.sigmoid(output).squeeze(-1).round().cpu().numpy())
                        
            metrics['val_loss'] = running_val_loss / len(data_loader)
            metrics['f1']       = f1_score      (running_labels,running_predicts, zero_division = 0)
            metrics['acc']      = accuracy_score(running_labels,running_predicts)
            metrics['recal']    = recall_score  (running_labels,running_predicts, zero_division = 0)
                
            return metrics
        
      
    def train(self): 
        train_loader, val_loader, test_loader = self.splits_data_to_Train_Val_Test()
        
        if hasattr(self.cfg, 'WARMUP_STEPS'):
            total_steps = len(train_loader) * self.cfg.EPOCHS
            self.scheduler = get_scheduler(self.optimizer,self.cfg.WARMUP_STEPS,total_steps)

        for epoch in range(self.cfg.EPOCHS):
            if self.use_features:
                avg_train_loss  = self._train_epoch_with_features(train_loader)
                metrics         = self._val_epoch_with_features  (val_loader)
                
            else:
                avg_train_loss  = self._train_epoch(train_loader)
                metrics         = self._val_epoch(val_loader)
            
            avg_val_loss = metrics['val_loss']
            
            self.history['train_loss'].append(avg_train_loss)
            self.history['val_loss'].append(avg_val_loss)
            self.history['f1'].append(metrics['f1'])
            self.history['acc'].append(metrics['acc'])
            self.history['recal'].append(metrics['recal'])
            
            print(
                          f"Epoka: [{epoch+1}/{self.cfg.EPOCHS}]",
                  f" | Train Loss: {avg_train_loss  :.4f}",
                    f" | Val Loss: {avg_val_loss    :.4f}",
                      f" | Val F1: {metrics['f1']   :.4f}",
                     f" | Val Acc: {metrics['acc']  :.4f}",
                   f" | Val Recal: {metrics['recal']:.4f}"
            )
            
            if hasattr(self.cfg, 'WARMUP_STEPS') is False:
                self.scheduler.step()
            
            self.early_stopping(avg_val_loss, self.model)
            if self.early_stopping.early_stop:
                print(f"Zatrzymano trening wcześnie w epoce {epoch+1}. Brak poprawy funkcji straty.")
                break
                
        self.evaluate(test_loader)
        #self.plot_history()
        
        
    def plot_history(self):
        epoki = range(1, len(self.history['train_loss']) + 1)
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        
        ax1.plot(epoki, self.history['train_loss'], label='Train Loss', marker='o')
        ax1.plot(epoki, self.history['val_loss'], label='Val Loss', marker='o')
        ax1.set_title('Zmiana funkcji straty')
        ax1.set_xlabel('Epoka')
        ax1.set_ylabel('Loss')
        ax1.grid(True, linestyle='--', alpha=0.7)
        ax1.legend()
        
        ax2.plot(epoki, self.history['f1'], label='Val F1', marker='s')
        ax2.plot(epoki, self.history['acc'], label='Val Acc', marker='s')
        ax2.plot(epoki, self.history['recal'], label='Val Recall', marker='s')
        ax2.set_title('Metryki walidacyjne')
        ax2.set_xlabel('Epoka')
        ax2.set_ylabel('Wartość')
        ax2.grid(True, linestyle='--', alpha=0.7)
        ax2.legend()
        
        plt.tight_layout()
        plt.show()
        
