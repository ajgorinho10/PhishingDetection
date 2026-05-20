from models_utils import CharTokenizer
from models.transformers import cfg
from models.transformers.model import Transformer as model1
from trainer import Trainer_Tokens

import torch

tokenizer = CharTokenizer()
model = model1(cfg)
scaler = model.load_model()
model.eval()
model.to(cfg.DEVICE)
trainer = Trainer_Tokens(model, cfg, None)

user_input = None
while True:
    user_input = input("Wprowadź url:")
    
    if user_input == "exit": break
    
    text_tokenized = tokenizer.encode(user_input)
    text_tokenized_tensor = torch.tensor(text_tokenized, dtype=torch.long).unsqueeze(0).to(cfg.DEVICE)
    X_features_tensor = None

    if cfg.USE_FEATURES:

        X_features = trainer.get_data_features([text_tokenized])
        X_features_tensor = torch.tensor(X_features.numpy(), dtype=torch.float32).to(cfg.DEVICE)

    with torch.no_grad():
        output_raw = None
        if cfg.USE_FEATURES:
            output_raw = model(text_tokenized_tensor, X_features_tensor)
        else:
            output_raw = model(text_tokenized_tensor)
            
        output = torch.sigmoid(output_raw).squeeze(-1)

    print(output)



