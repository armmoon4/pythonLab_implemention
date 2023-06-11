
number = int(input())
prev_num, curr_num = 0, 1
fibonacci = [prev_num, curr_num]

while curr_num <= number:
    next_num = prev_num + curr_num
    fibonacci.append(next_num)
    prev_num, curr_num = curr_num, next_num

print(fibonacci)
