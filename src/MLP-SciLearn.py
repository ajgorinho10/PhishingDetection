
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, f1_score
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import TfidfVectorizer

from Set_Processor import ImportData


class MLP:
    def __init__(self):
        self.df = None
        self.X = None
        self.y = None

    def import_data(self):
        data = ImportData()
        self.df,self.X,self.y = data.read_set_3()

    def import_data_NLP(self):
        data = ImportData()
        data.Import_set_3()
        self.X, self.y = data.Get_NLP()

    def run_model(self):
        self.import_data()
        x_df = self.df.drop(columns=['label','url'])
        y_df = self.df['label']

        X_train, X_test, y_train, y_test = train_test_split(x_df, y_df, test_size=0.2, random_state=42)

        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)

        mlp = MLPClassifier(
            hidden_layer_sizes=(10, 5),
            activation='relu',
            solver='adam',
            alpha=0.0001,
            early_stopping=True,
            random_state=42,
            verbose=True
        )

        mlp.fit(X_train_scaled, y_train)
        y_pred = mlp.predict(X_test_scaled)

        skutecznosc = accuracy_score(y_test, y_pred)
        print(f"Skuteczność modelu (Accuracy): {skutecznosc * 100:.2f}%")

        print("\nSzczegółowy raport:")
        print(classification_report(y_test, y_pred))

        print("\nMacierz Pomyłek (Confusion Matrix):")
        print(confusion_matrix(y_test, y_pred))

    def run_model_NLP(self):
        self.import_data_NLP()
        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)

        vectorizer = TfidfVectorizer(analyzer='char', ngram_range=(3, 5), max_features=3000)
        X_train_nlp = vectorizer.fit_transform(X_train)
        X_test_nlp = vectorizer.transform(X_test)

        mlp_nlp = MLPClassifier(
            hidden_layer_sizes=(100,),
            activation='relu',
            solver='adam',
            max_iter=50,
            early_stopping=True,
            random_state=42,
            verbose=True
        )

        print("Trenowanie...")
        mlp_nlp.fit(X_train_nlp, y_train.values)

        y_pred = mlp_nlp.predict(X_test_nlp)

        print("\nRAPORT KOŃCOWY: MLP (NLP TF-IDF)")
        print(classification_report(y_test.values, y_pred))
        print("Macierz Pomyłek:")
        print(confusion_matrix(y_test.values, y_pred))

if __name__ == "__main__":
    mlp = MLP()
    #mlp.run_model()
    mlp.run_model_NLP()
