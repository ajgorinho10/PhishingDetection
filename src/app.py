import joblib
import re
from pathlib import Path
import xgboost as xgb


class PhishingScanner:
    def __init__(self):
        # 1. Ustalenie bezpiecznych ścieżek
        # Skoro app.py jest w src/, musimy wyjść "piętro wyżej" (.parent) do folderu models/
        katalog_glowny = Path(__file__).resolve().parent.parent
        sciezka_modelu = katalog_glowny / "models" / "phishing_NLPxgboost_model.pkl"
        sciezka_vectorizera = katalog_glowny / "models" / "vectorizer_tfidf.pkl"

        # 2. Ładowanie "mózgu" (modelu) i "słownika" (vectorizera)
        try:
            print("⏳ Ładowanie silnika AI (XGBoost) i słownika NLP...")
            self.model = joblib.load(sciezka_modelu)
            self.vectorizer = joblib.load(sciezka_vectorizera)
            print("✅ System gotowy do działania!\n")
        except FileNotFoundError as e:
            print(f"❌ Błąd: Nie znaleziono plików w folderze 'models/'! Szczegóły: {e}")
            print("Upewnij się, że wytrenowałeś i zapisałeś model w Drzewa.py.")
            exit()

    def clean_url(self, url):
        # Czyszczenie linku dokładnie tak samo, jak podczas treningu!
        url = str(url).lower().strip()
        url = re.sub(r'^https?:\/\/', '', url)
        url = re.sub(r'^www\.', '', url)
        return url

    def scan(self, url):
        # 1. Czyszczenie
        cleaned_url = self.clean_url(url)

        # 2. Zamiana tekstu na liczby (Wektoryzacja TF-IDF)
        X_nlp = self.vectorizer.transform([cleaned_url])

        # 3. Zamiana macierzy na natywny format XGBoost (DMatrix) - TO NAPRAWIA TWÓJ BŁĄD!
        feature_names = self.vectorizer.get_feature_names_out().tolist()
        dmatrix = xgb.DMatrix(X_nlp, feature_names=feature_names)

        # 4. Predykcja AI (w natywnym API predict zwraca od razu szansę na phishing od 0 do 1)
        prob_phishing_raw = self.model.predict(dmatrix)[0]

        # Obliczenia
        prob_phishing = prob_phishing_raw * 100
        prob_bezpieczna = (1.0 - prob_phishing_raw) * 100
        prediction = 1 if prob_phishing_raw > 0.5 else 0

        # 5. Ładny interfejs graficzny w konsoli
        print("=" * 60)
        print(f"🔍 Analizowany link: {url}")
        print(f"   (Po oczyszczeniu): {cleaned_url}")
        print("-" * 60)

        if prediction == 1:
            print(f"🚨 WERDYKT: PHISHING (Wykryto zagrożenie!)")
            print(f"📈 Prawdopodobieństwo oszustwa: {prob_phishing:.2f}%")
        else:
            print(f"✅ WERDYKT: STRONA BEZPIECZNA")
            print(f"📉 Prawdopodobieństwo, że to bezpieczna strona: {prob_bezpieczna:.2f}%")
        print("=" * 60)


if __name__ == "__main__":
    skaner = PhishingScanner()

    print("=============================================")
    print("🛡️  TERMINALOWY SKANER PHISHINGU (AI MODEL) 🛡️")
    print("Wpisz 'exit', 'wyjdz' lub 'q', aby zamknąć.")
    print("=============================================")

    # Nieskończona pętla do sprawdzania linków na bieżąco
    while True:
        user_input = input("\n👉 Wklej adres URL do sprawdzenia: ").strip()

        if user_input.lower() in ['exit', 'wyjdz', 'quit', 'q']:
            print("Zamykanie skanera. Do widzenia!")
            break

        if user_input:
            skaner.scan(user_input)