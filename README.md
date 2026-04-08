# to do:
- sprawdzić drzewa,SVM,MLP
- sprawdzić czy LSTM działa dobrze
- dodać transformer


# Ważne
kazdy set przed samym treningiem jest dzielony:
- 70% trening
- 15% validacja
- 15% test



set 1 - set treningowy
set 2 - set testowy
set 3 - set testowy
set 4 - set testowy, najnowsze dane


do setu pierwszego processed dodanje przypadki które model źle sklasyfikował w secie:
- NR 4



# CNN_LSTM wyniki:

## set - 4
### Metryki
- Precision : 0.9994   (ile z 'phishing' to naprawdę phishing)
- Recall    : 0.9413   (ile phishingów zostało wykrytych)
- F1        : 0.9695
- FPR       : 0.0000   (ile legit URL-i fałszywie oznaczono jako phishing)

### Błędy wysokiej pewności (|prob−0.5| > 0.4)
- Liczba: 1361 / 3309 błędów ogółem
  → Im więcej, tym poważniejszy distribution shift

### F1 według długości URL
- [  0– 50 znaków]  n=1,040,321  F1=0.9747
- [ 50–100 znaków]  n=  8,022  F1=0.9859
- [100–150 znaków]  n=  1,852  F1=0.9350
- [150–200 znaków]  n=  4,925  F1=0.9047
- [200–999 znaków]  n=    770  F1=0.9948

### Rozkład predykcji
- [0.0–0.1]  n= 988,521  acc=0.999  █████████████████████████████████████
- [0.1–0.2]  n=  13,055  acc=0.942  
- [0.2–0.3]  n=     880  acc=0.491  
- [0.3–0.4]  n=     411  acc=0.119  
- [0.4–0.5]  n=     384  acc=0.055  
- [0.5–0.6]  n=     367  acc=0.981  
- [0.6–0.7]  n=     438  acc=0.984  
- [0.7–0.8]  n=     632  acc=0.986  
- [0.8–0.9]  n=   1,564  acc=0.999  
- [0.9–1.0]  n=  49,664  acc=1.000  █

### Top 10 domen w błędach (Domena | Model | Prawda)

-  1.190×  docs.google.com                      Model: Legit (0)    Prawda: Phishing (1)
-     10×  lookerstudio.google.com              Model: Legit (0)    Prawda: Phishing (1)
-      7×  docs.zoom.us                         Model: Legit (0)    Prawda: Phishing (1)
-      7×  storage.cloud.google.com             Model: Legit (0)    Prawda: Phishing (1)
-      6×  cakeresume.com                       Model: Legit (0)    Prawda: Phishing (1)
-      5×  s.yam.com                            Model: Legit (0)    Prawda: Phishing (1)
-      4×  share.hsforms.com                    Model: Legit (0)    Prawda: Phishing (1)
-      4×  sites.google.com                     Model: Legit (0)    Prawda: Phishing (1)
-      4×  forms.office.com                     Model: Legit (0)    Prawda: Phishing (1)
-      3×  hotm.art                             Model: Legit (0)    Prawda: Phishing (1)

## set - 1
── Metryki ─────────────────────────────────
  Precision : 0.9851   (ile z 'phishing' to naprawdę phishing)
  Recall    : 0.9487   (ile phishingów zostało wykrytych)
  F1        : 0.9666
  FPR       : 0.0040   (ile legit URL-i fałszywie oznaczono jako phishing)

── Błędy wysokiej pewności (|prob−0.5|>0.4) ──
  Liczba: 2806 / 6399 błędów ogółem
  → Im więcej, tym poważniejszy distribution shift

── F1 według długości URL ──────────────────
  [  0– 50 znaków]  n=282,101  F1=0.9492
  [ 50–100 znaków]  n=136,470  F1=0.9899
  [100–150 znaków]  n= 17,188  F1=0.9948
  [150–200 znaków]  n=  3,694  F1=0.9975
  [200–999 znaków]  n=  3,727  F1=0.9979

── Rozkład predykcji ───────────────────────
  [0.0–0.1]  n= 339,743  acc=0.993  ██████████████████████████████
  [0.1–0.2]  n=   5,084  acc=0.852  
  [0.2–0.3]  n=   2,037  acc=0.723  
  [0.3–0.4]  n=   1,389  acc=0.559  
  [0.4–0.5]  n=   1,089  acc=0.433  
  [0.5–0.6]  n=     996  acc=0.659  
  [0.6–0.7]  n=   1,125  acc=0.771  
  [0.7–0.8]  n=   1,561  acc=0.846  
  [0.8–0.9]  n=   2,706  acc=0.922  
  [0.9–1.0]  n=  87,474  acc=0.996  ███████

── Top 10 domen w błędach (Domena | Model | Prawda) ──
      44×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
      20×  twitter.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      13×  plus.google.com                     | Model: Legit (0)    | Prawda: Phishing (1)
      12×  worldpostjournal.com                | Model: Legit (0)    | Prawda: Phishing (1)
      10×  angelfire.com                       | Model: Legit (0)    | Prawda: Phishing (1)
       7×  sitesumo.com                        | Model: Legit (0)    | Prawda: Phishing (1)
       6×  twitter.com                         | Model: Phishing (1) | Prawda: Legit (0)
       6×  turl.ca                             | Model: Legit (0)    | Prawda: Phishing (1)
       5×  reocities.com                       | Model: Legit (0)    | Prawda: Phishing (1)
       5×  facebook.com                        | Model: Legit (0)    | Prawda: Phishing (1)

