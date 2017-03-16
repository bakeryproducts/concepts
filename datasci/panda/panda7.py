# pandas correlation  
import pandas as pd
import matplotlib.pyplot as plt
import quandl

def norm(x):
    for el in x:
        x[el]=100*(x[el]-x[el][0])/x[el][0]
    return x

akey = open('api.txt','r').read()
quandl.ApiConfig.api_key=akey
#df2 = quandl.get('FMAC/HPI_USA')
#mort = quandl.get('FMAC/MORTG',trim_start='1975-01-01')
#mort.to_pickle('mortg')

df_hpi = pd.read_pickle('HPI_states')
df_mort = pd.read_pickle('mortg')
df_mort.columns=['MORT']
#df1=df.pct_change()

df1=df_hpi
#df1=pd.DataFrame(df_hpi['TX'])

df_hpi = norm(df1)
df_mort=norm(df_mort)
df_mort=df_mort.resample('D').mean()
df_mort=df_mort.resample('M').mean()

df = df_hpi.join(df_mort)
hpi_corr = df_hpi.corr()
#print(hpi_corr)
#print(hpi_corr.describe())

dfm=df.corr()['AL']
print(dfm[1:].max(),dfm[1:].idxmax())
print(dfm)
df.plot()
plt.legend().remove()
#plt.show()

