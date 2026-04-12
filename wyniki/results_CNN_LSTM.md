
# CNN_LSTM (NLP + Cechy)
## SET - 1
### Metryki
-  Precision : 0.9670   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.9558   (ile phishingów zostało wykrytych)
-  F1        : 0.9614
-  FPR       : 0.0092   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 175 / 7486 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=282,101  F1=0.9426
-  [ 50–100 znaków]  n=136,470  F1=0.9871
-  [100–150 znaków]  n= 17,188  F1=0.9934
-  [150–200 znaków]  n=  3,694  F1=0.9955
-  [200–999 znaków]  n=  3,727  F1=0.9957

### Rozkład predykcji
-  [0.0–0.1]  n= 248,289  acc=1.000  ██████████████████████
-  [0.1–0.2]  n=  55,039  acc=0.988  ████
-  [0.2–0.3]  n=  28,531  acc=0.962  ██
-  [0.3–0.4]  n=   9,975  acc=0.889  
-  [0.4–0.5]  n=   5,023  acc=0.734  
-  [0.5–0.6]  n=   3,869  acc=0.538  
-  [0.6–0.7]  n=   4,247  acc=0.799  
-  [0.7–0.8]  n=   5,622  acc=0.939  
-  [0.8–0.9]  n=  11,150  acc=0.988  █
-  [0.9–1.0]  n=  71,459  acc=0.999  ██████

### Top 10 domen w błędach (Domena | Model | Prawda)
      43×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
      27×  twitter.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      10×  angelfire.com                       | Model: Legit (0)    | Prawda: Phishing (1)
      10×  worldpostjournal.com                | Model: Legit (0)    | Prawda: Phishing (1)
      10×  plus.google.com                     | Model: Legit (0)    | Prawda: Phishing (1)
       9×  angelfire.com                       | Model: Phishing (1) | Prawda: Legit (0)
       9×  telegra.ph                          | Model: Legit (0)    | Prawda: Phishing (1)
       8×  twitter.com                         | Model: Phishing (1) | Prawda: Legit (0)
       8×  grotown.com                         | Model: Legit (0)    | Prawda: Phishing (1)
       7×  moreepa.co.uk                       | Model: Legit (0)    | Prawda: Phishing (1)


## SET - 2
### Metryki
-  Precision : 0.9785   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.9511   (ile phishingów zostało wykrytych)
-  F1        : 0.9646
-  FPR       : 0.0092   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 314 / 10593 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=314,244  F1=0.9455
-  [ 50–100 znaków]  n=152,865  F1=0.9907
-  [100–150 znaków]  n= 18,789  F1=0.9943
-  [150–200 znaków]  n=  7,058  F1=0.9981
-  [200–999 znaków]  n=  4,461  F1=0.9963

### Rozkład predykcji
-  [0.0–0.1]  n= 248,428  acc=0.999  ███████████████████
-  [0.1–0.2]  n=  55,861  acc=0.974  ████
-  [0.2–0.3]  n=  29,349  acc=0.935  ██
-  [0.3–0.4]  n=  10,651  acc=0.833  
-  [0.4–0.5]  n=   5,679  acc=0.649  
-  [0.5–0.6]  n=   4,650  acc=0.616  
-  [0.6–0.7]  n=   5,445  acc=0.843  
-  [0.7–0.8]  n=   7,545  acc=0.955  
-  [0.8–0.9]  n=  18,002  acc=0.992  █
-  [0.9–1.0]  n= 111,853  acc=0.999  ████████

### Top 10 domen w błędach (Domena | Model | Prawda)
      43×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
      27×  twitter.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      11×  cakeresume.com                      | Model: Legit (0)    | Prawda: Phishing (1)
      10×  plus.google.com                     | Model: Legit (0)    | Prawda: Phishing (1)
      10×  angelfire.com                       | Model: Legit (0)    | Prawda: Phishing (1)
      10×  worldpostjournal.com                | Model: Legit (0)    | Prawda: Phishing (1)
       9×  telegra.ph                          | Model: Legit (0)    | Prawda: Phishing (1)
       9×  angelfire.com                       | Model: Phishing (1) | Prawda: Legit (0)
       8×  grotown.com                         | Model: Legit (0)    | Prawda: Phishing (1)
       8×  twitter.com                         | Model: Phishing (1) | Prawda: Legit (0)


