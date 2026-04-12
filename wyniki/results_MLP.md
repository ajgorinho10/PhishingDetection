# MLP (NLP-TfIDF + Cechy):
## SET - 1
### Metryki
-  Precision : 0.9644   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.9305   (ile phishingów zostało wykrytych)
-  F1        : 0.9471
-  FPR       : 0.0097   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 113 / 10127 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=282,101  F1=0.9219
-  [ 50–100 znaków]  n=136,470  F1=0.9816
-  [100–150 znaków]  n= 17,188  F1=0.9851
-  [150–200 znaków]  n=  3,694  F1=0.9900
-  [200–999 znaków]  n=  3,727  F1=0.9958

### Rozkład predykcji
-  [0.0–0.1]  n= 220,651  acc=1.000  ███████████████████
-  [0.1–0.2]  n=  67,180  acc=0.992  ██████
-  [0.2–0.3]  n=  40,279  acc=0.964  ███
-  [0.3–0.4]  n=  14,629  acc=0.859  █
-  [0.4–0.5]  n=   6,415  acc=0.584  
-  [0.5–0.6]  n=   4,713  acc=0.630  
-  [0.6–0.7]  n=   6,937  acc=0.869  
-  [0.7–0.8]  n=  12,442  acc=0.960  █
-  [0.8–0.9]  n=  19,177  acc=0.991  █
-  [0.9–1.0]  n=  50,781  acc=0.999  ████

### Top 10 domen w błędach (Domena | Model | Prawda)
      98×  twitter.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      24×  twitter.com                         | Model: Phishing (1) | Prawda: Legit (0)
      22×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
      20×  httpss:                             | Model: Phishing (1) | Prawda: Legit (0)
      16×  ckuik.com                           | Model: Phishing (1) | Prawda: Legit (0)
      11×  ow.ly                               | Model: Phishing (1) | Prawda: Legit (0)
      11×  angelfire.com                       | Model: Legit (0)    | Prawda: Phishing (1)
       8×  letras.terra.com.br                 | Model: Phishing (1) | Prawda: Legit (0)
       8×  pastebin.com                        | Model: Phishing (1) | Prawda: Legit (0)
       7×  ioffer.com                          | Model: Phishing (1) | Prawda: Legit (0)


## SET - 2
### Metryki
-  Precision : 0.9765   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.9164   (ile phishingów zostało wykrytych)
-  F1        : 0.9455
-  FPR       : 0.0097   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 180 / 16029 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=314,244  F1=0.9236
-  [ 50–100 znaków]  n=152,865  F1=0.9754
-  [100–150 znaków]  n= 18,789  F1=0.9638
-  [150–200 znaków]  n=  7,058  F1=0.9944
-  [200–999 znaków]  n=  4,461  F1=0.9926

### Rozkład predykcji
-  [0.0–0.1]  n= 220,719  acc=0.999  █████████████████
-  [0.1–0.2]  n=  68,037  acc=0.980  █████
-  [0.2–0.3]  n=  41,861  acc=0.928  ███
-  [0.3–0.4]  n=  16,407  acc=0.766  █
-  [0.4–0.5]  n=   8,034  acc=0.467  
-  [0.5–0.6]  n=   7,168  acc=0.757  
-  [0.6–0.7]  n=  11,667  acc=0.922  
-  [0.7–0.8]  n=  18,940  acc=0.974  █
-  [0.8–0.9]  n=  25,109  acc=0.993  ██
-  [0.9–1.0]  n=  79,521  acc=1.000  ██████

### Top 10 domen w błędach (Domena | Model | Prawda)
     701×  cloudflare-ipfs.com                 | Model: Legit (0)    | Prawda: Phishing (1)
     184×  cf-ipfs.com                         | Model: Legit (0)    | Prawda: Phishing (1)
     149×  ipfs.eth.aragon.network             | Model: Legit (0)    | Prawda: Phishing (1)
      98×  twitter.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      24×  twitter.com                         | Model: Phishing (1) | Prawda: Legit (0)
      22×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
      20×  httpss:                             | Model: Phishing (1) | Prawda: Legit (0)
      16×  ckuik.com                           | Model: Phishing (1) | Prawda: Legit (0)
      13×  flipsnack.com                       | Model: Legit (0)    | Prawda: Phishing (1)
      11×  ow.ly                               | Model: Phishing (1) | Prawda: Legit (0)


