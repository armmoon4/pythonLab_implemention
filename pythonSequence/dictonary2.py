#answer 1:>>>
dictonary_a={
  "name": ["Moon", "Mahim", "Natasha", "Jihan"],
  "age": [22,13,11,18]
}
keys=[]
items=[]
for  i, j in dictonary_a.items():
  keys.append(i)
  items.append(j)
print(keys)
print(items)

#answer 2(a)>>>
dictonary_a=dict()
dictonary_a= {"name":["Moon","Mahim","Natasha","Jihan"],
"roll":[45, 66, 19, 10],
"hobby":["programming","eating","travelling","games"]}
hobbies=[]
for i, name in enumerate(dictonary_a["name"]):
    if "a" in name:
        hobbies.append(dictonary_a["hobby"][i])

print(hobbies)

#answer 2(b):>>>>
b=dict()
b = {"name":["Moon","Mahim","Natasha","Jihan"],
"roll":[45, 66, 19, 10],
"hobby":["programming","eating","travelling","games"]}
dictonary_a=b.copy()
dictonary_a["age"] = [22,13,11,18]
print(dictonary_a)