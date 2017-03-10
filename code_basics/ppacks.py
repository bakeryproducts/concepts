from struct import *

packed_data = pack('iif', 2, 3, .22)
print(packed_data)

print(calcsize('iif'))

org = unpack('iif',packed_data)
print(org)

