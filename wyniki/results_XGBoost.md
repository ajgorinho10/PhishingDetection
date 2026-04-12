# XGBoost (NLP-TfIDF + Cechy):
## SET - 1
### Metryki
-  Precision : 0.9526   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.9001   (ile phishingów zostało wykrytych)
-  F1        : 0.9256
-  FPR       : 0.0126   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 2770 / 14107 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=282,101  F1=0.8898
-  [ 50–100 znaków]  n=136,470  F1=0.9741
-  [100–150 znaków]  n= 17,188  F1=0.9804
-  [150–200 znaków]  n=  3,694  F1=0.9856
-  [200–999 znaków]  n=  3,727  F1=0.9949

### Rozkład predykcji
-  [0.0–0.1]  n= 315,331  acc=0.992  ████████████████████████████
-  [0.1–0.2]  n=  18,161  acc=0.915  █
-  [0.2–0.3]  n=   8,397  acc=0.753  
-  [0.3–0.4]  n=   5,060  acc=0.679  
-  [0.4–0.5]  n=   4,159  acc=0.504  
-  [0.5–0.6]  n=   3,994  acc=0.630  
-  [0.6–0.7]  n=   4,781  acc=0.766  
-  [0.7–0.8]  n=   6,089  acc=0.865  
-  [0.8–0.9]  n=  11,531  acc=0.946  █
-  [0.9–1.0]  n=  65,701  acc=0.995  █████

### Top 10 domen w błędach (Domena | Model | Prawda)
      74×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
      44×  twitter.com                         | Model: Phishing (1) | Prawda: Legit (0)
      41×  ckuik.com                           | Model: Phishing (1) | Prawda: Legit (0)
      39×  twitter.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      27×  vrbo.com                            | Model: Phishing (1) | Prawda: Legit (0)
      17×  httpss:                             | Model: Phishing (1) | Prawda: Legit (0)
      16×  worldpostjournal.com                | Model: Legit (0)    | Prawda: Phishing (1)
      14×  badoo.com                           | Model: Phishing (1) | Prawda: Legit (0)
      14×  lazygirls.info                      | Model: Phishing (1) | Prawda: Legit (0)
      13×  trade.mar.cx                        | Model: Phishing (1) | Prawda: Legit (0)


## SET - 2
### Metryki
-  Precision : 0.9688   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.8920   (ile phishingów zostało wykrytych)
-  F1        : 0.9288
-  FPR       : 0.0126   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 4954 / 20745 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=314,244  F1=0.8985
-  [ 50–100 znaków]  n=152,865  F1=0.9702
-  [100–150 znaków]  n= 18,789  F1=0.9572
-  [150–200 znaków]  n=  7,058  F1=0.9920
-  [200–999 znaków]  n=  4,461  F1=0.9916

### Rozkład predykcji
-  [0.0–0.1]  n= 317,516  acc=0.985  █████████████████████████
-  [0.1–0.2]  n=  19,395  acc=0.857  █
-  [0.2–0.3]  n=   9,688  acc=0.653  
-  [0.3–0.4]  n=   6,099  acc=0.563  
-  [0.4–0.5]  n=   5,050  acc=0.415  
-  [0.5–0.6]  n=   5,026  acc=0.706  
-  [0.6–0.7]  n=   6,184  acc=0.820  
-  [0.7–0.8]  n=   9,458  acc=0.913  
-  [0.8–0.9]  n=  19,502  acc=0.968  █
-  [0.9–1.0]  n=  99,545  acc=0.997  ████████

### Top 10 domen w błędach (Domena | Model | Prawda)
     716×  cloudflare-ipfs.com                 | Model: Legit (0)    | Prawda: Phishing (1)
     312×  cf-ipfs.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      74×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
      72×  ipfs.eth.aragon.network             | Model: Legit (0)    | Prawda: Phishing (1)
      44×  twitter.com                         | Model: Phishing (1) | Prawda: Legit (0)
      41×  ckuik.com                           | Model: Phishing (1) | Prawda: Legit (0)
      39×  twitter.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      27×  vrbo.com                            | Model: Phishing (1) | Prawda: Legit (0)
      18×  im-creator.com                      | Model: Legit (0)    | Prawda: Phishing (1)
      17×  httpss:                             | Model: Phishing (1) | Prawda: Legit (0)


