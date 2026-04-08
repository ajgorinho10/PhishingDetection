from pathlib import Path
import pandas as pd
import csv

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
        df1_ok = self.read_and_clear_data(self.data1_path, 0)
        df2_ok = self.read_and_clear_data(self.data2_path, 0)
        
        df1_bad = self.read_and_clear_data(self.data3_path, 1)
        df2_bad = self.read_and_clear_data(self.data4_path, 1)
        
        df = pd.concat([df1_ok, df2_ok, df1_bad, df2_bad], ignore_index=True)
        df = df.sample(frac=1, random_state=42).reset_index(drop=True)

        df.drop_duplicates(subset=['url'], keep='first', inplace=True)
        
        self.df = df
        return df
    
    def read_and_clear_data(self, path, label_value):
        parsed_data = []
        
        with open(path, 'r', encoding='utf-8', errors='replace') as f:
            lines = f.readlines()

        # Tu nie omijamy nagłówka (lines[1:]), bo to czysty plik txt bez nagłówków. Czytamy od lines[0:]
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            # Dodajemy całą linię jako URL, bez rsplit
            parsed_data.append(line)

        # Konwersja do DataFrame
        df = pd.DataFrame(parsed_data, columns=['url'])
 
        df['label'] = label_value
        df['url'] = df['url'].astype(str)
        
        # UWAGA LOGICZNA:
        # Usuwanie schematów URL musi być spójne dla WSZYSTKICH zbiorów (1, 2, 3 i 5).
        # Jeśli w innych klasach ImportSetX nie ma poniższych dwóch linii, zakomentuj je również tutaj.
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