# MLP (NLP-TfIDF)
## SET - 4
### Metryki
-  Precision : 0.0826   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.8289   (ile phishingów zostało wykrytych)
-  F1        : 0.1503
-  FPR       : 0.5146   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 169315 / 524187 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=1,040,321  F1=0.1114
-  [ 50–100 znaków]  n=  8,022  F1=0.8813
-  [100–150 znaków]  n=  1,852  F1=0.9682
-  [150–200 znaków]  n=  4,925  F1=0.9950
-  [200–999 znaków]  n=    770  F1=0.9283

### Rozkład predykcji
-  [0.0–0.1]  n= 105,665  acc=0.966  ████
-  [0.1–0.2]  n= 116,250  acc=0.977  ████
-  [0.2–0.3]  n= 104,920  acc=0.986  ███
-  [0.3–0.4]  n=  98,040  acc=0.990  ███
-  [0.4–0.5]  n=  70,078  acc=0.988  ██
-  [0.5–0.6]  n=  63,060  acc=0.014  ██
-  [0.6–0.7]  n=  73,811  acc=0.017  ██
-  [0.7–0.8]  n=  93,923  acc=0.063  ███
-  [0.8–0.9]  n= 130,025  acc=0.031  ████
-  [0.9–1.0]  n= 200,144  acc=0.172  ███████

### Top 10 domen w błędach (Domena | Model | Prawda)
      94×  qr-codes.io                         | Model: Legit (0)    | Prawda: Phishing (1)
      87×  flowcode.com                        | Model: Legit (0)    | Prawda: Phishing (1)
      74×  linkin.bio                          | Model: Legit (0)    | Prawda: Phishing (1)
      54×  us2.campaign-archive.com            | Model: Legit (0)    | Prawda: Phishing (1)
      53×  us6.campaign-archive.com            | Model: Legit (0)    | Prawda: Phishing (1)
      46×  storage.cloud.google.com            | Model: Legit (0)    | Prawda: Phishing (1)
      45×  us4.campaign-archive.com            | Model: Legit (0)    | Prawda: Phishing (1)
      43×  us20.campaign-archive.com           | Model: Legit (0)    | Prawda: Phishing (1)
      43×  us9.campaign-archive.com            | Model: Legit (0)    | Prawda: Phishing (1)
      43×  us15.campaign-archive.com           | Model: Legit (0)    | Prawda: Phishing (1)


## SET - 1
### Metryki
-  Precision : 0.9577   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.9148   (ile phishingów zostało wykrytych)
-  F1        : 0.9358
-  FPR       : 0.0114   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 2650 / 12240 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=282,101  F1=0.9041
-  [ 50–100 znaków]  n=136,470  F1=0.9801
-  [100–150 znaków]  n= 17,188  F1=0.9808
-  [150–200 znaków]  n=  3,694  F1=0.9892
-  [200–999 znaków]  n=  3,727  F1=0.9943

### Rozkład predykcji
-  [0.0–0.1]  n= 321,495  acc=0.994  █████████████████████████████
-  [0.1–0.2]  n=  15,312  acc=0.878  █
-  [0.2–0.3]  n=   6,651  acc=0.751  
-  [0.3–0.4]  n=   3,903  acc=0.608  
-  [0.4–0.5]  n=   2,730  acc=0.502  
-  [0.5–0.6]  n=   2,444  acc=0.609  
-  [0.6–0.7]  n=   2,720  acc=0.715  
-  [0.7–0.8]  n=   3,723  acc=0.814  
-  [0.8–0.9]  n=   7,705  acc=0.901  
-  [0.9–1.0]  n=  76,521  acc=0.990  ██████

### Top 10 domen w błędach (Domena | Model | Prawda)
     126×  twitter.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      36×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
      16×  httpss:                             | Model: Phishing (1) | Prawda: Legit (0)
      14×  ckuik.com                           | Model: Phishing (1) | Prawda: Legit (0)
      12×  angelfire.com                       | Model: Legit (0)    | Prawda: Phishing (1)
      12×  zip.net                             | Model: Legit (0)    | Prawda: Phishing (1)
      11×  ow.ly                               | Model: Phishing (1) | Prawda: Legit (0)
      10×  twitter.com                         | Model: Phishing (1) | Prawda: Legit (0)
       9×  forms.office.com                    | Model: Legit (0)    | Prawda: Phishing (1)
       8×  pastebin.com                        | Model: Phishing (1) | Prawda: Legit (0)


