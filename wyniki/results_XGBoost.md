# XGBoost (NLP-TfIDF + Cechy)
## SET - 1
### Metryki
-  Precision : 0.9605   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.9139   (ile phishingów zostało wykrytych)
-  F1        : 0.9367
-  FPR       : 0.0106   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 1618 / 12047 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=282,101  F1=0.9079
-  [ 50–100 znaków]  n=136,470  F1=0.9762
-  [100–150 znaków]  n= 17,188  F1=0.9800
-  [150–200 znaków]  n=  3,694  F1=0.9834
-  [200–999 znaków]  n=  3,727  F1=0.9949

### Rozkład predykcji
-  [0.0–0.1]  n= 317,321  acc=0.996  ████████████████████████████
-  [0.1–0.2]  n=  16,208  acc=0.912  █
-  [0.2–0.3]  n=   7,553  acc=0.791  
-  [0.3–0.4]  n=   5,334  acc=0.644  
-  [0.4–0.5]  n=   4,044  acc=0.473  
-  [0.5–0.6]  n=   3,688  acc=0.680  
-  [0.6–0.7]  n=   4,479  acc=0.790  
-  [0.7–0.8]  n=   6,154  acc=0.884  
-  [0.8–0.9]  n=  11,202  acc=0.950  █
-  [0.9–1.0]  n=  67,221  acc=0.996  ██████

### Top 10 domen w błędach (Domena | Model | Prawda)
      50×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
      44×  twitter.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      37×  ckuik.com                           | Model: Phishing (1) | Prawda: Legit (0)
      33×  twitter.com                         | Model: Phishing (1) | Prawda: Legit (0)
      17×  httpss:                             | Model: Phishing (1) | Prawda: Legit (0)
      16×  naymz.com                           | Model: Phishing (1) | Prawda: Legit (0)
      15×  lazygirls.info                      | Model: Phishing (1) | Prawda: Legit (0)
      15×  angelfire.com                       | Model: Legit (0)    | Prawda: Phishing (1)
      12×  badoo.com                           | Model: Phishing (1) | Prawda: Legit (0)
      12×  fireangel.biz                       | Model: Phishing (1) | Prawda: Legit (0)


## SET - 2
### Metryki
-  Precision : 0.9727   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.8605   (ile phishingów zostało wykrytych)
-  F1        : 0.9132
-  FPR       : 0.0106   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 3264 / 24826 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=314,244  F1=0.8859
-  [ 50–100 znaków]  n=152,865  F1=0.9547
-  [100–150 znaków]  n= 18,789  F1=0.9454
-  [150–200 znaków]  n=  7,058  F1=0.9137
-  [200–999 znaków]  n=  4,461  F1=0.9885

### Rozkład predykcji
-  [0.0–0.1]  n= 318,968  acc=0.991  █████████████████████████
-  [0.1–0.2]  n=  18,305  acc=0.808  █
-  [0.2–0.3]  n=  10,070  acc=0.593  
-  [0.3–0.4]  n=   8,198  acc=0.419  
-  [0.4–0.5]  n=   7,698  acc=0.248  
-  [0.5–0.6]  n=   8,273  acc=0.857  
-  [0.6–0.7]  n=   9,374  acc=0.900  
-  [0.7–0.8]  n=  11,433  acc=0.937  
-  [0.8–0.9]  n=  19,991  acc=0.972  █
-  [0.9–1.0]  n=  85,153  acc=0.997  ██████

### Top 10 domen w błędach (Domena | Model | Prawda)
     820×  docs.google.com                     | Model: Legit (0)    | Prawda: Phishing (1)
     622×  cloudflare-ipfs.com                 | Model: Legit (0)    | Prawda: Phishing (1)
     324×  cf-ipfs.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      98×  flowcode.com                        | Model: Legit (0)    | Prawda: Phishing (1)
      58×  rp.mockplus.com                     | Model: Legit (0)    | Prawda: Phishing (1)
      50×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
      47×  ipfs.eth.aragon.network             | Model: Legit (0)    | Prawda: Phishing (1)
      44×  twitter.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      37×  ckuik.com                           | Model: Phishing (1) | Prawda: Legit (0)
      36×  cakeresume.com                      | Model: Legit (0)    | Prawda: Phishing (1)


