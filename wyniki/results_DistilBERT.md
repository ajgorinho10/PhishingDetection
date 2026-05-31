# DistilBERT (NLP + Cechy):
## SET - 1
### Metryki
-  Precision : 0.9919   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.9649   (ile phishingów zostało wykrytych)
-  F1        : 0.9782
-  FPR       : 0.0022   (ile legit URL-i fałszywie oznaczono jako phishing)

### Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 2532 / 4190 błędów ogółem

### F1 według długości URL
-  [  0– 50 znaków]  n=282,101  F1=0.9675
-  [ 50–100 znaków]  n=136,470  F1=0.9927
-  [100–150 znaków]  n= 17,188  F1=0.9949
-  [150–200 znaków]  n=  3,694  F1=0.9979
-  [200–999 znaków]  n=  3,727  F1=0.9988

### Rozkład predykcji
-  [0.0–0.1]  n= 345,945  acc=0.994  ███████████████████████████████
-  [0.1–0.2]  n=   1,246  acc=0.599  
-  [0.2–0.3]  n=     530  acc=0.426  
-  [0.3–0.4]  n=     343  acc=0.347  
-  [0.4–0.5]  n=     313  acc=0.300  
-  [0.5–0.6]  n=     300  acc=0.683  
-  [0.6–0.7]  n=     375  acc=0.768  
-  [0.7–0.8]  n=     495  acc=0.836  
-  [0.8–0.9]  n=   1,094  acc=0.865  
-  [0.9–1.0]  n=  92,563  acc=0.996  ████████

### Top 10 domen w błędach (Domena | Model | Prawda)
      22×  sites.google.com                    | Model: Legit (0)    | Prawda: Phishing (1)
      20×  twitter.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      12×  pastebin.com                        | Model: Legit (0)    | Prawda: Phishing (1)
       9×  angelfire.com                       | Model: Legit (0)    | Prawda: Phishing (1)
       7×  plus.google.com                     | Model: Legit (0)    | Prawda: Phishing (1)
       5×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
       5×  angelfire.com                       | Model: Phishing (1) | Prawda: Legit (0)
       5×  facebook.com                        | Model: Legit (0)    | Prawda: Phishing (1)
       5×  dailypoliticsnews.com               | Model: Legit (0)    | Prawda: Phishing (1)
       4×  embedit.in                          | Model: Phishing (1) | Prawda: Legit (0)

## SET - 2
### Metryki
-  Precision : 0.9947   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.9580   (ile phishingów zostało wykrytych)
-  F1        : 0.9760
-  FPR       : 0.0022   (ile legit URL-i fałszywie oznaczono jako phishing)

### Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 4641 / 7140 błędów ogółem

### F1 według długości URL
-  [  0– 50 znaków]  n=314,244  F1=0.9631
-  [ 50–100 znaków]  n=152,865  F1=0.9936
-  [100–150 znaków]  n= 18,789  F1=0.9949
-  [150–200 znaków]  n=  7,058  F1=0.9991
-  [200–999 znaków]  n=  4,461  F1=0.9984

### Rozkład predykcji
-  [0.0–0.1]  n= 348,055  acc=0.988  ███████████████████████████
-  [0.1–0.2]  n=   1,590  acc=0.469  
-  [0.2–0.3]  n=     749  acc=0.302  
-  [0.3–0.4]  n=     489  acc=0.241  
-  [0.4–0.5]  n=     444  acc=0.212  
-  [0.5–0.6]  n=     419  acc=0.773  
-  [0.6–0.7]  n=     524  acc=0.834  
-  [0.7–0.8]  n=     694  acc=0.883  
-  [0.8–0.9]  n=   1,579  acc=0.906  
-  [0.9–1.0]  n= 142,920  acc=0.997  ███████████

### Top 10 domen w błędach (Domena | Model | Prawda)
      23×  sites.google.com                    | Model: Legit (0)    | Prawda: Phishing (1)
      20×  twitter.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      17×  cf-ipfs.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      12×  pastebin.com                        | Model: Legit (0)    | Prawda: Phishing (1)
       9×  "https:                             | Model: Legit (0)    | Prawda: Phishing (1)
       9×  linkedin.com                        | Model: Legit (0)    | Prawda: Phishing (1)
       9×  angelfire.com                       | Model: Legit (0)    | Prawda: Phishing (1)
       7×  im-creator.com                      | Model: Legit (0)    | Prawda: Phishing (1)
       7×  plus.google.com                     | Model: Legit (0)    | Prawda: Phishing (1)
       7×  cakeresume.com                      | Model: Legit (0)    | Prawda: Phishing (1)

