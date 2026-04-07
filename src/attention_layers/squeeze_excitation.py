import torch
import torch.nn as nn

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