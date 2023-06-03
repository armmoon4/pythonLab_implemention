def capitalize(lower_case_word):
    first_letter = lower_case_word[0]
    capitalized_word = chr(ord(first_letter) - 32) + lower_case_word[1:]
    return capitalized_word

def capitalize_line(line):
    words = line.split()
    capitalized_words = [capitalize(word) for word in words]
    capitalized_line = ' '.join(capitalized_words)
    return capitalized_line
line = input("Enter a line of lowercase ASCII words: ")
capitalized_line = capitalize_line(line)
print(capitalized_line)