## SET - 3
### Metryki
-  Precision : 0.9312   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.6801   (ile phishingów zostało wykrytych)
-  F1        : 0.7861
-  FPR       : 0.0433   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 12683 / 136235 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=570,056  F1=0.7298
-  [ 50–100 znaków]  n=182,694  F1=0.9402
-  [100–150 znaków]  n= 25,912  F1=0.9700
-  [150–200 znaków]  n=  6,871  F1=0.9763
-  [200–999 znaków]  n=  9,325  F1=0.9892

### Rozkład predykcji
-  [0.0–0.1]  n= 367,687  acc=0.975  ██████████████████
-  [0.1–0.2]  n=  44,170  acc=0.533  ██
-  [0.2–0.3]  n=  38,643  acc=0.361  █
-  [0.3–0.4]  n=  41,508  acc=0.174  ██
-  [0.4–0.5]  n=  34,092  acc=0.156  █
-  [0.5–0.6]  n=  23,139  acc=0.817  █
-  [0.6–0.7]  n=  21,512  acc=0.820  █
-  [0.7–0.8]  n=  29,703  acc=0.884  █
-  [0.8–0.9]  n=  37,755  acc=0.905  █
-  [0.9–1.0]  n= 156,737  acc=0.979  ███████

### Top 10 domen w błędach (Domena | Model | Prawda)
     955×  pastehtml.com                       | Model: Legit (0)    | Prawda: Phishing (1)
     207×  angelfire.com                       | Model: Phishing (1) | Prawda: Legit (0)
     173×  villakidsbuffetinfantil.com         | Model: Legit (0)    | Prawda: Phishing (1)
     165×  freewebs.com                        | Model: Phishing (1) | Prawda: Legit (0)
     123×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
     107×  ddj.com                             | Model: Phishing (1) | Prawda: Legit (0)
     104×  home.comcast.net                    | Model: Legit (0)    | Prawda: Phishing (1)
      72×  painterspaintings.com               | Model: Legit (0)    | Prawda: Phishing (1)
      51×  fibtex.lodz.pl                      | Model: Phishing (1) | Prawda: Legit (0)
      50×  home.earthlink.net                  | Model: Phishing (1) | Prawda: Legit (0)


## SET - 4
### Metryki
-  Precision : 0.2136   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.8126   (ile phishingów zostało wykrytych)
-  F1        : 0.3383
-  FPR       : 0.1673   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 13252 / 177751 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=1,040,321  F1=0.2729
-  [ 50–100 znaków]  n=  8,022  F1=0.8855
-  [100–150 znaków]  n=  1,852  F1=0.8923
-  [150–200 znaków]  n=  4,925  F1=0.9060
-  [200–999 znaków]  n=    770  F1=0.9401

### Rozkład predykcji
-  [0.0–0.1]  n=  50,103  acc=0.953  █
-  [0.1–0.2]  n= 179,676  acc=0.987  ██████
-  [0.2–0.3]  n= 269,657  acc=0.991  ██████████
-  [0.3–0.4]  n= 240,895  acc=0.993  █████████
-  [0.4–0.5]  n= 102,880  acc=0.984  ███
-  [0.5–0.6]  n=  48,470  acc=0.049  █
-  [0.6–0.7]  n=  40,459  acc=0.159  █
-  [0.7–0.8]  n=  40,755  acc=0.097  █
-  [0.8–0.9]  n=  46,221  acc=0.146  █
-  [0.9–1.0]  n=  36,800  acc=0.704  █

### Top 10 domen w błędach (Domena | Model | Prawda)
     976×  docs.google.com                     | Model: Legit (0)    | Prawda: Phishing (1)
      93×  flowcode.com                        | Model: Legit (0)    | Prawda: Phishing (1)
      58×  rp.mockplus.com                     | Model: Legit (0)    | Prawda: Phishing (1)
      53×  us6.campaign-archive.com            | Model: Legit (0)    | Prawda: Phishing (1)
      52×  us2.campaign-archive.com            | Model: Legit (0)    | Prawda: Phishing (1)
      45×  us4.campaign-archive.com            | Model: Legit (0)    | Prawda: Phishing (1)
      43×  us20.campaign-archive.com           | Model: Legit (0)    | Prawda: Phishing (1)
      43×  us15.campaign-archive.com           | Model: Legit (0)    | Prawda: Phishing (1)
      42×  us11.campaign-archive.com           | Model: Legit (0)    | Prawda: Phishing (1)
      41×  us10.campaign-archive.com           | Model: Legit (0)    | Prawda: Phishing (1)




