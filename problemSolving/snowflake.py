def generate_snowflake(n):
    # Create an n x n matrix filled with "."
    matrix = [["." for _ in range(n)] for _ in range(n)]

    mid_row = n // 2
    for j in range(n):
        matrix[mid_row][j] = "*"

    mid_col = n // 2
    for i in range(n):
        matrix[i][mid_col] = "*"

    for i in range(n):
        matrix[i][i] = "*"
        matrix[i][n - i - 1] = "*"

    return matrix
n = int(input("Enter an odd number: "))
snowflake = generate_snowflake(n)

for row in snowflake:
    print(" ".join(row))
