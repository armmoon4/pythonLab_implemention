
def print_even_index_elements(numbers):
    for i in range(0, len(numbers), 2):
        print(numbers[i])

numbers = input("Enter a list of numbers, separated by space: ").split()
numbers = [int(num) for num in numbers]
print_even_index_elements(numbers)
