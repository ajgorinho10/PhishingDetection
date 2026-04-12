import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import torch
import torch.nn as nn

from Set_Processor import ImportData
from models_utils import ModelTokens
from .config import cfg
from attention_layers import AdditiveAttention, SqueezeExcitation, SpatialAttention

class CNNBlock(nn.Module):
    def __init__(self, in_channels: int, out_channels: int, kernel_size: int):
        super().__init__()
        
        self.conv = nn.Sequential(
            nn.Conv1d(
                in_channels=in_channels,
                out_channels=out_channels,
                kernel_size=kernel_size,
                padding=kernel_size // 2
            ),
            nn.BatchNorm1d(out_channels),
            nn.ReLU(inplace=True)
        )
        
        self.se = SqueezeExcitation(out_channels, 4)
        self.sa = SpatialAttention()
        
    def forward(self, x, mask=None):
        x = self.conv(x)
        
        if mask is not None:
            mask_expanded = mask.unsqueeze(1)
            x = x.masked_fill(mask_expanded, 0.0)
            
        x = self.se(x, mask)
        x = self.sa(x, mask)
        return x

class CnnLstm2(nn.Module, ModelTokens):
    def __init__(self, cfg):
        super().__init__()
        
        self.cfg = cfg
        
        self.embedding = nn.Embedding(
            num_embeddings = self.cfg.VOCAB_SIZE,
            embedding_dim  = self.cfg.EMBED_DIM,
            padding_idx    = self.cfg.PAD_IDX
        )
        
        with torch.no_grad():
            self.embedding.weight[self.cfg.PAD_IDX].fill_(0)
            
        # 2. Użycie nowej klasy CNNBlock zamiast nn.Sequential
        self.conv_blocks = nn.ModuleList([
            CNNBlock(
                in_channels=self.cfg.EMBED_DIM,
                out_channels=self.cfg.CNN_FILTERS,
                kernel_size=k
            )
            for k in self.cfg.CNN_KERNELS
        ])
        
        self.conv_out_dim = self.cfg.CNN_FILTERS * len(self.cfg.CNN_KERNELS)
        
        self.cnn_proj = nn.Sequential(
            nn.Linear(in_features=self.conv_out_dim, out_features=self.conv_out_dim//2),
            nn.ReLU(),
            nn.Dropout(self.cfg.DROPOUT * 0.5),
        )
        
        self.lstm = nn.LSTM(
            input_size      = self.conv_out_dim//2,
            hidden_size     = self.cfg.LSTM_UNITS,
            num_layers      = 1,
            batch_first     = True,
            bidirectional   = True,
            dropout         = 0.0 
        )
        
        self.lstm_out_dim = self.cfg.LSTM_UNITS * 2   
        self.attention_additive = AdditiveAttention(self.lstm_out_dim, self.cfg.ATTN_DIM)
        
        
        self.classifier_in_dim = self.lstm_out_dim
        if self.cfg.USE_FEATURES:
            self.classifier_in_dim += self.cfg.FEATURES_LEN
        
        self.classifier = nn.Sequential(
            nn.Linear(
                in_features  = self.classifier_in_dim,
                out_features = self.classifier_in_dim // 2
            ),
            nn.ReLU(),
            nn.Dropout(self.cfg.DROPOUT),
            nn.Linear(
                in_features  = self.classifier_in_dim // 2,
                out_features = 1
            ),
        )
    
    def forward(self, x, features = None,return_attention: bool = False):
        mask = (x == self.cfg.PAD_IDX)
        
        x_emb = self.embedding(x)
        x_emb = x_emb.permute(0, 2, 1)
        
        # 3. Pętla przekazująca tensor x_emb oraz maskę do każdego bloku
        conv_outs = []
        for block in self.conv_blocks:
            out = block(x_emb, mask)
            conv_outs.append(out)
    
        x_cat = torch.cat(conv_outs, dim=1)
        x_cat = x_cat.permute(0, 2, 1)
        
        cnn_proj_out = self.cnn_proj(x_cat)
        
        lstm_out, (h_n, c_n) = self.lstm(cnn_proj_out)
        
        context, attn_weights = self.attention_additive(lstm_out, mask)
        
        if features is not None:
            combined = torch.cat([context, features], dim=-1)
        else:
            combined = context
        logit = self.classifier(combined)
 
        if return_attention:
            return logit, attn_weights
        return logit
        


if __name__ == "__main__":
    data = ImportData()
    data.Import_set_4()
    X, y = data.Get_NLP()
    
    model = CnnLstm2(cfg)
    #model.evaluate(X, y)
    

    model.run_training(X, y)
    '''
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
    '''
    