current_row = int(input())
current_col = int(input())
destination_row = int(input())
destination_col = int(input())

if current_row == destination_row:
    print('YES')
elif current_col == destination_col:
    print('YES')
else:
    print('NO')
