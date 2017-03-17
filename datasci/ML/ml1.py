# ML google stock
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import quandl
import math
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

api_key = open('api.txt', 'r').read()
quandl.ApiConfig.api_key = api_key
# df = quandl.get('WIKI/GOOGL')
# df.to_pickle('googl')
df = pd.read_pickle('googl')
df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]
df.columns = ['AO', 'AH', 'AL', 'AC', 'AV']

df['HL_PCT'] = 100 * (df['AH'] - df['AL']) / df['AL']
df['OC_PCT'] = 100 * (df['AC'] - df['AO']) / df['AO']
df = df[['AC', 'HL_PCT', 'OC_PCT', 'AV']]
# df.fillna(-99999,inplace=True)


forecast_col = 'AC'
forecast_shift = int(math.ceil(len(df) * .01))
df['Y'] = df[forecast_col].shift(-forecast_shift)
df.dropna(inplace=True)

X = np.array(df.drop('Y', axis=1))
# print(df.drop(['AV','AC'],axis=1))

y = np.array(df['Y'])

X = preprocessing.scale(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2)

clf = svm.SVR()
# clf = LinearRegression()
clf.fit(X_train, y_train)
acc = clf.score(X_test, y_test)

print(acc)
df.plot()
# plt.show()
