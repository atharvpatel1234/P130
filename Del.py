import csv 
import pandas as pd 

df=pd.read_csv("Data.csv")
print(df.shape)

del df["Luminosity"]
del df["Star_name"]
del df["Distance"]
del df["Mass"]
del df["Radius"]
print(df.shape)

df.to_csv('Main.csv')