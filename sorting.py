import random

li = [random.randint(-10, 10) for _ in range(10)]
print(li, '  origin list')

# new list
# s_li = sorted()  # reverse = True

# sort in place
li.sort(reverse=True)

# sort by abs value
s_li = sorted(li, key=abs)

print(li, '  sorted origin list')
print(s_li, '  sorted in new list')

# dict
names = ['clark', 'bruce', 'peter', 'wade']
identity = ['superman', 'batman', 'spiderman', 'deadpool']

reveal = {name: hero for name, hero in zip(names, identity)}

print(reveal)
print(sorted(reveal))  # sorted() - by keys

# sort in object of class
from operator import attrgetter


class Person:
    def __init__(self, age, name, iq):
        self.age = age
        self.name = name
        self.iq = iq

    def __repr__(self):
        return '{} is {} and iq is {}'.format(self.name, self.age, self.iq)


p1 = Person(19, 'AJack', 120)
p2 = Person(15, 'Mary', 90)
p3 = Person(49, 'CGranny', 160)

ps = [p1, p2, p3]

#lambda key
s1_ps = sorted(ps, key=lambda p: p.age)


#attrgetter key from operator
s2_ps = sorted(ps, key=attrgetter('age'))

print (s2_ps)
