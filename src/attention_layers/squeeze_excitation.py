import torch
import torch.nn as nn

class SqueezeExcitation(nn.Module):
    def __init__(self, num_filters: int, reduction: int = 4):
        super().__init__()
        mid = max((num_filters // reduction), 8)
        
        self.fc1 = nn.Linear(num_filters, mid)
        self.relu = nn.ReLU(inplace=True)
        self.fc2 = nn.Linear(mid, num_filters)
        self.sigmoid = nn.Sigmoid()
        
    def forward(self, x, mask=None):
        # x: (Batch, Channels, SeqLen)
        # mask: (Batch, SeqLen)
        
        if mask is not None:
            mask_expanded = mask.unsqueeze(1)  # (Batch, 1, SeqLen)
            x_masked = x.masked_fill(mask_expanded, 0.0)
            
            # Poprawka: sumowanie po rozszerzonej masce (3D)
            valid_lengths = (~mask_expanded).sum(dim=2, keepdim=True).clamp(min=1)
            s = x_masked.sum(dim=2, keepdim=True) / valid_lengths  
        else:
            s = x.mean(dim=2, keepdim=True)  
            
        s = s.squeeze(2)
        w = self.fc1(s)
        w = self.relu(w)
        w = self.fc2(w)
        w = self.sigmoid(w)
        w = w.unsqueeze(2)
        
        return x * w