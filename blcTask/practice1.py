i=1

while i<=3:

  i=i+1

  a=input("Enter the ID:")

  m1 = int (input("Enter the marks in the first subject: "))

  m2 = int (input("Enter the marks in the second subject: "))

  m3 = int (input("Enter the marks in the third subject: "))

  if m1<100 and m2<100 and m3<100:

   total=m1+m2+m3

   average=total/3

   print("ID:",a)

   print("Avarage mark=",average)