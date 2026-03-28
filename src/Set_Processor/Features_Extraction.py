import pandas as pd
import re
import math
from collections import Counter
import Levenshtein

class FeaturesExtraction:
    def __init__(self):
        self.df = None
        self.X = None
        self.y = None
        pass

    def Extract_Features(self,data,path):
        self.df = data

        self.df = self.df.dropna(subset=['url'])

        self.df = self.df.drop_duplicates(subset=['url'])

        self.df['url_length'] = self.df['url'].apply(self.get_url_length)
        self.df['qty_dots'] = self.df['url'].apply(self.count_dots)
        self.df['qty_hyphens'] = self.df['url'].apply(self.count_hyphens)
        self.df['qty_subdomains'] = self.df['url'].apply(self.count_subdomains)
        self.df['qty_semi'] = self.df['url'].apply(self.count_semi)
        self.df['has_redirect'] = self.df['url'].apply(self.has_redirect_pattern)
        self.df['lev_distance'] = self.df['url'].apply(self.LevCheck)
        self.df['homoglyphs'] = self.df['url'].apply(self.count_homoglyphs)
        self.df['entropy'] = self.df['url'].apply(self.calculate_entropy)
        self.df['suspicious_keywords_count'] = self.df['url'].apply(self.count_suspicious_keywords)

        self.X = self.df.drop(columns=['url', 'label'])
        self.y = self.df['label']

        self.df.to_csv(path, index=False)

        return self.df, self.X, self.y

    def count_dash(self,url):
        return str(url).count('/')

    def get_url_length(self,url):
        return len(str(url))

    def count_dots(self,url):
        return str(url).count('.')

    def count_hyphens(self,url):
        return str(url).count('-')

    def count_semi(self,url):
        return str(url).count(';')

    def count_subdomains(self,url):
        dots = str(url).count('.')
        return dots - 1 if dots > 1 else 0

    def has_redirect_pattern(self, url):
        url_lower = str(url).lower()
        patterns = ['?u=', '?url=', '?redirect=', '?next=', '&url=']
        for p in patterns:
            if p in url_lower:
                return 1
        return 0

    def get_df(self):
        return self.df

    def get_x(self):
        return self.X

    def get_y(self):
        return self.y

    def count_suspicious_keywords(self,url):
        suspicious_keywords = [
            'login', 'verify', 'update', 'account', 'secure',
            'bank', 'password', 'credential', 'support',
            'service', 'authenticate', 'billing', 'wallet',
            'confirm', 'admin', 'free', 'bonus', 'payment',
            '.io', '.to', 'ghost', 'konto' , 'oferta'
        ]

        full_url = str(url).lower()

        index = full_url.find("/")
        if index != -1:
            url_domain = full_url[:index]
            url_path = full_url[index + 1:]
        else:
            url_domain = full_url
            url_path = ""

        score = 0
        for word in suspicious_keywords:
            if word in url_domain:
                score += 2

            if word in url_path:
                score += 1

        return score

    def LevCheck(self, url):
        suspicious_keywords = [
            'login', 'verify', 'update', 'account', 'secure',
            'bank', 'password', 'credential', 'support',
            'service', 'authenticate', 'billing', 'wallet',
            'confirm', 'admin', 'free', 'bonus', 'payment',
            'ghost', 'konto', 'oferta'
        ]

        full_url = str(url).lower()
        score = 0

        # Rozcinamy cały link na pojedyncze słowa (dzielimy po kropkach, myślnikach, ukośnikach itp.)
        # np. z 'secure-log1n.com/update' zrobi listę: ['secure', 'log1n', 'com', 'update']
        url_tokens = re.split(r'[\W_]+', full_url)

        # Filtrujemy puste tokeny
        url_tokens = [token for token in url_tokens if token]

        for word in suspicious_keywords:
            for token in url_tokens:
                # Optymalizacja: sprawdzamy Levenshteina tylko dla tokenów o podobnej długości
                # Nie ma sensu porównywać słowa "bank" (4 litery) z tokenem "a" (1 litera)
                if abs(len(word) - len(token)) <= 2:
                    dist = Levenshtein.distance(word, token)

                    # Jeśli to jest IDEALNE trafienie (dist == 0), haker użył słowa wprost
                    # Jeśli dist to 1 lub 2, haker użył literówki (Typosquatting)
                    if dist == 1 or dist == 2:
                        score += 1

        return score

    def count_homoglyphs(self, url):
        """Opcja 2: Szukanie sztuczek wizualnych hakerów"""
        url_lower = str(url).lower()

        # Wyciągamy samą domenę (odcinamy wszystko po ' / ')
        index = url_lower.find("/")
        domain = url_lower[:index] if index != -1 else url_lower

        count = 0
        # 1. Szukamy zera ukrytego między literami (np. faceb00k, g00gle)
        count += len(re.findall(r'[a-z]0[a-z]', domain))

        # 2. Szukamy jedynki ukrytej między literami (np. paypa1)
        count += len(re.findall(r'[a-z]1[a-z]', domain))

        # 3. Szukamy zbitki 'rn', która udaje 'm' (np. steamconmunity)
        count += domain.count('rn')

        # 4. Szukamy zbitki 'vv', która udaje 'w'
        count += domain.count('vv')

        return count

    def calculate_entropy(self, url):
        """Opcja 3: Entropia Shannona (miara chaosu)"""
        url_str = str(url)
        if not url_str:
            return 0.0

        # Liczymy, ile razy występuje każdy znak
        counts = Counter(url_str)
        length = len(url_str)

        # Obliczamy prawdopodobieństwa i stosujemy wzór Shannona
        entropy = 0.0
        for count in counts.values():
            p = count / length
            entropy -= p * math.log2(p)

        return entropy

