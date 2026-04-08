from pathlib import Path
import pandas as pd
import csv

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
        parsed_data = []
        
        # 1. Bezpieczny odczyt pliku linia po linii (ignoruje błędy kodowania bajtów)
        with open(self.data_path, 'r', encoding='utf-8', errors='replace') as f:
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
        df = pd.DataFrame(parsed_data, columns=['url', 'status'])
        
        df = df.rename(columns={'status': 'label'})
        df['label'] = df['label'].apply(lambda x : 1 if str(x).strip() == '0' else 0)


        df['url'] = df['url'].astype(str)
        df['url'] = df['url'].str.replace(r'^https?:\/\/', '', regex=True)
        df['url'] = df['url'].str.replace(r'^www\.', '', regex=True)
        df.drop_duplicates(subset=['url'], inplace=True)
        df['label'] = df['label'].astype('int8')

        self.df = df

        return df

if __name__ == '__main__':
    x = ImportSet3()
    x.import_data()
    print(x.df['label'].value_counts())
    print(x.df.head())