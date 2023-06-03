def find_max_position(matrix):
    max_element = float('-inf')
    max_position = (0, 0)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > max_element:
                max_element = matrix[i][j]
                max_position = (i, j)

    return max_position

rows, cols = map(int, input("Enter the number of rows and columns (separated by a space): ").split())
matrix = []

for _ in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

max_position = find_max_position(matrix)
print(max_position[0], max_position[1])
