# LSTM (NLP + Cechy):
## SET - 1
### Metryki
-  Precision : 0.9790   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.9578   (ile phishingów zostało wykrytych)
-  F1        : 0.9683
-  FPR       : 0.0058   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 2340 / 6121 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=282,101  F1=0.9522
-  [ 50–100 znaków]  n=136,470  F1=0.9902
-  [100–150 znaków]  n= 17,188  F1=0.9942
-  [150–200 znaków]  n=  3,694  F1=0.9969
-  [200–999 znaków]  n=  3,727  F1=0.9972

### Rozkład predykcji
-  [0.0–0.1]  n= 337,367  acc=0.995  ██████████████████████████████
-  [0.1–0.2]  n=   5,579  acc=0.864  
-  [0.2–0.3]  n=   2,296  acc=0.770  
-  [0.3–0.4]  n=   1,432  acc=0.659  
-  [0.4–0.5]  n=   1,166  acc=0.559  
-  [0.5–0.6]  n=   1,059  acc=0.573  
-  [0.6–0.7]  n=   1,106  acc=0.665  
-  [0.7–0.8]  n=   1,512  acc=0.763  
-  [0.8–0.9]  n=   2,359  acc=0.868  
-  [0.9–1.0]  n=  89,328  acc=0.994  ████████

### Top 10 domen w błędach (Domena | Model | Prawda)
      30×  twitter.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      21×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
      12×  angelfire.com                       | Model: Legit (0)    | Prawda: Phishing (1)
      10×  twitter.com                         | Model: Phishing (1) | Prawda: Legit (0)
       8×  vk.com                              | Model: Legit (0)    | Prawda: Phishing (1)
       7×  hulkshare.com                       | Model: Phishing (1) | Prawda: Legit (0)
       7×  duniaflowmeter.com                  | Model: Legit (0)    | Prawda: Phishing (1)
       6×  oocities.org                        | Model: Legit (0)    | Prawda: Phishing (1)
       5×  pastebin.com                        | Model: Phishing (1) | Prawda: Legit (0)
       5×  sites.google.com                    | Model: Legit (0)    | Prawda: Phishing (1)


## SET - 2
### Metryki
-  Precision : 0.9860   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.9288   (ile phishingów zostało wykrytych)
-  F1        : 0.9565
-  FPR       : 0.0058   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 5471 / 12813 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=314,244  F1=0.9327
-  [ 50–100 znaków]  n=152,865  F1=0.9885
-  [100–150 znaków]  n= 18,789  F1=0.9917
-  [150–200 znaków]  n=  7,058  F1=0.9977
-  [200–999 znaków]  n=  4,461  F1=0.9968

### Rozkład predykcji
-  [0.0–0.1]  n= 340,498  acc=0.985  ███████████████████████████
-  [0.1–0.2]  n=   6,902  acc=0.699  
-  [0.2–0.3]  n=   3,172  acc=0.557  
-  [0.3–0.4]  n=   2,097  acc=0.450  
-  [0.4–0.5]  n=   1,861  acc=0.350  
-  [0.5–0.6]  n=   1,789  acc=0.747  
-  [0.6–0.7]  n=   2,080  acc=0.822  
-  [0.7–0.8]  n=   2,758  acc=0.870  
-  [0.8–0.9]  n=   4,713  acc=0.934  
-  [0.9–1.0]  n= 131,593  acc=0.996  ██████████

### Top 10 domen w błędach (Domena | Model | Prawda)
      91×  flowcode.com                        | Model: Legit (0)    | Prawda: Phishing (1)
      42×  cakeresume.com                      | Model: Legit (0)    | Prawda: Phishing (1)
      36×  rp.mockplus.com                     | Model: Legit (0)    | Prawda: Phishing (1)
      30×  twitter.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      29×  sites.google.com                    | Model: Legit (0)    | Prawda: Phishing (1)
      21×  indd.adobe.com                      | Model: Legit (0)    | Prawda: Phishing (1)
      21×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
      17×  jemi.so                             | Model: Legit (0)    | Prawda: Phishing (1)
      15×  flow.page                           | Model: Legit (0)    | Prawda: Phishing (1)
      13×  klrn.wpenginepowered.com            | Model: Legit (0)    | Prawda: Phishing (1)


