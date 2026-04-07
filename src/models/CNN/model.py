import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


import torch
from torch import nn
import torch.nn.functional as F

import numpy as np

from Set_Processor import ImportData
from config import cfg
from models_utils import Trainer, BaseModel
from attention_layers import SqueezeExcitation, SpatialAttention

    
        
class CNNBlocks(nn.Module):
    def __init__(self, in_dim:int, out_dim:int , kernel_size: int ):
        super().__init__()
        
        self.conv = nn.Sequential(
                nn.Conv1d(
                    in_channels=in_dim,
                    out_channels=out_dim,
                    kernel_size=kernel_size,
                    padding=kernel_size//2
                ),
                nn.BatchNorm1d(out_dim),
                nn.ReLU(inplace=True)
            )
        
        
        self.attention = nn.Sequential(
            SqueezeExcitation(out_dim, 4),
            SpatialAttention()
        )
        
    def forward(self, x):
        x = self.conv(x)
        x = self.attention(x)
        
        return F.relu(x)


class CNN(nn.Module, BaseModel):
    def __init__(self, cfg):
        super(CNN, self).__init__()
        
        self.cfg = cfg

        self.embedding = nn.Embedding(
            num_embeddings = self.cfg.VOCAB_SIZE,
            embedding_dim  = self.cfg.EMBED_DIM,
            padding_idx    = self.cfg.PAD_IDX
        )
        
        self.conv_blocks = nn.Sequential(
                CNNBlocks(in_dim = self.cfg.EMBED_DIM,   out_dim = self.cfg.CNN_FILTERS,    kernel_size = self.cfg.CNN_KERNELS[0]),
                CNNBlocks(in_dim = self.cfg.CNN_FILTERS, out_dim = self.cfg.CNN_FILTERS,    kernel_size = self.cfg.CNN_KERNELS[1]),
                CNNBlocks(in_dim = self.cfg.CNN_FILTERS, out_dim = self.cfg.CNN_FILTERS//2, kernel_size = self.cfg.CNN_KERNELS[2])
            )
        
        
        self.gap = nn.AdaptiveAvgPool1d(1)
        self.gmp = nn.AdaptiveMaxPool1d(1)
        
        self.classifier_dim = self.cfg.CNN_FILTERS
        
        self.classifier = nn.Sequential(
            nn.Linear(in_features = self.classifier_dim, out_features = self.classifier_dim//2),
            nn.ReLU(),
            nn.Dropout(self.cfg.DROPOUT),
            
            nn.Linear(in_features = self.classifier_dim//2, out_features = 1)
        )

    def forward(self,x):
        x = self.embedding(x)
        x = x.permute(0, 2, 1)
        
    
        blocks = self.conv_blocks(x)
        
        gap = self.gap(blocks).squeeze(-1)
        gmp = self.gmp(blocks).squeeze(-1)
        x = torch.cat([gap,gmp],dim = 1)

        x = self.classifier(x)
        
        return x

        


if __name__ == "__main__":

    data = ImportData()
    data.Import_set_3()
    X, y = data.Get_NLP()

    cnn = CNN(cfg)
    cnn.run_training(X,y)
    
    print(f"{"-" * 50}")
    print("Evaluacja set 2\n")
    data.Import_set_2()
    X, y = data.Get_NLP()
    cnn.evaluate(X, y)
    
    print(f"{"-" * 50}")
    print("Evaluacja set 5\n")
    data.Import_set_5()
    X, y = data.Get_NLP()
    cnn.evaluate(X, y)


