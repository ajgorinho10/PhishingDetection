from sklearn.naive_bayes import MultinomialNB, GaussianNB
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import time

from Set_Processor import ImportData

class NaiveBayes:
    def __init__(self):
        self.df = None
        self.X = None
        self.y = None

    def import_data(self):
        x = ImportData()
        self.df,self.X, self.y = x.scal_sets()
        pass

    def import_data_nlp(self):
        x = ImportData()
        self.X,self.y = x.Get_Scalet_sets()
        pass

    def train_nlp(self):
        self.import_data_nlp()
        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=0.3, random_state=42)

        vectorizer = TfidfVectorizer(analyzer='char', ngram_range=(3, 5), max_features=3000)
        X_train_nlp = vectorizer.fit_transform(X_train)
        X_test_nlp = vectorizer.transform(X_test)

        print("\nTRENOWANIE: Naive Bayes")
        nb_model = MultinomialNB()

        start_time = time.time()
        nb_model.fit(X_train_nlp, y_train.values)
        nb_time = time.time() - start_time
        print(f"Zakończono w {nb_time:.2f}s")

        y_pred_nb = nb_model.predict(X_test_nlp)

        print("\n" + "-" * 40)
        print("RAPORT KOŃCOWY: Naive Bayes + TF-IDF")
        print("-" * 40)
        print(classification_report(y_test.values, y_pred_nb))
        print("Macierz Pomyłek:")
        print(confusion_matrix(y_test.values, y_pred_nb))

    def train(self):
        self.import_data()
        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=0.3, random_state=42)

        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)

        nb_model = GaussianNB()
        start_time = time.time()
        nb_model.fit(X_train_scaled, y_train.values)
        nb_time = time.time() - start_time
        print(f"Zakończono w {nb_time:.2f}s")

        y_pred_nb = nb_model.predict(X_test_scaled)

        print("\n" + "-" * 40)
        print("RAPORT KOŃCOWY: Naive Bayes + CECHY RĘCZNE")
        print("-" * 40)
        print(classification_report(y_test.values, y_pred_nb))
        print("Macierz Pomyłek:")
        print(confusion_matrix(y_test.values, y_pred_nb))

if __name__ == "__main__":
    nb = NaiveBayes()
    nb.train()
    #nb.train_nlp()