#user defined function

def add(a, b):
    c=a+b
    return c

a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
d=add(a,b)
print("The sum is", d)