## SET - 1
### Metryki
-  Precision : 0.9605   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.9139   (ile phishingów zostało wykrytych)
-  F1        : 0.9367
-  FPR       : 0.0106   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 1618 / 12047 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=282,101  F1=0.9079
-  [ 50–100 znaków]  n=136,470  F1=0.9762
-  [100–150 znaków]  n= 17,188  F1=0.9800
-  [150–200 znaków]  n=  3,694  F1=0.9834
-  [200–999 znaków]  n=  3,727  F1=0.9949

### Rozkład predykcji
-  [0.0–0.1]  n= 317,321  acc=0.996  ████████████████████████████
-  [0.1–0.2]  n=  16,208  acc=0.912  █
-  [0.2–0.3]  n=   7,553  acc=0.791  
-  [0.3–0.4]  n=   5,334  acc=0.644  
-  [0.4–0.5]  n=   4,044  acc=0.473  
-  [0.5–0.6]  n=   3,688  acc=0.680  
-  [0.6–0.7]  n=   4,479  acc=0.790  
-  [0.7–0.8]  n=   6,154  acc=0.884  
-  [0.8–0.9]  n=  11,202  acc=0.950  █
-  [0.9–1.0]  n=  67,221  acc=0.996  ██████

### Top 10 domen w błędach (Domena | Model | Prawda)
      50×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
      44×  twitter.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      37×  ckuik.com                           | Model: Phishing (1) | Prawda: Legit (0)
      33×  twitter.com                         | Model: Phishing (1) | Prawda: Legit (0)
      17×  httpss:                             | Model: Phishing (1) | Prawda: Legit (0)
      16×  naymz.com                           | Model: Phishing (1) | Prawda: Legit (0)
      15×  lazygirls.info                      | Model: Phishing (1) | Prawda: Legit (0)
      15×  angelfire.com                       | Model: Legit (0)    | Prawda: Phishing (1)
      12×  badoo.com                           | Model: Phishing (1) | Prawda: Legit (0)
      12×  fireangel.biz                       | Model: Phishing (1) | Prawda: Legit (0)


## SET - 2
### Metryki
-  Precision : 0.9727   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.8605   (ile phishingów zostało wykrytych)
-  F1        : 0.9132
-  FPR       : 0.0106   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 3264 / 24826 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=314,244  F1=0.8859
-  [ 50–100 znaków]  n=152,865  F1=0.9547
-  [100–150 znaków]  n= 18,789  F1=0.9454
-  [150–200 znaków]  n=  7,058  F1=0.9137
-  [200–999 znaków]  n=  4,461  F1=0.9885

### Rozkład predykcji
-  [0.0–0.1]  n= 318,968  acc=0.991  █████████████████████████
-  [0.1–0.2]  n=  18,305  acc=0.808  █
-  [0.2–0.3]  n=  10,070  acc=0.593  
-  [0.3–0.4]  n=   8,198  acc=0.419  
-  [0.4–0.5]  n=   7,698  acc=0.248  
-  [0.5–0.6]  n=   8,273  acc=0.857  
-  [0.6–0.7]  n=   9,374  acc=0.900  
-  [0.7–0.8]  n=  11,433  acc=0.937  
-  [0.8–0.9]  n=  19,991  acc=0.972  █
-  [0.9–1.0]  n=  85,153  acc=0.997  ██████

### Top 10 domen w błędach (Domena | Model | Prawda)
     820×  docs.google.com                     | Model: Legit (0)    | Prawda: Phishing (1)
     622×  cloudflare-ipfs.com                 | Model: Legit (0)    | Prawda: Phishing (1)
     324×  cf-ipfs.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      98×  flowcode.com                        | Model: Legit (0)    | Prawda: Phishing (1)
      58×  rp.mockplus.com                     | Model: Legit (0)    | Prawda: Phishing (1)
      50×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
      47×  ipfs.eth.aragon.network             | Model: Legit (0)    | Prawda: Phishing (1)
      44×  twitter.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      37×  ckuik.com                           | Model: Phishing (1) | Prawda: Legit (0)
      36×  cakeresume.com                      | Model: Legit (0)    | Prawda: Phishing (1)


