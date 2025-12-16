import numpy as n

print(n.__version__)


array = n.array([1, 2, 3])
array *= 3

print(type(array))

array = n.array([['a', 'b'],
                ['a', 'b']])

print(array.ndim)
print(array.shape)
