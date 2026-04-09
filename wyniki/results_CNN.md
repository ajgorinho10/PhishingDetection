# CNN (NLP + Cechy)
## set - 4
### Metryki
-  Precision : 0.1649   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.8737   (ile phishingów zostało wykrytych)
-  F1        : 0.2774
-  FPR       : 0.2474   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 85683 / 254470 błędów ogółem

### F1 według długości URL
-  [  0– 50 znaków]  n=1,040,321  F1=0.2155
-  [ 50–100 znaków]  n=  8,022  F1=0.9069
-  [100–150 znaków]  n=  1,852  F1=0.9740
-  [150–200 znaków]  n=  4,925  F1=0.9995
-  [200–999 znaków]  n=    770  F1=0.9855

### Rozkład predykcji
-  [0.0–0.1]  n= 332,469  acc=0.991  ████████████
-  [0.1–0.2]  n= 187,179  acc=0.993  ███████
-  [0.2–0.3]  n= 111,453  acc=0.991  ████
-  [0.3–0.4]  n=  73,672  acc=0.989  ██
-  [0.4–0.5]  n=  54,877  acc=0.984  ██
-  [0.5–0.6]  n=  48,330  acc=0.020  █
-  [0.6–0.7]  n=  41,602  acc=0.029  █
-  [0.7–0.8]  n=  39,662  acc=0.040  █
-  [0.8–0.9]  n=  41,532  acc=0.064  █
-  [0.9–1.0]  n= 125,140  acc=0.339  ████

### Top 10 domen w błędach (Domena | Model | Prawda)
      81×  flowcode.com                        | Model: Legit (0)    | Prawda: Phishing (1)
      54×  us2.campaign-archive.com            | Model: Legit (0)    | Prawda: Phishing (1)
      53×  us6.campaign-archive.com            | Model: Legit (0)    | Prawda: Phishing (1)
      45×  us4.campaign-archive.com            | Model: Legit (0)    | Prawda: Phishing (1)
      43×  us20.campaign-archive.com           | Model: Legit (0)    | Prawda: Phishing (1)
      43×  us9.campaign-archive.com            | Model: Legit (0)    | Prawda: Phishing (1)
      42×  us11.campaign-archive.com           | Model: Legit (0)    | Prawda: Phishing (1)
      42×  us15.campaign-archive.com           | Model: Legit (0)    | Prawda: Phishing (1)
      41×  us10.campaign-archive.com           | Model: Legit (0)    | Prawda: Phishing (1)
      41×  linkin.bio                          | Model: Legit (0)    | Prawda: Phishing (1)
## set - 1
### Metryki
-  Precision : 0.9833   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.9564   (ile phishingów zostało wykrytych)
-  F1        : 0.9697
-  FPR       : 0.0046   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 1699 / 5829 błędów ogółem

### F1 według długości URL
-  [  0– 50 znaków]  n=282,101  F1=0.9551
-  [ 50–100 znaków]  n=136,470  F1=0.9893
-  [100–150 znaków]  n= 17,188  F1=0.9935
-  [150–200 znaków]  n=  3,694  F1=0.9969
-  [200–999 znaków]  n=  3,727  F1=0.9978

### Rozkład predykcji
-  [0.0–0.1]  n= 336,897  acc=0.996  ██████████████████████████████
-  [0.1–0.2]  n=   6,086  acc=0.866  
-  [0.2–0.3]  n=   2,580  acc=0.738  
-  [0.3–0.4]  n=   1,564  acc=0.582  
-  [0.4–0.5]  n=   1,267  acc=0.474  
-  [0.5–0.6]  n=   1,365  acc=0.646  
-  [0.6–0.7]  n=   1,559  acc=0.775  
-  [0.7–0.8]  n=   2,041  acc=0.872  
-  [0.8–0.9]  n=   3,367  acc=0.933  
-  [0.9–1.0]  n=  86,478  acc=0.997  ███████

### Top 10 domen w błędach (Domena | Model | Prawda)
      39×  twitter.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      32×  facebook.com                        | Model: Phishing (1) | Prawda: Legit (0)
      27×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
      16×  angelfire.com                       | Model: Legit (0)    | Prawda: Phishing (1)
       7×  twitter.com                         | Model: Phishing (1) | Prawda: Legit (0)
       7×  newmanamechurch.org                 | Model: Legit (0)    | Prawda: Phishing (1)
       7×  plus.google.com                     | Model: Legit (0)    | Prawda: Phishing (1)
       6×  borcuodeme.com                      | Model: Legit (0)    | Prawda: Phishing (1)
       6×  home.earthlink.net                  | Model: Legit (0)    | Prawda: Phishing (1)
       5×  pastebin.com                        | Model: Phishing (1) | Prawda: Legit (0)


