book_genres = {'sci fi': 12, 'mystery': 15, 'horror': 8, 'mythology': 10, 'young_adult': 4, 'adventure':14}
max_value = 0
max_key = ''
for key, value in book_genres.items():
    if value > max_value:
        max_value = value
        max_key = key
print("The highest selling book genre is '{}' and the number of books sold are {}.".format(max_key, max_value))
