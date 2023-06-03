def print_greater_elements(numbers):
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i-1]:
            print(numbers[i])
numbers = input("Enter a list of numbers, separated by space: ").split()
numbers = [int(num) for num in numbers]
print_greater_elements(numbers)
