# LSTM (NLP + Cechy):
## SET - 1
### Metryki
-  Precision : 0.9702   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.9241   (ile phishingów zostało wykrytych)
-  F1        : 0.9466
-  FPR       : 0.0080   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 191 / 10159 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=282,101  F1=0.9221
-  [ 50–100 znaków]  n=136,470  F1=0.9787
-  [100–150 znaków]  n= 17,188  F1=0.9884
-  [150–200 znaków]  n=  3,694  F1=0.9930
-  [200–999 znaków]  n=  3,727  F1=0.9922

### Rozkład predykcji
-  [0.0–0.1]  n= 235,893  acc=0.999  █████████████████████
-  [0.1–0.2]  n=  57,474  acc=0.985  █████
-  [0.2–0.3]  n=  37,691  acc=0.953  ███
-  [0.3–0.4]  n=  12,462  acc=0.848  █
-  [0.4–0.5]  n=   6,842  acc=0.606  
-  [0.5–0.6]  n=   5,600  acc=0.694  
-  [0.6–0.7]  n=   5,976  acc=0.891  
-  [0.7–0.8]  n=   8,413  acc=0.970  
-  [0.8–0.9]  n=  17,232  acc=0.993  █
-  [0.9–1.0]  n=  55,621  acc=1.000  █████

### Top 10 domen w błędach (Domena | Model | Prawda)
      60×  twitter.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      44×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
      25×  telegra.ph                          | Model: Legit (0)    | Prawda: Phishing (1)
      18×  gulsproductions.com                 | Model: Legit (0)    | Prawda: Phishing (1)
      17×  borcuodeme.com                      | Model: Legit (0)    | Prawda: Phishing (1)
      14×  worldpostjournal.com                | Model: Legit (0)    | Prawda: Phishing (1)
      13×  angelfire.com                       | Model: Legit (0)    | Prawda: Phishing (1)
      11×  jeffott.net                         | Model: Phishing (1) | Prawda: Legit (0)
      11×  ow.ly                               | Model: Phishing (1) | Prawda: Legit (0)
      11×  associatepublisher.com              | Model: Phishing (1) | Prawda: Legit (0)


## SET - 2
### Metryki
-  Precision : 0.9806   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.9222   (ile phishingów zostało wykrytych)
-  F1        : 0.9505
-  FPR       : 0.0080   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 235 / 14566 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=314,244  F1=0.9253
-  [ 50–100 znaków]  n=152,865  F1=0.9838
-  [100–150 znaków]  n= 18,789  F1=0.9899
-  [150–200 znaków]  n=  7,058  F1=0.9964
-  [200–999 znaków]  n=  4,461  F1=0.9931

### Rozkład predykcji
-  [0.0–0.1]  n= 235,937  acc=0.999  ██████████████████
-  [0.1–0.2]  n=  58,371  acc=0.970  ████
-  [0.2–0.3]  n=  38,847  acc=0.925  ███
-  [0.3–0.4]  n=  13,565  acc=0.779  █
-  [0.4–0.5]  n=   8,051  acc=0.515  
-  [0.5–0.6]  n=   7,185  acc=0.761  
-  [0.6–0.7]  n=   8,034  acc=0.919  
-  [0.7–0.8]  n=  11,917  acc=0.979  
-  [0.8–0.9]  n=  31,854  acc=0.996  ██
-  [0.9–1.0]  n=  83,702  acc=1.000  ██████

### Top 10 domen w błędach (Domena | Model | Prawda)
      60×  twitter.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      44×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
      25×  telegra.ph                          | Model: Legit (0)    | Prawda: Phishing (1)
      18×  gulsproductions.com                 | Model: Legit (0)    | Prawda: Phishing (1)
      17×  borcuodeme.com                      | Model: Legit (0)    | Prawda: Phishing (1)
      15×  klrn.wpenginepowered.com            | Model: Legit (0)    | Prawda: Phishing (1)
      14×  cakeresume.com                      | Model: Legit (0)    | Prawda: Phishing (1)
      14×  worldpostjournal.com                | Model: Legit (0)    | Prawda: Phishing (1)
      13×  angelfire.com                       | Model: Legit (0)    | Prawda: Phishing (1)
      11×  jeffott.net                         | Model: Phishing (1) | Prawda: Legit (0)


