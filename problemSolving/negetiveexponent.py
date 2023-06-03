def power(a, n):
    result = 1
    if n > 0:
        for _ in range(n):
            result *= a
    elif n < 0:
        for _ in range(abs(n)):
            result /= a
    return result
a = float(input("Enter the base: "))
n = int(input("Enter the exponent: "))
result = power(a, n)

print(result)
