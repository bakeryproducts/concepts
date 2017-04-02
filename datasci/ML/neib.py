import pandas as pd
import matplotlib
import numpy as np
from sklearn import preprocessing,neighbors
from sklearn.model_selection import train_test_split

df = pd.read_csv('cancer_data.csv')
df.drop(['id'],1,inplace=True)
df.replace('?',-99999,inplace=True)

df= df.drop([12])

X = df.drop('class',1)
y = df['class']

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=.2)

print(len(X_train)/len(X_test))

clf = neighbors.KNeighborsClassifier()
clf.fit(X_train,y_train)
acc = clf.score(X_test,y_test)

#   1041801,5,3,3,3,2,3,4,4,1,4
test_data = np.array([5,3,3,3,2,3,4,4,1])
test_data=test_data.reshape(1,-1)
pred = []
for _ in range(50):
    pred_i = clf.predict(test_data)
    pred.append(pred_i[0])

print(acc,pred)
