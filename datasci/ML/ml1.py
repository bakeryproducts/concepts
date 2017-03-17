# 1 in ML, google stocks analysis
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import quandl

api_key= open('api.txt','r').read()
quandl.ApiConfig.api_key=api_key
# df = quandl.get('WIKI/GOOGL')
# df.to_pickle('googl')
df = pd.read_pickle('googl')
df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]
df.columns=['AO','AH','AL','AC','AV']

df['HL_PCT'] = 100*(df['AH']-df['AL'])/df['AL']
df['OC_PCT'] = 100*(df['AC']-df['AO'])/df['AO']

df = df[['AC','HL_PCT','OC_PCT','AV']]

print(df['AV'].describe())

df.plot()
plt.show()
