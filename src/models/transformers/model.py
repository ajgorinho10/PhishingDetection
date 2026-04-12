import math
import torch
import torch.nn as nn

from models_utils import ModelTokens
from .config import cfg


# Kodowanie pozycji znaków - https://github.com/pytorch/examples/blob/main/word_language_model/model.py
class PositionalEncoding(nn.Module):
    def __init__(self, d_model, dropout=0.1, max_len=5000):
        super().__init__()
        self.dropout = nn.Dropout(p=dropout)

        pe = torch.zeros(max_len, d_model)
        position = torch.arange(0, max_len, dtype=torch.float).unsqueeze(1)
        div_term = torch.exp(torch.arange(0, d_model, 2).float() * (-math.log(10000.0) / d_model))
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)
        
        pe = pe.unsqueeze(0) 
        self.register_buffer('pe', pe)

    def forward(self, x):
        x = x + self.pe[:, :x.size(1), :]
        return self.dropout(x)
    
    
class TransformerLayer(nn.Module):
    def __init__(self, d_model, n_heads, dim_ff, dropout):
        super().__init__()
        
        self.norm1 = nn.LayerNorm(d_model)
        self.attn = nn.MultiheadAttention(
            embed_dim   = d_model,
            num_heads   = n_heads,
            dropout     = dropout,
            batch_first = True
        )
        
        self.norm2 = nn.LayerNorm(d_model)
        self.ffn   = nn.Sequential(
            nn.Linear(d_model, dim_ff),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(dim_ff, d_model),
            nn.Dropout(dropout),
        )
        
    def forward(self, x, key_padding_mask=None):
        residual = x
        
        x = self.norm1(x)
        attn_out, _ = self.attn(
            query = x,
            key = x,
            value = x,
            key_padding_mask = key_padding_mask,
            need_weights = False
        )
        
        x = residual + attn_out
        
        residual = x
        
        x = self.norm2(x)
        x = residual + self.ffn(x)
        
        return x
        


class Transformer(nn.Module, ModelTokens):
    def __init__(self, cfg):
        super().__init__()
        self.cfg = cfg
        
        self.embedding = nn.Embedding(
            num_embeddings = cfg.VOCAB_SIZE + 1,
            embedding_dim  = cfg.EMBED_DIM,
            padding_idx    = cfg.PADIDX
        )
        
        nn.init.normal_(self.embedding.weight,mean=0.0,std=0.02)
        
        with torch.no_grad():
            self.embedding.weight[cfg.PADIDX].fill_(0)
            
        self.pos_encoding = PositionalEncoding(
            d_model = cfg.EMBED_DIM,
            dropout = cfg.DROPOUT,
            max_len = cfg.MAX_LEN + 1
        )
        
        self.encoder_layers = nn.ModuleList([
            TransformerLayer(
                d_model=cfg.EMBED_DIM,
                n_heads=cfg.N_HEADS,
                dim_ff=cfg.DIM_FF,
                dropout=cfg.DROPOUT
            )
            for _ in range(cfg.N_LAYERS)
        ])
        
        self.norm_out = nn.LayerNorm(cfg.EMBED_DIM)
        
        clf_in = cfg.EMBED_DIM + (cfg.FEATURES_LEN if cfg.USE_FEATURES else 0)
        
        self.classifier = nn.Sequential(
            nn.Linear(clf_in, cfg.DENSE_DIM),
            nn.GELU(),
            nn.Dropout(cfg.DROPOUT),
            nn.Linear(cfg.DENSE_DIM, cfg.DENSE_DIM//2),
            nn.GELU(),
            nn.Dropout(cfg.DROPOUT * 0.5),
            nn.Linear(cfg.DENSE_DIM//2, 1)
        )
        
        cls_token = torch.full((1,1),cfg.CLS_IDX, dtype=torch.long)
        self.register_buffer('cls_token',cls_token)
        
    def _prepend_cls(self, x):
        B = x.size(0)
        cls = self.cls_token.expand(B, 1)
        return torch.cat([cls,x], dim = 1)

    def forward(self, x, features=None, return_attention = False):
        padding_mask = (x == self.cfg.PADIDX)
        cls_mask     = torch.zeros(x.size(0), 1, dtype=torch.bool, device= x.device)
        full_mask    = torch.cat([cls_mask,padding_mask], dim=1)
        
        x_cls = self._prepend_cls(x)
        emb   = self.embedding(x_cls)
        emb   = self.pos_encoding(emb)
        
        out = emb
        for layer in self.encoder_layers:
            out = layer(out, key_padding_mask = full_mask)
            
        out = self.norm_out(out)
        
        cls_repr = out[:, 0, :]
        
        if features is not None:
            cls_repr = torch.cat([cls_repr, features],dim = -1)
            
        logit = self.classifier(cls_repr)
        return logit
    
if __name__ == "__main__":
    from Set_Processor import ImportData
    dane = ImportData()
    dane.Import_set_4()
    X, y = dane.Get_NLP()

    mlp = Transformer(cfg)
    mlp.run_training(X, y)