# Tranformer(NLP + Cechy)
## SET - 1
### Metryki
-  Precision : 0.9289   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.8447   (ile phishingów zostało wykrytych)
-  F1        : 0.8848
-  FPR       : 0.0182   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 149 / 21442 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=282,101  F1=0.8423
-  [ 50–100 znaków]  n=136,470  F1=0.9314
-  [100–150 znaków]  n= 17,188  F1=0.9686
-  [150–200 znaków]  n=  3,694  F1=0.9838
-  [200–999 znaków]  n=  3,727  F1=0.9889

### Rozkład predykcji
-  [0.0–0.1]  n= 130,227  acc=0.999  ███████████
-  [0.1–0.2]  n= 114,271  acc=0.987  ██████████
-  [0.2–0.3]  n=  69,061  acc=0.952  ██████
-  [0.3–0.4]  n=  26,123  acc=0.830  ██
-  [0.4–0.5]  n=  14,883  acc=0.610  █
-  [0.5–0.6]  n=  11,699  acc=0.658  █
-  [0.6–0.7]  n=  10,840  acc=0.861  
-  [0.7–0.8]  n=  12,024  acc=0.952  █
-  [0.8–0.9]  n=  18,167  acc=0.990  █
-  [0.9–1.0]  n=  35,909  acc=0.999  ███

### Top 10 domen w błędach (Domena | Model | Prawda)
      83×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
      50×  twitter.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      37×  torrentz.eu                         | Model: Phishing (1) | Prawda: Legit (0)
      27×  twitter.com                         | Model: Phishing (1) | Prawda: Legit (0)
      26×  veganvet.net                        | Model: Legit (0)    | Prawda: Phishing (1)
      24×  angelfire.com                       | Model: Legit (0)    | Prawda: Phishing (1)
      22×  associatepublisher.com              | Model: Phishing (1) | Prawda: Legit (0)
      22×  gulsproductions.com                 | Model: Legit (0)    | Prawda: Phishing (1)
      21×  gosgmart.com                        | Model: Legit (0)    | Prawda: Phishing (1)
      20×  sitesumo.com                        | Model: Legit (0)    | Prawda: Phishing (1)


## SET - 2
### Metryki
-  Precision : 0.9537   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.8554   (ile phishingów zostało wykrytych)
-  F1        : 0.9019
-  FPR       : 0.0182   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 222 / 28237 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=314,244  F1=0.8592
-  [ 50–100 znaków]  n=152,865  F1=0.9521
-  [100–150 znaków]  n= 18,789  F1=0.9730
-  [150–200 znaków]  n=  7,058  F1=0.9925
-  [200–999 znaków]  n=  4,461  F1=0.9899

### Rozkład predykcji
-  [0.0–0.1]  n= 130,299  acc=0.999  ██████████
-  [0.1–0.2]  n= 115,389  acc=0.978  █████████
-  [0.2–0.3]  n=  70,632  acc=0.931  █████
-  [0.3–0.4]  n=  28,047  acc=0.773  ██
-  [0.4–0.5]  n=  16,993  acc=0.534  █
-  [0.5–0.6]  n=  14,171  acc=0.718  █
-  [0.6–0.7]  n=  14,211  acc=0.894  █
-  [0.7–0.8]  n=  16,930  acc=0.966  █
-  [0.8–0.9]  n=  30,413  acc=0.994  ██
-  [0.9–1.0]  n=  60,378  acc=0.999  ████

### Top 10 domen w błędach (Domena | Model | Prawda)
      83×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
      50×  twitter.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      37×  torrentz.eu                         | Model: Phishing (1) | Prawda: Legit (0)
      27×  twitter.com                         | Model: Phishing (1) | Prawda: Legit (0)
      26×  veganvet.net                        | Model: Legit (0)    | Prawda: Phishing (1)
      26×  cakeresume.com                      | Model: Legit (0)    | Prawda: Phishing (1)
      24×  angelfire.com                       | Model: Legit (0)    | Prawda: Phishing (1)
      22×  gulsproductions.com                 | Model: Legit (0)    | Prawda: Phishing (1)
      22×  associatepublisher.com              | Model: Phishing (1) | Prawda: Legit (0)
      21×  gosgmart.com                        | Model: Legit (0)    | Prawda: Phishing (1)


