import numpy as np
arr = np.array([[1,2,3],[4,5,6]])
print(arr)
print(arr.shape)
print(arr.size)
print(arr.itemsize)

print('reshape:  ')
ressshape = np.reshape(arr,(3,2))
print(ressshape)

print('transpose: ')
trrrrrr = np.transpose(arr)
print(trrrrrr)