def calculate_sequence_length():
    count = 0

    while True:
        num = int(input("Enter a non-negative integer (0 to end the sequence): "))
        if num == 0:
            break
        count += 1

    return count

result = calculate_sequence_length()
print(result)
