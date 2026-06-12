import streamlit as st
import torch
from transformers import DistilBertTokenizer
from models.transformers.config import cfg
from models.transformers.model import DistilBERT_Model

@st.cache_resource
def load_system():
    tokenizer = DistilBertTokenizer.from_pretrained(cfg.MODEL_NAME)
    model = DistilBERT_Model(cfg)
    wagi = torch.load(cfg.PATH, map_location=cfg.DEVICE)
    model.load_state_dict(wagi)
    model.eval()
    model.to(cfg.DEVICE)
    
    return tokenizer, model

tokenizer, model = load_system()

st.title("Weryfikator Adresów URL")
st.write("Wykrywanie phishingowych adresów URL przy użyciu architektury Transformer.")

with st.form("skaner_form"):
    user_input = st.text_input("Wprowadź adres URL do analizy:")
    submit_button = st.form_submit_button("Skanuj adres")

if submit_button:
    if user_input:
        inputs = tokenizer(
            user_input,
            return_tensors="pt",
            max_length=cfg.MAX_LEN,
            padding="max_length",
            truncation=True
        )
        
        input_ids = inputs["input_ids"].to(cfg.DEVICE)
        attention_mask = inputs["attention_mask"].to(cfg.DEVICE)

        with torch.no_grad():
            output_raw = model(input_ids, attention_mask)
            output = torch.sigmoid(output_raw).squeeze(-1)
            prob = output.item()

        st.subheader("Wynik analizy:")
        if prob > 0.5:
            st.error(f"Adres niebezpieczny. Prawdopodobieństwo phishingu: {prob:.4f}")
        else:
            st.success(f"Adres bezpieczny. Prawdopodobieństwo phishingu: {prob:.4f}")
    else:
        st.warning("Proszę wprowadzić adres URL.")