def print_even_numbers(numbers):
    for num in numbers:
        if num % 2 == 0:
            print(num)
numbers = input("Enter a list of numbers, separated by space: ").split()
numbers = [int(num) for num in numbers]
print_even_numbers(numbers)