## SET - 3
### Metryki
-  Precision : 0.9207   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.6084   (ile phishingów zostało wykrytych)
-  F1        : 0.7327
-  FPR       : 0.0452   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 3075 / 163436 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=570,056  F1=0.6586
-  [ 50–100 znaków]  n=182,694  F1=0.9197
-  [100–150 znaków]  n= 25,912  F1=0.9682
-  [150–200 znaków]  n=  6,871  F1=0.9774
-  [200–999 znaków]  n=  9,325  F1=0.9916

### Rozkład predykcji
-  [0.0–0.1]  n= 143,138  acc=0.982  ███████
-  [0.1–0.2]  n= 186,903  acc=0.708  █████████
-  [0.2–0.3]  n= 109,981  acc=0.746  █████
-  [0.3–0.4]  n=  63,118  acc=0.529  ███
-  [0.4–0.5]  n=  48,567  acc=0.397  ██
-  [0.5–0.6]  n=  41,397  acc=0.727  ██
-  [0.6–0.7]  n=  37,489  acc=0.883  █
-  [0.7–0.8]  n=  39,906  acc=0.947  ██
-  [0.8–0.9]  n=  50,526  acc=0.979  ██
-  [0.9–1.0]  n=  73,921  acc=0.994  ███

### Top 10 domen w błędach (Domena | Model | Prawda)
   1,896×  tools.ietf.org                      | Model: Phishing (1) | Prawda: Legit (0)
     961×  pastehtml.com                       | Model: Legit (0)    | Prawda: Phishing (1)
     203×  angelfire.com                       | Model: Phishing (1) | Prawda: Legit (0)
     159×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
     145×  en.academic.ru                      | Model: Phishing (1) | Prawda: Legit (0)
      98×  gamespot.com                        | Model: Phishing (1) | Prawda: Legit (0)
      93×  home.comcast.net                    | Model: Legit (0)    | Prawda: Phishing (1)
      88×  answers.yahoo.com                   | Model: Phishing (1) | Prawda: Legit (0)
      70×  "http:                              | Model: Phishing (1) | Prawda: Legit (0)
      66×  globetrotter-games.com              | Model: Phishing (1) | Prawda: Legit (0)


## SET - 4
### Metryki
-  Precision : 0.9550   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.8762   (ile phishingów zostało wykrytych)
-  F1        : 0.9139
-  FPR       : 0.0143   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 165 / 25346 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=420,725  F1=0.8889
-  [ 50–100 znaków]  n=144,404  F1=0.9421
-  [100–150 znaków]  n= 19,044  F1=0.9745
-  [150–200 znaków]  n=  8,626  F1=0.9941
-  [200–999 znaków]  n=  4,487  F1=0.9898

### Rozkład predykcji
-  [0.0–0.1]  n= 145,603  acc=0.999  █████████
-  [0.1–0.2]  n= 192,831  acc=0.990  ████████████
-  [0.2–0.3]  n=  74,088  acc=0.943  ████
-  [0.3–0.4]  n=  27,612  acc=0.797  █
-  [0.4–0.5]  n=  16,293  acc=0.560  █
-  [0.5–0.6]  n=  13,508  acc=0.702  
-  [0.6–0.7]  n=  13,421  acc=0.887  
-  [0.7–0.8]  n=  16,398  acc=0.965  █
-  [0.8–0.9]  n=  26,039  acc=0.993  █
-  [0.9–1.0]  n=  71,542  acc=0.999  ████

### Top 10 domen w błędach (Domena | Model | Prawda)
      83×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
      50×  twitter.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      37×  torrentz.eu                         | Model: Phishing (1) | Prawda: Legit (0)
      27×  twitter.com                         | Model: Phishing (1) | Prawda: Legit (0)
      26×  veganvet.net                        | Model: Legit (0)    | Prawda: Phishing (1)
      24×  angelfire.com                       | Model: Legit (0)    | Prawda: Phishing (1)
      22×  associatepublisher.com              | Model: Phishing (1) | Prawda: Legit (0)
      22×  gulsproductions.com                 | Model: Legit (0)    | Prawda: Phishing (1)
      21×  gosgmart.com                        | Model: Legit (0)    | Prawda: Phishing (1)
      20×  grotown.com                         | Model: Legit (0)    | Prawda: Phishing (1)


