from ctypes import sizeof
from sys import getsizeof


a = b'atilio\n'
print(a[6])
print(getsizeof(a))

cad = str(97)
print(cad.encode('ascii'))


