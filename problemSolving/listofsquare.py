def print_squares(N):
    i = 1
    while i**2 <= N:
        print(i**2)
        i += 1

N = int(input("Enter a number: "))
print_squares(N)
