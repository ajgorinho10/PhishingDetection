import torch
import torch.nn as nn
import torch.nn.functional as F

import numpy as np

from typing import Optional, Tuple

from config import cfg
from trainer import Trainer

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

class CNN_LSTM(nn.Module):
    def __init__(self):
        super().__init__()
        
        self.embedding = nn.Embedding(
            num_embeddings=cfg.VOCAB_SIZE,
            embedding_dim=cfg.EMBED_DIM,
            padding_idx=cfg.PAD_IDX
        )
        #self.embedding.weight.data[cfg.PAD_IDX].zero_()
        
        self.conv_blocks = nn.ModuleList([
            nn.Sequential(
               nn.Conv1d(
                   in_channels  = cfg.EMBED_DIM,
                   out_channels = cfg.CNN_FILTERS,
                   kernel_size  = k,
                   padding      = k//2
               ),
               nn.BatchNorm1d(cfg.CNN_FILTERS),
               nn.ReLU(),
               nn.MaxPool1d(kernel_size = 2, stride= 2)
            ) 
            for k in cfg.CNN_KERNELS
        ])
        
        self.conv_out_dim = cfg.CNN_FILTERS * len(cfg.CNN_KERNELS)
        
        self.cnn_proj = nn.Sequential(
            nn.Linear(
                in_features=self.conv_out_dim,
                out_features=cfg.EMBED_DIM
            ),
            nn.ReLU(),
            nn.Dropout(cfg.DROPOUT * 0.5)
        )
        
        self.lstm = nn.LSTM(
            input_size      = cfg.EMBED_DIM,
            hidden_size     = cfg.LSTM_UNITS,
            num_layers      = 1,
            batch_first     = True,
            bidirectional   = True,
            dropout         = 0.0 
        )
        
        self.lstm_out_dim = cfg.LSTM_UNITS * 2
        
        
        self.attention = AdditiveAttention(self.lstm_out_dim, cfg.ATTN_DIM)
        
        self.classifier = nn.Sequential(
            nn.Linear(
                in_features  = self.lstm_out_dim,
                out_features = cfg.DENSE_DIM
            ),
            nn.ReLU(),
            nn.Dropout(cfg.DROPOUT),
            
            nn.Linear(
                in_features  = cfg.DENSE_DIM,
                out_features = 64
            ),
            nn.ReLU(),
            nn.Dropout(cfg.DROPOUT * 0.5),
            
            nn.Linear(
                in_features  = 64,
                out_features = 1
            ),
        )
    
    
    def forward(self, x, return_attention:bool = False):
        x = self.embedding(x)
        x = x.permute(0,2,1)
        
        x = [block(x) for block in self.conv_blocks]
        
        min_len = min(c.size(-1) for c in x)
        conv_outs = [c[:, :, :min_len] for c in x]
    
        x = torch.cat(conv_outs,dim=1)
        x = x.permute(0,2,1)
        x = self.cnn_proj(x)
        
        lstm_out, (h_n, c_n) = self.lstm(x)
        #x = torch.cat(( h_n[-2], h_n[-1] ), dim=1)
        context, attn_weighs = self.attention(lstm_out)
        
        x = self.classifier(context)
        
        if return_attention:
            return x, attn_weighs
        
        return x
    
    
    def run_trenning(self, X, y):
        data_to_trainer = [X, y]
        trainer = Trainer(self, data_to_trainer)
        trainer.train()
        
    def evaluate(self, X, y):
        trainer = Trainer(self,None)
        data_loader = trainer.get_data_loaders(*trainer.get_tokenized_tensors(X, y),shuffled = False)
        trainer.evaluate(data_loader)
        
        
        
        

if __name__ == "__main__":
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from Set_Processor import ImportData
    data = ImportData()
    data.Import_set_3()
    X, y = data.Get_NLP()
    
    model = CNN_LSTM()
    model.run_trenning(X, y)

    
    print(f"{"-" * 50}")
    print("Evaluacja set 2\n")
    data.Import_set_2()
    X, y = data.Get_NLP()
    model.evaluate(X, y)
    
    print(f"{"-" * 50}")
    print("Evaluacja set 5\n")
    data.Import_set_5()
    X, y = data.Get_NLP()
    model.evaluate(X, y)
    
    