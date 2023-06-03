import math
# Step 1: Input area of the square
area_of_square = float(input("Enter the area of the square: "))
# Step 2: Calculate side length of the square
side_length = math.sqrt(area_of_square)
# Step 3: Calculate radius of quarter circle
radius = side_length / 2
# Step 4: Calculate area of one quarter circle
area_of_quarter_circle = math.pi * radius**2 / 4
# Step 5: Calculate area of all four quarter circles
area_of_four_quarter_circles = 4 * area_of_quarter_circle
# Step 6: Calculate area of shaded region
area_of_shaded_region = area_of_square - area_of_four_quarter_circles
# Step 7: Calculate perimeter of shaded region
perimeter_of_shaded_region = (4 * side_length) + (2 * math.pi * radius)
# Step 8: Print the calculated area and perimeter of the shaded region
print("Area of the shaded region:", area_of_shaded_region)
print("Perimeter of the shaded region:", perimeter_of_shaded_region)
