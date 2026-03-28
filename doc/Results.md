# Native-Bayes
### NLP(TF-IDF)
```text
                                      precision    recall  f1-score   support
                        
                                   0       0.94      0.99      0.96    402885
                                   1       0.86      0.58      0.69     58878
                        
                            accuracy                           0.93    461763
                           macro avg       0.90      0.78      0.83    461763
                        weighted avg       0.93      0.93      0.93    461763
                        
                        Macierz Pomyłek:
                        [[397374   5511]
                         [ 24863  34015]]
```

### CECHY
```text
                                      precision    recall  f1-score   support
                        
                                   0       0.91      0.96      0.93    403661
                                   1       0.60      0.38      0.47     62257
                        
                            accuracy                           0.88    465918
                           macro avg       0.76      0.67      0.70    465918
                        weighted avg       0.87      0.88      0.87    465918
                        
                        Macierz Pomyłek:
                        [[387989  15672]
                         [ 38517  23740]]
```

# SVM
### NLP(TF-IDF)
```text
                                      precision    recall  f1-score   support
                        
                                   0       0.96      0.99      0.98    402885
                                   1       0.93      0.75      0.83     58878
                        
                            accuracy                           0.96    461763
                           macro avg       0.95      0.87      0.91    461763
                        weighted avg       0.96      0.96      0.96    461763
                        
                        Macierz Pomyłek:
                        [[399748   3137]
                         [ 14673  44205]]
```

### CECHY
```text
                                      precision    recall  f1-score   support
                        
                                   0       0.90      0.99      0.94    403661
                                   1       0.78      0.32      0.45     62257
                        
                            accuracy                           0.90    465918
                           macro avg       0.84      0.65      0.70    465918
                        weighted avg       0.89      0.90      0.88    465918
                        
                        Macierz Pomyłek:
                        [[397962   5699]
                         [ 42399  19858]]
```

# Drzewa
## RandomForest

### NLP(TF-IDF)
```text
                                      precision    recall  f1-score   support
                        
                                   0       0.93      1.00      0.96    268465
                                   1       0.99      0.49      0.66     39377
                        
                            accuracy                           0.93    307842
                           macro avg       0.96      0.74      0.81    307842
                        weighted avg       0.94      0.93      0.92    307842
                        
                        Macierz Pomyłek:
                        [[268285    180]
                         [ 20064  19313]]
```

### CECHY
```text
                                      precision    recall  f1-score   support
                        
                                   0       0.93      0.97      0.95    269171
                                   1       0.76      0.54      0.63     41441
                        
                            accuracy                           0.92    310612
                           macro avg       0.85      0.76      0.79    310612
                        weighted avg       0.91      0.92      0.91    310612
                        
                        
                        Macierz Pomyłek (Confusion Matrix):
                        [[262059   7112]
                         [ 19042  22399]]
```


## XGBoost
### NLP(TF-IDF)
```text
                                      precision    recall  f1-score   support
                        
                                   0       0.98      0.99      0.99    402885
                                   1       0.94      0.88      0.91     58878
                        
                            accuracy                           0.98    461763
                           macro avg       0.96      0.94      0.95    461763
                        weighted avg       0.98      0.98      0.98    461763
                        
                        Macierz Pomyłek:
                        [[399636   3249]
                         [  7116  51762]]
```

### CECHY
```text
                                      precision    recall  f1-score   support
                        
                                   0       0.95      0.95      0.95    269171
                                   1       0.66      0.64      0.65     41441
                        
                            accuracy                           0.91    310612
                           macro avg       0.80      0.80      0.80    310612
                        weighted avg       0.91      0.91      0.91    310612
                        
                        
                        Macierz Pomyłek (XGBoost):
                        [[255438  13733]
                         [ 14777  26664]]
```


# MLP
## SciLearn
### NLP(TF-IDF) (100->1)
```text
                                  precision    recall  f1-score   support
                    
                               0       0.98      0.99      0.99    268465
                               1       0.96      0.87      0.91     39377
                    
                        accuracy                           0.98    307842
                       macro avg       0.97      0.93      0.95    307842
                    weighted avg       0.98      0.98      0.98    307842
                    
                    Macierz Pomyłek:
                    [[266857   1608]
                     [  5169  34208]]
```

### CECHY (10->5->1)
```text
                                  precision    recall  f1-score   support
                    
                               0       0.93      0.98      0.95    269171
                               1       0.77      0.49      0.60     41441
                    
                        accuracy                           0.91    310612
                       macro avg       0.85      0.73      0.77    310612
                    weighted avg       0.90      0.91      0.90    310612
                    
                    
                    Macierz Pomyłek (Confusion Matrix):
                    [[263281   5890]
                     [ 21288  20153]]
```

## PyTorch
### NLP(TF-IDF) (256->64->16->1)
```text
                                  precision    recall  f1-score   support
                    
                             0.0       0.98      0.99      0.99    402885
                             1.0       0.95      0.88      0.92     58878
                    
                        accuracy                           0.98    461763
                       macro avg       0.97      0.94      0.95    461763
                    weighted avg       0.98      0.98      0.98    461763
                    
                    Macierz Pomyłek:
                    [[400068   2817]
                     [  6828  52050]]
```

### CECHY (256->64->16->1)
```text
                                  precision    recall  f1-score   support
                    
                             0.0       0.93      0.98      0.95    403661
                             1.0       0.79      0.50      0.62     62257
                    
                        accuracy                           0.92    465918
                       macro avg       0.86      0.74      0.78    465918
                    weighted avg       0.91      0.92      0.91    465918
                    
                    Macierz Pomyłek:
                    [[395351   8310]
                     [ 30819  31438]]
```

# CNN
Typ danych: Tokenizacja
## PyTorch
```text
                                  precision    recall  f1-score   support
                    
                             0.0       0.99      0.99      0.99    402885
                             1.0       0.96      0.91      0.94     58878
                    
                        accuracy                           0.98    461763
                       macro avg       0.97      0.95      0.96    461763
                    weighted avg       0.98      0.98      0.98    461763
                    
                    Macierz Pomyłek:
                    [[400579   2306]
                     [  5057  53821]]
```

# Bi-LSTM
```text
                                  precision    recall  f1-score   support
                    
                             0.0       0.99      1.00      0.99    402885
                             1.0       0.98      0.95      0.96     58878
                    
                        accuracy                           0.99    461763
                       macro avg       0.98      0.97      0.98    461763
                    weighted avg       0.99      0.99      0.99    461763
                    
                    Macierz Pomyłek:
                    [[401578   1307]
                     [  3099  55779]]

```

# DistilBERT
transformer-based language models
```text
F1-Score:  0.9763
Precision: 0.9867
Recall:    0.9662


MACIERZ POMYŁEK (TRANSFORMER):
[[402121    764]
 [  1993  56885]]
```