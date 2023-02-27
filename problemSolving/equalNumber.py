a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))
c = int(input("Enter the third integer: "))

if a == b == c:
    print("3")
elif a == b or b == c or a == c:
    print("2")
else:
    print("0")
