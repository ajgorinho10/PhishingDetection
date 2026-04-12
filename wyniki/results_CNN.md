# CNN (NLP + Cechy)
## SET - 1
### Metryki
-  Precision : 0.9277   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.9404   (ile phishingów zostało wykrytych)
-  F1        : 0.9340
-  FPR       : 0.0207   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 125 / 12955 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=282,101  F1=0.9072
-  [ 50–100 znaków]  n=136,470  F1=0.9678
-  [100–150 znaków]  n= 17,188  F1=0.9835
-  [150–200 znaków]  n=  3,694  F1=0.9910
-  [200–999 znaków]  n=  3,727  F1=0.9939

### Rozkład predykcji
-  [0.0–0.1]  n= 156,919  acc=1.000  ██████████████
-  [0.1–0.2]  n=  98,994  acc=0.994  ████████
-  [0.2–0.3]  n=  56,717  acc=0.975  █████
-  [0.3–0.4]  n=  21,731  acc=0.922  █
-  [0.4–0.5]  n=  10,037  acc=0.794  
-  [0.5–0.6]  n=   7,474  acc=0.447  
-  [0.6–0.7]  n=   7,184  acc=0.738  
-  [0.7–0.8]  n=  10,362  acc=0.922  
-  [0.8–0.9]  n=  20,627  acc=0.987  █
-  [0.9–1.0]  n=  53,159  acc=0.999  ████

### Top 10 domen w błędach (Domena | Model | Prawda)
      75×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
      45×  twitter.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      32×  angelfire.com                       | Model: Phishing (1) | Prawda: Legit (0)
      29×  interment.net                       | Model: Phishing (1) | Prawda: Legit (0)
      28×  encycl.opentopia.com                | Model: Phishing (1) | Prawda: Legit (0)
      23×  twitter.com                         | Model: Phishing (1) | Prawda: Legit (0)
      22×  associatepublisher.com              | Model: Phishing (1) | Prawda: Legit (0)
      17×  support.microsoft.com               | Model: Phishing (1) | Prawda: Legit (0)
      15×  worldpostjournal.com                | Model: Legit (0)    | Prawda: Phishing (1)
      15×  meetwomen.com                       | Model: Legit (0)    | Prawda: Phishing (1)


## SET - 2
### Metryki
-  Precision : 0.9521   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.9363   (ile phishingów zostało wykrytych)
-  F1        : 0.9442
-  FPR       : 0.0207   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 246 / 16805 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=314,244  F1=0.9181
-  [ 50–100 znaków]  n=152,865  F1=0.9781
-  [100–150 znaków]  n= 18,789  F1=0.9865
-  [150–200 znaków]  n=  7,058  F1=0.9960
-  [200–999 znaków]  n=  4,461  F1=0.9946

### Rozkład predykcji
-  [0.0–0.1]  n= 157,041  acc=0.999  ████████████
-  [0.1–0.2]  n=  99,624  acc=0.988  ████████
-  [0.2–0.3]  n=  57,681  acc=0.959  ████
-  [0.3–0.4]  n=  22,866  acc=0.876  █
-  [0.4–0.5]  n=  11,038  acc=0.722  
-  [0.5–0.6]  n=   8,761  acc=0.528  
-  [0.6–0.7]  n=   9,462  acc=0.801  
-  [0.7–0.8]  n=  14,689  acc=0.945  █
-  [0.8–0.9]  n=  33,934  acc=0.992  ██
-  [0.9–1.0]  n=  82,367  acc=0.999  ██████

### Top 10 domen w błędach (Domena | Model | Prawda)
      75×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
      45×  twitter.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      32×  angelfire.com                       | Model: Phishing (1) | Prawda: Legit (0)
      29×  interment.net                       | Model: Phishing (1) | Prawda: Legit (0)
      28×  encycl.opentopia.com                | Model: Phishing (1) | Prawda: Legit (0)
      23×  twitter.com                         | Model: Phishing (1) | Prawda: Legit (0)
      22×  associatepublisher.com              | Model: Phishing (1) | Prawda: Legit (0)
      17×  support.microsoft.com               | Model: Phishing (1) | Prawda: Legit (0)
      15×  meetwomen.com                       | Model: Legit (0)    | Prawda: Phishing (1)
      15×  worldpostjournal.com                | Model: Legit (0)    | Prawda: Phishing (1)