## set - 2
### Metryki
-  Precision : 0.9887   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.9098   (ile phishingów zostało wykrytych)
-  F1        : 0.9476
-  FPR       : 0.0046   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 5444 / 15266 błędów ogółem

### F1 według długości URL
-  [  0– 50 znaków]  n=314,244  F1=0.9196
-  [ 50–100 znaków]  n=152,865  F1=0.9836
-  [100–150 znaków]  n= 18,789  F1=0.9924
-  [150–200 znaków]  n=  7,058  F1=0.9981
-  [200–999 znaków]  n=  4,461  F1=0.9963

### Rozkład predykcji
-  [0.0–0.1]  n= 340,641  acc=0.985  ███████████████████████████
-  [0.1–0.2]  n=   8,078  acc=0.653  
-  [0.2–0.3]  n=   3,997  acc=0.477  
-  [0.3–0.4]  n=   2,701  acc=0.337  
-  [0.4–0.5]  n=   2,412  acc=0.249  
-  [0.5–0.6]  n=   2,577  acc=0.813  
-  [0.6–0.7]  n=   2,923  acc=0.880  
-  [0.7–0.8]  n=   3,775  acc=0.931  
-  [0.8–0.9]  n=   6,005  acc=0.962  
-  [0.9–1.0]  n= 124,354  acc=0.998  █████████

### Top 10 domen w błędach (Domena | Model | Prawda)
      84×  flowcode.com                        | Model: Legit (0)    | Prawda: Phishing (1)
      39×  twitter.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      32×  facebook.com                        | Model: Phishing (1) | Prawda: Legit (0)
      30×  cakeresume.com                      | Model: Legit (0)    | Prawda: Phishing (1)
      27×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
      23×  sites.google.com                    | Model: Legit (0)    | Prawda: Phishing (1)
      18×  cf-ipfs.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      16×  jemi.so                             | Model: Legit (0)    | Prawda: Phishing (1)
      16×  angelfire.com                       | Model: Legit (0)    | Prawda: Phishing (1)
      15×  klrn.wpenginepowered.com            | Model: Legit (0)    | Prawda: Phishing (1)
## set - 3
### Metryki
-  Precision : 0.9559   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.7988   (ile phishingów zostało wykrytych)
-  F1        : 0.8704
-  FPR       : 0.0318   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 29958 / 87598 błędów ogółem

### F1 według długości URL
-  [  0– 50 znaków]  n=570,056  F1=0.8402
-  [ 50–100 znaków]  n=182,694  F1=0.9537
-  [100–150 znaków]  n= 25,912  F1=0.9791
-  [150–200 znaków]  n=  6,871  F1=0.9869
-  [200–999 znaków]  n=  9,325  F1=0.9946

### Rozkład predykcji
-  [0.0–0.1]  n= 418,019  acc=0.942  █████████████████████
-  [0.1–0.2]  n=  27,847  acc=0.359  █
-  [0.2–0.3]  n=  17,122  acc=0.262  
-  [0.3–0.4]  n=  12,948  acc=0.215  
-  [0.4–0.5]  n=  11,417  acc=0.195  
-  [0.5–0.6]  n=  11,916  acc=0.833  
-  [0.6–0.7]  n=  12,993  acc=0.855  
-  [0.7–0.8]  n=  15,384  acc=0.881  
-  [0.8–0.9]  n=  23,253  acc=0.910  █
-  [0.9–1.0]  n= 244,047  acc=0.976  ████████████

### Top 10 domen w błędach (Domena | Model | Prawda)
     271×  babinet.cz                          | Model: Legit (0)    | Prawda: Phishing (1)
     142×  home.comcast.net                    | Model: Legit (0)    | Prawda: Phishing (1)
     141×  pastehtml.com                       | Model: Legit (0)    | Prawda: Phishing (1)
      97×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
      78×  angelfire.com                       | Model: Phishing (1) | Prawda: Legit (0)
      68×  tools.ietf.org                      | Model: Phishing (1) | Prawda: Legit (0)
      60×  storage.googleapis.com              | Model: Legit (0)    | Prawda: Phishing (1)
      59×  "http:                              | Model: Phishing (1) | Prawda: Legit (0)
      51×  fibtex.lodz.pl                      | Model: Phishing (1) | Prawda: Legit (0)
      46×  globetrotter-games.com              | Model: Phishing (1) | Prawda: Legit (0)

