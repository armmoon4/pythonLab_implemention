def count_word_occurrences(text):
    words = text.split()
    word_counts = {}
    occurrences = []
    for word in words:
        if word in word_counts:
            occurrences.append(word_counts[word])
            word_counts[word] += 1
        else:
            occurrences.append(0)
            word_counts[word] = 1
    return occurrences
text = input("Enter the text: ")
occurrences = count_word_occurrences(text)
print(*occurrences)
