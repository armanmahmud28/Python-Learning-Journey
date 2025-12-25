import numpy as np
print(np.__version__)

arr = np.array([[1, 2, 3, 4, 5],
                [1, 2, 3, 4, 5],
                [1, 2, 3, 4, 5]])
print(arr)
print(type(arr))
print()
print(f"This {arr.ndim}D Array.")

d = np.array([[[1, 2, 3],
               [4, 5, 6]],
              [[1, 2, 3],
               [4, 5, 6]]])
print(d)
print(f"This {d.ndim}D Array")
m = d.copy()
print(m)
