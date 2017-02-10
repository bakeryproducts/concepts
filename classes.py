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

jack.talk()
pet = Pet('wtf',0)
#pet.talk() # error abstraction

