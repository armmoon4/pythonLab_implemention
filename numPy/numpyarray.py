import numpy as np
arr = np.array([[1 , 2 , 3 ] , [4 , 5 , 6] , [ 7 , 8, 9]])
print(arr)
print(type(arr))

print("diminsion print")

a = np.array([1, 2, 3, 4, 5])
b = np.array([[1, 2, 3], [4, 5, 6]])
c = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)