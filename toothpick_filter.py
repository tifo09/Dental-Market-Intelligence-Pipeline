import pandas as pd
import numpy as np
import re

df= pd.read_csv("toothpick.csv")

df["price"]=df["price"].astype(str).str.replace("EGP","")
df["price"]=df["price"].astype(str).str.replace(",","")
df["price"]=pd.to_numeric(df["price"],'coerce')
df["brand"]=df["brand"].fillna("unknown")
df=df.dropna(subset=['price'])
df["price_category"]=np.where(df["price"]>500,'expensive','affordable')
df["category"]=df["category"].astype(str).str.replace(r'(?<=[a-z])(?=[A-Z])',' ',regex=True) 

df.to_csv('cleaned_tp.csv',index=False)

print(df.head(4))

#print(df["price"].dtype)



