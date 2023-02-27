#function with multiple parameters

def divisor(x,y,m):
    if x%m==0 and y%m==0:
        print("%d & %d are divisible by %d"%(x,y,m))
    elif x%m==0:
        print("only %d is divisible by %d"%(x,m))
    elif y%m==0:
        print("only %d is divisible by %d"%(y,m))
    else:
        print("none of %d & %d is divisible by %d"%(x,y,m))

divisor(10,20,5)
divisor(12,20,5)
divisor(10,22,5)
divisor(2,5,3)