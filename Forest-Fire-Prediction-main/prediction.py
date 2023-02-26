import numpy as np
import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib

df=pd.read_csv('forestfires.csv')

df=df.drop(['X','Y','month','day'],axis=1)

def preprocessing(df):
    df=df.copy()
    
    Y=df['area'].apply(lambda x: 1 if x>0 else 0)

    X=df.drop('area',axis=1)

    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,train_size=0.60,shuffle=True,random_state=0)

    scaler=StandardScaler()
    scaler.fit(X_train)
    #standardized^ input feature.
    #used classification 

    X_train=pd.DataFrame(scaler.transform(X_train),columns=X.columns)
    X_test=pd.DataFrame(scaler.transform(X_test),columns=X.columns)

    return X_train,X_test,Y_train,Y_test


X_train,X_test,Y_train,Y_test=preprocessing(df)

#instantiate mlp
nn_classifier_model=MLPClassifier(activation='relu',hidden_layer_sizes=(16,16),n_iter_no_change=100,solver='adam')
nn_classifier_model.fit(X_train,Y_train)
#python object is stored as pkl file , basically the content.
model=joblib.dump(nn_classifier_model,'forestfiremodel.pkl')
#model=open(r"D:\sabni\Documents\GitHub\Forest-Fire-Prediction-main\Forest-Fire-Prediction-main\forestfiremodel.pkl")

#multilayer perceptron classifier (mlp), learning rate =0.001,  run until no changes is observed for 100 iteration, hidden layer =16 , neuron-16
#targeted var = area , on the basis of which fire is predicted.