## SET - 3
### Metryki
-  Precision : 0.9644   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.7665   (ile phishingów zostało wykrytych)
-  F1        : 0.8541
-  FPR       : 0.0244   (ile legit URL-i fałszywie oznaczono jako phishing)

### Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 81024 / 96354 błędów ogółem

### F1 według długości URL
-  [  0– 50 znaków]  n=570,056  F1=0.8134
-  [ 50–100 znaków]  n=182,694  F1=0.9714
-  [100–150 znaków]  n= 25,912  F1=0.9874
-  [150–200 znaków]  n=  6,871  F1=0.9905
-  [200–999 znaków]  n=  9,325  F1=0.9958

### Rozkład predykcji
-  [0.0–0.1]  n= 485,322  acc=0.847  ████████████████████████
-  [0.1–0.2]  n=   7,859  acc=0.352  
-  [0.2–0.3]  n=   3,982  acc=0.299  
-  [0.3–0.4]  n=   2,818  acc=0.271  
-  [0.4–0.5]  n=   2,428  acc=0.264  
-  [0.5–0.6]  n=   2,468  acc=0.764  
-  [0.6–0.7]  n=   2,814  acc=0.775  
-  [0.7–0.8]  n=   3,910  acc=0.785  
-  [0.8–0.9]  n=   7,954  acc=0.806  
-  [0.9–1.0]  n= 275,391  acc=0.975  █████████████

### Top 10 domen w błędach (Domena | Model | Prawda)
     287×  angelfire.com                       | Model: Phishing (1) | Prawda: Legit (0)
     151×  home.comcast.net                    | Model: Legit (0)    | Prawda: Phishing (1)
     101×  pastehtml.com                       | Model: Legit (0)    | Prawda: Phishing (1)
      72×  painterspaintings.com               | Model: Legit (0)    | Prawda: Phishing (1)
      50×  fibtex.lodz.pl                      | Model: Phishing (1) | Prawda: Legit (0)
      47×  linkedin.com                        | Model: Legit (0)    | Prawda: Phishing (1)
      34×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
      31×  xs4all.nl                           | Model: Phishing (1) | Prawda: Legit (0)
      30×  pagesperso-orange.fr                | Model: Phishing (1) | Prawda: Legit (0)
      27×  2cocktails.com                      | Model: Legit (0)    | Prawda: Phishing (1)

## SET - 4
### Metryki
-  Precision : 0.9947   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.9716   (ile phishingów zostało wykrytych)
-  F1        : 0.9830
-  FPR       : 0.0018   (ile legit URL-i fałszywie oznaczono jako phishing)

### Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 3160 / 5155 błędów ogółem

### F1 według długości URL
-  [  0– 50 znaków]  n=420,725  F1=0.9762
-  [ 50–100 znaków]  n=144,404  F1=0.9938
-  [100–150 znaków]  n= 19,044  F1=0.9959
-  [150–200 znaków]  n=  8,626  F1=0.9993
-  [200–999 znaków]  n=  4,487  F1=0.9988

### Rozkład predykcji
-  [0.0–0.1]  n= 444,434  acc=0.994  █████████████████████████████
-  [0.1–0.2]  n=   1,474  acc=0.581  
-  [0.2–0.3]  n=     636  acc=0.390  
-  [0.3–0.4]  n=     411  acc=0.304  
-  [0.4–0.5]  n=     373  acc=0.252  
-  [0.5–0.6]  n=     371  acc=0.733  
-  [0.6–0.7]  n=     452  acc=0.799  
-  [0.7–0.8]  n=     623  acc=0.862  
-  [0.8–0.9]  n=   1,344  acc=0.890  
-  [0.9–1.0]  n= 147,217  acc=0.998  █████████

### Top 10 domen w błędach (Domena | Model | Prawda)
      25×  sites.google.com                    | Model: Legit (0)    | Prawda: Phishing (1)
      20×  twitter.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      12×  pastebin.com                        | Model: Legit (0)    | Prawda: Phishing (1)
       9×  angelfire.com                       | Model: Legit (0)    | Prawda: Phishing (1)
       7×  plus.google.com                     | Model: Legit (0)    | Prawda: Phishing (1)
       6×  onedrive.live.com                   | Model: Legit (0)    | Prawda: Phishing (1)
       5×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
       5×  angelfire.com                       | Model: Phishing (1) | Prawda: Legit (0)
       5×  dailypoliticsnews.com               | Model: Legit (0)    | Prawda: Phishing (1)
       5×  facebook.com                        | Model: Legit (0)    | Prawda: Phishing (1)

