import quandl
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

#url = 'https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States'
#df1 = pd.read_html(url)
#df1 = df1[0][1]
#pd.to_pickle(df1,'states')

df1 = pd.read_pickle('states')
states_df=df1.drop([0,1])

main_df = pd.DataFrame()
api_key = open('api.txt','r').read()
quandl.ApiConfig.api_key=api_key

for state in states_df:

    df = quandl.get('FMAC/HPI_'+str(state))
    df.rename(columns={'Value':str(state)},inplace=True)

    if main_df.empty:
        main_df=df
    else:
        main_df = pd.concat([main_df,df],axis=1)

main_df.to_pickle('HPI_states')
print(main_df.head())
# df = pd.read_pickle('picklesaveDF')
# df['Value_3'] = df['Value_2']*1.1       # new column
# #df.pct_change()                         # percentages
# df['pp']=100* (df['Value_3']-df['Value_3'][0])/df["Value_3"][0]                      #percentages
#
# print(df.head())
#
# df['pp'].plot()
# plt.legend().remove()
# plt.show()