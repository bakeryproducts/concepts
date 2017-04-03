# KNN by hands
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from collections import Counter
style.use('fivethirtyeight')

def knn(data,predict,k=1):
    distances=[]
    for set_name,set_values in data.items():
        for point in set_values:
            dist = np.linalg.norm(np.array(point)-np.array(predict))
            distances.append((dist,set_name))
    votes=np.array(sorted(distances))[:,1]
    vote = Counter(votes[:k]).most_common(1)[0][0]
    return vote

n=20
a = np.random.rand(n,2)
b = .5+2*np.random.rand(n,2)
c = 1.5+2*np.random.rand(n,2)

dataset = {'r':a,'b':b,'g':c}
col1 = 'r'
col2 = 'b'
col3 = 'g'
#feature=np.array([2,2])
features = 3.5*np.random.rand(n,2)

for fpoint in features:
    cdecision = knn(dataset,fpoint,3)
    plt.scatter(fpoint[0], fpoint[1], color=cdecision, s=200, edgecolors='orange')

plt.scatter(a[:,0],a[:,1],color=col1)
plt.scatter(b[:,0],b[:,1],color=col2)
plt.scatter(c[:,0],c[:,1],color=col3)

plt.show()
