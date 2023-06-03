def find_exponent(N):
    x = 0
    power_of_2 = 1
    while power_of_2 * 2 <= N:
        power_of_2 *= 2
        x += 1
    return x, power_of_2
N = int(input("Enter a number: "))
exponent, result = find_exponent(N)
print( exponent , result)