## SET - 3
### Metryki
-  Precision : 0.9088   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.7017   (ile phishingów zostało wykrytych)
-  F1        : 0.7919
-  FPR       : 0.0608   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 7076 / 135744 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=570,056  F1=0.7342
-  [ 50–100 znaków]  n=182,694  F1=0.9482
-  [100–150 znaków]  n= 25,912  F1=0.9764
-  [150–200 znaków]  n=  6,871  F1=0.9872
-  [200–999 znaków]  n=  9,325  F1=0.9936

### Rozkład predykcji
-  [0.0–0.1]  n= 176,113  acc=0.964  ████████
-  [0.1–0.2]  n= 145,885  acc=0.778  ███████
-  [0.2–0.3]  n=  98,160  acc=0.704  ████
-  [0.3–0.4]  n=  54,331  acc=0.595  ██
-  [0.4–0.5]  n=  36,248  acc=0.444  █
-  [0.5–0.6]  n=  33,683  acc=0.675  █
-  [0.6–0.7]  n=  34,257  acc=0.792  █
-  [0.7–0.8]  n=  41,074  acc=0.888  ██
-  [0.8–0.9]  n=  65,948  acc=0.963  ███
-  [0.9–1.0]  n= 109,247  acc=0.993  █████

### Top 10 domen w błędach (Domena | Model | Prawda)
     672×  angelfire.com                       | Model: Phishing (1) | Prawda: Legit (0)
     304×  pastehtml.com                       | Model: Legit (0)    | Prawda: Phishing (1)
     156×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
     126×  sourceforge.net                     | Model: Phishing (1) | Prawda: Legit (0)
     117×  support.microsoft.com               | Model: Phishing (1) | Prawda: Legit (0)
      85×  home.comcast.net                    | Model: Legit (0)    | Prawda: Phishing (1)
      66×  members.tripod.com                  | Model: Phishing (1) | Prawda: Legit (0)
      57×  w3.org                              | Model: Phishing (1) | Prawda: Legit (0)
      51×  code.google.com                     | Model: Phishing (1) | Prawda: Legit (0)
      50×  fibtex.lodz.pl                      | Model: Phishing (1) | Prawda: Legit (0)


## SET - 4
### Metryki
-  Precision : 0.9523   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.9504   (ile phishingów zostało wykrytych)
-  F1        : 0.9513
-  FPR       : 0.0165   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 134 / 14934 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=420,725  F1=0.9351
-  [ 50–100 znaków]  n=144,404  F1=0.9740
-  [100–150 znaków]  n= 19,044  F1=0.9872
-  [150–200 znaków]  n=  8,626  F1=0.9969
-  [200–999 znaków]  n=  4,487  F1=0.9950

### Rozkład predykcji
-  [0.0–0.1]  n= 181,368  acc=1.000  ████████████
-  [0.1–0.2]  n= 154,232  acc=0.995  ██████████
-  [0.2–0.3]  n=  72,740  acc=0.974  ████
-  [0.3–0.4]  n=  24,627  acc=0.907  █
-  [0.4–0.5]  n=  11,092  acc=0.762  
-  [0.5–0.6]  n=   8,437  acc=0.496  
-  [0.6–0.7]  n=   8,713  acc=0.780  
-  [0.7–0.8]  n=  14,160  acc=0.942  
-  [0.8–0.9]  n=  31,432  acc=0.991  ██
-  [0.9–1.0]  n=  90,534  acc=0.999  ██████

### Top 10 domen w błędach (Domena | Model | Prawda)
      75×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
      45×  twitter.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      32×  angelfire.com                       | Model: Phishing (1) | Prawda: Legit (0)
      29×  interment.net                       | Model: Phishing (1) | Prawda: Legit (0)
      28×  encycl.opentopia.com                | Model: Phishing (1) | Prawda: Legit (0)
      23×  twitter.com                         | Model: Phishing (1) | Prawda: Legit (0)
      22×  associatepublisher.com              | Model: Phishing (1) | Prawda: Legit (0)
      17×  support.microsoft.com               | Model: Phishing (1) | Prawda: Legit (0)
      15×  meetwomen.com                       | Model: Legit (0)    | Prawda: Phishing (1)
      15×  worldpostjournal.com                | Model: Legit (0)    | Prawda: Phishing (1)


