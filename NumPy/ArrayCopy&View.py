import numpy as np

arr = np.array([1, 2, 2, 4, 2, 5])
n = arr.copy()
print(f"array is: {n.base}")
arr[1] = 0
print(arr)
print(n)

a = np.array([5, 6, 7, 8, 9, 9])
m = a.view()
print(f"array is:{m.base}")
a[0] = 1
print(a)
print(m)
