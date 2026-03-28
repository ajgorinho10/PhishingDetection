import time

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC

from Set_Processor import ImportData

class SVM:
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


        svc_model = LinearSVC(random_state=42, dual=False)

        start_time = time.time()
        svc_model.fit(X_train_nlp, y_train.values)
        svc_time = time.time() - start_time
        print(f"Zakończono w {svc_time:.2f}s")

        y_pred_svc = svc_model.predict(X_test_nlp)

        print("\n" + "-" * 40)
        print("RAPORT KOŃCOWY: LinearSVC + TF-IDF")
        print("-" * 40)
        print(classification_report(y_test.values, y_pred_svc))
        print("Macierz Pomyłek:")
        print(confusion_matrix(y_test.values, y_pred_svc))

    def train(self):
        self.import_data()
        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=0.3, random_state=42)

        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)

        svc_model = LinearSVC(random_state=42, dual=False, max_iter=1000)

        start_time = time.time()
        svc_model.fit(X_train_scaled, y_train.values)
        svc_time = time.time() - start_time
        print(f"Zakończono w {svc_time:.2f}s")

        y_pred_svc = svc_model.predict(X_test_scaled)

        print("\n" + "-" * 40)
        print("RAPORT KOŃCOWY: LinearSVC + CECHY RĘCZNE")
        print("-" * 40)
        print(classification_report(y_test.values, y_pred_svc))
        print("Macierz Pomyłek:")
        print(confusion_matrix(y_test.values, y_pred_svc))

if __name__ == "__main__":
    svm = SVM()
    svm.train()
    svm.train_nlp()