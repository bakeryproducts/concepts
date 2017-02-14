'''
legend
\d any number
\D anything but number
\s space
\S !space
\w any character
\W !char
. any char bu not newline
\b whitespace around words
\. a period

modifiers
{1,3}
+ match 1 or more
?       0 or 1
*       0 or more
$       end of string
^       beginning
[]  range or variance [A-Z]

'''

import re

exstring = '''
Jessica is 15 years old and Daniel is 27 years old
Edward is 97 and his grandfather Oscar is 102
'''

ages = re.findall(r'\d{1,3}',exstring)
names = re.findall(r'[A-Z][a-z]*',exstring)

data = {name:age for name,age in zip(names,ages)}
print(data)

