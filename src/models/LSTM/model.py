import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from Set_Processor import ImportData

import torch
import torch.nn as nn

import numpy as np

from models_utils import ModelTokens
from .config import cfg
from attention_layers import AdditiveAttention




class LSTM(nn.Module, ModelTokens):
    def __init__(self, cfg):
        super().__init__()
        
        self.cfg = cfg
        
        self.embanding = nn.Embedding(
            num_embeddings = self.cfg.VOCAB_SIZE,
            embedding_dim  = self.cfg.EMBED_DIM,
            padding_idx    = self.cfg.PAD_IDX
        )
        
        #Warstwa LSTM
        self.lstm1 =nn.LSTM(
                input_size    = self.cfg.EMBED_DIM,
                hidden_size   = self.cfg.LSTM_UNITS,
                num_layers    = 1,
                bias          = False,
                batch_first   = True,
                dropout       = 0.0,
                bidirectional = True
            )
            
        self.dropout = nn.Dropout(self.cfg.DROPOUT)
            
        self.lstm2 = nn.LSTM(
                input_size    = self.cfg.LSTM_UNITS*2,
                hidden_size   = self.cfg.EMBED_DIM,
                num_layers    = 1,
                bias          = False,
                batch_first   = True,
                dropout       = 0.0,
                bidirectional = True
            )
            
        
        self.lstm_out_dim = self.cfg.EMBED_DIM * 2
        
        self.attention = AdditiveAttention(self.lstm_out_dim, self.cfg.ATTN_DIM)
        
        self.classifier_in_dim = self.lstm_out_dim + (self.cfg.FEATURES_LEN if self.cfg.USE_FEATURES else 0)

        self.classifier = nn.Sequential(
            nn.Linear(
                in_features  = self.classifier_in_dim,
                out_features = self.classifier_in_dim//2
            ),
            
            nn.ReLU(),
            nn.Dropout(self.cfg.DROPOUT),
            
            nn.Linear(
                in_features  = self.classifier_in_dim//2,
                out_features = 1
            ),
        )
        
        
    def forward(self, x, features = None, return_attention: bool = False):
        mask = (x == self.cfg.PAD_IDX)
        
        x = self.embanding(x)
     
        x, _ = self.lstm1(x)
        
        x = self.dropout(x)
        
        lstm_out, _ = self.lstm2(x)
        
        context, attn_weights = self.attention(lstm_out, mask)
        
        if features != None:
            context = torch.cat([context, features], dim = -1)
        
        x = self.classifier(context)
        
        if return_attention:
            return x, attn_weights
        
        return x



if __name__ == "__main__":
    
    data = ImportData()
    data.Import_set_4()
    X_data, y_data = data.Get_NLP()
    
    lstm = LSTM(cfg)
    lstm.run_training(X=X_data, y=y_data)
    
    '''
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
    '''