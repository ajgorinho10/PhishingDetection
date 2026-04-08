import pandas as pd

from .Features_Extraction import FeaturesExtraction
from .Import_Set_1 import ImportSet1
from .Import_Set_2 import ImportSet2
from .Import_Set_3 import ImportSet3
from .Import_Set_4 import ImportSet4
from .Import_Set_5 import ImportSet5


class ImportData:
    def __init__(self):
        self.df = None
        self.X = None
        self.y = None

        self.path_to_save = None
        self.set1 = ImportSet1()
        self.set2 = ImportSet2()
        self.set3 = ImportSet3()
        self.set4 = ImportSet4()
        self.set5 = ImportSet5()
        pass

    def Import_set_1(self):
        self.df = self.set1.import_data()
        self.path_to_save = self.set1.processed_path

    def read_set_1(self):
        self.df = pd.read_csv(self.set1.processed_path)
        self.X = self.df.drop(columns=['url','label'])
        self.y = self.df['label']

        return self.df, self.X, self.y

    def Import_set_2(self):
        self.df = self.set2.import_data()
        self.path_to_save = self.set2.processed_path

    def read_set_2(self):
        self.df = pd.read_csv(self.set2.processed_path)
        self.X = self.df.drop(columns=['url', 'label'])
        self.y = self.df['label']

        return self.df, self.X, self.y

    def Import_set_3(self):
        self.df = self.set3.import_data()
        self.path_to_save = self.set3.processed_path

    def read_set_3(self):
        self.df = pd.read_csv(self.set3.processed_path)
        self.X = self.df.drop(columns=['url', 'label'])
        self.y = self.df['label']

        return self.df, self.X, self.y
    
    def Import_set_4(self):
        self.df = self.set4.import_data()
        self.path_to_save = self.set4.processed_path

    def read_set_5(self):
        self.df = pd.read_csv(self.set4.processed_path)
        self.X = self.df.drop(columns=['url', 'label'])
        self.y = self.df['label']

    
    def Import_set_5(self):
        self.df = self.set5.import_data()
        self.path_to_save = self.set5.processed_path

    def read_set_5(self):
        self.df = pd.read_csv(self.set5.processed_path)
        self.X = self.df.drop(columns=['url', 'label'])
        self.y = self.df['label']

        return self.df, self.X, self.y

    def Extract_features(self):
        features = FeaturesExtraction()

        data,X,y = features.Extract_Features(self.df,self.path_to_save)
        self.df = data
        self.X = X
        self.y = y

        return data, X, y

    def Get_NLP(self):
        data = self.df
        data = data.dropna(subset=['url']).drop_duplicates(subset=['url'])
        data['url'] = data['url'].astype(str)

        X = data['url']
        y = data['label']

        self.X = X
        self.y = y
        self.df = data

        return X, y


if __name__ == "__main__":
    x = ImportData()
    x.Import_set_3()
    x.Extract_features()
    print(x.df.head())
