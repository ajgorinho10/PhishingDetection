import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


import torch
from torch import nn
import torch.nn.functional as F

import numpy as np

from Set_Processor import ImportData
from .config import cfg
from models_utils import Trainer, BaseModel
from attention_layers import SqueezeExcitation, SpatialAttention

from Set_Processor import FeaturesExtraction

    
        
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
        
        
        self.se = SqueezeExcitation(out_dim, 4)
        self.sa = SpatialAttention()
        
    def forward(self, x, mask=None):
        x = self.conv(x)
        x = self.se(x, mask)
        x = self.sa(x, mask)
        
        return F.relu(x)


class CNN(nn.Module, BaseModel):
    def __init__(self, cfg):
        super(CNN, self).__init__()
        
        self.cfg = cfg
        self.features = FeaturesExtraction()

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
        
              
        self.classifier_dim = self.cfg.CNN_FILTERS
        if self.cfg.USE_FEATURES:
            self.classifier_dim += self.cfg.FEATURES_LEN
        
        self.classifier = nn.Sequential(
            nn.Linear(in_features = self.classifier_dim, out_features = self.classifier_dim//2),
            nn.ReLU(),
            nn.Dropout(self.cfg.DROPOUT),
            
            nn.Linear(in_features = self.classifier_dim//2, out_features = self.classifier_dim//4),
            nn.ReLU(),
            nn.Dropout(self.cfg.DROPOUT * 0.5),
            
            nn.Linear(in_features = self.classifier_dim//4, out_features = 1),
        )

    def forward(self, x, features=None):
        mask = (x == self.cfg.PAD_IDX)  # (Batch, SeqLen)
        
        x = self.embedding(x)
        x = x.permute(0, 2, 1)  # (Batch, Channels, SeqLen)
        
        # Przejście przez bloki konwolucyjne z maską
        blocks = x
        for block in self.conv_blocks:
            blocks = block(blocks, mask)
            
        # 3. Zastąpienie spłaszczania True GAP & GMP
        mask_expanded = mask.unsqueeze(1)  # (Batch, 1, SeqLen)
        valid_lengths = (~mask).sum(dim=1, keepdim=True).clamp(min=1)  # (Batch, 1)
        
        # Agregacja średniej
        blocks_masked_avg = blocks.masked_fill(mask_expanded, 0.0)
        gap = blocks_masked_avg.sum(dim=2) / valid_lengths
        

        blocks_masked_max = blocks.masked_fill(mask_expanded, -1e9)
        gmp = blocks_masked_max.max(dim=2)[0]
        

        x_out = torch.cat([gap, gmp], dim=1)


        if self.cfg.USE_FEATURES and features is not None:
            x_out = torch.cat([x_out, features], dim=-1)
        
        logits = self.classifier(x_out)
        
        return logits

        


if __name__ == "__main__":

    data = ImportData()
    data.Import_set_5()

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
    data.Import_set_3()
    X, y = data.Get_NLP()
    cnn.evaluate(X, y)


