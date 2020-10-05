import numpy as np
import pandas as pd

#set pandas default number format

algae=pd.read_csv("homework1/homework1/algae.txt",delimiter=' ')
df = pd.DataFrame(data=algae)

print(df)

print(df.groupby('speed').agg({'speed':'size'}))

meanvar = pd.DataFrame()
df2=df.drop(['season','size','speed','a1'],axis=1)
meanvar["mean"]=(df2.mean())
meanvar["var"]=(df2.var().round(decimals=4))

#change formatting
with pd.option_context('display.float_format', '{:.4f}'.format):
    print(meanvar)
