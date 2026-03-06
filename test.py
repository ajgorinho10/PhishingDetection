import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

print("Wczytywanie surowych danych...")
# Tutaj potrzebujemy SUROWYCH adresów URL, a nie naszych wyliczonych kropek i entropii!
# Najlepiej wczytać dane złączone, zanim usunęliśmy kolumnę 'url'
df_ok = pd.read_csv('data/oksites.csv', names=['rank', 'url'])[['url']]
df_ok['label'] = 0

df_bad = pd.read_csv('data/badsites.csv', usecols=['url'])
df_bad['label'] = 1
df_bad['url'] = df_bad['url'].str.replace(r'^https?:\/\/', '', regex=True)
df_bad['url'] = df_bad['url'].str.replace(r'^www\.', '', regex=True)

df = pd.concat([df_ok, df_bad], ignore_index=True)
df = df.dropna(subset=['url']).drop_duplicates(subset=['url'])
df['url'] = df['url'].astype(str)

X = df['url'] # Naszym wejściem jest SAM TEKST!
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# =======================================================
# KROK 1: MAGIA NLP (Wektoryzacja TF-IDF)
# =======================================================
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
rf_nlp = RandomForestClassifier(n_estimators=100, max_depth=20, n_jobs=-1, random_state=42)
rf_nlp.fit(X_train_nlp, y_train)

# Przewidywanie
y_pred = rf_nlp.predict(X_test_nlp)

# =======================================================
# RAPORT KOŃCOWY
# =======================================================
print("\n" + "="*50)
print("RAPORT: NLP (TF-IDF) + RANDOM FOREST")
print("="*50)
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