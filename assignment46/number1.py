import numpy as np

arr = np.array([[4, 2, 7],
                [1, 6, 3],
                [9, 5, 8]])

min_over_axis_1 = np.min(arr, axis=1)  # Perform min over axis 1
max_of_min = np.max(min_over_axis_1)  # Find the max of the min values

print("Original array:")
print(arr)
print("Minimum values over axis 1:")
print(min_over_axis_1)
print("Maximum value of the minimum values:")
print(max_of_min)
