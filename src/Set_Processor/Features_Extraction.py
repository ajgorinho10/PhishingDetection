import pandas as pd
import re
from urllib.parse import urlparse

class FeaturesExtraction:
    def __init__(self):
        self.df = None
        self.X = None
        self.y = None
        
        # Prekompilowane reguły dla wydajności (O(1) lookups)
        self.ipv4_pattern = re.compile(r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$')
        self.shorteners = {'bit.ly', 'tinyurl.com', 'v.ht', 'is.gd', 't.co', 'goo.gl', 'ow.ly', 'cutt.ly', 'rb.gy', 'qrco.de'}
        self.risky_tlds = {'.xyz', '.top', '.pw', '.ru', '.cc', '.tk', '.ml', '.ga', '.cf', '.gq', '.info', '.site', '.click'}
        self.keywords = {'login', 'verify', 'update', 'account', 'secure', 'bank', 'password', 'credential', 'support', 'service', 'authenticate', 'billing', 'wallet', 'confirm', 'admin', 'free', 'bonus', 'payment', 'ghost', 'konto', 'oferta'}

    def Extract_Features(self, data, path):
        self.df = data
        self.df = self.df.dropna(subset=['url'])
        self.df = self.df.drop_duplicates(subset=['url'])

        # Podstawowe cechy (szybkie)
        self.df['url_length'] = self.df['url'].apply(len)
        self.df['qty_dots'] = self.df['url'].apply(lambda x: str(x).count('.'))
        self.df['qty_hyphens'] = self.df['url'].apply(lambda x: str(x).count('-'))
        self.df['qty_subdomains'] = self.df['url'].apply(self.count_subdomains)
        self.df['has_redirect'] = self.df['url'].apply(self.has_redirect_pattern)
        
        # Nowe, zoptymalizowane cechy
        self.df['has_ip_domain'] = self.df['url'].apply(self.has_ip_domain)
        self.df['is_shortener'] = self.df['url'].apply(self.is_shortener)
        self.df['special_char_ratio'] = self.df['url'].apply(self.special_char_ratio)
        self.df['is_risky_tld'] = self.df['url'].apply(self.is_risky_tld)
        self.df['path_depth'] = self.df['url'].apply(self.get_path_depth)
        self.df['has_punycode'] = self.df['url'].apply(self.has_punycode)
        self.df['digit_to_letter_ratio'] = self.df['url'].apply(self.digit_to_letter_ratio)
        self.df['keyword_in_subdomain'] = self.df['url'].apply(self.keyword_in_subdomain)

        self.X = self.df.drop(columns=['url', 'label'])
        self.y = self.df['label']

        self.df.to_csv(path, index=False)
        return self.df, self.X, self.y

    # --- FUNKCJE POMOCNICZE ---
    def _parse_url(self, url):
        url_str = str(url).lower()
        if not url_str.startswith(('http://', 'https://')):
            url_str = 'http://' + url_str
        try:
            return urlparse(url_str)
        except:
            return None

    def _get_domain(self, parsed_url):
        if not parsed_url: return ""
        return parsed_url.netloc.split(':')[0] # Usunięcie portu, jeśli istnieje

    # --- EKSTRAKCJA CECH ---
    def count_subdomains(self, url):
        parsed = self._parse_url(url)
        domain = self._get_domain(parsed)
        dots = domain.count('.')
        return dots - 1 if dots > 1 else 0

    def has_redirect_pattern(self, url):
        url_lower = str(url).lower()
        patterns = ['?u=', '?url=', '?redirect=', '?next=', '&url=']
        for p in patterns:
            if p in url_lower:
                return 1
        return 0

    def has_ip_domain(self, url):
        domain = self._get_domain(self._parse_url(url))
        if self.ipv4_pattern.match(domain):
            return 1
        return 0

    def is_shortener(self, url):
        domain = self._get_domain(self._parse_url(url))
        if domain in self.shorteners:
            return 1
        return 0

    def special_char_ratio(self, url):
        url_str = str(url)
        if not url_str: return 0.0
        special_chars = sum(1 for c in url_str if c in '-_?=&;')
        return special_chars / len(url_str)

    def is_risky_tld(self, url):
        domain = self._get_domain(self._parse_url(url))
        if '.' in domain:
            tld = domain[domain.rfind('.'):]
            if tld in self.risky_tlds:
                return 1
        return 0

    def get_path_depth(self, url):
        parsed = self._parse_url(url)
        if not parsed: return 0
        path = parsed.path
        # Ignoruj końcowy ukośnik
        if path.endswith('/'): path = path[:-1]
        return path.count('/')

    def has_punycode(self, url):
        if 'xn--' in str(url).lower():
            return 1
        return 0

    def digit_to_letter_ratio(self, url):
        url_str = str(url)
        digits = sum(c.isdigit() for c in url_str)
        letters = sum(c.isalpha() for c in url_str)
        return digits / (letters + 1e-5)

    def keyword_in_subdomain(self, url):
        domain = self._get_domain(self._parse_url(url))
        parts = domain.split('.')
        # Jeśli domena to np. login.bank.com, sprawdzamy 'login' (pomijamy 'bank' i 'com')
        if len(parts) > 2:
            subdomains = parts[:-2]
            for sub in subdomains:
                if any(kw in sub for kw in self.keywords):
                    return 1
        return 0