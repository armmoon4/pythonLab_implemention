def calculate_days(x, y):
    distance = x
    days = 1

    while distance < y:
        distance += distance * 0.1
        days += 1

    return days
x = int(input())
y = int(input())
result = calculate_days(x, y)
print(result)
