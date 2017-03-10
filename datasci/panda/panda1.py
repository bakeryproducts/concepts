# all about pandas

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import pandas_datareader.data as web
from matplotlib import style

style.use('ggplot')


start = datetime.datetime(2010,1,1)
end = datetime.datetime(2015,1,1)

web_stats={'day' : [1,2,3,4,5],
           'visitors':[43,25,65,34,75],
            'rate':[76,23,76,45,21]
            }

df = pd.DataFrame(web_stats)    # converts to table

print(df)
#print(df.tail(2))       # return last 2 of data
#df = web.DataReader('XOM','yahoo',start,end)

#print(df.head())        # head of data, like first five rows or smth
#df['Adj Close'].plot()  # column

newdf = df.set_index('day')         # as said
#df.set_index('day',inplace=True)   # set index in df themself
#print(newdf)
#print(df['rate'])            # calls column
#print(df.rate)               # calls like attr
#print(df[['day','rate']])    # several c's

#print(df.rate.tolist())
#a = np.array(df[['day','rate']])
#print(a)

#custdf = pd.DataFrame(a)
#print(custdf)

#plt.show()