## SET - 3
### Metryki
-  Precision : 0.9395   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.7414   (ile phishingów zostało wykrytych)
-  F1        : 0.8288
-  FPR       : 0.0412   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 7385 / 112749 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=570,056  F1=0.7812
-  [ 50–100 znaków]  n=182,694  F1=0.9625
-  [100–150 znaków]  n= 25,912  F1=0.9838
-  [150–200 znaków]  n=  6,871  F1=0.9892
-  [200–999 znaków]  n=  9,325  F1=0.9940

### Rozkład predykcji
-  [0.0–0.1]  n= 282,498  acc=0.979  ██████████████
-  [0.1–0.2]  n= 110,684  acc=0.634  █████
-  [0.2–0.3]  n=  59,516  acc=0.632  ██
-  [0.3–0.4]  n=  30,511  acc=0.519  █
-  [0.4–0.5]  n=  21,261  acc=0.426  █
-  [0.5–0.6]  n=  19,583  acc=0.691  
-  [0.6–0.7]  n=  22,178  acc=0.799  █
-  [0.7–0.8]  n=  28,177  acc=0.889  █
-  [0.8–0.9]  n=  49,440  acc=0.951  ██
-  [0.9–1.0]  n= 171,098  acc=0.991  ████████

### Top 10 domen w błędach (Domena | Model | Prawda)
     306×  pastehtml.com                       | Model: Legit (0)    | Prawda: Phishing (1)
     271×  angelfire.com                       | Model: Phishing (1) | Prawda: Legit (0)
     142×  home.comcast.net                    | Model: Legit (0)    | Prawda: Phishing (1)
     118×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
      68×  painterspaintings.com               | Model: Legit (0)    | Prawda: Phishing (1)
      62×  globetrotter-games.com              | Model: Phishing (1) | Prawda: Legit (0)
      59×  ddj.com                             | Model: Phishing (1) | Prawda: Legit (0)
      57×  w3.org                              | Model: Phishing (1) | Prawda: Legit (0)
      51×  fibtex.lodz.pl                      | Model: Phishing (1) | Prawda: Legit (0)
      49×  pagesperso-orange.fr                | Model: Phishing (1) | Prawda: Legit (0)


## SET - 4
### Metryki
-  Precision : 0.9786   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.9625   (ile phishingów zostało wykrytych)
-  F1        : 0.9705
-  FPR       : 0.0073   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 192 / 8996 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=420,725  F1=0.9585
-  [ 50–100 znaków]  n=144,404  F1=0.9893
-  [100–150 znaków]  n= 19,044  F1=0.9950
-  [150–200 znaków]  n=  8,626  F1=0.9984
-  [200–999 znaków]  n=  4,487  F1=0.9965

### Rozkład predykcji
-  [0.0–0.1]  n= 274,392  acc=1.000  ██████████████████
-  [0.1–0.2]  n= 118,287  acc=0.992  ███████
-  [0.2–0.3]  n=  36,510  acc=0.959  ██
-  [0.3–0.4]  n=  11,408  acc=0.871  
-  [0.4–0.5]  n=   5,678  acc=0.691  
-  [0.5–0.6]  n=   4,495  acc=0.592  
-  [0.6–0.7]  n=   5,279  acc=0.837  
-  [0.7–0.8]  n=   7,743  acc=0.955  
-  [0.8–0.9]  n=  16,434  acc=0.992  █
-  [0.9–1.0]  n= 117,109  acc=1.000  ███████

### Top 10 domen w błędach (Domena | Model | Prawda)
      43×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
      27×  twitter.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      10×  plus.google.com                     | Model: Legit (0)    | Prawda: Phishing (1)
      10×  angelfire.com                       | Model: Legit (0)    | Prawda: Phishing (1)
      10×  worldpostjournal.com                | Model: Legit (0)    | Prawda: Phishing (1)
       9×  angelfire.com                       | Model: Phishing (1) | Prawda: Legit (0)
       9×  telegra.ph                          | Model: Legit (0)    | Prawda: Phishing (1)
       8×  grotown.com                         | Model: Legit (0)    | Prawda: Phishing (1)
       8×  twitter.com                         | Model: Phishing (1) | Prawda: Legit (0)
       7×  moreepa.co.uk                       | Model: Legit (0)    | Prawda: Phishing (1)

