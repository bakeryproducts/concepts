# Quandl api  and pandas

import quandl
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# api_key = open('api.txt','r').read()
# quandl.ApiConfig.api_key=api_key
# df = quandl.get_table("WIKI/PRICES")
# df.to_csv('test.csv')

df = pd.read_csv('test.csv',usecols=(1,2,4,5))
#print(df.head(2))
newdf = df[['date','high','low']]

s = pd.Series(['newdate',55,35],index = ['date','high','low'])
print(newdf.tail(2))
moddf = newdf.append(s,ignore_index=True)
print(moddf.tail(2))