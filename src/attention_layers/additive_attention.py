import torch
import torch.nn as nn
import torch.nn.functional as F
from typing import Optional,Tuple

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
        
        energy = self.v(torch.tanh(self.W(hidden)))  # (B, T, 1)
        energy = energy.squeeze(-1)                  # (B, T)
        
        if mask is not None:
            energy = energy.masked_fill(mask, float("-inf"))
            
        weights = F.softmax(energy, dim=-1)          # (B, T)
        context = torch.bmm(weights.unsqueeze(1), hidden).squeeze(1)  # (B, H)
        
        return context, weights