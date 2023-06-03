def remove_between_first_and_last_h(s):
    first_h_index = s.find('h')
    last_h_index = s.rfind('h')
    if first_h_index != -1 and last_h_index != -1:
        return s[:first_h_index] + s[last_h_index + 1:]
    else:
        return s

input_string = input("Enter a string: ")
result = remove_between_first_and_last_h(input_string)
print(result)
