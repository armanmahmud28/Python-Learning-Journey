import numpy as np

array = np.array([1, 2, 3])
array *= 3

print(type(array))

array = np.array([['a', 'b'],
                  ['a', 'b']])

print(array.ndim)
print(array.shape)


print(array[0, 1])
