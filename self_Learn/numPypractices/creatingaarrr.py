import numpy as np
arr = np.array([[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]])
print(arr)
print(type(arr))
print(arr.ndim)
print("Printing Specific Value:")
print(arr[0, 2, 1])
print(arr[0, 2, 1:5])