# CNN_LSTM (NLP)
## SET - 1
### Metryki
-  Precision : 0.9643   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.9559   (ile phishingów zostało wykrytych)
-  F1        : 0.9601
-  FPR       : 0.0100   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 186 / 7751 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=282,101  F1=0.9408
-  [ 50–100 znaków]  n=136,470  F1=0.9864
-  [100–150 znaków]  n= 17,188  F1=0.9926
-  [150–200 znaków]  n=  3,694  F1=0.9957
-  [200–999 znaków]  n=  3,727  F1=0.9943

### Rozkład predykcji
-  [0.0–0.1]  n= 246,998  acc=1.000  ██████████████████████
-  [0.1–0.2]  n=  54,017  acc=0.987  ████
-  [0.2–0.3]  n=  30,286  acc=0.966  ██
-  [0.3–0.4]  n=  10,418  acc=0.889  
-  [0.4–0.5]  n=   4,863  acc=0.734  
-  [0.5–0.6]  n=   3,640  acc=0.521  
-  [0.6–0.7]  n=   3,774  acc=0.757  
-  [0.7–0.8]  n=   5,103  acc=0.908  
-  [0.8–0.9]  n=  10,013  acc=0.976  
-  [0.9–1.0]  n=  74,092  acc=0.999  ██████

### Top 10 domen w błędach (Domena | Model | Prawda)
      62×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
      49×  twitter.com                         | Model: Phishing (1) | Prawda: Legit (0)
      16×  twitter.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      16×  plus.google.com                     | Model: Legit (0)    | Prawda: Phishing (1)
      13×  angelfire.com                       | Model: Legit (0)    | Prawda: Phishing (1)
       9×  veganvet.net                        | Model: Legit (0)    | Prawda: Phishing (1)
       8×  swapalop.com                        | Model: Phishing (1) | Prawda: Legit (0)
       8×  abbreviations.com                   | Model: Phishing (1) | Prawda: Legit (0)
       8×  grotown.com                         | Model: Legit (0)    | Prawda: Phishing (1)
       7×  view.aimini.com                     | Model: Phishing (1) | Prawda: Legit (0)


## SET - 2
### Metryki
-  Precision : 0.9767   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.9514   (ile phishingów zostało wykrytych)
-  F1        : 0.9639
-  FPR       : 0.0100   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 414 / 10825 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=314,244  F1=0.9445
-  [ 50–100 znaków]  n=152,865  F1=0.9904
-  [100–150 znaków]  n= 18,789  F1=0.9937
-  [150–200 znaków]  n=  7,058  F1=0.9982
-  [200–999 znaków]  n=  4,461  F1=0.9954

### Rozkład predykcji
-  [0.0–0.1]  n= 247,226  acc=0.999  ███████████████████
-  [0.1–0.2]  n=  54,808  acc=0.973  ████
-  [0.2–0.3]  n=  30,975  acc=0.944  ██
-  [0.3–0.4]  n=  11,134  acc=0.831  
-  [0.4–0.5]  n=   5,515  acc=0.647  
-  [0.5–0.6]  n=   4,295  acc=0.594  
-  [0.6–0.7]  n=   4,759  acc=0.808  
-  [0.7–0.8]  n=   6,594  acc=0.929  
-  [0.8–0.9]  n=  13,861  acc=0.983  █
-  [0.9–1.0]  n= 118,296  acc=0.999  █████████

### Top 10 domen w błędach (Domena | Model | Prawda)
      62×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
      49×  twitter.com                         | Model: Phishing (1) | Prawda: Legit (0)
      16×  twitter.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      16×  plus.google.com                     | Model: Legit (0)    | Prawda: Phishing (1)
      15×  klrn.wpenginepowered.com            | Model: Legit (0)    | Prawda: Phishing (1)
      13×  angelfire.com                       | Model: Legit (0)    | Prawda: Phishing (1)
      11×  wepik.com                           | Model: Legit (0)    | Prawda: Phishing (1)
       9×  veganvet.net                        | Model: Legit (0)    | Prawda: Phishing (1)
       8×  abbreviations.com                   | Model: Phishing (1) | Prawda: Legit (0)
       8×  grotown.com                         | Model: Legit (0)    | Prawda: Phishing (1)