## SET - 3
### Metryki
-  Precision : 0.9312   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.6801   (ile phishingów zostało wykrytych)
-  F1        : 0.7861
-  FPR       : 0.0433   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 12683 / 136235 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=570,056  F1=0.7298
-  [ 50–100 znaków]  n=182,694  F1=0.9402
-  [100–150 znaków]  n= 25,912  F1=0.9700
-  [150–200 znaków]  n=  6,871  F1=0.9763
-  [200–999 znaków]  n=  9,325  F1=0.9892

### Rozkład predykcji
-  [0.0–0.1]  n= 367,687  acc=0.975  ██████████████████
-  [0.1–0.2]  n=  44,170  acc=0.533  ██
-  [0.2–0.3]  n=  38,643  acc=0.361  █
-  [0.3–0.4]  n=  41,508  acc=0.174  ██
-  [0.4–0.5]  n=  34,092  acc=0.156  █
-  [0.5–0.6]  n=  23,139  acc=0.817  █
-  [0.6–0.7]  n=  21,512  acc=0.820  █
-  [0.7–0.8]  n=  29,703  acc=0.884  █
-  [0.8–0.9]  n=  37,755  acc=0.905  █
-  [0.9–1.0]  n= 156,737  acc=0.979  ███████

### Top 10 domen w błędach (Domena | Model | Prawda)
     955×  pastehtml.com                       | Model: Legit (0)    | Prawda: Phishing (1)
     207×  angelfire.com                       | Model: Phishing (1) | Prawda: Legit (0)
     173×  villakidsbuffetinfantil.com         | Model: Legit (0)    | Prawda: Phishing (1)
     165×  freewebs.com                        | Model: Phishing (1) | Prawda: Legit (0)
     123×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
     107×  ddj.com                             | Model: Phishing (1) | Prawda: Legit (0)
     104×  home.comcast.net                    | Model: Legit (0)    | Prawda: Phishing (1)
      72×  painterspaintings.com               | Model: Legit (0)    | Prawda: Phishing (1)
      51×  fibtex.lodz.pl                      | Model: Phishing (1) | Prawda: Legit (0)
      50×  home.earthlink.net                  | Model: Phishing (1) | Prawda: Legit (0)


## SET - 4
### Metryki
-  Precision : 0.2136   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.8126   (ile phishingów zostało wykrytych)
-  F1        : 0.3383
-  FPR       : 0.1673   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 13252 / 177751 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=1,040,321  F1=0.2729
-  [ 50–100 znaków]  n=  8,022  F1=0.8855
-  [100–150 znaków]  n=  1,852  F1=0.8923
-  [150–200 znaków]  n=  4,925  F1=0.9060
-  [200–999 znaków]  n=    770  F1=0.9401

### Rozkład predykcji
-  [0.0–0.1]  n=  50,103  acc=0.953  █
-  [0.1–0.2]  n= 179,676  acc=0.987  ██████
-  [0.2–0.3]  n= 269,657  acc=0.991  ██████████
-  [0.3–0.4]  n= 240,895  acc=0.993  █████████
-  [0.4–0.5]  n= 102,880  acc=0.984  ███
-  [0.5–0.6]  n=  48,470  acc=0.049  █
-  [0.6–0.7]  n=  40,459  acc=0.159  █
-  [0.7–0.8]  n=  40,755  acc=0.097  █
-  [0.8–0.9]  n=  46,221  acc=0.146  █
-  [0.9–1.0]  n=  36,800  acc=0.704  █

### Top 10 domen w błędach (Domena | Model | Prawda)
     976×  docs.google.com                     | Model: Legit (0)    | Prawda: Phishing (1)
      93×  flowcode.com                        | Model: Legit (0)    | Prawda: Phishing (1)
      58×  rp.mockplus.com                     | Model: Legit (0)    | Prawda: Phishing (1)
      53×  us6.campaign-archive.com            | Model: Legit (0)    | Prawda: Phishing (1)
      52×  us2.campaign-archive.com            | Model: Legit (0)    | Prawda: Phishing (1)
      45×  us4.campaign-archive.com            | Model: Legit (0)    | Prawda: Phishing (1)
      43×  us20.campaign-archive.com           | Model: Legit (0)    | Prawda: Phishing (1)
      43×  us15.campaign-archive.com           | Model: Legit (0)    | Prawda: Phishing (1)
      42×  us11.campaign-archive.com           | Model: Legit (0)    | Prawda: Phishing (1)
      41×  us10.campaign-archive.com           | Model: Legit (0)    | Prawda: Phishing (1)


