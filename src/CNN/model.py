import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import torch
from torch import nn
import torch.nn.functional as F

import numpy as np

from Set_Processor import ImportData
from config import cfg
from trainer import Trainer


class SqueezeExcitation(nn.Module):
    def __init__(self, num_filters:int, reduction:int = 4):
        super().__init__()
        
        mid = max((num_filters//reduction),8)
        
        
        self.squeeze = nn.AdaptiveAvgPool1d(1)
        
        self.extraction = nn.Sequential(
            nn.Flatten(),
            nn.Linear(in_features=num_filters, out_features=mid ),
            nn.ReLU(inplace=True),
            nn.Linear(in_features=mid, out_features=num_filters),
            nn.Sigmoid()
        )
        
    def forward(self, x):
        s = self.squeeze(x)
        w = self.extraction(s)
        w = w.unsqueeze(-1)
        
        return x * w
    
    
class SpatialAttention(nn.Module):
    def __init__(self, kernel_size: int = max(*cfg.CNN_KERNELS)):
        super().__init__()
        
        pad = kernel_size // 2
        self.conv = nn.Conv1d(
            in_channels=2, 
            out_channels=1, 
            kernel_size = kernel_size, 
            padding=pad, 
            bias=False
        )
        self.sigmoid = nn.Sigmoid()
        
    def forward(self, x):
        avg_feat = x.mean(dim=1, keepdim=True)
        max_feat = x.max(dim=1, keepdim=True).values
        cat = torch.cat([avg_feat, max_feat], dim=1)
        w = self.sigmoid(self.conv(cat))
        return x * w    
        
        
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


class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()

        self.embedding = nn.Embedding(
            num_embeddings = cfg.VOCAB_SIZE,
            embedding_dim  = cfg.EMBED_DIM,
            padding_idx    = cfg.PAD_IDX
        )
        
        self.conv_blocks = nn.Sequential(
                CNNBlocks(in_dim = cfg.EMBED_DIM,   out_dim = cfg.CNN_FILTERS,    kernel_size = cfg.CNN_KERNELS[0]),
                CNNBlocks(in_dim = cfg.CNN_FILTERS, out_dim = cfg.CNN_FILTERS,    kernel_size = cfg.CNN_KERNELS[1]),
                CNNBlocks(in_dim = cfg.CNN_FILTERS, out_dim = cfg.CNN_FILTERS//2, kernel_size = cfg.CNN_KERNELS[2])
            )
        
        
        self.gap = nn.AdaptiveAvgPool1d(1)
        self.gmp = nn.AdaptiveMaxPool1d(1)
        
        self.classifier_dim = cfg.CNN_FILTERS
        
        self.classifier = nn.Sequential(
            nn.Linear(in_features = self.classifier_dim, out_features = self.classifier_dim//2),
            nn.ReLU(),
            nn.Dropout(cfg.DROPOUT),
            
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
    X, y = data.Get_NLP()

    cnn = CNN()
    cnn.train_model(X,y)
    
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