# Tranformer(NLP):
## SET - 1
### Metryki
-  Precision : 0.9240   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.8648   (ile phishingów zostało wykrytych)
-  F1        : 0.8934
-  FPR       : 0.0201   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 139 / 20113 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=282,101  F1=0.8546
-  [ 50–100 znaków]  n=136,470  F1=0.9373
-  [100–150 znaków]  n= 17,188  F1=0.9720
-  [150–200 znaków]  n=  3,694  F1=0.9859
-  [200–999 znaków]  n=  3,727  F1=0.9910

### Rozkład predykcji
-  [0.0–0.1]  n= 128,314  acc=0.999  ███████████
-  [0.1–0.2]  n= 116,337  acc=0.990  ██████████
-  [0.2–0.3]  n=  69,115  acc=0.954  ██████
-  [0.3–0.4]  n=  24,228  acc=0.850  ██
-  [0.4–0.5]  n=  13,984  acc=0.635  █
-  [0.5–0.6]  n=  11,482  acc=0.623  █
-  [0.6–0.7]  n=   9,694  acc=0.829  
-  [0.7–0.8]  n=  10,458  acc=0.942  
-  [0.8–0.9]  n=  15,547  acc=0.983  █
-  [0.9–1.0]  n=  44,045  acc=0.998  ███

### Top 10 domen w błędach (Domena | Model | Prawda)
      60×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
      45×  twitter.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      27×  twitter.com                         | Model: Phishing (1) | Prawda: Legit (0)
      23×  angelfire.com                       | Model: Legit (0)    | Prawda: Phishing (1)
      22×  sitesumo.com                        | Model: Legit (0)    | Prawda: Phishing (1)
      21×  associatepublisher.com              | Model: Phishing (1) | Prawda: Legit (0)
      21×  gulsproductions.com                 | Model: Legit (0)    | Prawda: Phishing (1)
      18×  borcuodeme.com                      | Model: Legit (0)    | Prawda: Phishing (1)
      16×  worldpostjournal.com                | Model: Legit (0)    | Prawda: Phishing (1)
      13×  grotown.com                         | Model: Legit (0)    | Prawda: Phishing (1)


## SET - 2
### Metryki
-  Precision : 0.9501   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.8702   (ile phishingów zostało wykrytych)
-  F1        : 0.9084
-  FPR       : 0.0201   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 152 / 26620 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=314,244  F1=0.8715
-  [ 50–100 znaków]  n=152,865  F1=0.9511
-  [100–150 znaków]  n= 18,789  F1=0.9756
-  [150–200 znaków]  n=  7,058  F1=0.9938
-  [200–999 znaków]  n=  4,461  F1=0.9914

### Rozkład predykcji
-  [0.0–0.1]  n= 128,326  acc=0.999  ██████████
-  [0.1–0.2]  n= 117,341  acc=0.981  █████████
-  [0.2–0.3]  n=  70,755  acc=0.932  █████
-  [0.3–0.4]  n=  26,024  acc=0.791  ██
-  [0.4–0.5]  n=  16,041  acc=0.554  █
-  [0.5–0.6]  n=  14,580  acc=0.703  █
-  [0.6–0.7]  n=  12,781  acc=0.870  █
-  [0.7–0.8]  n=  14,214  acc=0.957  █
-  [0.8–0.9]  n=  21,799  acc=0.988  █
-  [0.9–1.0]  n=  75,602  acc=0.999  ██████

### Top 10 domen w błędach (Domena | Model | Prawda)
     401×  ipfs.eth.aragon.network             | Model: Legit (0)    | Prawda: Phishing (1)
      60×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
      45×  twitter.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      27×  twitter.com                         | Model: Phishing (1) | Prawda: Legit (0)
      23×  taplink.cc                          | Model: Legit (0)    | Prawda: Phishing (1)
      23×  angelfire.com                       | Model: Legit (0)    | Prawda: Phishing (1)
      22×  tinyurl.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      22×  sitesumo.com                        | Model: Legit (0)    | Prawda: Phishing (1)
      21×  gulsproductions.com                 | Model: Legit (0)    | Prawda: Phishing (1)
      21×  associatepublisher.com              | Model: Phishing (1) | Prawda: Legit (0)