## SET - 3
### Metryki
-  Precision : 0.9156   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.6097   (ile phishingów zostało wykrytych)
-  F1        : 0.7320
-  FPR       : 0.0485   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 68290 / 164333 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=570,056  F1=0.6537
-  [ 50–100 znaków]  n=182,694  F1=0.9375
-  [100–150 znaków]  n= 25,912  F1=0.9719
-  [150–200 znaków]  n=  6,871  F1=0.9771
-  [200–999 znaków]  n=  9,325  F1=0.9904

### Rozkład predykcji
-  [0.0–0.1]  n= 416,028  acc=0.845  ████████████████████
-  [0.1–0.2]  n=  45,737  acc=0.563  ██
-  [0.2–0.3]  n=  42,156  acc=0.294  ██
-  [0.3–0.4]  n=  24,301  acc=0.324  █
-  [0.4–0.5]  n=  21,604  acc=0.403  █
-  [0.5–0.6]  n=  22,772  acc=0.791  █
-  [0.6–0.7]  n=  19,782  acc=0.787  
-  [0.7–0.8]  n=  20,283  acc=0.810  █
-  [0.8–0.9]  n=  32,607  acc=0.872  █
-  [0.9–1.0]  n= 149,676  acc=0.975  ███████

### Top 10 domen w błędach (Domena | Model | Prawda)
     954×  pastehtml.com                       | Model: Legit (0)    | Prawda: Phishing (1)
     271×  babinet.cz                          | Model: Legit (0)    | Prawda: Phishing (1)
     181×  angelfire.com                       | Model: Phishing (1) | Prawda: Legit (0)
     169×  villakidsbuffetinfantil.com         | Model: Legit (0)    | Prawda: Phishing (1)
     154×  freewebs.com                        | Model: Phishing (1) | Prawda: Legit (0)
     151×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
     110×  ddj.com                             | Model: Phishing (1) | Prawda: Legit (0)
      78×  home.earthlink.net                  | Model: Phishing (1) | Prawda: Legit (0)
      72×  painterspaintings.com               | Model: Legit (0)    | Prawda: Phishing (1)
      63×  everything.explained.today          | Model: Phishing (1) | Prawda: Legit (0)


## SET - 4
### Metryki
-  Precision : 0.9697   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.9202   (ile phishingów zostało wykrytych)
-  F1        : 0.9443
-  FPR       : 0.0100   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 3507 / 16683 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=420,725  F1=0.9229
-  [ 50–100 znaków]  n=144,404  F1=0.9775
-  [100–150 znaków]  n= 19,044  F1=0.9838
-  [150–200 znaków]  n=  8,626  F1=0.9949
-  [200–999 znaków]  n=  4,487  F1=0.9938

### Rozkład predykcji
-  [0.0–0.1]  n= 408,557  acc=0.992  ███████████████████████████
-  [0.1–0.2]  n=  21,370  acc=0.906  █
-  [0.2–0.3]  n=  11,251  acc=0.781  
-  [0.3–0.4]  n=   5,674  acc=0.638  
-  [0.4–0.5]  n=   4,740  acc=0.460  
-  [0.5–0.6]  n=   4,552  acc=0.670  
-  [0.6–0.7]  n=   5,555  acc=0.796  
-  [0.7–0.8]  n=   7,318  acc=0.886  
-  [0.8–0.9]  n=  14,216  acc=0.956  
-  [0.9–1.0]  n= 114,102  acc=0.997  ███████

### Top 10 domen w błędach (Domena | Model | Prawda)
      74×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
      44×  twitter.com                         | Model: Phishing (1) | Prawda: Legit (0)
      41×  ckuik.com                           | Model: Phishing (1) | Prawda: Legit (0)
      39×  twitter.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      27×  vrbo.com                            | Model: Phishing (1) | Prawda: Legit (0)
      17×  httpss:                             | Model: Phishing (1) | Prawda: Legit (0)
      16×  worldpostjournal.com                | Model: Legit (0)    | Prawda: Phishing (1)
      14×  badoo.com                           | Model: Phishing (1) | Prawda: Legit (0)
      14×  lazygirls.info                      | Model: Phishing (1) | Prawda: Legit (0)
      13×  trade.mar.cx                        | Model: Phishing (1) | Prawda: Legit (0)