# CNN (NLP):
## SET - 1
### Metryki
-  Precision : 0.9340   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.9537   (ile phishingów zostało wykrytych)
-  F1        : 0.9437
-  FPR       : 0.0190   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 119 / 11082 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=282,101  F1=0.9193
-  [ 50–100 znaków]  n=136,470  F1=0.9765
-  [100–150 znaków]  n= 17,188  F1=0.9873
-  [150–200 znaków]  n=  3,694  F1=0.9924
-  [200–999 znaków]  n=  3,727  F1=0.9946

### Rozkład predykcji
-  [0.0–0.1]  n= 205,001  acc=1.000  ██████████████████
-  [0.1–0.2]  n=  72,003  acc=0.993  ██████
-  [0.2–0.3]  n=  40,716  acc=0.973  ███
-  [0.3–0.4]  n=  18,472  acc=0.923  █
-  [0.4–0.5]  n=   7,475  acc=0.813  
-  [0.5–0.6]  n=   5,161  acc=0.378  
-  [0.6–0.7]  n=   5,948  acc=0.646  
-  [0.7–0.8]  n=   8,474  acc=0.889  
-  [0.8–0.9]  n=  16,281  acc=0.984  █
-  [0.9–1.0]  n=  63,673  acc=0.999  █████

### Top 10 domen w błędach (Domena | Model | Prawda)
      72×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
      44×  twitter.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      23×  twitter.com                         | Model: Phishing (1) | Prawda: Legit (0)
      22×  google.com                          | Model: Phishing (1) | Prawda: Legit (0)
      17×  facebook.com                        | Model: Phishing (1) | Prawda: Legit (0)
      16×  loot.co.za                          | Model: Phishing (1) | Prawda: Legit (0)
      14×  httpss:                             | Model: Phishing (1) | Prawda: Legit (0)
      13×  4shared.com                         | Model: Phishing (1) | Prawda: Legit (0)
      13×  plus.google.com                     | Model: Phishing (1) | Prawda: Legit (0)
      12×  trade.mar.cx                        | Model: Phishing (1) | Prawda: Legit (0)


## SET - 2
### Metryki
-  Precision : 0.9563   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.9478   (ile phishingów zostało wykrytych)
-  F1        : 0.9520
-  FPR       : 0.0190   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 238 / 14490 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=314,244  F1=0.9288
-  [ 50–100 znaków]  n=152,865  F1=0.9833
-  [100–150 znaków]  n= 18,789  F1=0.9889
-  [150–200 znaków]  n=  7,058  F1=0.9969
-  [200–999 znaków]  n=  4,461  F1=0.9954

### Rozkład predykcji
-  [0.0–0.1]  n= 205,120  acc=0.999  ████████████████
-  [0.1–0.2]  n=  72,618  acc=0.984  █████
-  [0.2–0.3]  n=  41,609  acc=0.952  ███
-  [0.3–0.4]  n=  19,446  acc=0.876  █
-  [0.4–0.5]  n=   8,284  acc=0.733  
-  [0.5–0.6]  n=   6,111  acc=0.475  
-  [0.6–0.7]  n=   7,538  acc=0.721  
-  [0.7–0.8]  n=  11,703  acc=0.920  
-  [0.8–0.9]  n=  29,266  acc=0.991  ██
-  [0.9–1.0]  n=  95,768  acc=0.999  ███████

### Top 10 domen w błędach (Domena | Model | Prawda)
      72×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
      44×  twitter.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      23×  twitter.com                         | Model: Phishing (1) | Prawda: Legit (0)
      21×  google.com                          | Model: Phishing (1) | Prawda: Legit (0)
      19×  jemi.so                             | Model: Legit (0)    | Prawda: Phishing (1)
      17×  facebook.com                        | Model: Phishing (1) | Prawda: Legit (0)
      16×  loot.co.za                          | Model: Phishing (1) | Prawda: Legit (0)
      14×  httpss:                             | Model: Phishing (1) | Prawda: Legit (0)
      13×  plus.google.com                     | Model: Phishing (1) | Prawda: Legit (0)
      13×  flipsnack.com                       | Model: Legit (0)    | Prawda: Phishing (1)