# XGBoost (NLP-TfIDF)
## SET - 1
### Metryki
-  Precision : 0.9454   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.8761   (ile phishingów zostało wykrytych)
-  F1        : 0.9094
-  FPR       : 0.0143   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 1263 / 17006 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=282,101  F1=0.8663
-  [ 50–100 znaków]  n=136,470  F1=0.9682
-  [100–150 znaków]  n= 17,188  F1=0.9743
-  [150–200 znaków]  n=  3,694  F1=0.9813
-  [200–999 znaków]  n=  3,727  F1=0.9913

### Rozkład predykcji
-  [0.0–0.1]  n= 298,042  acc=0.996  ██████████████████████████
-  [0.1–0.2]  n=  29,875  acc=0.915  ██
-  [0.2–0.3]  n=  12,374  acc=0.776  █
-  [0.3–0.4]  n=   7,214  acc=0.613  
-  [0.4–0.5]  n=   5,374  acc=0.461  
-  [0.5–0.6]  n=   5,668  acc=0.666  
-  [0.6–0.7]  n=   5,809  acc=0.794  
-  [0.7–0.8]  n=  10,088  acc=0.880  
-  [0.8–0.9]  n=  10,485  acc=0.957  
-  [0.9–1.0]  n=  58,275  acc=0.997  █████

### Top 10 domen w błędach (Domena | Model | Prawda)
      91×  twitter.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      61×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
      24×  ckuik.com                           | Model: Phishing (1) | Prawda: Legit (0)
      21×  twitter.com                         | Model: Phishing (1) | Prawda: Legit (0)
      15×  angelfire.com                       | Model: Legit (0)    | Prawda: Phishing (1)
      15×  jmetalloysllp.com                   | Model: Legit (0)    | Prawda: Phishing (1)
      14×  gulsproductions.com                 | Model: Legit (0)    | Prawda: Phishing (1)
      14×  kitsgnt.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      14×  innogenap.com                       | Model: Legit (0)    | Prawda: Phishing (1)
      13×  arvindudyog.com                     | Model: Legit (0)    | Prawda: Phishing (1)


## SET - 2
### Metryki
-  Precision : 0.9622   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.8270   (ile phishingów zostało wykrytych)
-  F1        : 0.8895
-  FPR       : 0.0143   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 2478 / 31175 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=314,244  F1=0.8615
-  [ 50–100 znaków]  n=152,865  F1=0.9169
-  [100–150 znaków]  n= 18,789  F1=0.9280
-  [150–200 znaków]  n=  7,058  F1=0.9893
-  [200–999 znaków]  n=  4,461  F1=0.9835

### Rozkład predykcji
-  [0.0–0.1]  n= 299,257  acc=0.992  ████████████████████████
-  [0.1–0.2]  n=  33,127  acc=0.825  ██
-  [0.2–0.3]  n=  14,998  acc=0.640  █
-  [0.3–0.4]  n=  11,917  acc=0.371  
-  [0.4–0.5]  n=   7,749  acc=0.320  
-  [0.5–0.6]  n=  10,694  acc=0.823  
-  [0.6–0.7]  n=  10,598  acc=0.887  
-  [0.7–0.8]  n=  21,292  acc=0.943  █
-  [0.8–0.9]  n=  17,317  acc=0.974  █
-  [0.9–1.0]  n=  70,514  acc=0.997  █████

### Top 10 domen w błędach (Domena | Model | Prawda)
     732×  cloudflare-ipfs.com                 | Model: Legit (0)    | Prawda: Phishing (1)
     520×  cf-ipfs.com                         | Model: Legit (0)    | Prawda: Phishing (1)
     243×  ipfs.eth.aragon.network             | Model: Legit (0)    | Prawda: Phishing (1)
      93×  flowcode.com                        | Model: Legit (0)    | Prawda: Phishing (1)
      91×  twitter.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      61×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
      57×  rp.mockplus.com                     | Model: Legit (0)    | Prawda: Phishing (1)
      38×  tinyurl.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      36×  cakeresume.com                      | Model: Legit (0)    | Prawda: Phishing (1)
      24×  ckuik.com                           | Model: Phishing (1) | Prawda: Legit (0)


