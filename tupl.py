# namedtuple
from collections import namedtuple

Person = namedtuple('Person',['name','age'])

p = Person('George','24')

print(p.age)
print(p.name)

print(p._asdict())
p2 = p._replace(name='bill')

print(p,p2)