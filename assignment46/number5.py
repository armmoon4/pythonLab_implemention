# Input from the user
number = int(input())

# First two terms of the series
prev_num, curr_num = 0, 1

# Generate and print the Fibonacci series
fibonacci = [prev_num, curr_num]

while curr_num <= number:
    next_num = prev_num + curr_num
    fibonacci.append(next_num)
    prev_num, curr_num = curr_num, next_num

print(fibonacci)
