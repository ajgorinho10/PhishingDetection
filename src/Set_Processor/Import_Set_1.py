from pathlib import Path
import pandas as pd

#https://huggingface.co/datasets/semihGuner2002/PhishingURLsDataset
class ImportSet1:
    def __init__(self):
        self.df = None

        self.ok_data_path = None
        self.bad_data_path = None
        self.processed_path = None
        self.path_to_files()
        pass

    def path_to_files(self):
        katalog_glowny = Path(__file__).resolve().parent.parent.parent

        self.ok_data_path = katalog_glowny / "data/set_1/raw/urldata.csv"
        self.processed_path = katalog_glowny / "data/set_1/processed/set1.csv"

    def import_data(self):
        df = pd.read_csv(self.ok_data_path, sep=',')
        df = df.drop(df.index[0])

        df = df.loc[:, ['url', 'label']]
        df['label'] = df['label'].apply(lambda x: 0 if str(x).strip() == 'benign' else 1)
        df['label'].astype('int8')


        df['url'] = df['url'].astype('str')
        df['url'] = df['url'].str.replace(r'^https?:\/\/', '', regex=True)
        df['url'] = df['url'].str.replace(r'^www\.', '', regex=True)

        df = df.drop_duplicates(keep='first')
        df.to_csv(self.processed_path,sep=',', index=False)
        
        self.df = df
        return df
    
    def read_data(self):
        df = pd.read_csv(self.processed_path)
        self.df = df
        
        return df

if __name__ == '__main__':
    x = ImportSet1()
    x.import_data()
    #x.read_data()
    print(x.df.head(5))