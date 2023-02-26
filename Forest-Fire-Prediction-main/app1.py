import pandas as pd
import pickle
import joblib
model=joblib.load('forestfiremodel.pkl')
df=pd.read_csv("manasvi.csv")
x=df[["FFMC","DMC","DC","ISI","temp","RH","wind","rain"]].values
y=(model.predict_proba(x))
df["predict_proba"]=y[:,1]
print(df.to_html())