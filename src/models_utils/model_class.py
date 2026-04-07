
from models_utils import Trainer

class BaseModel:
    def __init__(self, cfg):
        self.cfg = cfg

    def run_training(self, X, y):
        data_to_trainer = [X, y]
        trainer = Trainer(
            self, 
            data_sets=data_to_trainer, 
            cfg=self.cfg
        )
        trainer.train()
        
    def evaluate(self, X, y):
        trainer = Trainer(self, cfg=self.cfg, data_sets=None)
        data_loader = trainer.get_data_loaders(*trainer.get_tokenized_tensors(X, y), shuffled=False)
        trainer.evaluate(data_loader)