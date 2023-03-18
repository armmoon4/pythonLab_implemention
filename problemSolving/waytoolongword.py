n = int(input())
for i in range(n):
    a = input()
    if len(a) > 10:
        abbribiation = a[0] + str(len(a)-2) + a[-1]
        print(abbribiation)
    else:
        print(a)