## SET - 3
### Metryki
-  Precision : 0.9566   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.8065   (ile phishingów zostało wykrytych)
-  F1        : 0.8752
-  FPR       : 0.0315   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 28399 / 84677 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=570,056  F1=0.8448
-  [ 50–100 znaków]  n=182,694  F1=0.9614
-  [100–150 znaków]  n= 25,912  F1=0.9827
-  [150–200 znaków]  n=  6,871  F1=0.9892
-  [200–999 znaków]  n=  9,325  F1=0.9945

### Rozkład predykcji
-  [0.0–0.1]  n= 419,020  acc=0.948  █████████████████████
-  [0.1–0.2]  n=  23,745  acc=0.351  █
-  [0.2–0.3]  n=  16,398  acc=0.221  
-  [0.3–0.4]  n=  13,509  acc=0.170  
-  [0.4–0.5]  n=  11,960  acc=0.152  
-  [0.5–0.6]  n=  10,822  acc=0.861  
-  [0.6–0.7]  n=  10,798  acc=0.860  
-  [0.7–0.8]  n=  12,679  acc=0.871  
-  [0.8–0.9]  n=  19,199  acc=0.891  
-  [0.9–1.0]  n= 256,816  acc=0.974  ████████████

### Top 10 domen w błędach (Domena | Model | Prawda)
     283×  pastehtml.com                       | Model: Legit (0)    | Prawda: Phishing (1)
     166×  angelfire.com                       | Model: Phishing (1) | Prawda: Legit (0)
     136×  home.comcast.net                    | Model: Legit (0)    | Prawda: Phishing (1)
     123×  s.yam.com                           | Model: Legit (0)    | Prawda: Phishing (1)
      82×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
      51×  fibtex.lodz.pl                      | Model: Phishing (1) | Prawda: Legit (0)
      47×  erlang.se                           | Model: Phishing (1) | Prawda: Legit (0)
      45×  linkedin.com                        | Model: Legit (0)    | Prawda: Phishing (1)
      43×  xs4all.nl                           | Model: Phishing (1) | Prawda: Legit (0)
      42×  pagesperso-orange.fr                | Model: Phishing (1) | Prawda: Legit (0)


## SET - 4
### Metryki
-  Precision : 0.1558   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.8816   (ile phishingów zostało wykrytych)
-  F1        : 0.2649
-  FPR       : 0.2670   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 81217 / 273626 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=1,040,321  F1=0.2037
-  [ 50–100 znaków]  n=  8,022  F1=0.9309
-  [100–150 znaków]  n=  1,852  F1=0.9768
-  [150–200 znaków]  n=  4,925  F1=0.9992
-  [200–999 znaków]  n=    770  F1=0.9941

### Rozkład predykcji
-  [0.0–0.1]  n= 218,387  acc=0.987  ████████
-  [0.1–0.2]  n= 185,170  acc=0.993  ███████
-  [0.2–0.3]  n= 141,395  acc=0.993  █████
-  [0.3–0.4]  n= 110,791  acc=0.993  ████
-  [0.4–0.5]  n=  83,873  acc=0.991  ███
-  [0.5–0.6]  n=  63,001  acc=0.012  ██
-  [0.6–0.7]  n=  48,303  acc=0.018  █
-  [0.7–0.8]  n=  40,570  acc=0.030  █
-  [0.8–0.9]  n=  41,770  acc=0.051  █
-  [0.9–1.0]  n= 122,656  acc=0.361  ████

### Top 10 domen w błędach (Domena | Model | Prawda)
     109×  eu.jotform.com                      | Model: Legit (0)    | Prawda: Phishing (1)
      92×  flowcode.com                        | Model: Legit (0)    | Prawda: Phishing (1)
      52×  us6.campaign-archive.com            | Model: Legit (0)    | Prawda: Phishing (1)
      52×  us2.campaign-archive.com            | Model: Legit (0)    | Prawda: Phishing (1)
      51×  l.ead.me                            | Model: Legit (0)    | Prawda: Phishing (1)
      50×  linqapp.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      44×  us4.campaign-archive.com            | Model: Legit (0)    | Prawda: Phishing (1)
      43×  us20.campaign-archive.com           | Model: Legit (0)    | Prawda: Phishing (1)
      41×  us9.campaign-archive.com            | Model: Legit (0)    | Prawda: Phishing (1)
      39×  us5.campaign-archive.com            | Model: Legit (0)    | Prawda: Phishing (1)