# DistilBERT (NLP):
## SET - 1
### Metryki
-  Precision : 0.9876   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.9749   (ile phishingów zostało wykrytych)
-  F1        : 0.9812
-  FPR       : 0.0034   (ile legit URL-i fałszywie oznaczono jako phishing)

### Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 1913 / 3643 błędów ogółem

### F1 według długości URL
-  [  0– 50 znaków]  n=282,101  F1=0.9714
-  [ 50–100 znaków]  n=136,470  F1=0.9947
-  [100–150 znaków]  n= 17,188  F1=0.9970
-  [150–200 znaków]  n=  3,694  F1=0.9992
-  [200–999 znaków]  n=  3,727  F1=0.9990

### Rozkład predykcji
-  [0.0–0.1]  n= 342,830  acc=0.996  ██████████████████████████████
-  [0.1–0.2]  n=   2,323  acc=0.836  
-  [0.2–0.3]  n=     871  acc=0.710  
-  [0.3–0.4]  n=     544  acc=0.599  
-  [0.4–0.5]  n=     422  acc=0.547  
-  [0.5–0.6]  n=     354  acc=0.480  
-  [0.6–0.7]  n=     362  acc=0.588  
-  [0.7–0.8]  n=     459  acc=0.667  
-  [0.8–0.9]  n=     807  acc=0.750  
-  [0.9–1.0]  n=  94,232  acc=0.995  ████████

### Top 10 domen w błędach (Domena | Model | Prawda)
      21×  twitter.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      18×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
      12×  plus.google.com                     | Model: Legit (0)    | Prawda: Phishing (1)
      10×  angelfire.com                       | Model: Legit (0)    | Prawda: Phishing (1)
       5×  pastebin.com                        | Model: Phishing (1) | Prawda: Legit (0)
       5×  facebook.com                        | Model: Legit (0)    | Prawda: Phishing (1)
       4×  home.earthlink.net                  | Model: Phishing (1) | Prawda: Legit (0)
       4×  horizonsrecruitment.co.uk           | Model: Phishing (1) | Prawda: Legit (0)
       4×  dailypoliticsnews.com               | Model: Legit (0)    | Prawda: Phishing (1)
       4×  natoint.com                         | Model: Legit (0)    | Prawda: Phishing (1)

## SET - 2
### Metryki
-  Precision : 0.9920   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.9684   (ile phishingów zostało wykrytych)
-  F1        : 0.9800
-  FPR       : 0.0034   (ile legit URL-i fałszywie oznaczono jako phishing)

### Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 3498 / 5987 błędów ogółem

### F1 według długości URL
-  [  0– 50 znaków]  n=314,244  F1=0.9687
-  [ 50–100 znaków]  n=152,865  F1=0.9958
-  [100–150 znaków]  n= 18,789  F1=0.9971
-  [150–200 znaków]  n=  7,058  F1=0.9997
-  [200–999 znaków]  n=  4,461  F1=0.9990

### Rozkład predykcji
-  [0.0–0.1]  n= 344,417  acc=0.991  ███████████████████████████
-  [0.1–0.2]  n=   2,621  acc=0.741  
-  [0.2–0.3]  n=   1,059  acc=0.584  
-  [0.3–0.4]  n=     676  acc=0.482  
-  [0.4–0.5]  n=     563  acc=0.410  
-  [0.5–0.6]  n=     484  acc=0.620  
-  [0.6–0.7]  n=     524  acc=0.716  
-  [0.7–0.8]  n=     671  acc=0.772  
-  [0.8–0.9]  n=   1,192  acc=0.831  
-  [0.9–1.0]  n= 145,256  acc=0.997  ███████████

### Top 10 domen w błędach (Domena | Model | Prawda)
      21×  twitter.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      18×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
      12×  plus.google.com                     | Model: Legit (0)    | Prawda: Phishing (1)
      10×  angelfire.com                       | Model: Legit (0)    | Prawda: Phishing (1)
       5×  pastebin.com                        | Model: Phishing (1) | Prawda: Legit (0)
       5×  facebook.com                        | Model: Legit (0)    | Prawda: Phishing (1)
       4×  home.earthlink.net                  | Model: Phishing (1) | Prawda: Legit (0)
       4×  natoint.com                         | Model: Legit (0)    | Prawda: Phishing (1)
       4×  dailypoliticsnews.com               | Model: Legit (0)    | Prawda: Phishing (1)
       4×  athena.hhmtelemedicine.com          | Model: Legit (0)    | Prawda: Phishing (1)

## SET - 3
### Metryki
-  Precision : 0.9556   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.7865   (ile phishingów zostało wykrytych)
-  F1        : 0.8629
-  FPR       : 0.0315   (ile legit URL-i fałszywie oznaczono jako phishing)

### Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 77318 / 92036 błędów ogółem

### F1 według długości URL
-  [  0– 50 znaków]  n=570,056  F1=0.8257
-  [ 50–100 znaków]  n=182,694  F1=0.9699
-  [100–150 znaków]  n= 25,912  F1=0.9858
-  [150–200 znaków]  n=  6,871  F1=0.9918
-  [200–999 znaków]  n=  9,325  F1=0.9958

### Rozkład predykcji
-  [0.0–0.1]  n= 472,823  acc=0.855  ███████████████████████
-  [0.1–0.2]  n=   8,737  acc=0.530  
-  [0.2–0.3]  n=   4,595  acc=0.451  
-  [0.3–0.4]  n=   3,230  acc=0.433  
-  [0.4–0.5]  n=   2,578  acc=0.416  
-  [0.5–0.6]  n=   2,501  acc=0.618  
-  [0.6–0.7]  n=   2,736  acc=0.641  
-  [0.7–0.8]  n=   3,401  acc=0.674  
-  [0.8–0.9]  n=   5,944  acc=0.713  
-  [0.9–1.0]  n= 288,401  acc=0.970  ██████████████

### Top 10 domen w błędach (Domena | Model | Prawda)
     269×  angelfire.com                       | Model: Phishing (1) | Prawda: Legit (0)
     126×  home.comcast.net                    | Model: Legit (0)    | Prawda: Phishing (1)
      71×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
      70×  painterspaintings.com               | Model: Legit (0)    | Prawda: Phishing (1)
      51×  fibtex.lodz.pl                      | Model: Phishing (1) | Prawda: Legit (0)
      35×  pastehtml.com                       | Model: Legit (0)    | Prawda: Phishing (1)
      35×  globetrotter-games.com              | Model: Phishing (1) | Prawda: Legit (0)
      33×  pagesperso-orange.fr                | Model: Phishing (1) | Prawda: Legit (0)
      29×  home.earthlink.net                  | Model: Phishing (1) | Prawda: Legit (0)
      28×  www-03.ibm.com                      | Model: Phishing (1) | Prawda: Legit (0)

## SET - 4
### Metryki
-  Precision : 0.9919   (ile z 'phishing' to naprawdę phishing)
-  Recall    : 0.9793   (ile phishingów zostało wykrytych)
-  F1        : 0.9856
-  FPR       : 0.0028   (ile legit URL-i fałszywie oznaczono jako phishing)

### Błędy wysokiej pewności (|prob−0.5|>0.4)
-  Liczba: 2354 / 4400 błędów ogółem

### F1 według długości URL
-  [  0– 50 znaków]  n=420,725  F1=0.9794
-  [ 50–100 znaków]  n=144,404  F1=0.9957
-  [100–150 znaków]  n= 19,044  F1=0.9977
-  [150–200 znaków]  n=  8,626  F1=0.9997
-  [200–999 znaków]  n=  4,487  F1=0.9991

### Rozkład predykcji
-  [0.0–0.1]  n= 440,945  acc=0.996  █████████████████████████████
-  [0.1–0.2]  n=   2,657  acc=0.809  
-  [0.2–0.3]  n=     991  acc=0.679  
-  [0.3–0.4]  n=     627  acc=0.571  
-  [0.4–0.5]  n=     489  acc=0.507  
-  [0.5–0.6]  n=     420  acc=0.540  
-  [0.6–0.7]  n=     433  acc=0.642  
-  [0.7–0.8]  n=     555  acc=0.717  
-  [0.8–0.9]  n=     978  acc=0.789  
-  [0.9–1.0]  n= 149,240  acc=0.997  █████████

### Top 10 domen w błędach (Domena | Model | Prawda)
      21×  twitter.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      18×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
      12×  plus.google.com                     | Model: Legit (0)    | Prawda: Phishing (1)
      10×  angelfire.com                       | Model: Legit (0)    | Prawda: Phishing (1)
       5×  sites.google.com                    | Model: Legit (0)    | Prawda: Phishing (1)
       5×  pastebin.com                        | Model: Phishing (1) | Prawda: Legit (0)
       5×  facebook.com                        | Model: Legit (0)    | Prawda: Phishing (1)
       4×  dailypoliticsnews.com               | Model: Legit (0)    | Prawda: Phishing (1)
       4×  horizonsrecruitment.co.uk           | Model: Phishing (1) | Prawda: Legit (0)
       4×  home.earthlink.net                  | Model: Phishing (1) | Prawda: Legit (0)
