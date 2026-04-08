from pathlib import Path
import pandas as pd
import csv

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
        
    def import_csv(self,path, cloumns):
        parsed_data = []
        
        # 1. Bezpieczny odczyt pliku linia po linii (ignoruje błędy kodowania bajtów)
        with open(path, 'r', encoding='utf-8', errors='replace') as f:
            lines = f.readlines()

        # 2. Ręczny podział od prawej strony (z pominięciem nagłówka w pierwszej linii)
        for line in lines[1:]:
            line = line.strip()
            if not line:
                continue
            
            parts = line.rsplit(',', 1)
            if len(parts) == 2:
                parsed_data.append(parts)

        # 3. Konwersja do DataFrame
        df = pd.DataFrame(parsed_data, columns=cloumns)
        
        return df

    def import_data(self):
        df_data1 = self.import_csv(self.data1_path, ['url', 'type'])
        df_data1['label'] = df_data1['type'].apply(lambda x: 0 if str(x).strip().lower() == 'legitimate' else 1)
        df_data1 = df_data1.drop(columns=['type'])

        df_data2 = self.import_csv(self.data2_path,['url','Type'])
        df_data2['label'] = df_data2['Type'].apply(lambda x: 0 if str(x).strip().lower() == 'legitimate' else 1)
        df_data2 = df_data2.drop(columns=['Type'])


        df = pd.concat([df_data1, df_data2], ignore_index=True)

        df['url'] = df['url'].astype(str)
        df['url'] = df['url'].str.replace(r'^https?:\/\/', '', regex=True)
        df['url'] = df['url'].str.replace(r'^www\.', '', regex=True)

        df = df.sample(frac=1, random_state=42).reset_index(drop=True)
        
        df['label'] = df['label'].astype('int8')
        df = df.drop_duplicates(keep='first')

        self.df = df

        return df

if __name__ == "__main__":
    obj = ImportSet2()
    obj.import_data()
    print(obj.df)