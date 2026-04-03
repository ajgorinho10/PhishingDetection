from Set_Processor import ImportData

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import TensorDataset, DataLoader

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

import numpy as np



class LSTM(nn.Module):
    def __init__(self, first_layer = 32, max_len = 50):
        super(LSTM,self).__init__()
        
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.slownik = None
        self.vocab_size = None
        self.embed_dim = first_layer
        self.max_len = max_len
        
        #Zamian liczby na wektor o rozmiarze 64
        self.embanding = None
        
        #Warstwa LSTM
        self.lstm = nn.LSTM(
            input_size=first_layer,
            hidden_size=first_layer*2,
            num_layers=2,
            bias=True,
            batch_first=True,
            dropout=0.2,
            bidirectional=True
            )
        
        self.dropout = nn.Dropout(0.2)
        
        #Warstwa klasyfikacji
        self.linear1 = nn.Linear(
            in_features=first_layer*4,
            out_features=first_layer//2
            )
        
        self.linear2 = nn.Linear(
            in_features=first_layer//2,
            out_features=1
            )
        
    def forward(self,x):
        x = self.embanding(x)
     
        lstm_out, (h_n, c_n) = self.lstm(x)
        #print(h_n.shape)
        #rint(h_n[-2].shape)
        #print(h_n[-1].shape)
        x = torch.cat((h_n[-2], h_n[-1]), dim=1)
        #print(x.shape)
        #print("\n")
        

        x = self.dropout(x)
        x = self.linear1(x)
        x = self.dropout(x)
        x = self.linear2(x)
        
        return F.sigmoid(x)
    
    
    
    def tokenize(self, data):
        surowe_znaki = "abcdefghijklmnopqrstuvwxyz0123456789-,;.!?:'\"/\\|_@#$%^&*~`+-=<>()[]{}"
        unikalne_znaki = list(set(surowe_znaki))

        char_to_int = {c: i+1 for i, c in enumerate(sorted(unikalne_znaki))} if self.slownik is None else self.slownik
        self.slownik = char_to_int

        self.vocab_size = len(unikalne_znaki) + 1
        self.embanding = nn.Embedding(self.vocab_size, self.embed_dim)

        X_sequences = []
        for url in data:
            seq = [char_to_int.get(c.lower(),0) for c in url]

            seq = seq[:self.max_len]

            if len(seq) < self.max_len:
                seq += [0]* (self.max_len - len(seq))
            X_sequences.append(seq)

        return X_sequences
    
    
    def prepare_data_to_trening(self, X, y):
        
        #Tokenizacja adresów url
        X_tokenized = self.tokenize(X)
        
        #Podział zbioru danych
        X_train, X_test, y_train, y_test = train_test_split(X_tokenized, y, test_size = 0.3, random_state = 42)
        
        #Zamiana na tesory
        X_train_tesnor = torch.tensor(X_train,dtype=torch.long)
        X_test_tesnor = torch.tensor(X_test,dtype=torch.long)
        
        y_train_tesnor = torch.tensor(y_train.values,dtype=torch.float32).view(-1,1)
        y_test_tesnor = torch.tensor(y_test.values,dtype=torch.float32).view(-1,1)
        
        return X_train_tesnor,X_test_tesnor,y_train_tesnor,y_test_tesnor
    
    
    def train_model(self, X, y, epochs, save_model = False):
        X_train, X_test, y_train, y_test = self.prepare_data_to_trening(X, y)
        
        trainDataSet = TensorDataset(X_train,y_train)
        trainDataLoader = DataLoader(trainDataSet, batch_size=128, shuffle=True)
        print(f"Dane: OK!")
        
        self.to(self.device)
        print(f"Deviec: {self.device}")
        
        optimalizer = torch.optim.Adam(self.parameters(), lr = 0.001)
        loss_f = nn.BCELoss()
        
        for epoch in range(epochs):
            self.train()
            running_loss = 0.0
            
            for batch_X, batch_y in trainDataLoader:
                batch_X, batch_y = batch_X.to(self.device), batch_y.to(self.device)
                
                optimalizer.zero_grad()
                output = self(batch_X)
                loss = loss_f(output,batch_y)
                loss.backward()
                optimalizer.step()
                
                running_loss += loss.item()
                
            print(f" Epoch [{epoch+1}/{epochs}] Loss: {running_loss/len(trainDataLoader):.3f}")
            
            
        print(f"Trening zakonczony !")
        
        testDataSet = TensorDataset(X_test,y_test)
        testDataLoader = DataLoader(testDataSet,batch_size = 128, shuffle = False)
        
        
        wszystkie_predykcje = []
        wszystkie_etykiety = []
        
        self.eval()
        with torch.no_grad():
            for batch_X,batch_y in testDataLoader:
                batch_X, batch_y = batch_X.to(self.device), batch_y.to(self.device)
                
                output_raw = self(batch_X)
                output = output_raw.round().cpu().numpy()
                
                wszystkie_predykcje.extend(output)
                wszystkie_etykiety.extend(batch_y.cpu().numpy())
            
        
        print(f"Raport")
        print(classification_report(wszystkie_etykiety,wszystkie_predykcje))
        print(confusion_matrix(wszystkie_etykiety,wszystkie_predykcje))
        
        
        if save_model:
           torch.save(self.state_dict(),"models/LSTM_v1.pth")
                
        
    def predicts(self, url):
        url_tokenized = self.tokenize([url])
        url_tensor = torch.tensor(url_tokenized)
        
        self.load_state_dict(torch.load("models/LSTM_v1.pth"))
        self.eval()
        with torch.no_grad():
            return (self(url_tensor).item())
        
    def test_at_diffrent_dataset(self, X, y):
        
        X_tokenized = self.tokenize(X)
        X_tensor = torch.tensor(X_tokenized, dtype=torch.long)
        y_tensor = torch.tensor(y.values, dtype=torch.float32).view(-1,1)
        
        dataset = TensorDataset(X_tensor,y_tensor)
        dataLoader = DataLoader(dataset,batch_size=128)
        
        wszystkie_predykcje = []
        wszystkie_etykiety = []
        
        self.load_state_dict(torch.load('models/LSTM_v1.pth'))
        self.to(self.device)
        self.eval()
        
        with torch.no_grad():
            for batch_X,batch_y in dataLoader:
                    batch_X, batch_y = batch_X.to(self.device), batch_y.to(self.device)
                    
                    output_raw = self(batch_X)
                    output = output_raw.round().cpu().numpy()
                    
                    wszystkie_predykcje.extend(output)
                    wszystkie_etykiety.extend(batch_y.cpu().numpy())
            
        
        print(f"Raport")
        print(classification_report(wszystkie_etykiety,wszystkie_predykcje))
        print(confusion_matrix(wszystkie_etykiety,wszystkie_predykcje))
        
    


if __name__ == "__main__":
    
    #data = ImportData()
    #data.Import_set_3()
    #X_data, y_data = data.Get_NLP()
    
    lstm = LSTM()
    #lstm.train_model(X=X_data, y=y_data, epochs=15,save_model=True)
    print(lstm.predicts("LokalizatorOrange.pl/lokalizuje8"))
    #lstm.test_at_diffrent_dataset(X_data,y_data)