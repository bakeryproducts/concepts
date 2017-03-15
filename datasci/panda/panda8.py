# pandas rolling stats
import pandas as pd
import matplotlib.pyplot as plt

fig = plt.figure()
ax1=plt.subplot2grid((2,1),(0,0))
ax2=plt.subplot2grid((2,1),(1,0),sharex=ax1)

df = pd.read_pickle('HPI_states')
df_tx = df['TX'].rename('TX_HPI')
df_txa = df_tx.resample('A').mean()
df_mean=pd.rolling_mean(df_tx,12).rename('mean')
df_std = pd.rolling_std(df_tx,12).rename('std')

dfm = pd.concat([df_tx,df_mean,df_std],axis=1)  # df from series
#dfm.dropna(inplace=True)                # drops NAN from DF
#dfm.fillna(method='ffill',inplace=True) # fill NANS  forwards
#dfm.fillna(method='bfill',inplace=True) # fill NANS  backwards
# also can do value= -9999
dfm = pd.DataFrame(dfm)

dfm[['TX_HPI','mean']].plot(ax=ax1)
dfm['std'].plot(ax=ax2)
print(dfm.head())
plt.legend(loc=4)
plt.show()
