# advanced math

import random
import numpy

li = [random.randint(1, 10) for _ in range(10)]

print li

# import statistics  #not working ?

print numpy.mean(li)  # mean value
print numpy.std(li)  # standart deviation
print numpy.var(li)  # variance
