list2 = [item for item in range(1, 6)]
print(list2)

list3 = list(range(1,6))
print(list3)

list4 = [item * 3 for item in range(1, 6)]
print(list4)

list5 = [item for item in range(1, 11) if item % 2 == 0]
print(list5)

colors = ['red', 'orange', 'yellow', 'green', 'blue']
colors2 = [item.upper() for item in colors]
print(colors2)