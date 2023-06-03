import numpy as np

# Create a 3D array filled with zeros
array_3d = np.zeros((4, 3, 2))

# Extract the middle and right corner 2 rows
middle_rows = array_3d[1:3, :, :]
right_corner_rows = array_3d[-2:, :, :]

# Print the results
print("Middle rows:")
print(middle_rows)
print("\nRight corner rows:")
print(right_corner_rows)
