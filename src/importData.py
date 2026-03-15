import pandas as pd

from Features_Extraction import FeaturesExtraction
from Import_Set_1 import ImportSet1
from Import_Set_2 import ImportSet2


class ImportData:
    def __init__(self):
        self.df = None
        self.X = None
        self.y = None

        self.path_to_save = None
        self.set1 = ImportSet1()
        self.set2 = ImportSet2()
        pass

    def Import_set_1(self):
        self.df = self.set1.import_data()
        self.path_to_save = self.set1.processed_path

    def read_set_1(self):
        self.df = pd.read_csv(self.set1.processed_path)
        self.X = self.df.drop(columns=['url', 'label'])
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


    def Get_Scalet_sets(self):
        self.Import_set_1()
        data1 = self.df

        self.Import_set_2()
        data2 = self.df

        data = pd.concat([data1, data2], ignore_index=True)
        data = data.sample(frac=1, random_state=42).reset_index(drop=True)

        data = data.dropna(subset=['url']).drop_duplicates(subset=['url'])
        data['url'] = data['url'].astype(str)

        X = data['url']
        y = data['label']

        return X, y

    def scal_sets(self):
        self.read_set_1()
        x1 = self.df

        self.read_set_2()
        x2 = self.df

        df = pd.concat([x1,x2], ignore_index=True)

        return df


if __name__ == "__main__":
    x = ImportData()
    x.Import_set_2()
    x.Extract_features()
    print(x.df.head())
