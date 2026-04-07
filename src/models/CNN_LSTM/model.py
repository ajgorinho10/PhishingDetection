import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from Set_Processor import ImportData

import torch
import torch.nn as nn
import torch.nn.functional as F

import numpy as np
from typing import Optional, Tuple

from attention_layers import AdditiveAttention
from models_utils import Trainer, BaseModel
from CNN_LSTM import cfg


class CNN_LSTM(nn.Module, BaseModel):
    def __init__(self, cfg):
        super().__init__()
        
        self.cfg = cfg
        
        self.embedding = nn.Embedding(
            num_embeddings=self.cfg.VOCAB_SIZE,
            embedding_dim=self.cfg.EMBED_DIM,
            padding_idx=self.cfg.PAD_IDX
        )
        
        # Inicjalizacja paddingu zerami (dobra praktyka)
        with torch.no_grad():
            self.embedding.weight[self.cfg.PAD_IDX].fill_(0)
        
        # Konwolucja zachowująca oryginalną długość sekwencji (brak MaxPool)
        self.conv_blocks = nn.ModuleList([
            nn.Sequential(
               nn.Conv1d(
                   in_channels  = self.cfg.EMBED_DIM,
                   out_channels = self.cfg.CNN_FILTERS,
                   kernel_size  = k,
                   padding      = k // 2
               ),
               nn.BatchNorm1d(self.cfg.CNN_FILTERS),
               nn.ReLU()
            ) 
            for k in self.cfg.CNN_KERNELS
        ])
        
        self.conv_out_dim = self.cfg.CNN_FILTERS * len(self.cfg.CNN_KERNELS)
        
        # Bezpośrednie przekazanie wyjścia CNN do LSTM
        self.lstm = nn.LSTM(
            input_size      = self.conv_out_dim,
            hidden_size     = self.cfg.LSTM_UNITS,
            num_layers      = 1,
            batch_first     = True,
            bidirectional   = True,
            dropout         = 0.0 
        )
        
        self.lstm_out_dim = self.cfg.LSTM_UNITS * 2
        self.attention = AdditiveAttention(self.lstm_out_dim, self.cfg.ATTN_DIM)
        
        # Zoptymalizowany klasyfikator bez nadmiernego dropoutu
        self.classifier = nn.Sequential(
            nn.Linear(
                in_features  = self.lstm_out_dim,
                out_features = self.lstm_out_dim // 2
            ),
            nn.ReLU(),
            nn.Dropout(self.cfg.DROPOUT),
            nn.Linear(
                in_features  = self.lstm_out_dim // 2,
                out_features = 1
            ),
        )
    
    def forward(self, x, return_attention: bool = False):
        # 1. Generowanie maski dla tokenów paddingu
        mask = (x == self.cfg.PAD_IDX)
        
        # 2. Embedding
        x_emb = self.embedding(x)
        x_emb = x_emb.permute(0, 2, 1)
        
        # 3. Ekstrakcja cech (Równoległe filtry)
        conv_outs = [block(x_emb) for block in self.conv_blocks]
    
        # Ponieważ padding zachowuje długość sekwencji, możemy bezpiecznie łączyć
        x_cat = torch.cat(conv_outs, dim=1)
        x_cat = x_cat.permute(0, 2, 1)
        
        # 4. Przetwarzanie sekwencyjne
        lstm_out, _ = self.lstm(x_cat)
        
        # 5. Wyliczanie wagi z maską
        context, attn_weights = self.attention(lstm_out, mask=mask)
        
        # 6. Klasyfikacja
        logits = self.classifier(context)
        
        if return_attention:
            return logits, attn_weights
        
        return logits


if __name__ == "__main__":
    
    data = ImportData()
    data.Import_set_3()
    X, y = data.Get_NLP()
    
    model = CNN_LSTM(cfg)
    model.run_training(X, y)
    
    print("-" * 50)
    print("Evaluacja set 2\n")
    data.Import_set_2()
    X, y = data.Get_NLP()
    model.evaluate(X, y)
    
    print("-" * 50)
    print("Evaluacja set 3\n")
    data.Import_set_5()
    X, y = data.Get_NLP()
    model.evaluate(X, y)