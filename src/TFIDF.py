import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

from importData import *

data = ImportData()
data.read_set_2()
X, y = data.Get_NLP()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

vectorizer = TfidfVectorizer(analyzer='char', ngram_range=(3, 5), max_features=3000)
X_train_nlp = vectorizer.fit_transform(X_train)
X_test_nlp = vectorizer.transform(X_test)

cechy_nlp = vectorizer.get_feature_names_out()

# 2. Bierzemy TYLKO 5 pierwszych wierszy i zamieniamy kompresję na zwykłą tabelę (.toarray())
mala_macierz = X_train_nlp[:5].toarray()

# 3. Tworzymy ładną tabelkę w Pandas
df_tfidf = pd.DataFrame(mala_macierz, columns=cechy_nlp)

# 4. Dodajemy oryginalne linki na sam początek (żeby wiedzieć, na co patrzymy)
# Używamy .values, aby uniknąć problemu z indeksami po train_test_split
df_tfidf.insert(0, 'Oryginalny_URL', X_train[:5].values)

# 5. Ponieważ wydrukowanie 3000 kolumn w konsoli zaleje ekran zerami,
# napiszmy sprytną pętlę, która dla każdego z tych 5 linków pokaże tylko te zbitki, które model uznał za ważne (> 0)

for index, row in df_tfidf.iterrows():
    url = row['Oryginalny_URL']
    print("\n" + "-" * 50)
    print(f"🔗 Link: {url}")

    # 1. Wyciągamy z wiersza wszystko OPRÓCZ kolumny z tekstem
    tylko_liczby = row.drop('Oryginalny_URL')

    # 2. Teraz bezpiecznie pytamy, które ułamki są większe od 0, bo mamy same liczby!
    aktywne_cechy = tylko_liczby[tylko_liczby > 0].sort_values(ascending=False)

    print(f"Wyłapano {len(aktywne_cechy)} ważnych zbitek (n-gramów). Oto top 5 najsilniejszych dla tego linku:")
    print(aktywne_cechy.head(5).to_string())