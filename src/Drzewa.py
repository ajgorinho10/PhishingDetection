from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, f1_score
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import GridSearchCV, StratifiedKFold

import xgboost as xgb
from xgboost import XGBClassifier

import joblib
import pandas as pd
from pathlib import Path

from src.Set_Processor.importData import ImportData

class TrainModel:
    def __init__(self):
        self.y = None
        self.X = None
        self.df = None

        self.path_models = Path(__file__).resolve().parent.parent / "models"

        self.import_data()
        #self.NLP_import_data()

    def import_data(self):
        self.df,self.X, self.y = ImportData().scal_sets()

    def NLP_import_data(self):
        x = ImportData()
        x.Import_set_2()

        self.X, self.y = x.Get_Scalet_sets()

    def train_RandomForest(self,save = False):
        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)
        model = RandomForestClassifier(
            n_estimators=100,
            random_state=42,

        )
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        skutecznosc = accuracy_score(y_test, y_pred)
        print(f"Skuteczność modelu (Accuracy): {skutecznosc * 100:.2f}%")

        print("\nSzczegółowy raport:")
        print(classification_report(y_test, y_pred))

        print("\nMacierz Pomyłek (Confusion Matrix):")
        print(confusion_matrix(y_test, y_pred))

        if(save):
            nazwa_pliku = self.path_models / 'phishing_randomforest_model.pkl'
            joblib.dump(model, nazwa_pliku)

        importances = model.feature_importances_
        cechy = X_train.columns
        print("\n🔍 RAPORT WAŻNOŚCI CECH (Feature Importances):")
        for cecha, waga in zip(cechy, importances):
            print(f"- {cecha}: {waga * 100:.2f}%")

    def train_XGBoost(self,save = False):
        xgb_model = XGBClassifier(
            n_estimators=90,
            learning_rate=0.2,
            random_state=42,
            eval_metric='logloss',
            scale_pos_weight=2,
            device='cuda',
            tree_method='hist'
        )

        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)
        xgb_model.fit(X_train, y_train)

        y_pred_xgb = xgb_model.predict(X_test)

        if(save):
            nazwa_pliku = self.path_models / 'phishing_xgboost_model.pkl'
            joblib.dump(xgb_model, nazwa_pliku)

        print("Szczegółowy raport dla XGBoost:")
        print(classification_report(y_test, y_pred_xgb))

        print("\nMacierz Pomyłek (XGBoost):")
        print(confusion_matrix(y_test, y_pred_xgb))

        importances = xgb_model.feature_importances_
        cechy = X_train.columns
        print("\n🔍 RAPORT WAŻNOŚCI CECH (Feature Importances):")
        for cecha, waga in zip(cechy, importances):
            print(f"- {cecha}: {waga * 100:.2f}%")

    def findParametersXGBoost(self):
        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)

        dtrain = xgb.DMatrix(X_train, label=y_train)
        dtest = xgb.DMatrix(X_test, label=y_test)

        learning_rate_range = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
        result = []

        for n_estimators in range(5, 100, 5):
            for learning_rate in learning_rate_range:
                for scale_pos_weight in range(1, 18):
                    params = {
                        'objective': 'binary:logistic',
                        'eval_metric': 'logloss',
                        'tree_method': 'hist',
                        'device': 'cuda',
                        'learning_rate': learning_rate,
                        'scale_pos_weight': scale_pos_weight,
                        'random_state': 42
                    }

                    bst = xgb.train(params, dtrain, num_boost_round=n_estimators)
                    preds_proba = bst.predict(dtest)
                    y_pred_xgb = (preds_proba > 0.5).astype(int)

                    r = f1_score(y_test, y_pred_xgb)
                    result.append({
                        "n_estimators": n_estimators,
                        "learning_rate": learning_rate,
                        "scale_pos_weight": scale_pos_weight,
                        "f1": r
                    })

        bestf1 = 0
        best_params = None

        for r in result:
            if r["f1"] > bestf1:
                bestf1 = r["f1"]
                best_params = r

        print("\nZakończono! Najlepsze hiperparametry to:")
        print(best_params)

    def NLP_RandomForest(self):
        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)
        print("Uruchamianie procesora NLP (TF-IDF na n-gramach znakowych)...")
        # analyzer='char' -> tniemy na znaki, nie na słowa
        # ngram_range=(3, 5) -> bierzemy zbitki po 3, 4 i 5 liter
        # max_features=3000 -> ograniczamy do 3000 najpopularniejszych zbitek, żeby nie ugotować RAM-u
        vectorizer = TfidfVectorizer(analyzer='char', ngram_range=(3, 5), max_features=3000)

        # Uczymy słownika na danych treningowych i od razu zamieniamy tekst na liczby
        X_train_nlp = vectorizer.fit_transform(X_train)
        # Dane testowe TYLKO transformujemy (żeby model nie ściągał)
        X_test_nlp = vectorizer.transform(X_test)

        print(f"Zakończono NLP! Twój tekst zamienił się w macierz o rozmiarze: {X_train_nlp.shape}")

        # =======================================================
        # KROK 2: TRENOWANIE RANDOM FOREST
        # =======================================================
        print("Trenowanie Random Forest na cechach NLP (to może potrwać, mamy 3000 kolumn!)...")
        # Używamy n_jobs=-1, żeby wykorzystać wszystkie rdzenie procesora (CPU)
        rf_nlp = RandomForestClassifier(n_estimators=150, max_depth=20, n_jobs=-1, random_state=42)
        rf_nlp.fit(X_train_nlp, y_train)

        # Przewidywanie
        y_pred = rf_nlp.predict(X_test_nlp)

        # =======================================================
        # RAPORT KOŃCOWY
        # =======================================================
        print("\n" + "=" * 50)
        print("RAPORT: NLP (TF-IDF) + RANDOM FOREST")
        print("=" * 50)
        print(classification_report(y_test, y_pred))
        print("Macierz Pomyłek:")
        print(confusion_matrix(y_test, y_pred))

        # Zobaczmy, co NLP uznało za najbardziej podejrzane zbitki liter!
        print("\n🔍 TOP 15 NAJWAŻNIEJSZYCH ZBITEK ZNAKÓW (N-gramów):")
        importances = rf_nlp.feature_importances_
        cechy_nlp = vectorizer.get_feature_names_out()

        wspolczynniki = pd.DataFrame({
            'N-gram': cechy_nlp,
            'Waga': importances
        })
        wspolczynniki = wspolczynniki.sort_values(by='Waga', ascending=False).head(15)
        print(wspolczynniki.to_string(index=False))

    def NLP_XGBoost(self,save = False):
        print("Przygotowywanie danych")
        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=0.3, random_state=42)

        vectorizer = TfidfVectorizer(analyzer='char', ngram_range=(3, 5), max_features=10000)
        X_train_nlp = vectorizer.fit_transform(X_train)
        X_test_nlp = vectorizer.transform(X_test)

        cechy_nlp = vectorizer.get_feature_names_out()

        dtrain = xgb.DMatrix(X_train_nlp, label=y_train, feature_names=list(cechy_nlp))
        dtest = xgb.DMatrix(X_test_nlp, feature_names=list(cechy_nlp))

        params = {
            'objective': 'binary:logistic',
            'eval_metric': 'logloss',
            'tree_method': 'hist',
            'device': 'cuda',
            'learning_rate': 0.5,
            'scale_pos_weight': 2,
            'random_state': 42
        }

        print("Trenowanie modelu...")
        xgb_nlp = xgb.train(params, dtrain, num_boost_round=150)

        y_pred = xgb_nlp.predict(dtest)
        y_pred = (y_pred > 0.5).astype(int)

        print("\n" + "=" * 50)
        print("RAPORT: NLP (TF-IDF) + XGBOOST (Native API)")
        print("=" * 50)
        print(classification_report(y_test, y_pred))
        print("Macierz Pomyłek:")
        print(confusion_matrix(y_test, y_pred))

        print("\n15 NAJWAŻNIEJSZYCH ZBITEK ZNAKÓW (N-gramów):")
        importances_dict = xgb_nlp.get_score(importance_type='gain')

        wspolczynniki = pd.DataFrame(list(importances_dict.items()), columns=['N-gram', 'Waga'])
        wspolczynniki = wspolczynniki.sort_values(by='Waga', ascending=False).head(15)
        print(wspolczynniki.to_string(index=False))

        if(save):
            model_path = self.path_models / 'phishing_NLPxgboost_model.pkl'
            Vec_path = self.path_models / 'vectorizer_tfidf.pkl'

            joblib.dump(xgb_nlp, model_path)
            joblib.dump(vectorizer, Vec_path)
            print("Model i Vectorizer zostały pomyślnie zapisane na dysku!")

    def NLP_XGBoost_find_parameters(self):
        print("Przygotowywanie danych")

        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=0.3, random_state=42)

        vectorizer = TfidfVectorizer(analyzer='char', ngram_range=(3, 5), max_features=3000)
        X_train_nlp = vectorizer.fit_transform(X_train)
        X_test_nlp = vectorizer.transform(X_test)

        xgb_model = XGBClassifier(
            objective='binary:logistic',
            eval_metric='logloss',
            tree_method='hist',
            device='cuda',
            random_state=42
        )

        param_grid = {
            'n_estimators': [50, 100, 150, 200],
            'learning_rate': [0.1, 0.2, 0.3, 0.4, 0.5, 0.6],
            'scale_pos_weight': [1, 2, 3, 4, 5]
        }

        cv = StratifiedKFold(n_splits=3, shuffle=True, random_state=42)

        grid_search = GridSearchCV(
            estimator=xgb_model,
            param_grid=param_grid,
            scoring='f1',
            cv=cv,
            verbose=2,
            n_jobs=1
        )

        print("\nSTART")
        X_train_nlp = X_train_nlp.toarray()
        X_test_nlp = X_test_nlp.toarray()

        grid_search.fit(X_train_nlp, y_train.values)

        # 7. Prezentacja wyników
        print("\n" + "=" * 50)
        print("KONIEC")
        print(f"Najlepsze znalezione parametry: {grid_search.best_params_}")
        print(f"Najlepszy wynik F1: {grid_search.best_score_:.4f}")
        print("=" * 50)

        print("\nSprawdzenie zwycięskiego modelu:")
        best_model = grid_search.best_estimator_

        y_pred = best_model.predict(X_test_nlp)

        print(classification_report(y_test.values, y_pred))
        print("Macierz Pomyłek:")
        print(confusion_matrix(y_test.values, y_pred))



if __name__ == "__main__":
    trainModel = TrainModel()
    #trainModel.findParametersXGBoost()
    trainModel.train_XGBoost(save = False)
    #trainModel.train_RandomForest(save=False)

    #trainModel.train_linear()
    #trainModel.native_bayes()

    #trainModel.NLP_RandomForest()
    #trainModel.NLP_XGBoost(False)
    #trainModel.NLP_XGBoost_find_parameters()

