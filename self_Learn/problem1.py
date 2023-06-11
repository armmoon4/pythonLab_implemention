import numpy as np
arr = np.array([[4, 2, 7],
                [9, 5, 8]])

minover1 = np.min(arr, axis=1)
max_of_min = np.var(minover1)
print(minover1)
print(max_of_min)
