import string
from typing import Dict,List

from .global_config import cfg

class CharTokenizer:
    """
    Mapuje każdy znak URL-a na indeks.
    Alfabet: ASCII printable (32-127) + PAD + UNK.
    """
    def __init__(self, max_len: int = cfg.MAX_LEN):
        self.max_len = max_len
        # Indeksy 0 i 1 zarezerwowane dla PAD i UNK
        chars = list(string.printable)  # 100 znaków
        self.char2idx: Dict[str, int] = {
            c: i + 2 for i, c in enumerate(chars)
        }
        self.vocab_size = len(chars) + 2  # +PAD +UNK

    def encode(self, url: str) -> List[int]:
        """URL → lista indeksów. Przy przekroczeniu max_len wycina środek."""
        if len(url) > self.max_len:
            # Zostawia np. pierwsze 40 znaków i resztę uzupełnia końcówką
            keep_front = 40
            keep_back = self.max_len - keep_front
            url = url[:keep_front] + url[-keep_back:]
            
        url = url.lower()
        ids = [self.char2idx.get(c, cfg.UNK_IDX) for c in url]
        # Padding po prawej
        ids += [cfg.PAD_IDX] * (self.max_len - len(ids))
        return ids
    
    def encode_dataset(self, data: list) -> List[int]:
        return [ self.encode(url) for url in data ]
    
    def get_dictionary(self):
        return self.char2idx
    
    
if __name__ == "__main__":
    x = CharTokenizer()
    
    
    print(x.encode_dataset(["siema.com","siema.txt"]))
    
    #print(len(x.char2idx))
    #print(x.char2idx)
    #print(x.encode("abcd.com"))