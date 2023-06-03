
def find_f_indices(s):
    first_index = s.find('f')
    last_index = s.rfind('f')
    if first_index != -1:
        if first_index == last_index:
            return str(first_index)
        else:
            return str(first_index) + ' ' + str(last_index)
    else:
        return None

input_string = input("Enter a string: ")
result = find_f_indices(input_string)
if result is not None:
    print(result)