## SET - 2
### Metryki
-  Precision : 0.9707   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.8594   (ile phishingów zostało wykrytych)
-  F1        : 0.9117
-  FPR       : 0.0114   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 6260 / 25268 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=314,244  F1=0.8775
-  [ 50–100 znaków]  n=152,865  F1=0.9546
-  [100–150 znaków]  n= 18,789  F1=0.9522
-  [150–200 znaków]  n=  7,058  F1=0.9906
-  [200–999 znaków]  n=  4,461  F1=0.9874

### Rozkład predykcji
-  [0.0–0.1]  n= 325,104  acc=0.983  ██████████████████████████
-  [0.1–0.2]  n=  18,833  acc=0.714  █
-  [0.2–0.3]  n=   9,483  acc=0.527  
-  [0.3–0.4]  n=   5,546  acc=0.428  
-  [0.4–0.5]  n=   4,153  acc=0.330  
-  [0.5–0.6]  n=   4,168  acc=0.771  
-  [0.6–0.7]  n=   4,782  acc=0.838  
-  [0.7–0.8]  n=   7,077  acc=0.902  
-  [0.8–0.9]  n=  15,134  acc=0.950  █
-  [0.9–1.0]  n= 103,183  acc=0.993  ████████

### Top 10 domen w błędach (Domena | Model | Prawda)
     492×  cloudflare-ipfs.com                 | Model: Legit (0)    | Prawda: Phishing (1)
     316×  cf-ipfs.com                         | Model: Legit (0)    | Prawda: Phishing (1)
     162×  ipfs.eth.aragon.network             | Model: Legit (0)    | Prawda: Phishing (1)
     126×  twitter.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      91×  flowcode.com                        | Model: Legit (0)    | Prawda: Phishing (1)
      45×  storage.cloud.google.com            | Model: Legit (0)    | Prawda: Phishing (1)
      36×  ipfs.io                             | Model: Legit (0)    | Prawda: Phishing (1)
      36×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
      34×  cakeresume.com                      | Model: Legit (0)    | Prawda: Phishing (1)
      27×  docs.google.com                     | Model: Legit (0)    | Prawda: Phishing (1)


## SET - 3
### Metryki
-  Precision : 0.9426   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.7833   (ile phishingów zostało wykrytych)
-  F1        : 0.8556
-  FPR       : 0.0411   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 26256 / 97337 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=570,056  F1=0.8276
-  [ 50–100 znaków]  n=182,694  F1=0.9312
-  [100–150 znaków]  n= 25,912  F1=0.9656
-  [150–200 znaków]  n=  6,871  F1=0.9729
-  [200–999 znaków]  n=  9,325  F1=0.9837

### Rozkład predykcji
-  [0.0–0.1]  n= 389,915  acc=0.949  ███████████████████
-  [0.1–0.2]  n=  37,951  acc=0.530  █
-  [0.2–0.3]  n=  28,067  acc=0.401  █
-  [0.3–0.4]  n=  17,903  acc=0.259  
-  [0.4–0.5]  n=  15,232  acc=0.211  
-  [0.5–0.6]  n=  14,364  acc=0.818  
-  [0.6–0.7]  n=  21,522  acc=0.887  █
-  [0.7–0.8]  n=  23,995  acc=0.891  █
-  [0.8–0.9]  n=  41,529  acc=0.916  ██
-  [0.9–1.0]  n= 204,468  acc=0.969  ██████████

### Top 10 domen w błędach (Domena | Model | Prawda)
     214×  webring.com                         | Model: Phishing (1) | Prawda: Legit (0)
     169×  villakidsbuffetinfantil.com         | Model: Legit (0)    | Prawda: Phishing (1)
     169×  angelfire.com                       | Model: Phishing (1) | Prawda: Legit (0)
     139×  home.comcast.net                    | Model: Legit (0)    | Prawda: Phishing (1)
     115×  twitter.com                         | Model: Legit (0)    | Prawda: Phishing (1)
     114×  freewebs.com                        | Model: Phishing (1) | Prawda: Legit (0)
     104×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
      78×  ddj.com                             | Model: Phishing (1) | Prawda: Legit (0)
      72×  painterspaintings.com               | Model: Legit (0)    | Prawda: Phishing (1)
      61×  s.yam.com                           | Model: Legit (0)    | Prawda: Phishing (1)


