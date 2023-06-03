def interchange_string(s):
    length = len(s)
    half = length // 2
    return s[half:] + s[:half]
input_string = input()
result = interchange_string(input_string)
print(result)
