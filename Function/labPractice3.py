# 3 Take user input n(where n > 5). If n is odd print the sum of all natural numbers else print the square of all natural numbers.

def odd():
    for i in range(1, n):
        i += 1
    print("Sum:", i + i)


def even():
    for i in range(1, n):
        i += 1
        print("Square:", i * i)


n = int(input("Enter the number of inputs: "))
if n > 5:
    if n % 2 == 0:
        even()
    else:
        odd()

