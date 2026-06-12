import joblib
import scipy.sparse as sp
import numpy as np
from sklearn.model_selection import train_test_split
from .trainer_tfidf import Trainer_TfIDF
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, f1_score, recall_score
import time

class Trainer_XGB(Trainer_TfIDF):
    def __init__(self, model_wrapper, cfg, dataset=None):
        super().__init__(model_wrapper, cfg, dataset)
        self.model_wrapper = model_wrapper
        
    def train(self):
        X, y = self.dataset[0], self.dataset[1]
        
        X_train, X_test_val, y_train, y_test_val = train_test_split(X, y, test_size=0.3, random_state=42)
        X_test, X_val, y_test, y_val             = train_test_split(X_test_val, y_test_val, test_size=0.5, random_state=42)
        
        X_train_tfidf = self.ftidfVectorizer.fit_transform(X_train)
        X_val_tfidf   = self.ftidfVectorizer.transform(X_val)
        joblib.dump(self.ftidfVectorizer, self.cfg.FTIDF_PATH)
        
        if self.use_features:
            X_train_feat = self.get_data_features(X_train).numpy()
            X_val_feat   = self.get_data_features(X_val).numpy()
            
            X_train_feat = self.scaler.fit_transform(X_train_feat)
            X_val_feat   = self.scaler.transform(X_val_feat)
            joblib.dump(self.scaler, self.cfg.SCALER_PATH)
            
            X_train_final = sp.hstack([X_train_tfidf, X_train_feat])
            X_val_final   = sp.hstack([X_val_tfidf, X_val_feat])
        else:
            X_train_final = X_train_tfidf
            X_val_final   = X_val_tfidf
        

        X_train_final = X_train_final.tocsr().astype(np.float32)
        X_val_final   = X_val_final.tocsr().astype(np.float32)


        y_train_np = (y_train.values if hasattr(y_train, 'values') else np.array(y_train)).flatten().astype(np.float32)
        y_val_np   = (y_val.values if hasattr(y_val, 'values') else np.array(y_val)).flatten().astype(np.float32)
        
        start_time = time.time()
        self.model_wrapper.model.fit(
            X_train_final, y_train_np,
            eval_set=[(X_train_final, y_train_np), (X_val_final, y_val_np)],
            verbose=50
        )
        end_time = time.time()
        print(f'Czas trenowania: {(end_time-start_time):.2f}')
        self.model_wrapper.save(self.cfg.PATH)

        # 2. Pobranie historii Loss
        results = self.model_wrapper.model.evals_result()
        metric_name = list(results['validation_0'].keys())[0]
        train_loss = results['validation_0'][metric_name]
        val_loss = results['validation_1'][metric_name]
        epochs = range(len(train_loss))

        # 3. Obliczenie metryk na zbiorze walidacyjnym (dla finalnego modelu)
        y_val_pred = self.model_wrapper.model.predict(X_val_final)
        
        # Używamy average='weighted', aby kod działał poprawnie zarówno dla klasyfikacji binarnej, jak i wieloklasowej
        acc = accuracy_score(y_val_np, y_val_pred)
        f1 = f1_score(y_val_np, y_val_pred, average='weighted')
        rec = recall_score(y_val_np, y_val_pred, average='weighted')

        # 4. Generowanie wykresów (1 wiersz, 2 kolumny)
        import matplotlib.pyplot as plt
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

        # --- Wykres 1: Train & Val Loss ---
        ax1.plot(epochs, train_loss, label='Train Loss', color='blue')
        ax1.plot(epochs, val_loss, label='Validation Loss', color='orange')
        ax1.set_xlabel('Iteracje (Liczba drzew)')
        ax1.set_ylabel(f'Błąd ({metric_name})')
        ax1.set_title('Krzywa uczenia XGBoost')
        ax1.legend()
        ax1.grid(True)

        # --- Wykres 2: Accuracy, F1, Recall ---
        metrics_names = ['Accuracy', 'F1 Score', 'Recall']
        metrics_values = [acc, f1, rec]
        bars = ax2.bar(metrics_names, metrics_values, color=['#4CAF50', '#2196F3', '#FF9800'])
        ax2.set_ylim(0, 1.1) # Wymuszenie skali 0-1
        ax2.set_title('Metryki końcowe na zbiorze walidacyjnym')
        ax2.set_ylabel('Wartość')

        # Dodanie etykiet liczbowych nad słupkami
        for bar in bars:
            yval = bar.get_height()
            ax2.text(bar.get_x() + bar.get_width()/2, yval + 0.02, round(yval, 4), ha='center', va='bottom')

        plt.tight_layout()
        plt.show()