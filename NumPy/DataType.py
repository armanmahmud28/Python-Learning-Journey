import numpy as np

arr = np.array([1.1, 1.2, 1.3, 1.4])

newarr = arr.astype('i')
print(newarr)
new = arr.astype('u')
print(new)
print(new.dtype)