# MLP (NLP-FtIDF + Cechy)
## SET - 4
### Metryki
-  Precision : 0.1319   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.8357   (ile phishingów zostało wykrytych)
-  F1        : 0.2279
-  FPR       : 0.3075   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 97839 / 316655 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=1,040,321  F1=0.1775
-  [ 50–100 znaków]  n=  8,022  F1=0.8971
-  [100–150 znaków]  n=  1,852  F1=0.9192
-  [150–200 znaków]  n=  4,925  F1=0.9002
-  [200–999 znaków]  n=    770  F1=0.9566

### Rozkład predykcji
-  [0.0–0.1]  n= 273,242  acc=0.985  ██████████
-  [0.1–0.2]  n= 163,923  acc=0.986  ██████
-  [0.2–0.3]  n= 135,166  acc=0.988  █████
-  [0.3–0.4]  n=  73,101  acc=0.992  ██
-  [0.4–0.5]  n=  56,283  acc=0.990  ██
-  [0.5–0.6]  n=  52,244  acc=0.012  █
-  [0.6–0.7]  n=  51,012  acc=0.016  █
-  [0.7–0.8]  n=  55,055  acc=0.024  ██
-  [0.8–0.9]  n=  61,855  acc=0.061  ██
-  [0.9–1.0]  n= 134,035  acc=0.300  █████

### Top 10 domen w błędach (Domena | Model | Prawda)
    1,081×  docs.google.com                     | Model: Legit (0)    | Prawda: Phishing (1)
      93×  qr-codes.io                         | Model: Legit (0)    | Prawda: Phishing (1)
      92×  flowcode.com                        | Model: Legit (0)    | Prawda: Phishing (1)
      53×  us6.campaign-archive.com            | Model: Legit (0)    | Prawda: Phishing (1)
      52×  us2.campaign-archive.com            | Model: Legit (0)    | Prawda: Phishing (1)
      45×  us4.campaign-archive.com            | Model: Legit (0)    | Prawda: Phishing (1)
      43×  us20.campaign-archive.com           | Model: Legit (0)    | Prawda: Phishing (1)
      43×  us15.campaign-archive.com           | Model: Legit (0)    | Prawda: Phishing (1)
      42×  us11.campaign-archive.com           | Model: Legit (0)    | Prawda: Phishing (1)
      41×  us10.campaign-archive.com           | Model: Legit (0)    | Prawda: Phishing (1)


## SET - 1
### Metryki
-  Precision : 0.9654   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.9543   (ile phishingów zostało wykrytych)
-  F1        : 0.9598
-  FPR       : 0.0096   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 2328 / 7784 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=282,101  F1=0.9417
-  [ 50–100 znaków]  n=136,470  F1=0.9853
-  [100–150 znaków]  n= 17,188  F1=0.9872
-  [150–200 znaków]  n=  3,694  F1=0.9904
-  [200–999 znaków]  n=  3,727  F1=0.9960

### Rozkład predykcji
-  [0.0–0.1]  n= 332,381  acc=0.995  █████████████████████████████
-  [0.1–0.2]  n=   7,792  acc=0.887  
-  [0.2–0.3]  n=   3,274  acc=0.774  
-  [0.3–0.4]  n=   1,927  acc=0.679  
-  [0.4–0.5]  n=   1,481  acc=0.554  
-  [0.5–0.6]  n=   1,434  acc=0.517  
-  [0.6–0.7]  n=   1,593  acc=0.628  
-  [0.7–0.8]  n=   2,370  acc=0.740  
-  [0.8–0.9]  n=   4,651  acc=0.860  
-  [0.9–1.0]  n=  86,301  acc=0.991  ███████

### Top 10 domen w błędach (Domena | Model | Prawda)
      65×  twitter.com                         | Model: Phishing (1) | Prawda: Legit (0)
      41×  twitter.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      25×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
      21×  httpss:                             | Model: Phishing (1) | Prawda: Legit (0)
      13×  angelfire.com                       | Model: Legit (0)    | Prawda: Phishing (1)
      12×  ckuik.com                           | Model: Phishing (1) | Prawda: Legit (0)
      11×  ow.ly                               | Model: Phishing (1) | Prawda: Legit (0)
      10×  pastebin.com                        | Model: Phishing (1) | Prawda: Legit (0)
       8×  letras.terra.com.br                 | Model: Phishing (1) | Prawda: Legit (0)
       8×  lazygirls.info                      | Model: Phishing (1) | Prawda: Legit (0)


