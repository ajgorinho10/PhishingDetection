from pathlib import Path
import pandas as pd

class ImportSet3:
    def __init__(self):
        self.df = None

        self.data_path = None
        self.processed_path = None
        self.path_to_files()
        pass

    def path_to_files(self):
        katalog_glowny = Path(__file__).resolve().parent.parent.parent

        self.data_path = katalog_glowny / "data/set_3/raw/new_data_urls.csv"
        self.processed_path = katalog_glowny / "data/set_3/processed/set3.csv"

    def import_data(self):
        df = pd.read_csv(self.data_path, names=['url', 'status'], dtype={'url': str, 'status': str})
        df = df.drop(index=0)
        df = df.rename(columns={'status': 'label'})
        df['label'] = df['label'].apply(lambda x : 1 if x == '0' else 0)


        df.drop_duplicates(subset=['url'], inplace=True)
        df['url'] = df['url'].astype(str)
        df['url'] = df['url'].str.replace(r'^https?:\/\/', '', regex=True)
        df['url'] = df['url'].str.replace(r'^www\.', '', regex=True)

        self.df = df

        return df

if __name__ == '__main__':
    x = ImportSet3()
    x.import_data()
    print(x.df['label'].value_counts())
    print(x.df.head())