## SET - 3
### Metryki
-  Precision : 0.9139   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.7317   (ile phishingów zostało wykrytych)
-  F1        : 0.8127
-  FPR       : 0.0595   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 7746 / 124135 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=570,056  F1=0.7626
-  [ 50–100 znaków]  n=182,694  F1=0.9512
-  [100–150 znaków]  n= 25,912  F1=0.9806
-  [150–200 znaków]  n=  6,871  F1=0.9880
-  [200–999 znaków]  n=  9,325  F1=0.9944

### Rozkład predykcji
-  [0.0–0.1]  n= 230,449  acc=0.972  ███████████
-  [0.1–0.2]  n= 118,147  acc=0.719  █████
-  [0.2–0.3]  n=  79,395  acc=0.669  ███
-  [0.3–0.4]  n=  45,330  acc=0.595  ██
-  [0.4–0.5]  n=  26,895  acc=0.463  █
-  [0.5–0.6]  n=  24,546  acc=0.649  █
-  [0.6–0.7]  n=  32,577  acc=0.771  █
-  [0.7–0.8]  n=  43,852  acc=0.884  ██
-  [0.8–0.9]  n=  59,281  acc=0.950  ██
-  [0.9–1.0]  n= 134,474  acc=0.990  ██████

### Top 10 domen w błędach (Domena | Model | Prawda)
     258×  tools.ietf.org                      | Model: Phishing (1) | Prawda: Legit (0)
     245×  angelfire.com                       | Model: Phishing (1) | Prawda: Legit (0)
     150×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
     126×  home.comcast.net                    | Model: Legit (0)    | Prawda: Phishing (1)
      92×  code.google.com                     | Model: Phishing (1) | Prawda: Legit (0)
      73×  pastehtml.com                       | Model: Legit (0)    | Prawda: Phishing (1)
      66×  painterspaintings.com               | Model: Legit (0)    | Prawda: Phishing (1)
      65×  globetrotter-games.com              | Model: Phishing (1) | Prawda: Legit (0)
      54×  w3.org                              | Model: Phishing (1) | Prawda: Legit (0)
      51×  fibtex.lodz.pl                      | Model: Phishing (1) | Prawda: Legit (0)


## SET - 4
### Metryki
-  Precision : 0.9558   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.9605   (ile phishingów zostało wykrytych)
-  F1        : 0.9582
-  FPR       : 0.0154   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 132 / 12886 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=420,725  F1=0.9431
-  [ 50–100 znaków]  n=144,404  F1=0.9807
-  [100–150 znaków]  n= 19,044  F1=0.9900
-  [150–200 znaków]  n=  8,626  F1=0.9974
-  [200–999 znaków]  n=  4,487  F1=0.9954

### Rozkład predykcji
-  [0.0–0.1]  n= 229,780  acc=1.000  ███████████████
-  [0.1–0.2]  n= 127,207  acc=0.995  ████████
-  [0.2–0.3]  n=  56,469  acc=0.974  ███
-  [0.3–0.4]  n=  21,243  acc=0.907  █
-  [0.4–0.5]  n=   8,308  acc=0.780  
-  [0.5–0.6]  n=   5,804  acc=0.424  
-  [0.6–0.7]  n=   7,217  acc=0.697  
-  [0.7–0.8]  n=  11,625  acc=0.917  
-  [0.8–0.9]  n=  23,854  acc=0.989  █
-  [0.9–1.0]  n= 105,828  acc=1.000  ███████

### Top 10 domen w błędach (Domena | Model | Prawda)
      72×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
      44×  twitter.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      23×  twitter.com                         | Model: Phishing (1) | Prawda: Legit (0)
      21×  google.com                          | Model: Phishing (1) | Prawda: Legit (0)
      17×  facebook.com                        | Model: Phishing (1) | Prawda: Legit (0)
      16×  loot.co.za                          | Model: Phishing (1) | Prawda: Legit (0)
      14×  httpss:                             | Model: Phishing (1) | Prawda: Legit (0)
      13×  4shared.com                         | Model: Phishing (1) | Prawda: Legit (0)
      13×  plus.google.com                     | Model: Phishing (1) | Prawda: Legit (0)
      12×  trade.mar.cx                        | Model: Phishing (1) | Prawda: Legit (0)


