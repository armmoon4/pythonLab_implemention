#list operation <<<<<<<<

lst0=[1,2,3,32,2.32,43.23 , "python", [2,32,3]]
print(len(lst0))

lst0.append([12,2,12,2])  #add in last of the last
print(lst0)

lst0.insert(2 , "pandas")  #insertion in specific positin
print(lst0)

lst0.remove(3)  #remove in specific position
print(lst0)

print(lst0.index("python"))  #reversing of the list
print(lst0.count('pandas'))
print(lst0.reverse())

lst1=lst0.copy()
print(lst1)             #reversing

lst0.clear()       #empty list
print(lst0)