# XGBoost (NLP-TfIDF):
## SET - 1
### Metryki
-  Precision : 0.9565   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.7957   (ile phishingów zostało wykrytych)
-  F1        : 0.8688
-  FPR       : 0.0102   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 2050 / 23436 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=282,101  F1=0.7981
-  [ 50–100 znaków]  n=136,470  F1=0.9583
-  [100–150 znaków]  n= 17,188  F1=0.9666
-  [150–200 znaków]  n=  3,694  F1=0.9798
-  [200–999 znaków]  n=  3,727  F1=0.9908

### Rozkład predykcji
-  [0.0–0.1]  n= 291,902  acc=0.994  ██████████████████████████
-  [0.1–0.2]  n=  35,333  acc=0.905  ███
-  [0.2–0.3]  n=  20,875  acc=0.650  █
-  [0.3–0.4]  n=   7,949  acc=0.537  
-  [0.4–0.5]  n=   6,056  acc=0.381  
-  [0.5–0.6]  n=   5,892  acc=0.730  
-  [0.6–0.7]  n=   5,478  acc=0.846  
-  [0.7–0.8]  n=   6,034  acc=0.915  
-  [0.8–0.9]  n=   8,009  acc=0.958  
-  [0.9–1.0]  n=  55,676  acc=0.996  █████

### Top 10 domen w błędach (Domena | Model | Prawda)
     106×  twitter.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      71×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
      30×  ckuik.com                           | Model: Phishing (1) | Prawda: Legit (0)
      24×  182.92.184.208:8806                 | Model: Legit (0)    | Prawda: Phishing (1)
      23×  twitter.com                         | Model: Phishing (1) | Prawda: Legit (0)
      21×  158.255.193.15:4331                 | Model: Legit (0)    | Prawda: Phishing (1)
      21×  i-to.cc                             | Model: Legit (0)    | Prawda: Phishing (1)
      20×  telegra.ph                          | Model: Legit (0)    | Prawda: Phishing (1)
      19×  lihi.cc                             | Model: Legit (0)    | Prawda: Phishing (1)
      18×  cpc.cx                              | Model: Legit (0)    | Prawda: Phishing (1)


## SET - 2
### Metryki
-  Precision : 0.9710   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.7765   (ile phishingów zostało wykrytych)
-  F1        : 0.8629
-  FPR       : 0.0102   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 5438 / 37434 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=314,244  F1=0.8178
-  [ 50–100 znaków]  n=152,865  F1=0.9104
-  [100–150 znaków]  n= 18,789  F1=0.9242
-  [150–200 znaków]  n=  7,058  F1=0.9887
-  [200–999 znaków]  n=  4,461  F1=0.9864

### Rozkład predykcji
-  [0.0–0.1]  n= 295,290  acc=0.982  ███████████████████████
-  [0.1–0.2]  n=  38,663  acc=0.827  ███
-  [0.2–0.3]  n=  24,220  acc=0.560  █
-  [0.3–0.4]  n=  10,203  acc=0.418  
-  [0.4–0.5]  n=   7,739  acc=0.298  
-  [0.5–0.6]  n=   8,511  acc=0.813  
-  [0.6–0.7]  n=   9,219  acc=0.908  
-  [0.7–0.8]  n=   7,860  acc=0.935  
-  [0.8–0.9]  n=  11,566  acc=0.971  
-  [0.9–1.0]  n=  84,192  acc=0.997  ██████

### Top 10 domen w błędach (Domena | Model | Prawda)
   2,079×  ipfs.eth.aragon.network             | Model: Legit (0)    | Prawda: Phishing (1)
     746×  cloudflare-ipfs.com                 | Model: Legit (0)    | Prawda: Phishing (1)
     417×  cf-ipfs.com                         | Model: Legit (0)    | Prawda: Phishing (1)
     224×  shorturl.at                         | Model: Legit (0)    | Prawda: Phishing (1)
     106×  twitter.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      75×  nftstorage.link                     | Model: Legit (0)    | Prawda: Phishing (1)
      71×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
      53×  is.gd                               | Model: Legit (0)    | Prawda: Phishing (1)
      47×  jemi.so                             | Model: Legit (0)    | Prawda: Phishing (1)
      41×  s.free.fr                           | Model: Legit (0)    | Prawda: Phishing (1)


