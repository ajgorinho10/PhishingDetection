
#verified_online.csv - PishTank
#tranco_7NV9X.csv - tranco 1ml

from pathlib import Path
import pandas as pd
import csv

class ImportSet4:
    def __init__(self):
        self.df = None

        self.data1_path = None
        
        self.processed_path = None
        self.path_to_files()
        pass

    def path_to_files(self):
        katalog_glowny = Path(__file__).resolve().parent.parent.parent

        self.data1_path = katalog_glowny / "data/set_4/raw/verified_online.csv"
        self.data2_path = katalog_glowny / "data/set_4/raw/tranco_7NV9X.csv"
        
        self.processed_path = katalog_glowny / "data/set_4/processed/set4.csv"

    def import_data(self):
        df1 = self.read_and_clear_data(self.data1_path, 1, ['phish_id','url','phish_detail_url','submission_time','verified','verification_time','online','target'])
        df1 = df1.drop(df1.index[0])

        df2 = self.read_and_clear_data(self.data2_path, 0, ['id','url'])
        from .Import_Set_1 import ImportSet1
        set1 = ImportSet1()
        df3 = set1.import_data()
        
        df = pd.concat([df1, df2, df3], ignore_index=True)
        df = df.sample(frac=1, random_state=42).reset_index(drop=True)

        df.drop_duplicates(subset=['url'], keep='first', inplace=True)
        
        self.df = df
        return df
    
    def read_and_clear_data(self, path, label_value, column = None):
        df = pd.read_csv(path, sep=',', names = column)

        df = df.loc[:, ['url']]
 
        df['label'] = label_value
        df['url'] = df['url'].astype(str)
        df['label'] = df['label'].astype('int8')
        
        # UWAGA LOGICZNA:
        # Usuwanie schematów URL musi być spójne dla WSZYSTKICH zbiorów (1, 2, 3 i 5).
        # Jeśli w innych klasach ImportSetX nie ma poniższych dwóch linii, zakomentuj je również tutaj.
        df['url'] = df['url'].str.replace(r'^https?:\/\/', '', regex=True)
        df['url'] = df['url'].str.replace(r'^www\.', '', regex=True)
                 
        return df

if __name__ == '__main__':
    x = ImportSet4()
    x.import_data()
    
    print(x.df.head())
    print(x.df['label'].value_counts())
    print("Ilość adresów url: ",x.df['url'].count())
    print("Ilość etykiet dla url: ",x.df['label'].count())
    
    x.df.to_csv(x.processed_path,index=False)