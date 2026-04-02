from pathlib import Path
import pandas as pd

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

        self.ok_data_path = katalog_glowny / "data/set_1/raw/oksites.csv"
        self.bad_data_path = katalog_glowny / "data/set_1/raw/badsites.csv"
        self.processed_path = katalog_glowny / "data/set_1/processed/set1.csv"

    def import_data(self):
        df_ok = pd.read_csv(self.ok_data_path, names=['rank', 'url'])
        df_ok = df_ok[['url']]
        df_ok['label'] = 0

        df_bad = pd.read_csv(self.bad_data_path, usecols=['url'])
        df_bad['label'] = 1

        df = pd.concat([df_ok, df_bad], ignore_index=True)

        df['url'] = df['url'].astype(str)
        df['url'] = df['url'].str.replace(r'^https?:\/\/', '', regex=True)
        df['url'] = df['url'].str.replace(r'^www\.', '', regex=True)

        df = df.sample(frac=1, random_state=42).reset_index(drop=True)

        self.df = df

        return df

if __name__ == '__main__':
    x = ImportSet1()
    x.import_data()