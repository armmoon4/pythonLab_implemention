#labpractice >>> Take n(where n>4) inputs. Print the summation of mi and max.

n = int(input("Enter the number of inputs: "))
min_value = max_value = int(input("Enter a value: "))
for i in range(n-1):
    value = int(input("Enter a value: "))
    min_value = min(min_value, value)
    max_value = max(max_value, value)
print("Minimum Value:", min_value)
print("Maximum Value:",max_value)
print("Sum of minimum and maximum values:", min_value + max_value)