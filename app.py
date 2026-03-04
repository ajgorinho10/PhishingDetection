from xgboost import XGBClassifier
import joblib
from importData import ImportData
import pandas as pd

class Detect:
    def __init__(self):
        self.model = None
        self.loadModel()

    def loadModel(self):
        self.model = joblib.load("phishing_xgboost_model.pkl")

    def predict(self,data):
        data = data.lower()
        x = ImportData()

        data = data.replace("https://", "")
        data = data.replace("www.", "")
        print(data)

        dlugosc = x.get_url_length(data)
        dlugosc = x.get_url_length(data)
        kropki = x.count_dots(data)
        myslniki = x.count_hyphens(data)
        subdomeny = x.count_subdomains(data)
        podejrzane_slowa = x.count_suspicious_keywords(data)

        nowe_dane = pd.DataFrame(
            [[podejrzane_slowa, dlugosc, kropki, myslniki, subdomeny]],
            columns=['suspicious_keywords_count', 'url_length', 'qty_dots', 'qty_hyphens', 'qty_subdomains']
        )

        print(nowe_dane)

        werdykt = self.model.predict(nowe_dane)[0]
        pewnosc = self.model.predict_proba(nowe_dane)[0]

        print("Wynik:",werdykt)

