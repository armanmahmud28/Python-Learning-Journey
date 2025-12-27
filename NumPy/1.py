import numpy as nn
arr = nn.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))
print(arr.ndim)

for i in arr:
    for j in i:
        print(j)