## SET - 2
### Metryki
-  Precision : 0.9762   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.8999   (ile phishingów zostało wykrytych)
-  F1        : 0.9365
-  FPR       : 0.0096   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 7163 / 18517 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=314,244  F1=0.9231
-  [ 50–100 znaków]  n=152,865  F1=0.9578
-  [100–150 znaków]  n= 18,789  F1=0.9608
-  [150–200 znaków]  n=  7,058  F1=0.9111
-  [200–999 znaków]  n=  4,461  F1=0.9911

### Rozkład predykcji
-  [0.0–0.1]  n= 337,216  acc=0.981  ███████████████████████████
-  [0.1–0.2]  n=  10,038  acc=0.688  
-  [0.2–0.3]  n=   4,850  acc=0.523  
-  [0.3–0.4]  n=   2,943  acc=0.444  
-  [0.4–0.5]  n=   2,541  acc=0.323  
-  [0.5–0.6]  n=   2,482  acc=0.721  
-  [0.6–0.7]  n=   3,467  acc=0.829  
-  [0.7–0.8]  n=   5,321  acc=0.884  
-  [0.8–0.9]  n=  10,749  acc=0.939  
-  [0.9–1.0]  n= 117,856  acc=0.993  █████████

### Top 10 domen w błędach (Domena | Model | Prawda)
    1,089×  cloudflare-ipfs.com                 | Model: Legit (0)    | Prawda: Phishing (1)
     891×  docs.google.com                     | Model: Legit (0)    | Prawda: Phishing (1)
     321×  cf-ipfs.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      97×  flowcode.com                        | Model: Legit (0)    | Prawda: Phishing (1)
      83×  ipfs.eth.aragon.network             | Model: Legit (0)    | Prawda: Phishing (1)
      65×  twitter.com                         | Model: Phishing (1) | Prawda: Legit (0)
      41×  twitter.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      35×  cakeresume.com                      | Model: Legit (0)    | Prawda: Phishing (1)
      26×  storage.cloud.google.com            | Model: Legit (0)    | Prawda: Phishing (1)
      25×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)


## SET - 3
### Metryki
-  Precision : 0.9283   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.7642   (ile phishingów zostało wykrytych)
-  F1        : 0.8383
-  FPR       : 0.0509   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 42271 / 108531 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=570,056  F1=0.8009
-  [ 50–100 znaków]  n=182,694  F1=0.9418
-  [100–150 znaków]  n= 25,912  F1=0.9774
-  [150–200 znaków]  n=  6,871  F1=0.9811
-  [200–999 znaków]  n=  9,325  F1=0.9904

### Rozkład predykcji
-  [0.0–0.1]  n= 416,600  acc=0.918  ████████████████████
-  [0.1–0.2]  n=  31,307  acc=0.380  █
-  [0.2–0.3]  n=  19,908  acc=0.271  █
-  [0.3–0.4]  n=  13,032  acc=0.241  
-  [0.4–0.5]  n=  11,059  acc=0.222  
-  [0.5–0.6]  n=  10,114  acc=0.794  
-  [0.6–0.7]  n=  14,332  acc=0.845  
-  [0.7–0.8]  n=  18,989  acc=0.695  
-  [0.8–0.9]  n=  27,465  acc=0.864  █
-  [0.9–1.0]  n= 232,140  acc=0.966  ███████████

### Top 10 domen w błędach (Domena | Model | Prawda)
    3,189×  tools.ietf.org                      | Model: Phishing (1) | Prawda: Legit (0)
     782×  pastehtml.com                       | Model: Legit (0)    | Prawda: Phishing (1)
     282×  babinet.cz                          | Model: Legit (0)    | Prawda: Phishing (1)
     168×  villakidsbuffetinfantil.com         | Model: Legit (0)    | Prawda: Phishing (1)
     162×  webring.com                         | Model: Phishing (1) | Prawda: Legit (0)
     105×  home.comcast.net                    | Model: Legit (0)    | Prawda: Phishing (1)
      84×  twitter.com                         | Model: Phishing (1) | Prawda: Legit (0)
      84×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
      79×  angelfire.com                       | Model: Phishing (1) | Prawda: Legit (0)
      72×  painterspaintings.com               | Model: Legit (0)    | Prawda: Phishing (1)

