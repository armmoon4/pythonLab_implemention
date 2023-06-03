def smallest_divisor(n):
    divisor = 2
    while n % divisor != 0:
        divisor += 1
    return divisor

n = int(input("Enter an integer greater than or equal to 2: "))
result = smallest_divisor(n)
print(result)
