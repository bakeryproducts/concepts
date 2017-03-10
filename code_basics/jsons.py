#exporting and importing to JSON
peoples = {}

peoples['p1'] = {'name':'katat','age':13}
peoples['p2']={'name':'Andrew','age':21}

print peoples                   #type dict

import json

st = json.dumps(peoples)        #type string
print st

with open('testing.txt','w') as f:
    f.write(st)

with open('testing.txt','r') as f:
    tmp = f.read()
    new_st = json.loads(tmp)

print type(new_st)