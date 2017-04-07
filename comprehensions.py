# comprehensions in dict

names = ['clark', 'bruce', 'peter', 'wade']
identity = ['superman', 'batman', 'spiderman', 'deadpool']

reveal = {name: hero for name, hero in zip(names, identity)}
# print(reveal)

# generators
li = [n + 1 for n in range(10)]
print(li)

#
# def gen_foo(nums):
#     for i in nums:
#         yield i * i
#
# my_gen = gen_foo(li)

my_gen = (i*i for i in li )

for i in my_gen:
    print i

# also packs and unpacks
a,*b = 'SPAM'
# a = 'S' and b = ['P','A','M'] ?