## SET - 3
### Metryki
-  Precision : 0.9227   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.4824   (ile phishingów zostało wykrytych)
-  F1        : 0.6336
-  FPR       : 0.0349   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 59460 / 205397 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=570,056  F1=0.5168
-  [ 50–100 znaków]  n=182,694  F1=0.9109
-  [100–150 znaków]  n= 25,912  F1=0.9605
-  [150–200 znaków]  n=  6,871  F1=0.9701
-  [200–999 znaków]  n=  9,325  F1=0.9864

### Rozkład predykcji
-  [0.0–0.1]  n= 388,941  acc=0.853  ███████████████████
-  [0.1–0.2]  n=  72,655  acc=0.613  ███
-  [0.2–0.3]  n=  82,344  acc=0.253  ████
-  [0.3–0.4]  n=  36,611  acc=0.244  █
-  [0.4–0.5]  n=  21,941  acc=0.273  █
-  [0.5–0.6]  n=  21,478  acc=0.789  █
-  [0.6–0.7]  n=  16,842  acc=0.803  
-  [0.7–0.8]  n=  18,403  acc=0.859  
-  [0.8–0.9]  n=  23,444  acc=0.905  █
-  [0.9–1.0]  n= 112,287  acc=0.980  █████

### Top 10 domen w błędach (Domena | Model | Prawda)
     937×  pastehtml.com                       | Model: Legit (0)    | Prawda: Phishing (1)
     280×  babinet.cz                          | Model: Legit (0)    | Prawda: Phishing (1)
     170×  villakidsbuffetinfantil.com         | Model: Legit (0)    | Prawda: Phishing (1)
     150×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
     131×  home.comcast.net                    | Model: Legit (0)    | Prawda: Phishing (1)
     121×  angelfire.com                       | Model: Phishing (1) | Prawda: Legit (0)
     118×  freewebs.com                        | Model: Phishing (1) | Prawda: Legit (0)
      96×  twitter.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      90×  x.co                                | Model: Legit (0)    | Prawda: Phishing (1)
      81×  affiliatealmanac.com                | Model: Legit (0)    | Prawda: Phishing (1)


## SET - 4
### Metryki
-  Precision : 0.9687   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.8430   (ile phishingów zostało wykrytych)
-  F1        : 0.9015
-  FPR       : 0.0094   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 2522 / 28299 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=420,725  F1=0.8608
-  [ 50–100 znaków]  n=144,404  F1=0.9630
-  [100–150 znaków]  n= 19,044  F1=0.9714
-  [150–200 znaków]  n=  8,626  F1=0.9927
-  [200–999 znaków]  n=  4,487  F1=0.9881

### Rozkład predykcji
-  [0.0–0.1]  n= 361,164  acc=0.994  ████████████████████████
-  [0.1–0.2]  n=  47,240  acc=0.915  ███
-  [0.2–0.3]  n=  36,870  acc=0.766  ██
-  [0.3–0.4]  n=  10,711  acc=0.579  
-  [0.4–0.5]  n=   7,699  acc=0.391  
-  [0.5–0.6]  n=   7,250  acc=0.733  
-  [0.6–0.7]  n=   6,721  acc=0.850  
-  [0.7–0.8]  n=   7,621  acc=0.921  
-  [0.8–0.9]  n=  10,457  acc=0.964  
-  [0.9–1.0]  n= 101,602  acc=0.997  ██████

### Top 10 domen w błędach (Domena | Model | Prawda)
     106×  twitter.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      71×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
      48×  urlz.fr                             | Model: Legit (0)    | Prawda: Phishing (1)
      34×  tr.ee                               | Model: Legit (0)    | Prawda: Phishing (1)
      30×  ckuik.com                           | Model: Phishing (1) | Prawda: Legit (0)
      24×  182.92.184.208:8806                 | Model: Legit (0)    | Prawda: Phishing (1)
      23×  telegra.ph                          | Model: Legit (0)    | Prawda: Phishing (1)
      23×  twitter.com                         | Model: Phishing (1) | Prawda: Legit (0)
      21×  i-to.cc                             | Model: Legit (0)    | Prawda: Phishing (1)
      21×  158.255.193.15:4331                 | Model: Legit (0)    | Prawda: Phishing (1)

