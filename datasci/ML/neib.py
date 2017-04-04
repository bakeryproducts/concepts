# KNN
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import preprocessing, neighbors
from sklearn.model_selection import train_test_split

df = pd.read_csv('cancer_data.csv')
df.drop(['id'], 1, inplace=True)
df.replace('?', 0, inplace=True)

#df = df.drop([12])

X = df.drop('class',1)
#X = df[['clump', 'cell_size']]
y = df['class']

#   1041801,5,3,3,3,2,3,4,4,1,4
# test_data = np.array([5,3,3,3,2,3,4,4,1])
#test_data = np.array([5, 3])
#test_data = test_data.reshape(1, -1)
nn=30
mm=100
acc = np.empty([mm])
accmean=[]
pred = []

for i in range(nn):
    for j in range(mm):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2)
        clf = neighbors.KNeighborsClassifier(n_neighbors=2*i+1)
        clf.fit(X_train, y_train)
        acc[j] = clf.score(X_test, y_test)
     #   pred.append(clf.predict(test_data)[0])
    accmean.append(np.mean(acc))

#print(pred.count(4) / len(pred))
print(np.mean(acc))
plt.plot(accmean)
plt.show()
# x4 = df.loc[df['class'] == 4]
# x4 = x4[['clump', 'cell_size']]
# x2 = df.loc[df['class'] == 2]
# x2 = x2[['clump', 'cell_size']]
#
#
# plt.scatter(x2['clump'], x2['cell_size'],color='b')
# plt.scatter(x4['clump'], x4['cell_size'],color='r')
# plt.show()