# CNN (NLP)
## SET - 1
### Metryki
-  Precision : 0.9805   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.9546   (ile phishingów zostało wykrytych)
-  F1        : 0.9674
-  FPR       : 0.0053   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 2010 / 6278 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=282,101  F1=0.9515
-  [ 50–100 znaków]  n=136,470  F1=0.9885
-  [100–150 znaków]  n= 17,188  F1=0.9946
-  [150–200 znaków]  n=  3,694  F1=0.9961
-  [200–999 znaków]  n=  3,727  F1=0.9970

### Rozkład predykcji
-  [0.0–0.1]  n= 336,437  acc=0.995  ██████████████████████████████
-  [0.1–0.2]  n=   6,553  acc=0.853  
-  [0.2–0.3]  n=   2,616  acc=0.730  
-  [0.3–0.4]  n=   1,544  acc=0.627  
-  [0.4–0.5]  n=   1,163  acc=0.516  
-  [0.5–0.6]  n=   1,264  acc=0.631  
-  [0.6–0.7]  n=   1,342  acc=0.720  
-  [0.7–0.8]  n=   1,577  acc=0.821  
-  [0.8–0.9]  n=   2,647  acc=0.875  
-  [0.9–1.0]  n=  88,061  acc=0.996  ███████

### Top 10 domen w błędach (Domena | Model | Prawda)
      40×  twitter.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      24×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
      18×  facebook.com                        | Model: Phishing (1) | Prawda: Legit (0)
      18×  angelfire.com                       | Model: Legit (0)    | Prawda: Phishing (1)
      13×  plus.google.com                     | Model: Legit (0)    | Prawda: Phishing (1)
       9×  twitter.com                         | Model: Phishing (1) | Prawda: Legit (0)
       9×  callmr.com                          | Model: Legit (0)    | Prawda: Phishing (1)
       9×  sites.google.com                    | Model: Legit (0)    | Prawda: Phishing (1)
       6×  ow.ly                               | Model: Phishing (1) | Prawda: Legit (0)
       5×  q.gs                                | Model: Phishing (1) | Prawda: Legit (0)


## SET - 2
### Metryki
-  Precision : 0.9865   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.8872   (ile phishingów zostało wykrytych)
-  F1        : 0.9342
-  FPR       : 0.0053   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 8972 / 18970 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=314,244  F1=0.8962
-  [ 50–100 znaków]  n=152,865  F1=0.9827
-  [100–150 znaków]  n= 18,789  F1=0.9940
-  [150–200 znaków]  n=  7,058  F1=0.9967
-  [200–999 znaków]  n=  4,461  F1=0.9973

### Rozkład predykcji
-  [0.0–0.1]  n= 343,398  acc=0.975  ███████████████████████████
-  [0.1–0.2]  n=   9,276  acc=0.602  
-  [0.2–0.3]  n=   3,966  acc=0.481  
-  [0.3–0.4]  n=   2,453  acc=0.395  
-  [0.4–0.5]  n=   1,910  acc=0.314  
-  [0.5–0.6]  n=   2,037  acc=0.771  
-  [0.6–0.7]  n=   2,236  acc=0.832  
-  [0.7–0.8]  n=   2,673  acc=0.895  
-  [0.8–0.9]  n=   4,371  acc=0.924  
-  [0.9–1.0]  n= 125,143  acc=0.997  ██████████

### Top 10 domen w błędach (Domena | Model | Prawda)
      96×  flowcode.com                        | Model: Legit (0)    | Prawda: Phishing (1)
      52×  sites.google.com                    | Model: Legit (0)    | Prawda: Phishing (1)
      40×  twitter.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      27×  jemi.so                             | Model: Legit (0)    | Prawda: Phishing (1)
      24×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
      23×  flow.page                           | Model: Legit (0)    | Prawda: Phishing (1)
      19×  docs.google.com                     | Model: Legit (0)    | Prawda: Phishing (1)
      18×  facebook.com                        | Model: Phishing (1) | Prawda: Legit (0)
      18×  angelfire.com                       | Model: Legit (0)    | Prawda: Phishing (1)
      17×  tinyurl.com                         | Model: Legit (0)    | Prawda: Phishing (1)


