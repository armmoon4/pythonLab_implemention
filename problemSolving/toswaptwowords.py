def swap_words(s):
    words = s.split()
    if len(words) != 2:
        return s  # Return the input string as is if it doesn't contain exactly two words
    word1, word2 = words
    return word2 + " " + word1

input_string = input("Enter a string with two words: ")
result = swap_words(input_string)
print(result)