## SET - 3
### Metryki
-  Precision : 0.9438   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.7646   (ile phishingów zostało wykrytych)
-  F1        : 0.8448
-  FPR       : 0.0393   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 7203 / 103428 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=570,056  F1=0.8145
-  [ 50–100 znaków]  n=182,694  F1=0.9258
-  [100–150 znaków]  n= 25,912  F1=0.9618
-  [150–200 znaków]  n=  6,871  F1=0.9718
-  [200–999 znaków]  n=  9,325  F1=0.9847

### Rozkład predykcji
-  [0.0–0.1]  n= 344,876  acc=0.985  █████████████████
-  [0.1–0.2]  n=  55,220  acc=0.749  ██
-  [0.2–0.3]  n=  39,181  acc=0.392  █
-  [0.3–0.4]  n=  31,912  acc=0.251  █
-  [0.4–0.5]  n=  25,570  acc=0.219  █
-  [0.5–0.6]  n=  26,425  acc=0.824  █
-  [0.6–0.7]  n=  29,642  acc=0.877  █
-  [0.7–0.8]  n=  68,139  acc=0.944  ███
-  [0.8–0.9]  n=  43,652  acc=0.941  ██
-  [0.9–1.0]  n= 130,329  acc=0.984  ██████

### Top 10 domen w błędach (Domena | Model | Prawda)
     942×  pastehtml.com                       | Model: Legit (0)    | Prawda: Phishing (1)
     173×  villakidsbuffetinfantil.com         | Model: Legit (0)    | Prawda: Phishing (1)
     136×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
     128×  home.comcast.net                    | Model: Legit (0)    | Prawda: Phishing (1)
     124×  freewebs.com                        | Model: Phishing (1) | Prawda: Legit (0)
     112×  angelfire.com                       | Model: Phishing (1) | Prawda: Legit (0)
      85×  webring.com                         | Model: Phishing (1) | Prawda: Legit (0)
      81×  twitter.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      79×  affiliatealmanac.com                | Model: Legit (0)    | Prawda: Phishing (1)
      77×  ddj.com                             | Model: Phishing (1) | Prawda: Legit (0)


## SET - 4
### Metryki
-  Precision : 0.0770   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.8360   (ile phishingów zostało wykrytych)
-  F1        : 0.1411
-  FPR       : 0.5600   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 22736 / 569169 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=1,040,321  F1=0.1050
-  [ 50–100 znaków]  n=  8,022  F1=0.8815
-  [100–150 znaków]  n=  1,852  F1=0.9261
-  [150–200 znaków]  n=  4,925  F1=0.9976
-  [200–999 znaków]  n=    770  F1=0.9246

### Rozkład predykcji
-  [0.0–0.1]  n=  10,791  acc=0.830  
-  [0.1–0.2]  n=  46,181  acc=0.936  █
-  [0.2–0.3]  n=  97,686  acc=0.981  ███
-  [0.3–0.4]  n= 183,067  acc=0.993  ██████
-  [0.4–0.5]  n= 111,442  acc=0.989  ████
-  [0.5–0.6]  n= 139,583  acc=0.016  █████
-  [0.6–0.7]  n= 100,309  acc=0.040  ███
-  [0.7–0.8]  n= 223,286  acc=0.077  ████████
-  [0.8–0.9]  n= 107,395  acc=0.075  ████
-  [0.9–1.0]  n=  36,176  acc=0.422  █

### Top 10 domen w błędach (Domena | Model | Prawda)
      89×  flowcode.com                        | Model: Legit (0)    | Prawda: Phishing (1)
      57×  rp.mockplus.com                     | Model: Legit (0)    | Prawda: Phishing (1)
      53×  us6.campaign-archive.com            | Model: Legit (0)    | Prawda: Phishing (1)
      52×  us2.campaign-archive.com            | Model: Legit (0)    | Prawda: Phishing (1)
      45×  us4.campaign-archive.com            | Model: Legit (0)    | Prawda: Phishing (1)
      43×  us20.campaign-archive.com           | Model: Legit (0)    | Prawda: Phishing (1)
      43×  us15.campaign-archive.com           | Model: Legit (0)    | Prawda: Phishing (1)
      42×  us11.campaign-archive.com           | Model: Legit (0)    | Prawda: Phishing (1)
      41×  us10.campaign-archive.com           | Model: Legit (0)    | Prawda: Phishing (1)
      41×  us9.campaign-archive.com            | Model: Legit (0)    | Prawda: Phishing (1)