## SET - 3
### Metryki
-  Precision : 0.9230   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.6601   (ile phishingów zostało wykrytych)
-  F1        : 0.7697
-  FPR       : 0.0475   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 4361 / 145380 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=570,056  F1=0.7056
-  [ 50–100 znaków]  n=182,694  F1=0.9400
-  [100–150 znaków]  n= 25,912  F1=0.9753
-  [150–200 znaków]  n=  6,871  F1=0.9834
-  [200–999 znaków]  n=  9,325  F1=0.9916

### Rozkład predykcji
-  [0.0–0.1]  n= 242,105  acc=0.986  ████████████
-  [0.1–0.2]  n= 114,892  acc=0.714  █████
-  [0.2–0.3]  n=  87,388  acc=0.592  ████
-  [0.3–0.4]  n=  55,077  acc=0.446  ██
-  [0.4–0.5]  n=  32,223  acc=0.299  █
-  [0.5–0.6]  n=  26,954  acc=0.757  █
-  [0.6–0.7]  n=  36,039  acc=0.846  █
-  [0.7–0.8]  n=  45,155  acc=0.897  ██
-  [0.8–0.9]  n=  49,213  acc=0.948  ██
-  [0.9–1.0]  n= 105,900  acc=0.991  █████

### Top 10 domen w błędach (Domena | Model | Prawda)
     750×  pastehtml.com                       | Model: Legit (0)    | Prawda: Phishing (1)
     292×  babinet.cz                          | Model: Legit (0)    | Prawda: Phishing (1)
     177×  webring.com                         | Model: Phishing (1) | Prawda: Legit (0)
     166×  villakidsbuffetinfantil.com         | Model: Legit (0)    | Prawda: Phishing (1)
     131×  angelfire.com                       | Model: Phishing (1) | Prawda: Legit (0)
     108×  home.comcast.net                    | Model: Legit (0)    | Prawda: Phishing (1)
     108×  ddj.com                             | Model: Phishing (1) | Prawda: Legit (0)
      87×  twitter.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      76×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
      69×  painterspaintings.com               | Model: Legit (0)    | Prawda: Phishing (1)


## SET - 4
### Metryki
-  Precision : 0.9762   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.9440   (ile phishingów zostało wykrytych)
-  F1        : 0.9598
-  FPR       : 0.0080   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 127 / 12141 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=420,725  F1=0.9443
-  [ 50–100 znaków]  n=144,404  F1=0.9844
-  [100–150 znaków]  n= 19,044  F1=0.9875
-  [150–200 znaków]  n=  8,626  F1=0.9967
-  [200–999 znaków]  n=  4,487  F1=0.9955

### Rozkład predykcji
-  [0.0–0.1]  n= 232,453  acc=1.000  ███████████████
-  [0.1–0.2]  n= 122,689  acc=0.994  ████████
-  [0.2–0.3]  n=  65,407  acc=0.969  ████
-  [0.3–0.4]  n=  19,138  acc=0.861  █
-  [0.4–0.5]  n=   9,121  acc=0.657  
-  [0.5–0.6]  n=   5,453  acc=0.661  
-  [0.6–0.7]  n=   8,060  acc=0.881  
-  [0.7–0.8]  n=  15,078  acc=0.965  █
-  [0.8–0.9]  n=  25,574  acc=0.993  █
-  [0.9–1.0]  n=  94,362  acc=1.000  ██████

### Top 10 domen w błędach (Domena | Model | Prawda)
      98×  twitter.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      24×  twitter.com                         | Model: Phishing (1) | Prawda: Legit (0)
      22×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
      20×  httpss:                             | Model: Phishing (1) | Prawda: Legit (0)
      16×  ckuik.com                           | Model: Phishing (1) | Prawda: Legit (0)
      12×  ow.ly                               | Model: Phishing (1) | Prawda: Legit (0)
      11×  angelfire.com                       | Model: Legit (0)    | Prawda: Phishing (1)
       8×  vk.com                              | Model: Legit (0)    | Prawda: Phishing (1)
       8×  letras.terra.com.br                 | Model: Phishing (1) | Prawda: Legit (0)
       8×  pastebin.com                        | Model: Phishing (1) | Prawda: Legit (0)


