def find_synonym(dictionary, word):
    if word in dictionary:
        return dictionary[word]
    else:
        return "No synonym found"
n = int(input("Enter the number of word pairs in the dictionary: "))
dictionary = {}
for _ in range(n):
    word1, word2 = input("Enter word pair (separated by a space): ").split()
    dictionary[word1] = word2
    dictionary[word2] = word1
word_to_find = input("Enter the word to find a synonym for: ")
synonym = find_synonym(dictionary, word_to_find)
print(synonym)
