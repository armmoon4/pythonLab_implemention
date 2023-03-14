inp_dict = eval(input("Enter a dictionary: "))
sum = 0
count = 0
for value in inp_dict.values():
    sum += value
    count += 1
average = sum / count
print("Average is", average)
