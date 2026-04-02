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
                        
                                   0       0.93      0.96      0.94    128378
                                   1       0.95      0.92      0.93    110106
                        
                            accuracy                           0.94    238484
                           macro avg       0.94      0.94      0.94    238484
                        weighted avg       0.94      0.94      0.94    238484
                        
                        Macierz Pomyłek:
                        [[122747   5631]
                         [  8847 101259]]
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
                        
                                   0       0.97      0.94      0.95    128378
                                   1       0.93      0.96      0.95    110106
                        
                            accuracy                           0.95    238484
                           macro avg       0.95      0.95      0.95    238484
                        weighted avg       0.95      0.95      0.95    238484
                        
                        Macierz Pomyłek:
                        [[120436   7942]
                         [  4324 105782]]
```

### CECHY
```text
                                      precision    recall  f1-score   support
                        
                                   0       0.86      0.62      0.72     73593
                                   1       0.73      0.92      0.82     85396
                        
                            accuracy                           0.78    158989
                           macro avg       0.80      0.77      0.77    158989
                        weighted avg       0.79      0.78      0.77    158989
                        
                        
                        Macierz Pomyłek (XGBoost):
                        [[45302 28291]
                         [ 7179 78217]]
```


# MLP
## SciLearn
### NLP(TF-IDF) (100->1)
```text
                                  precision    recall  f1-score   support
                    
                               0       0.96      0.97      0.96     85396
                               1       0.96      0.95      0.96     73593
                    
                        accuracy                           0.96    158989
                       macro avg       0.96      0.96      0.96    158989
                    weighted avg       0.96      0.96      0.96    158989
                    
                    Macierz Pomyłek:
                    [[82781  2615]
                     [ 3392 70201]]
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
                    
                             0.0       0.97      0.97      0.97    128378
                             1.0       0.96      0.96      0.96    110106
                    
                        accuracy                           0.97    238484
                       macro avg       0.97      0.97      0.97    238484
                    weighted avg       0.97      0.97      0.97    238484
                    
                    Macierz Pomyłek:
                    [[124224   4154]
                     [  4096 106010]]
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
                                     
                             0.0       0.98      0.99      0.98    128378                
                             1.0       0.98      0.97      0.98    110106
                    
                        accuracy                           0.98    238484                 
                       macro avg       0.98      0.98      0.98    238484                   
                    weighted avg       0.98      0.98      0.98    238484
                    
                    Macierz Pomyłek:
                    [[126659   1719]
                     [  3080 107026]]
```

# Bi-LSTM
```text
                                  precision    recall  f1-score   support
                    
                             0.0       0.98      0.98      0.98    128378
                             1.0       0.98      0.97      0.98    110106
                    
                        accuracy                           0.98    238484
                       macro avg       0.98      0.98      0.98    238484
                    weighted avg       0.98      0.98      0.98    238484
                    
                    Macierz Pomyłek:
                    [[126217   2161]
                     [  2874 107232]]

```

# DistilBERT
transformer-based language models
```text
F1-Score:  0.9851
Precision: 0.9898
Recall:    0.9805


MACIERZ POMYŁEK (TRANSFORMER):
[[127269   1109]
 [  2149 107957]]
```