import numpy as np
# Create a 2D array
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
# Get the diagonal elements
diagonal = np.diagonal(arr)
# Print the diagonal elements
print(diagonal)
summation = diagonal.sum()
print(summation)