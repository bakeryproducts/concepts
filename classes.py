class Pet:
    def __init__(self,name,age):
        self.name= name
        self.age = age
    def talk(self):
        raise NotImplementedError('im an Abstract class you dummy!')

class Dog(Pet):
    def talk(self):
        print('imma doggo called '+ str(self.name))

jack = Dog('Jack',3)

#jack.talk()
pet = Pet('wtf',0)
#pet.talk() # error abstraction


class testi(dict):
    _history=[]
    def set(self,key,value):
        testi._history.append(key)
        self[key]=value

    def get_hist(self):
        return self._history

a = testi({'foo':99})
a.set('bar',98)
print(a.get_hist())
print(a['bar'])
a=testi()
a.set('car',9)
print(a.get_hist())         # history shares trough class

# print(testi.__dict__)
# print(a.__class__)
# print(testi.__class__)


class Bigdatamodel:
    def __init__(self):
        self._params=[]

b = Bigdatamodel()
b.params=[1,2]
print(b.params)