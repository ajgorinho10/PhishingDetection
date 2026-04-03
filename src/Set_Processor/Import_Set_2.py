from pathlib import Path
import pandas as pd

class ImportSet2:
    def __init__(self):
        self.df = None

        self.data1_path = None
        self.data2_path = None
        self.processed_path = None
        self.path_to_files()
        pass

    def path_to_files(self):
        katalog_glowny = Path(__file__).resolve().parent.parent.parent

        self.data1_path = katalog_glowny / "data/set_2/raw/URLdataset.csv"
        self.data2_path = katalog_glowny / "data/set_2/raw/PhishingURLs.csv"
        self.processed_path = katalog_glowny / "data/set_2/processed/set2.csv"

    def import_data(self):
        df_data1 = pd.read_csv(self.data1_path, names=['url', 'type'])
        df_data1 = df_data1.drop(index=0)

        df_data1['label'] = df_data1['type'].apply(lambda x: 0 if x == 'legitimate' else 1)
        df_data1 = df_data1.drop(columns=['type'])


        df_data2 = pd.read_csv(self.data2_path, usecols=['url','Type'])
        df_data2 = df_data2.drop(index=0)

        df_data2['label'] = df_data2['Type'].apply(lambda x: 0 if x == 'legitimate' else 1)
        df_data2 = df_data2.drop(columns=['Type'])


        df = pd.concat([df_data1, df_data2], ignore_index=True)

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