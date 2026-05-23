import torch
import torch.nn as nn
from transformers import DistilBertModel

from Set_Processor import ImportData
from .config import cfg


class DistilBERT_Model(nn.Module):
    def __init__(self, cfg):
        super().__init__()
        self.cfg = cfg
        self.distilbert = DistilBertModel.from_pretrained(cfg.MODEL_NAME)

        clf_in = self.distilbert.config.hidden_size + (cfg.FEATURES_LEN if cfg.USE_FEATURES else 0)

        self.classifier = nn.Sequential(
            nn.Linear(clf_in, cfg.DENSE_DIM),
            nn.GELU(),
            nn.Dropout(cfg.CLF_DROPOUT),
            nn.Linear(cfg.DENSE_DIM, 1)
        )

    def forward(self, input_ids, attention_mask, features=None):
        # POPRAWKA: attention_mask jako osobny argument zamiast generowania go tu
        outputs = self.distilbert(input_ids=input_ids, attention_mask=attention_mask)
        cls_repr = outputs.last_hidden_state[:, 0, :]

        if features is not None and self.cfg.USE_FEATURES:
            cls_repr = torch.cat([cls_repr, features], dim=-1)

        return self.classifier(cls_repr)

    def run_training(self, X, y):
        # POPRAWKA: lazy import wewnątrz metody — usuwa circular import
        from trainer import Trainer_DistilBERT
        trainer = Trainer_DistilBERT(self, self.cfg, [X, y])
        trainer.train()


if __name__ == "__main__":
    dane = ImportData()
    dane.Import_set_4()
    X, y = dane.Get_NLP()

    model = DistilBERT_Model(cfg)
    model.run_training(X, y)