# MLP (NLP-TfIDF):
## SET - 1
### Metryki
-  Precision : 0.9603   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.8475   (ile phishingów zostało wykrytych)
-  F1        : 0.9004
-  FPR       : 0.0099   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 141 / 18277 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=282,101  F1=0.8451
-  [ 50–100 znaków]  n=136,470  F1=0.9731
-  [100–150 znaków]  n= 17,188  F1=0.9761
-  [150–200 znaków]  n=  3,694  F1=0.9883
-  [200–999 znaków]  n=  3,727  F1=0.9943

### Rozkład predykcji
-  [0.0–0.1]  n= 202,967  acc=0.999  ██████████████████
-  [0.1–0.2]  n=  69,716  acc=0.990  ██████
-  [0.2–0.3]  n=  46,115  acc=0.948  ████
-  [0.3–0.4]  n=  26,383  acc=0.789  ██
-  [0.4–0.5]  n=  12,003  acc=0.492  █
-  [0.5–0.6]  n=   8,793  acc=0.747  
-  [0.6–0.7]  n=   9,902  acc=0.922  
-  [0.7–0.8]  n=  13,813  acc=0.977  █
-  [0.8–0.9]  n=  18,182  acc=0.996  █
-  [0.9–1.0]  n=  35,330  acc=1.000  ███

### Top 10 domen w błędach (Domena | Model | Prawda)
     136×  twitter.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      35×  sites.google.com                    | Model: Legit (0)    | Prawda: Phishing (1)
      33×  ckuik.com                           | Model: Phishing (1) | Prawda: Legit (0)
      23×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
      20×  182.92.184.208:8806                 | Model: Legit (0)    | Prawda: Phishing (1)
      19×  httpss:                             | Model: Phishing (1) | Prawda: Legit (0)
      18×  partyeazy.com                       | Model: Legit (0)    | Prawda: Phishing (1)
      17×  lihi.cc                             | Model: Legit (0)    | Prawda: Phishing (1)
      16×  gg.gg                               | Model: Legit (0)    | Prawda: Phishing (1)
      15×  cpc.cx                              | Model: Legit (0)    | Prawda: Phishing (1)


## SET - 2
### Metryki
-  Precision : 0.9732   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.8152   (ile phishingów zostało wykrytych)
-  F1        : 0.8872
-  FPR       : 0.0099   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 271 / 31450 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=314,244  F1=0.8512
-  [ 50–100 znaków]  n=152,865  F1=0.9242
-  [100–150 znaków]  n= 18,789  F1=0.9405
-  [150–200 znaków]  n=  7,058  F1=0.9931
-  [200–999 znaków]  n=  4,461  F1=0.9915

### Rozkład predykcji
-  [0.0–0.1]  n= 203,097  acc=0.999  ████████████████
-  [0.1–0.2]  n=  70,521  acc=0.979  █████
-  [0.2–0.3]  n=  49,563  acc=0.882  ███
-  [0.3–0.4]  n=  30,833  acc=0.675  ██
-  [0.4–0.5]  n=  16,345  acc=0.362  █
-  [0.5–0.6]  n=  11,554  acc=0.807  
-  [0.6–0.7]  n=  15,423  acc=0.950  █
-  [0.7–0.8]  n=  20,369  acc=0.984  █
-  [0.8–0.9]  n=  25,865  acc=0.997  ██
-  [0.9–1.0]  n=  53,893  acc=1.000  ████

### Top 10 domen w błędach (Domena | Model | Prawda)
   2,013×  ipfs.eth.aragon.network             | Model: Legit (0)    | Prawda: Phishing (1)
     560×  cloudflare-ipfs.com                 | Model: Legit (0)    | Prawda: Phishing (1)
     313×  cf-ipfs.com                         | Model: Legit (0)    | Prawda: Phishing (1)
     195×  shorturl.at                         | Model: Legit (0)    | Prawda: Phishing (1)
     136×  twitter.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      83×  nftstorage.link                     | Model: Legit (0)    | Prawda: Phishing (1)
      43×  jemi.so                             | Model: Legit (0)    | Prawda: Phishing (1)
      41×  s.free.fr                           | Model: Legit (0)    | Prawda: Phishing (1)
      35×  sites.google.com                    | Model: Legit (0)    | Prawda: Phishing (1)
      35×  taplink.cc                          | Model: Legit (0)    | Prawda: Phishing (1)


