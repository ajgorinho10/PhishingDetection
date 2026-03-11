from pathlib import Path
import pandas as pd

class ImportSet2:
    def __init__(self):
        self.df = None

        self.ok_data_path = None
        self.bad_data_path = None
        self.processed_path = None
        self.path_to_files()
        pass

    def path_to_files(self):
        katalog_glowny = Path(__file__).resolve().parent.parent

        self.ok_data_path = katalog_glowny / "data/set_2/raw/URLdataset.csv"
        self.bad_data_path = katalog_glowny / "data/set_2/raw/PhishingURLs.csv"
        self.processed_path = katalog_glowny / "data/set_2/processed/set2.csv"

    def import_data(self):
        df_ok = pd.read_csv(self.ok_data_path, names=['url', 'type'])
        df_ok = df_ok.drop(index=0)

        df_ok['label'] = df_ok['type'].apply(lambda x: 0 if x == 'legitimate' else 1)
        df_ok = df_ok.drop(columns=['type'])


        df_bad = pd.read_csv(self.bad_data_path, usecols=['url','Type'])
        df_bad = df_bad.drop(index=0)

        df_bad['label'] = df_bad['Type'].apply(lambda x: 0 if x == 'legitimate' else 1)
        df_bad = df_bad.drop(columns=['Type'])


        df = pd.concat([df_ok, df_bad], ignore_index=True)

        df['url'] = df['url'].astype(str)
        df['url'] = df['url'].str.replace(r'^https?:\/\/', '', regex=True)
        df['url'] = df['url'].str.replace(r'^www\.', '', regex=True)

        df = df.sample(frac=1, random_state=42).reset_index(drop=True)

        self.df = df

        return df

if __name__ == "__main__":
    obj = ImportSet2()
    obj.import_data()
    print(obj.df)