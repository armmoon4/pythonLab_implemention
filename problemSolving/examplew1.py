print("""
Hello this is script test of python 
   interpreted language i am testing 
        now "three" quotes text """)

a,b,c,d = input().split() #multiple user input
print(a,b,c,d)

x = 7
x + 10
print(x+10)

#control statement
grade = int(input())
if grade >= 90:
    print("A")
elif grade >= 80:
    print('B')
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("Congratulation Youre Failed")