## SET - 3
### Metryki
-  Precision : 0.9203   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.6406   (ile phishingów zostało wykrytych)
-  F1        : 0.7554
-  FPR       : 0.0478   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 750 / 152717 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=570,056  F1=0.6920
-  [ 50–100 znaków]  n=182,694  F1=0.9193
-  [100–150 znaków]  n= 25,912  F1=0.9688
-  [150–200 znaków]  n=  6,871  F1=0.9786
-  [200–999 znaków]  n=  9,325  F1=0.9919

### Rozkład predykcji
-  [0.0–0.1]  n= 137,423  acc=0.999  ██████
-  [0.1–0.2]  n= 177,520  acc=0.759  ████████
-  [0.2–0.3]  n= 124,948  acc=0.678  ██████
-  [0.3–0.4]  n=  55,732  acc=0.578  ██
-  [0.4–0.5]  n=  43,129  acc=0.403  ██
-  [0.5–0.6]  n=  40,167  acc=0.734  ██
-  [0.6–0.7]  n=  36,810  acc=0.856  █
-  [0.7–0.8]  n=  37,025  acc=0.931  █
-  [0.8–0.9]  n=  46,631  acc=0.973  ██
-  [0.9–1.0]  n=  95,561  acc=0.994  ████

### Top 10 domen w błędach (Domena | Model | Prawda)
     925×  pastehtml.com                       | Model: Legit (0)    | Prawda: Phishing (1)
     399×  angelfire.com                       | Model: Phishing (1) | Prawda: Legit (0)
     136×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
     119×  home.comcast.net                    | Model: Legit (0)    | Prawda: Phishing (1)
      94×  gamespot.com                        | Model: Phishing (1) | Prawda: Legit (0)
      87×  storage.googleapis.com              | Model: Legit (0)    | Prawda: Phishing (1)
      67×  "http:                              | Model: Phishing (1) | Prawda: Legit (0)
      66×  globetrotter-games.com              | Model: Phishing (1) | Prawda: Legit (0)
      61×  xs4all.nl                           | Model: Phishing (1) | Prawda: Legit (0)
      57×  "https:                             | Model: Phishing (1) | Prawda: Legit (0)


## SET - 4
### Metryki
-  Precision : 0.9518   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.8942   (ile phishingów zostało wykrytych)
-  F1        : 0.9221
-  FPR       : 0.0157   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 144 / 23204 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=420,725  F1=0.9000
-  [ 50–100 znaków]  n=144,404  F1=0.9473
-  [100–150 znaków]  n= 19,044  F1=0.9768
-  [150–200 znaków]  n=  8,626  F1=0.9948
-  [200–999 znaków]  n=  4,487  F1=0.9912

### Rozkład predykcji
-  [0.0–0.1]  n= 128,361  acc=0.999  ████████
-  [0.1–0.2]  n= 199,882  acc=0.993  █████████████
-  [0.2–0.3]  n=  84,380  acc=0.952  █████
-  [0.3–0.4]  n=  25,424  acc=0.821  █
-  [0.4–0.5]  n=  15,004  acc=0.595  █
-  [0.5–0.6]  n=  12,904  acc=0.664  
-  [0.6–0.7]  n=  11,478  acc=0.855  
-  [0.7–0.8]  n=  13,060  acc=0.953  
-  [0.8–0.9]  n=  21,653  acc=0.988  █
-  [0.9–1.0]  n=  85,189  acc=0.999  █████

### Top 10 domen w błędach (Domena | Model | Prawda)
      60×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
      45×  twitter.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      27×  twitter.com                         | Model: Phishing (1) | Prawda: Legit (0)
      23×  angelfire.com                       | Model: Legit (0)    | Prawda: Phishing (1)
      22×  sitesumo.com                        | Model: Legit (0)    | Prawda: Phishing (1)
      21×  associatepublisher.com              | Model: Phishing (1) | Prawda: Legit (0)
      21×  gulsproductions.com                 | Model: Legit (0)    | Prawda: Phishing (1)
      18×  borcuodeme.com                      | Model: Legit (0)    | Prawda: Phishing (1)
      16×  worldpostjournal.com                | Model: Legit (0)    | Prawda: Phishing (1)
      15×  storage.googleapis.com              | Model: Legit (0)    | Prawda: Phishing (1)
