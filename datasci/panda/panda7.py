
import pandas as pd
import matplotlib.pyplot as plt
import quandl

akey = open('api.txt','r').read()
quandl.ApiConfig.api_key=akey
#df2 = quandl.get('FMAC/HPI_USA')
#print(df2.head())


df = pd.read_pickle('HPI_states')
#df1=df.pct_change()

for col in df:
    df[col]=100*(df[col]-df[col][0])/df[col][0]


hpi_corr = df.corr()
print(hpi_corr)
print(hpi_corr.describe())

df.plot()
plt.legend().remove()
#plt.show()