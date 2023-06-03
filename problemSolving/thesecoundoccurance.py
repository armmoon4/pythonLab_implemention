def find_second_f_index(s):
    first_index = s.find('f')
    if first_index != -1:
        second_index = s.find('f', first_index + 1)
        if second_index != -1:
            return second_index
        else:
            return -1
    else:
        return -2

input_string = input("Enter a string: ")
result = find_second_f_index(input_string)
print(result)
