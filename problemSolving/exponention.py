def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n - 1)
a = float(input("Enter the base: "))
n = int(input("Enter the exponent: "))
result = power(a, n)
print(result)