# LSTM (NLP)
## SET - 1
### Metryki
-  Precision : 0.9794   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.9368   (ile phishingów zostało wykrytych)
-  F1        : 0.9576
-  FPR       : 0.0056   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 2962 / 8082 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=282,101  F1=0.9376
-  [ 50–100 znaków]  n=136,470  F1=0.9840
-  [100–150 znaków]  n= 17,188  F1=0.9910
-  [150–200 znaków]  n=  3,694  F1=0.9946
-  [200–999 znaków]  n=  3,727  F1=0.9958

### Rozkład predykcji
-  [0.0–0.1]  n= 337,874  acc=0.993  ██████████████████████████████
-  [0.1–0.2]  n=   5,887  acc=0.819  
-  [0.2–0.3]  n=   2,824  acc=0.685  
-  [0.3–0.4]  n=   1,853  acc=0.547  
-  [0.4–0.5]  n=   1,533  acc=0.453  
-  [0.5–0.6]  n=   1,394  acc=0.679  
-  [0.6–0.7]  n=   1,468  acc=0.749  
-  [0.7–0.8]  n=   1,961  acc=0.827  
-  [0.8–0.9]  n=   3,215  acc=0.897  
-  [0.9–1.0]  n=  85,195  acc=0.995  ███████

### Top 10 domen w błędach (Domena | Model | Prawda)
      35×  sites.google.com                    | Model: Legit (0)    | Prawda: Phishing (1)
      26×  twitter.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      19×  twitter.com                         | Model: Phishing (1) | Prawda: Legit (0)
      15×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
      15×  worldpostjournal.com                | Model: Legit (0)    | Prawda: Phishing (1)
      11×  plus.google.com                     | Model: Legit (0)    | Prawda: Phishing (1)
      10×  angelfire.com                       | Model: Legit (0)    | Prawda: Phishing (1)
       9×  vk.com                              | Model: Legit (0)    | Prawda: Phishing (1)
       8×  justaskaron.com                     | Model: Legit (0)    | Prawda: Phishing (1)
       8×  borcuodeme.com                      | Model: Legit (0)    | Prawda: Phishing (1)


## SET - 2
### Metryki
-  Precision : 0.9860   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.8916   (ile phishingów zostało wykrytych)
-  F1        : 0.9364
-  FPR       : 0.0056   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 7775 / 18366 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=314,244  F1=0.9040
-  [ 50–100 znaków]  n=152,865  F1=0.9805
-  [100–150 znaków]  n= 18,789  F1=0.9875
-  [150–200 znaków]  n=  7,058  F1=0.9735
-  [200–999 znaków]  n=  4,461  F1=0.9957

### Rozkład predykcji
-  [0.0–0.1]  n= 342,687  acc=0.979  ███████████████████████████
-  [0.1–0.2]  n=   7,538  acc=0.640  
-  [0.2–0.3]  n=   4,001  acc=0.483  
-  [0.3–0.4]  n=   3,018  acc=0.336  
-  [0.4–0.5]  n=   3,011  acc=0.231  
-  [0.5–0.6]  n=   3,016  acc=0.852  
-  [0.6–0.7]  n=   3,231  acc=0.886  
-  [0.7–0.8]  n=   4,047  acc=0.916  
-  [0.8–0.9]  n=   6,620  acc=0.950  
-  [0.9–1.0]  n= 120,294  acc=0.996  █████████

### Top 10 domen w błędach (Domena | Model | Prawda)
     289×  docs.google.com                     | Model: Legit (0)    | Prawda: Phishing (1)
     256×  new.express.adobe.com               | Model: Legit (0)    | Prawda: Phishing (1)
     103×  flowcode.com                        | Model: Legit (0)    | Prawda: Phishing (1)
      71×  sites.google.com                    | Model: Legit (0)    | Prawda: Phishing (1)
      42×  rp.mockplus.com                     | Model: Legit (0)    | Prawda: Phishing (1)
      36×  storage.cloud.google.com            | Model: Legit (0)    | Prawda: Phishing (1)
      34×  tinyurl.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      26×  twitter.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      25×  cakeresume.com                      | Model: Legit (0)    | Prawda: Phishing (1)
      22×  flow.page                           | Model: Legit (0)    | Prawda: Phishing (1)