## SET - 3
### Metryki
-  Precision : 0.9494   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.7127   (ile phishingów zostało wykrytych)
-  F1        : 0.8142
-  FPR       : 0.0328   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 3649 / 119730 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=570,056  F1=0.7604
-  [ 50–100 znaków]  n=182,694  F1=0.9643
-  [100–150 znaków]  n= 25,912  F1=0.9852
-  [150–200 znaków]  n=  6,871  F1=0.9889
-  [200–999 znaków]  n=  9,325  F1=0.9933

### Rozkład predykcji
-  [0.0–0.1]  n= 266,492  acc=0.989  █████████████
-  [0.1–0.2]  n= 111,674  acc=0.639  █████
-  [0.2–0.3]  n=  73,555  acc=0.659  ███
-  [0.3–0.4]  n=  38,070  acc=0.501  █
-  [0.4–0.5]  n=  28,820  acc=0.362  █
-  [0.5–0.6]  n=  28,956  acc=0.778  █
-  [0.6–0.7]  n=  32,068  acc=0.889  █
-  [0.7–0.8]  n=  37,543  acc=0.945  █
-  [0.8–0.9]  n=  54,380  acc=0.976  ██
-  [0.9–1.0]  n= 123,388  acc=0.995  ██████

### Top 10 domen w błędach (Domena | Model | Prawda)
     388×  pastehtml.com                       | Model: Legit (0)    | Prawda: Phishing (1)
     358×  angelfire.com                       | Model: Phishing (1) | Prawda: Legit (0)
     116×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
     103×  home.comcast.net                    | Model: Legit (0)    | Prawda: Phishing (1)
      59×  globetrotter-games.com              | Model: Phishing (1) | Prawda: Legit (0)
      51×  fibtex.lodz.pl                      | Model: Phishing (1) | Prawda: Legit (0)
      49×  twitter.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      37×  fun-dive.com                        | Model: Legit (0)    | Prawda: Phishing (1)
      37×  xs4all.nl                           | Model: Phishing (1) | Prawda: Legit (0)
      35×  pagesperso-orange.fr                | Model: Phishing (1) | Prawda: Legit (0)


## SET - 4
### Metryki
-  Precision : 0.9806   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.9377   (ile phishingów zostało wykrytych)
-  F1        : 0.9587
-  FPR       : 0.0064   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 203 / 12412 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=420,725  F1=0.9433
-  [ 50–100 znaków]  n=144,404  F1=0.9819
-  [100–150 znaków]  n= 19,044  F1=0.9903
-  [150–200 znaków]  n=  8,626  F1=0.9973
-  [200–999 znaków]  n=  4,487  F1=0.9932

### Rozkład predykcji
-  [0.0–0.1]  n= 250,638  acc=0.999  ████████████████
-  [0.1–0.2]  n= 129,339  acc=0.991  ████████
-  [0.2–0.3]  n=  48,279  acc=0.952  ███
-  [0.3–0.4]  n=  14,482  acc=0.822  
-  [0.4–0.5]  n=   7,733  acc=0.570  
-  [0.5–0.6]  n=   6,612  acc=0.732  
-  [0.6–0.7]  n=   7,544  acc=0.911  
-  [0.7–0.8]  n=  11,413  acc=0.977  
-  [0.8–0.9]  n=  25,236  acc=0.995  █
-  [0.9–1.0]  n=  96,059  acc=1.000  ██████

### Top 10 domen w błędach (Domena | Model | Prawda)
      60×  twitter.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      44×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
      25×  telegra.ph                          | Model: Legit (0)    | Prawda: Phishing (1)
      18×  gulsproductions.com                 | Model: Legit (0)    | Prawda: Phishing (1)
      17×  borcuodeme.com                      | Model: Legit (0)    | Prawda: Phishing (1)
      14×  worldpostjournal.com                | Model: Legit (0)    | Prawda: Phishing (1)
      13×  angelfire.com                       | Model: Legit (0)    | Prawda: Phishing (1)
      11×  jeffott.net                         | Model: Phishing (1) | Prawda: Legit (0)
      11×  ow.ly                               | Model: Phishing (1) | Prawda: Legit (0)
      11×  vk.com                              | Model: Legit (0)    | Prawda: Phishing (1)


