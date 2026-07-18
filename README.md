# Opis
Celem projektu jest wykrycie ataków pishingowych na podstawie adresów URL. 
Repozutorium zawiera stworzone modele uczenia maszynowego przy użyciu języka Python oraz bibliotek Scikit-learn i Pytorch. Głębokie modele zostały uzupełnione o warstwy uwagi.
Dokłdane wyniki algorytmów znajdują się w folderach 'wyniki' i 'wykresy'.

# Modele:
- CNN_LSTM
- CNN
- LSTM
- MLP
- XGBoost
- Transformer

| Architektura Modelu | Zbiór 1 | Zbiór 2 | Zbiór 3 | Zbiór 4 |
|---|---|---|---|---|
| CNN (Cechy) | 0.9340 | 0.9442 | 0.7919 | 0.9513 |
| CNN | 0.9437 | 0.9520 | 0.8127 | 0.9582 |
| CNN + LSTM (Cechy) | 0.9614 | 0.9646 | 0.8288 | 0.9705 |
| CNN + LSTM | 0.9601 | 0.9639 | 0.8375 | 0.9699 |
| LSTM (Cechy) | 0.9466 | 0.9505 | 0.8142 | 0.9587 |
| LSTM | 0.9390 | 0.9468 | 0.8061 | 0.9540 |
| MLP (Cechy) | 0.9471 | 0.9455 | 0.7697 | 0.9598 |
| MLP | 0.9004 | 0.8872 | 0.6595 | 0.9243 |
| XGBoost (Cechy) | 0.9256 | 0.9288 | 0.7320 | 0.9443 |
| XGBoost | 0.8688 | 0.8629 | 0.6336 | 0.9015 |
| DistilBERT (Cechy) | 0.9782 | 0.9760 | 0.8541 | 0.9830 |
| **DistilBERT** | **0.9812** | **0.9800** | **0.8629** | **0.9856** |
