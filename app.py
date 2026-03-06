from xgboost import XGBClassifier
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from importData import ImportData
import pandas as pd
import xgboost as xgb


class NLPXGBoostScanner:
    def __init__(self):

        try:
            self.vectorizer = joblib.load("models/vectorizer_tfidf.pkl")
            self.cechy_nlp = self.vectorizer.get_feature_names_out()
        except FileNotFoundError:
            raise Exception("Błąd: Nie znaleziono pliku vectorizer_tfidf.pkl")

        try:
            self.model = xgb.Booster()
            self.model.load_model("models/phishing_NLPxgboost_model.json")
        except xgb.core.XGBoostError:
            raise Exception("Błąd: Nie znaleziono pliku!")


    def skanuj_url(self, url):

        url_features = self.vectorizer.transform([url])
        dmatrix_url = xgb.DMatrix(url_features, feature_names=list(self.cechy_nlp))
        prawdopodobienstwo = self.model.predict(dmatrix_url)[0]

        print("=" * 60)
        print(f"🔍 ANALIZOWANY ADRES: {url}")
        print("=" * 60)

        if prawdopodobienstwo > 0.5:
            print(f"🚨 WERDYKT: ZŁOŚLIWY LINK (PHISHING)")
            print(f"⚠️ Pewność modelu: {prawdopodobienstwo * 100:.2f}%")
        else:
            print(f"✅ WERDYKT: BEZPIECZNA STRONA")
            print(f"🛡️ Prawdopodobieństwo zagrożenia: {prawdopodobienstwo * 100:.2f}%")
        print("-" * 60)




x = NLPXGBoostScanner()
x.skanuj_url("https://www.phishing_NLPxgboost_model.json")