## SET - 3
### Metryki
-  Precision : 0.9594   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.7774   (ile phishingów zostało wykrytych)
-  F1        : 0.8589
-  FPR       : 0.0284   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 28843 / 94056 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=570,056  F1=0.8231
-  [ 50–100 znaków]  n=182,694  F1=0.9607
-  [100–150 znaków]  n= 25,912  F1=0.9820
-  [150–200 znaków]  n=  6,871  F1=0.9865
-  [200–999 znaków]  n=  9,325  F1=0.9941

### Rozkład predykcji
-  [0.0–0.1]  n= 419,029  acc=0.943  █████████████████████
-  [0.1–0.2]  n=  29,342  acc=0.333  █
-  [0.2–0.3]  n=  20,573  acc=0.226  █
-  [0.3–0.4]  n=  15,125  acc=0.195  
-  [0.4–0.5]  n=  12,602  acc=0.176  
-  [0.5–0.6]  n=  11,255  acc=0.843  
-  [0.6–0.7]  n=  11,922  acc=0.860  
-  [0.7–0.8]  n=  14,842  acc=0.885  
-  [0.8–0.9]  n=  22,599  acc=0.911  █
-  [0.9–1.0]  n= 237,657  acc=0.979  ███████████

### Top 10 domen w błędach (Domena | Model | Prawda)
     486×  tools.ietf.org                      | Model: Phishing (1) | Prawda: Legit (0)
     177×  angelfire.com                       | Model: Phishing (1) | Prawda: Legit (0)
     172×  pastehtml.com                       | Model: Legit (0)    | Prawda: Phishing (1)
     114×  home.comcast.net                    | Model: Legit (0)    | Prawda: Phishing (1)
     112×  s.yam.com                           | Model: Legit (0)    | Prawda: Phishing (1)
      63×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
      61×  globetrotter-games.com              | Model: Phishing (1) | Prawda: Legit (0)
      59×  painterspaintings.com               | Model: Legit (0)    | Prawda: Phishing (1)
      51×  fibtex.lodz.pl                      | Model: Phishing (1) | Prawda: Legit (0)
      47×  linkedin.com                        | Model: Legit (0)    | Prawda: Phishing (1)


## SET - 4
### Metryki
-  Precision : 0.1592   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.8451   (ile phishingów zostało wykrytych)
-  F1        : 0.2680
-  FPR       : 0.2495   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 83398 / 258183 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=1,040,321  F1=0.2048
-  [ 50–100 znaków]  n=  8,022  F1=0.9398
-  [100–150 znaków]  n=  1,852  F1=0.9402
-  [150–200 znaków]  n=  4,925  F1=0.9717
-  [200–999 znaków]  n=    770  F1=0.9908

### Rozkład predykcji
-  [0.0–0.1]  n= 225,895  acc=0.986  ████████
-  [0.1–0.2]  n= 219,984  acc=0.993  ████████
-  [0.2–0.3]  n= 149,027  acc=0.991  █████
-  [0.3–0.4]  n=  97,206  acc=0.986  ███
-  [0.4–0.5]  n=  67,033  acc=0.979  ██
-  [0.5–0.6]  n=  48,731  acc=0.029  █
-  [0.6–0.7]  n=  41,729  acc=0.038  █
-  [0.7–0.8]  n=  40,992  acc=0.047  █
-  [0.8–0.9]  n=  46,489  acc=0.080  █
-  [0.9–1.0]  n= 118,830  acc=0.325  ████

### Top 10 domen w błędach (Domena | Model | Prawda)
     730×  docs.google.com                     | Model: Legit (0)    | Prawda: Phishing (1)
     294×  new.express.adobe.com               | Model: Legit (0)    | Prawda: Phishing (1)
     215×  eu.jotform.com                      | Model: Legit (0)    | Prawda: Phishing (1)
     141×  qrco.de                             | Model: Legit (0)    | Prawda: Phishing (1)
     101×  flowcode.com                        | Model: Legit (0)    | Prawda: Phishing (1)
     100×  l.ead.me                            | Model: Legit (0)    | Prawda: Phishing (1)
      51×  linqapp.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      51×  l.wl.co                             | Model: Legit (0)    | Prawda: Phishing (1)
      50×  sites.google.com                    | Model: Legit (0)    | Prawda: Phishing (1)
      42×  rp.mockplus.com                     | Model: Legit (0)    | Prawda: Phishing (1)

