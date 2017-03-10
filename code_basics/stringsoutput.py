#string formatting
person = {'name': 'Mike', 'age': 13}


#numeric callouts for arguments in dict
print('{1} ---{0[name]}--- {1}'.format(person,person['age']))


#cool way to print dictionary
print('{name} is {age}'.format(**person))


#decimal
pi = 3.1415926
ee = 2
print('{:.4f}'.format(pi))

print('{:03}'.format(ee))
