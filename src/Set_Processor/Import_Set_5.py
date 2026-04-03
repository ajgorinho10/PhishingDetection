from pathlib import Path
import pandas as pd

class ImportSet5:
    def __init__(self):
        self.df = None

        self.data1_path = None
        self.data2_path = None
        self.data3_path = None
        self.data4_path = None
        
        self.processed_path = None
        self.path_to_files()
        pass

    def path_to_files(self):
        katalog_glowny = Path(__file__).resolve().parent.parent.parent

        self.data1_path = katalog_glowny / "data/set_5/raw/benign_Test.txt"
        self.data2_path = katalog_glowny / "data/set_5/raw/benign_Train.txt"
        self.data3_path = katalog_glowny / "data/set_5/raw/malign_Test.txt"
        self.data4_path = katalog_glowny / "data/set_5/raw/malign_Train.txt"
        
        self.processed_path = katalog_glowny / "data/set_5/processed/set5.csv"

    def import_data(self):
        df1_ok = self.read_and_clear_data(self.data1_path,0)
        df2_ok = self.read_and_clear_data(self.data2_path,0)
        
        df1_bad = self.read_and_clear_data(self.data3_path,1)
        df2_bad = self.read_and_clear_data(self.data4_path,1)
        
        df = pd.concat([df1_ok,df2_ok,df1_bad,df2_bad], ignore_index=True)
        df = df.sample(frac=1, random_state=42).reset_index(drop=True)

        df.drop_duplicates(subset=['url'],keep='first',inplace=True)
        

        self.df = df
        return df
    
    def read_and_clear_data(self, path, label_value):
            df = pd.read_csv(path, header=None, names=["url"], keep_default_na=False,sep='\t')
            
            df['label'] = label_value
            
            df['url'] = df['url'].astype(str)
            df['url'] = df['url'].str.replace(r'^https?:\/\/', '', regex=True)
            df['url'] = df['url'].str.replace(r'^www\.', '', regex=True)
                     
            return df

if __name__ == '__main__':
    x = ImportSet5()
    x.import_data()
    print(x.df['label'].value_counts())
    print("Ilość adresów url: ",x.df['url'].count())
    print("Ilość etykiet dla url: ",x.df['label'].count())
    
    x.df.to_csv(x.processed_path,index=False)