## set - 2
── Metryki ─────────────────────────────────
  Precision : 0.9903   (ile z 'phishing' to naprawdę phishing)
  Recall    : 0.9342   (ile phishingów zostało wykrytych)
  F1        : 0.9614
  FPR       : 0.0040   (ile legit URL-i fałszywie oznaczono jako phishing)

── Błędy wysokiej pewności (|prob−0.5|>0.4) ──
  Liczba: 5472 / 11382 błędów ogółem
  → Im więcej, tym poważniejszy distribution shift

── F1 według długości URL ──────────────────
  [  0– 50 znaków]  n=314,245  F1=0.9444
  [ 50–100 znaków]  n=152,864  F1=0.9916
  [100–150 znaków]  n= 18,789  F1=0.9937
  [150–200 znaków]  n=  7,058  F1=0.9180
  [200–999 znaków]  n=  4,461  F1=0.9975

── Rozkład predykcji ───────────────────────
  [0.0–0.1]  n= 342,411  acc=0.985  ███████████████████████████
  [0.1–0.2]  n=   6,111  acc=0.709  
  [0.2–0.3]  n=   2,577  acc=0.572  
  [0.3–0.4]  n=   1,777  acc=0.438  
  [0.4–0.5]  n=   1,451  acc=0.325  
  [0.5–0.6]  n=   1,362  acc=0.750  
  [0.6–0.7]  n=   1,506  acc=0.829  
  [0.7–0.8]  n=   2,084  acc=0.884  
  [0.8–0.9]  n=   3,917  acc=0.947  
  [0.9–1.0]  n= 134,267  acc=0.997  ██████████

── Top 10 domen w błędach (Domena | Model | Prawda) ──
     877×  docs.google.com                     | Model: Legit (0)    | Prawda: Phishing (1)
      44×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
      20×  twitter.com                         | Model: Legit (0)    | Prawda: Phishing (1)
      13×  klrn.wpenginepowered.com            | Model: Legit (0)    | Prawda: Phishing (1)
      13×  plus.google.com                     | Model: Legit (0)    | Prawda: Phishing (1)
      12×  cakeresume.com                      | Model: Legit (0)    | Prawda: Phishing (1)
      12×  flipsnack.com                       | Model: Legit (0)    | Prawda: Phishing (1)
      12×  worldpostjournal.com                | Model: Legit (0)    | Prawda: Phishing (1)
      11×  hyperfollow.com                     | Model: Legit (0)    | Prawda: Phishing (1)
      10×  via0.com                            | Model: Legit (0)    | Prawda: Phishing (1)

## set - 3
── Metryki ─────────────────────────────────
  Precision : 0.9519   (ile z 'phishing' to naprawdę phishing)
  Recall    : 0.6994   (ile phishingów zostało wykrytych)
  F1        : 0.8063
  FPR       : 0.0305   (ile legit URL-i fałszywie oznaczono jako phishing)

── Błędy wysokiej pewności (|prob−0.5|>0.4) ──
  Liczba: 89992 / 123653 błędów ogółem
  → Im więcej, tym poważniejszy distribution shift

── F1 według długości URL ──────────────────
  [  0– 50 znaków]  n=570,056  F1=0.7499
  [ 50–100 znaków]  n=182,694  F1=0.9587
  [100–150 znaków]  n= 25,912  F1=0.9832
  [150–200 znaków]  n=  6,871  F1=0.9892
  [200–999 znaków]  n=  9,325  F1=0.9946

── Rozkład predykcji ───────────────────────
  [0.0–0.1]  n= 480,325  acc=0.825  ████████████████████████
  [0.1–0.2]  n=  18,320  acc=0.489  
  [0.2–0.3]  n=  10,303  acc=0.389  
  [0.3–0.4]  n=   8,254  acc=0.314  
  [0.4–0.5]  n=   7,298  acc=0.272  
  [0.5–0.6]  n=   7,251  acc=0.771  
  [0.6–0.7]  n=   7,912  acc=0.800  
  [0.7–0.8]  n=  10,309  acc=0.832  
  [0.8–0.9]  n=  16,640  acc=0.877  
  [0.9–1.0]  n= 228,334  acc=0.974  ███████████

── Top 10 domen w błędach (Domena | Model | Prawda) ──
     301×  tools.ietf.org                      | Model: Phishing (1) | Prawda: Legit (0)
     183×  angelfire.com                       | Model: Phishing (1) | Prawda: Legit (0)
     135×  home.comcast.net                    | Model: Legit (0)    | Prawda: Phishing (1)
     121×  sites.google.com                    | Model: Phishing (1) | Prawda: Legit (0)
      82×  pastehtml.com                       | Model: Legit (0)    | Prawda: Phishing (1)
      71×  painterspaintings.com               | Model: Legit (0)    | Prawda: Phishing (1)
      61×  globetrotter-games.com              | Model: Phishing (1) | Prawda: Legit (0)
      51×  fibtex.lodz.pl                      | Model: Phishing (1) | Prawda: Legit (0)
      41×  s.yam.com                           | Model: Legit (0)    | Prawda: Phishing (1)
      38×  "http:                              | Model: Phishing (1) | Prawda: Legit (0)