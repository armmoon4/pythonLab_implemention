#python standard library
#csv module

import csv

with open('test.csv', newline='') as csvfile:
    tmp = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in tmp:
        print(', '.join(row))