## SET - 3
### Metryki
-  Precision : 0.9553   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.7898   (ile phishingów zostało wykrytych)
-  F1        : 0.8647
-  FPR       : 0.0318   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 30769 / 90972 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=570,056  F1=0.8317
-  [ 50–100 znaków]  n=182,694  F1=0.9560
-  [100–150 znaków]  n= 25,912  F1=0.9818
-  [150–200 znaków]  n=  6,871  F1=0.9893
-  [200–999 znaków]  n=  9,325  F1=0.9946

### Rozkład predykcji
-  [0.0–0.1]  n= 417,897  acc=0.941  █████████████████████
-  [0.1–0.2]  n=  30,261  acc=0.355  █
-  [0.2–0.3]  n=  18,655  acc=0.245  
-  [0.3–0.4]  n=  13,230  acc=0.211  
-  [0.4–0.5]  n=  10,614  acc=0.186  
-  [0.5–0.6]  n=  11,417  acc=0.829  
-  [0.6–0.7]  n=  11,976  acc=0.851  
-  [0.7–0.8]  n=  13,606  acc=0.872  
-  [0.8–0.9]  n=  20,320  acc=0.900  █
-  [0.9–1.0]  n= 246,970  acc=0.975  ████████████

### Top 10 domen w błędach (Domena | Model | Prawda)
     286×  pastehtml.com                       | Model: Legit (0)    | Prawda: Phishing (1)
     133×  home.comcast.net                    | Model: Legit (0)    | Prawda: Phishing (1)
      86×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
      73×  storage.googleapis.com              | Model: Legit (0)    | Prawda: Phishing (1)
      67×  painterspaintings.com               | Model: Legit (0)    | Prawda: Phishing (1)
      66×  globetrotter-games.com              | Model: Phishing (1) | Prawda: Legit (0)
      60×  ddj.com                             | Model: Phishing (1) | Prawda: Legit (0)
      52×  babinet.cz                          | Model: Legit (0)    | Prawda: Phishing (1)
      51×  fibtex.lodz.pl                      | Model: Phishing (1) | Prawda: Legit (0)
      46×  microsoft.com                       | Model: Phishing (1) | Prawda: Legit (0)


## SET - 4
### Metryki
-  Precision : 0.1529   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.8525   (ile phishingów zostało wykrytych)
-  F1        : 0.2593
-  FPR       : 0.2641   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 99529 / 272302 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=1,040,321  F1=0.1981
-  [ 50–100 znaków]  n=  8,022  F1=0.9138
-  [100–150 znaków]  n=  1,852  F1=0.9788
-  [150–200 znaków]  n=  4,925  F1=0.9979
-  [200–999 znaków]  n=    770  F1=0.9921

### Rozkład predykcji
-  [0.0–0.1]  n= 287,322  acc=0.987  ██████████
-  [0.1–0.2]  n= 200,290  acc=0.991  ███████
-  [0.2–0.3]  n= 127,017  acc=0.992  ████
-  [0.3–0.4]  n=  77,538  acc=0.990  ██
-  [0.4–0.5]  n=  52,023  acc=0.986  █
-  [0.5–0.6]  n=  46,418  acc=0.018  █
-  [0.6–0.7]  n=  41,355  acc=0.023  █
-  [0.7–0.8]  n=  39,870  acc=0.029  █
-  [0.8–0.9]  n=  45,631  acc=0.043  █
-  [0.9–1.0]  n= 138,452  acc=0.309  █████

### Top 10 domen w błędach (Domena | Model | Prawda)
     109×  docs.google.com                     | Model: Legit (0)    | Prawda: Phishing (1)
      92×  flowcode.com                        | Model: Legit (0)    | Prawda: Phishing (1)
      84×  linkin.bio                          | Model: Legit (0)    | Prawda: Phishing (1)
      60×  sites.google.com                    | Model: Legit (0)    | Prawda: Phishing (1)
      58×  linqapp.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      52×  us2.campaign-archive.com            | Model: Legit (0)    | Prawda: Phishing (1)
      51×  us6.campaign-archive.com            | Model: Legit (0)    | Prawda: Phishing (1)
      44×  us4.campaign-archive.com            | Model: Legit (0)    | Prawda: Phishing (1)
      42×  us20.campaign-archive.com           | Model: Legit (0)    | Prawda: Phishing (1)
      42×  us9.campaign-archive.com            | Model: Legit (0)    | Prawda: Phishing (1)

