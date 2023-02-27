def divisor(x,y,m):
    if x%m == 0 and y%m==0:
        print(f'{x} & {y} are divisible by {m}')
    elif x%m==0:
        print(f'only {x} divisable by {m}')
    elif y%m==0:
        print(f'only {y} divisable by {m}')
    else:
        print(f'none of {x} and {y} is divisable by {m}')

divisor(10,20,5)
divisor(12,20,5)
divisor(10,22,5)
divisor(2,5,3)