# LSTM (NLP):
## SET - 1
### Metryki
-  Precision : 0.9578   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.9210   (ile phishingów zostało wykrytych)
-  F1        : 0.9390
-  FPR       : 0.0114   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 304 / 11659 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=282,101  F1=0.9131
-  [ 50–100 znaków]  n=136,470  F1=0.9737
-  [100–150 znaków]  n= 17,188  F1=0.9819
-  [150–200 znaków]  n=  3,694  F1=0.9875
-  [200–999 znaków]  n=  3,727  F1=0.9915

### Rozkład predykcji
-  [0.0–0.1]  n= 231,777  acc=0.999  ████████████████████
-  [0.1–0.2]  n=  58,091  acc=0.982  █████
-  [0.2–0.3]  n=  40,118  acc=0.954  ███
-  [0.3–0.4]  n=  12,569  acc=0.840  █
-  [0.4–0.5]  n=   6,921  acc=0.627  
-  [0.5–0.6]  n=   5,639  acc=0.618  
-  [0.6–0.7]  n=   6,041  acc=0.827  
-  [0.7–0.8]  n=   8,611  acc=0.941  
-  [0.8–0.9]  n=  16,523  acc=0.988  █
-  [0.9–1.0]  n=  56,914  acc=0.999  █████

### Top 10 domen w błędach (Domena | Model | Prawda)
      49×  twitter.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      28×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
      23×  sites.google.com                    | Model: Legit (0)    | Prawda: Phishing (1)
      20×  veganvet.net                        | Model: Legit (0)    | Prawda: Phishing (1)
      18×  angelfire.com                       | Model: Legit (0)    | Prawda: Phishing (1)
      17×  borcuodeme.com                      | Model: Legit (0)    | Prawda: Phishing (1)
      17×  worldpostjournal.com                | Model: Legit (0)    | Prawda: Phishing (1)
      15×  telegra.ph                          | Model: Legit (0)    | Prawda: Phishing (1)
      14×  gulsproductions.com                 | Model: Legit (0)    | Prawda: Phishing (1)
      12×  twitter.com                         | Model: Phishing (1) | Prawda: Legit (0)


## SET - 2
### Metryki
-  Precision : 0.9725   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.9223   (ile phishingów zostało wykrytych)
-  F1        : 0.9468
-  FPR       : 0.0114   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 561 / 15740 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=314,244  F1=0.9218
-  [ 50–100 znaków]  n=152,865  F1=0.9801
-  [100–150 znaków]  n= 18,789  F1=0.9846
-  [150–200 znaków]  n=  7,058  F1=0.9939
-  [200–999 znaków]  n=  4,461  F1=0.9917

### Rozkład predykcji
-  [0.0–0.1]  n= 232,036  acc=0.998  ██████████████████
-  [0.1–0.2]  n=  58,908  acc=0.969  ████
-  [0.2–0.3]  n=  41,151  acc=0.931  ███
-  [0.3–0.4]  n=  13,486  acc=0.783  █
-  [0.4–0.5]  n=   7,978  acc=0.544  
-  [0.5–0.6]  n=   7,428  acc=0.710  
-  [0.6–0.7]  n=   9,118  acc=0.886  
-  [0.7–0.8]  n=  14,033  acc=0.964  █
-  [0.8–0.9]  n=  29,176  acc=0.993  ██
-  [0.9–1.0]  n=  84,149  acc=0.999  ██████

### Top 10 domen w błędach (Domena | Model | Prawda)
      49×  twitter.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      28×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
      27×  sites.google.com                    | Model: Legit (0)    | Prawda: Phishing (1)
      20×  veganvet.net                        | Model: Legit (0)    | Prawda: Phishing (1)
      18×  angelfire.com                       | Model: Legit (0)    | Prawda: Phishing (1)
      17×  borcuodeme.com                      | Model: Legit (0)    | Prawda: Phishing (1)
      17×  worldpostjournal.com                | Model: Legit (0)    | Prawda: Phishing (1)
      15×  klrn.wpenginepowered.com            | Model: Legit (0)    | Prawda: Phishing (1)
      15×  tinyurl.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      15×  telegra.ph                          | Model: Legit (0)    | Prawda: Phishing (1)


