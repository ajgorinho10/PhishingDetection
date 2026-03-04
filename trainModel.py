from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, precision_score, recall_score, f1_score
from importData import ImportData

from sklearn import tree
import matplotlib.pyplot as plt
import xgboost as xgb
import joblib
import pandas as pd

from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

class TrainModel:
    def __init__(self):
        self.y = None
        self.X = None
        self.df = None
        self.import_data()
        #self.import_data2()


    def import_data(self):
        self.df = pd.read_csv("data/dataToTrain.csv")
        self.X = self.df.drop(columns=['url', 'label'])
        self.y = self.df['label']

    def import_data2(self):
        x = ImportData()
        self.df = x.get_df()
        self.X = x.get_x()
        self.y = x.get_y()


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
            nazwa_pliku = 'phishing_randomforest_model.pkl'
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
            nazwa_pliku = 'phishing_xgboost_model.pkl'
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


    def findParameters(self):
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

    def findParametersRandom(self):
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


trainModel = TrainModel()
trainModel.train_XGBoost(save = True)
#trainModel.train_RandomForest(save=True)
#trainModel.findParameters()