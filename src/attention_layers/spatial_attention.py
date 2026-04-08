import torch
import torch.nn as nn

class SpatialAttention(nn.Module):
    def __init__(self, kernel_size: int = 7):
        super().__init__()
        pad = kernel_size // 2
        self.conv = nn.Conv1d(
            in_channels=2, 
            out_channels=1, 
            kernel_size=kernel_size, 
            padding=pad, 
            bias=False
        )
        self.sigmoid = nn.Sigmoid()
        
    def forward(self, x, mask=None):
        avg_feat = x.mean(dim=1, keepdim=True)
        max_feat = x.max(dim=1, keepdim=True).values
        cat = torch.cat([avg_feat, max_feat], dim=1)
        w = self.sigmoid(self.conv(cat))
        
        out = x * w
        
        # Wyzerowanie rozmazanego paddingu
        if mask is not None:
            mask_expanded = mask.unsqueeze(1)
            out = out.masked_fill(mask_expanded, 0.0)
            
        return out