## SET - 3
### Metryki
-  Precision : 0.9424   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.7043   (ile phishingów zostało wykrytych)
-  F1        : 0.8061
-  FPR       : 0.0371   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 10697 / 124705 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=570,056  F1=0.7519
-  [ 50–100 znaków]  n=182,694  F1=0.9577
-  [100–150 znaków]  n= 25,912  F1=0.9810
-  [150–200 znaków]  n=  6,871  F1=0.9824
-  [200–999 znaków]  n=  9,325  F1=0.9901

### Rozkład predykcji
-  [0.0–0.1]  n= 267,438  acc=0.963  █████████████
-  [0.1–0.2]  n= 121,518  acc=0.612  ██████
-  [0.2–0.3]  n=  68,974  acc=0.734  ███
-  [0.3–0.4]  n=  33,351  acc=0.550  █
-  [0.4–0.5]  n=  28,593  acc=0.358  █
-  [0.5–0.6]  n=  32,370  acc=0.798  █
-  [0.6–0.7]  n=  28,228  acc=0.851  █
-  [0.7–0.8]  n=  34,808  acc=0.924  █
-  [0.8–0.9]  n=  57,567  acc=0.971  ██
-  [0.9–1.0]  n= 122,099  acc=0.994  ██████

### Top 10 domen w błędach (Domena | Model | Prawda)
     344×  pastehtml.com                       | Model: Legit (0)    | Prawda: Phishing (1)
     111×  angelfire.com                       | Model: Phishing (1) | Prawda: Legit (0)
      96×  home.comcast.net                    | Model: Legit (0)    | Prawda: Phishing (1)
      82×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
      72×  painterspaintings.com               | Model: Legit (0)    | Prawda: Phishing (1)
      66×  globetrotter-games.com              | Model: Phishing (1) | Prawda: Legit (0)
      51×  fibtex.lodz.pl                      | Model: Phishing (1) | Prawda: Legit (0)
      39×  linkedin.com                        | Model: Legit (0)    | Prawda: Phishing (1)
      38×  twitter.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      37×  fun-dive.com                        | Model: Legit (0)    | Prawda: Phishing (1)


## SET - 4
### Metryki
-  Precision : 0.9726   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.9361   (ile phishingów zostało wykrytych)
-  F1        : 0.9540
-  FPR       : 0.0091   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 359 / 13871 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=420,725  F1=0.9383
-  [ 50–100 znaków]  n=144,404  F1=0.9774
-  [100–150 znaków]  n= 19,044  F1=0.9857
-  [150–200 znaków]  n=  8,626  F1=0.9954
-  [200–999 znaków]  n=  4,487  F1=0.9921

### Rozkład predykcji
-  [0.0–0.1]  n= 269,024  acc=0.999  ██████████████████
-  [0.1–0.2]  n= 114,372  acc=0.988  ███████
-  [0.2–0.3]  n=  44,547  acc=0.945  ██
-  [0.3–0.4]  n=  13,860  acc=0.814  
-  [0.4–0.5]  n=   7,711  acc=0.590  
-  [0.5–0.6]  n=   6,473  acc=0.657  
-  [0.6–0.7]  n=   7,337  acc=0.855  
-  [0.7–0.8]  n=  11,637  acc=0.956  
-  [0.8–0.9]  n=  26,198  acc=0.992  █
-  [0.9–1.0]  n=  96,176  acc=0.999  ██████

### Top 10 domen w błędach (Domena | Model | Prawda)
      49×  twitter.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      30×  sites.google.com                    | Model: Legit (0)    | Prawda: Phishing (1)
      28×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
      20×  veganvet.net                        | Model: Legit (0)    | Prawda: Phishing (1)
      18×  angelfire.com                       | Model: Legit (0)    | Prawda: Phishing (1)
      17×  borcuodeme.com                      | Model: Legit (0)    | Prawda: Phishing (1)
      17×  worldpostjournal.com                | Model: Legit (0)    | Prawda: Phishing (1)
      15×  telegra.ph                          | Model: Legit (0)    | Prawda: Phishing (1)
      14×  gulsproductions.com                 | Model: Legit (0)    | Prawda: Phishing (1)
      12×  moreepa.co.uk                       | Model: Legit (0)    | Prawda: Phishing (1)

