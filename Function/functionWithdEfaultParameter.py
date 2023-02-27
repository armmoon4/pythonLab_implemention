#function with default parameter value

def check(a=0):
    if a==0:
        print("Zero")
    elif a>0:
        print("Positive")
    else:
        print("Negative")

check()     #without parameter
check(-4)   #with parameter