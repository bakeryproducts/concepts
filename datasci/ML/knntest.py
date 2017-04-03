import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
from matplotlib import style
from collections import Counter
style.use('fivethirtyeight')

def knn(data,predict,k=1):
    distances=[]
    for group in data:
        for point in data[group]:
            dist = np.linalg.norm(np.array(point)-np.array(predict))
            distances.append((dist,group))
    votes=np.array(sorted(distances))[:,1]
    vote = Counter(votes[:k]).most_common(1)[0][0]
    return vote

df = pd.read_csv('cancer_data.csv')
df.replace('?',-99999,inplace=True)
df.drop(['id'],1,inplace=True)
full_data = df.astype(float).values.tolist()
random.shuffle(full_data)

testsize=.2
trainset={2:[],4:[]}
testset={2:[],4:[]}

l = int(len(full_data)*testsize)
traindata=full_data[:-l]
testdata=full_data[-l:]

for i in traindata:
    trainset[i[-1]].append(i[:-1])

for i in testdata:
    testset[i[-1]].append(i[:-1])

correct = 0
total=0

for group in testset:
    for data in testset[group]:
        vote = knn(trainset,data,k=3)
        print(int(vote),end='')
        if group == vote:
            correct+=1
        total+=1

print(correct/total)