## SET - 3
### Metryki
-  Precision : 0.9373   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.7570   (ile phishingów zostało wykrytych)
-  F1        : 0.8375
-  FPR       : 0.0437   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 9575 / 108095 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=570,056  F1=0.7941
-  [ 50–100 znaków]  n=182,694  F1=0.9589
-  [100–150 znaków]  n= 25,912  F1=0.9812
-  [150–200 znaków]  n=  6,871  F1=0.9904
-  [200–999 znaków]  n=  9,325  F1=0.9943

### Rozkład predykcji
-  [0.0–0.1]  n= 281,305  acc=0.974  ██████████████
-  [0.1–0.2]  n= 110,582  acc=0.606  █████
-  [0.2–0.3]  n=  58,204  acc=0.692  ██
-  [0.3–0.4]  n=  29,224  acc=0.624  █
-  [0.4–0.5]  n=  18,367  acc=0.476  
-  [0.5–0.6]  n=  17,404  acc=0.662  
-  [0.6–0.7]  n=  20,376  acc=0.778  █
-  [0.7–0.8]  n=  26,242  acc=0.872  █
-  [0.8–0.9]  n=  43,429  acc=0.938  ██
-  [0.9–1.0]  n= 189,813  acc=0.989  █████████

### Top 10 domen w błędach (Domena | Model | Prawda)
     300×  angelfire.com                       | Model: Phishing (1) | Prawda: Legit (0)
     142×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
     140×  home.comcast.net                    | Model: Legit (0)    | Prawda: Phishing (1)
      74×  twitter.com                         | Model: Phishing (1) | Prawda: Legit (0)
      71×  painterspaintings.com               | Model: Legit (0)    | Prawda: Phishing (1)
      65×  babinet.cz                          | Model: Legit (0)    | Prawda: Phishing (1)
      59×  globetrotter-games.com              | Model: Phishing (1) | Prawda: Legit (0)
      51×  fibtex.lodz.pl                      | Model: Phishing (1) | Prawda: Legit (0)
      46×  pagesperso-orange.fr                | Model: Phishing (1) | Prawda: Legit (0)
      41×  microsoft.com                       | Model: Phishing (1) | Prawda: Legit (0)


## SET - 4
### Metryki
-  Precision : 0.9765   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.9635   (ile phishingów zostało wykrytych)
-  F1        : 0.9699
-  FPR       : 0.0080   (ile legit URL-i fałszywie oznaczono jako phishing)

###  Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 206 / 9175 błędów ogółem
### F1 według długości URL
-  [  0– 50 znaków]  n=420,725  F1=0.9579
-  [ 50–100 znaków]  n=144,404  F1=0.9890
-  [100–150 znaków]  n= 19,044  F1=0.9944
-  [150–200 znaków]  n=  8,626  F1=0.9985
-  [200–999 znaków]  n=  4,487  F1=0.9954

### Rozkład predykcji
-  [0.0–0.1]  n= 278,058  acc=1.000  ██████████████████
-  [0.1–0.2]  n= 114,981  acc=0.992  ███████
-  [0.2–0.3]  n=  35,897  acc=0.960  ██
-  [0.3–0.4]  n=  11,544  acc=0.867  
-  [0.4–0.5]  n=   5,320  acc=0.700  
-  [0.5–0.6]  n=   4,130  acc=0.558  
-  [0.6–0.7]  n=   4,443  acc=0.789  
-  [0.7–0.8]  n=   6,098  acc=0.921  
-  [0.8–0.9]  n=  13,346  acc=0.982  
-  [0.9–1.0]  n= 123,518  acc=0.999  ████████

### Top 10 domen w błędach (Domena | Model | Prawda)
      62×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
      49×  twitter.com                         | Model: Phishing (1) | Prawda: Legit (0)
      16×  plus.google.com                     | Model: Legit (0)    | Prawda: Phishing (1)
      16×  twitter.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      13×  angelfire.com                       | Model: Legit (0)    | Prawda: Phishing (1)
       9×  veganvet.net                        | Model: Legit (0)    | Prawda: Phishing (1)
       8×  swapalop.com                        | Model: Phishing (1) | Prawda: Legit (0)
       8×  abbreviations.com                   | Model: Phishing (1) | Prawda: Legit (0)
       8×  grotown.com                         | Model: Legit (0)    | Prawda: Phishing (1)
       7×  view.aimini.com                     | Model: Phishing (1) | Prawda: Legit (0)