## SET - 3
### Metryki
-  Precision : 0.9180   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.5146   (ile phishingów zostało wykrytych)
-  F1        : 0.6595
-  FPR       : 0.0396   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 6678 / 195575 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=570,056  F1=0.5528
-  [ 50–100 znaków]  n=182,694  F1=0.9174
-  [100–150 znaków]  n= 25,912  F1=0.9645
-  [150–200 znaków]  n=  6,871  F1=0.9728
-  [200–999 znaków]  n=  9,325  F1=0.9889

### Rozkład predykcji
-  [0.0–0.1]  n= 225,297  acc=0.972  ███████████
-  [0.1–0.2]  n= 113,564  acc=0.737  █████
-  [0.2–0.3]  n= 109,506  acc=0.572  █████
-  [0.3–0.4]  n=  87,413  acc=0.368  ████
-  [0.4–0.5]  n=  52,816  acc=0.237  ██
-  [0.5–0.6]  n=  39,050  acc=0.805  █
-  [0.6–0.7]  n=  32,355  acc=0.855  █
-  [0.7–0.8]  n=  35,683  acc=0.917  █
-  [0.8–0.9]  n=  39,293  acc=0.968  █
-  [0.9–1.0]  n=  59,969  acc=0.994  ███

### Top 10 domen w błędach (Domena | Model | Prawda)
     931×  pastehtml.com                       | Model: Legit (0)    | Prawda: Phishing (1)
     281×  babinet.cz                          | Model: Legit (0)    | Prawda: Phishing (1)
     212×  webring.com                         | Model: Phishing (1) | Prawda: Legit (0)
     167×  angelfire.com                       | Model: Phishing (1) | Prawda: Legit (0)
     130×  home.comcast.net                    | Model: Legit (0)    | Prawda: Phishing (1)
     125×  twitter.com                         | Model: Legit (0)    | Prawda: Phishing (1)
     112×  ddj.com                             | Model: Phishing (1) | Prawda: Legit (0)
      90×  x.co                                | Model: Legit (0)    | Prawda: Phishing (1)
      72×  painterspaintings.com               | Model: Legit (0)    | Prawda: Phishing (1)
      67×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)


## SET - 4
### Metryki
-  Precision : 0.9704   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.8824   (ile phishingów zostało wykrytych)
-  F1        : 0.9243
-  FPR       : 0.0093   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 168 / 22193 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=420,725  F1=0.8913
-  [ 50–100 znaków]  n=144,404  F1=0.9764
-  [100–150 znaków]  n= 19,044  F1=0.9803
-  [150–200 znaków]  n=  8,626  F1=0.9960
-  [200–999 znaków]  n=  4,487  F1=0.9933

### Rozkład predykcji
-  [0.0–0.1]  n= 217,111  acc=0.999  ██████████████
-  [0.1–0.2]  n= 111,267  acc=0.992  ███████
-  [0.2–0.3]  n=  71,578  acc=0.958  ████
-  [0.3–0.4]  n=  40,382  acc=0.832  ██
-  [0.4–0.5]  n=  17,344  acc=0.582  █
-  [0.5–0.6]  n=  10,579  acc=0.744  
-  [0.6–0.7]  n=  12,368  acc=0.923  
-  [0.7–0.8]  n=  19,713  acc=0.982  █
-  [0.8–0.9]  n=  26,219  acc=0.996  █
-  [0.9–1.0]  n=  70,774  acc=1.000  ████

### Top 10 domen w błędach (Domena | Model | Prawda)
     136×  twitter.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      47×  urlz.fr                             | Model: Legit (0)    | Prawda: Phishing (1)
      37×  sites.google.com                    | Model: Legit (0)    | Prawda: Phishing (1)
      33×  ckuik.com                           | Model: Phishing (1) | Prawda: Legit (0)
      26×  tr.ee                               | Model: Legit (0)    | Prawda: Phishing (1)
      23×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
      20×  182.92.184.208:8806                 | Model: Legit (0)    | Prawda: Phishing (1)
      19×  httpss:                             | Model: Phishing (1) | Prawda: Legit (0)
      18×  partyeazy.com                       | Model: Legit (0)    | Prawda: Phishing (1)
      18×  lihi.cc                             | Model: Legit (0)    | Prawda: Phishing (1)
