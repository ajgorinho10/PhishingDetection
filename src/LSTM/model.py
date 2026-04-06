import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Set_Processor import ImportData

import torch
import torch.nn as nn
import torch.nn.functional as F


import numpy as np
from typing import Optional,Tuple

from trainer import Trainer
from config import cfg


class AdditiveAttention(nn.Module):
    """
    Self-attention: ważone sumowanie ukrytych stanów LSTM.
 
    Wejście: (B, T, H)  — batch, czas, wymiar
    Wyjście: (B, H)     — kontekstowy wektor dla całego URL-a
    """
    def __init__(self, hidden_dim: int, attn_dim: int):
        super().__init__()
        self.W = nn.Linear(hidden_dim, attn_dim, bias=False)
        self.v = nn.Linear(attn_dim, 1, bias=False)
 
    def forward(
        self,
        hidden: torch.Tensor,                    # (B, T, H)
        mask: Optional[torch.Tensor] = None      # (B, T) bool
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        # Wylicz energię
        energy = self.v(torch.tanh(self.W(hidden)))  # (B, T, 1)
        energy = energy.squeeze(-1)                  # (B, T)
        if mask is not None:
            energy = energy.masked_fill(mask, float("-inf"))
        weights = F.softmax(energy, dim=-1)          # (B, T)
        context = torch.bmm(weights.unsqueeze(1), hidden).squeeze(1)  # (B, H)
        return context, weights


class LSTM(nn.Module):
    def __init__(self):
        super().__init__()
        
        self.embanding = nn.Embedding(
            num_embeddings = cfg.VOCAB_SIZE,
            embedding_dim  = cfg.EMBED_DIM,
            padding_idx    = cfg.PAD_IDX
        )
        
        #Warstwa LSTM
        self.lstm1 =nn.LSTM(
                input_size    = cfg.EMBED_DIM,
                hidden_size   = cfg.LSTM_UNITS,
                num_layers    = 1,
                bias          = False,
                batch_first   = True,
                dropout       = 0.0,
                bidirectional = True
            )
            
        self.dropout = nn.Dropout(cfg.DROPOUT)
            
        self.lstm2 = nn.LSTM(
                input_size    = cfg.LSTM_UNITS*2,
                hidden_size   = cfg.EMBED_DIM,
                num_layers    = 1,
                bias          = False,
                batch_first   = True,
                dropout       = 0.0,
                bidirectional = True
            )
            
        
        self.lstm_out_dim = cfg.EMBED_DIM * 2
        
        self.attention = AdditiveAttention(self.lstm_out_dim, cfg.ATTN_DIM)

        self.classifier = nn.Sequential(
            nn.Linear(
                in_features  = self.lstm_out_dim,
                out_features = self.lstm_out_dim//2
            ),
            
            nn.ReLU(),
            nn.Dropout(cfg.DROPOUT),
            
            nn.Linear(
                in_features  = self.lstm_out_dim//2,
                out_features = 1
            ),
        )
        
        
    def forward(self, x, return_attention: bool = False):
        x = self.embanding(x)
     
        x, _ = self.lstm1(x)
        
        x = self.dropout(x)
        
        lstm_out, _ = self.lstm2(x)
        
        context, attn_weights = self.attention(lstm_out)
        
        x = self.classifier(context)
        
        if return_attention:
            return x, attn_weights
        
        return x
    
    
    
    def train_model(self, X, y):
        trainer = Trainer(self, [X, y])
        trainer.train()
        
    def evaluate(self, X, y):
        trainer = Trainer(self, None)
        data_loader = trainer.get_data_loaders(*trainer.get_tokenized_tensors(X, y),shuffled = False)
        trainer.evaluate(data_loader)
    


if __name__ == "__main__":
    
    data = ImportData()
    data.Import_set_3()
    X_data, y_data = data.Get_NLP()
    
    lstm = LSTM()
    lstm.train_model(X=X_data, y=y_data)
    
    print(f"{"-" * 50}")
    print("Evaluacja set 2\n")
    data.Import_set_2()
    X, y = data.Get_NLP()
    lstm.evaluate(X, y)
    
    print(f"{"-" * 50}")
    print("Evaluacja set 5\n")
    data.Import_set_5()
    X, y = data.Get_NLP()
    lstm.evaluate(X, y)