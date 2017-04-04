# K NN test on cancer data
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
    confid = Counter(votes[:k]).most_common(1)[0][1]/k
    return vote,confid*100

df = pd.read_csv('cancer_data.csv')
df.replace('?',-99999,inplace=True)
df.drop(['id'],1,inplace=True)
full_data = df.astype(float).values.tolist()

accs = []
for _ in range(25):
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
            vote,conf = knn(trainset,data,k=5)
            #print(int(vote),' guess by {:.1f} but is '.format(conf),int(group),end='')
            if group == vote:
                correct+=1
            #    print()
            #else:print('\t WRONG')
            total+=1
    accs.append(correct/total)
    #print(correct/total)

print(accs)
print(sum(accs)/len(accs))

#0.964028776978417          x25