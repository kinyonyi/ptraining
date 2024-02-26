#lists 
names = ['dave','isaac','mercy','daniel']
countries = ['uganda','kenya','tanzania']

#indexing and slicing
#positive and negative indexing apply as well e.g
print(names[0])
print(names[-2])
print(names[::])#print(names), print(names[:])
print(names[::2])
print(names[::-1])

#list methods
print(len(names))
names.append("jacob")#adds jacob at the end of the list
print(names)
names.insert(0, "gerald")#inserts into the list at the specified index
print(names)
occurance = names.count("gerald")
print(occurance)
print(names.index("gerald"))#returns the index of gerald in the list
names.remove("mercy")#removes mercy from the list
names.pop(3)#removes item at specified index
copied = names.copy()
print(copied)
print(names.reverse())#reverses the list equivalent to names[::-1]
print("This is the sotrted list!")
print(names)
names.sort()
print(names)
names.reverse()#descending order of sorting
print(names)
names.extend(countries)#joins the countries list to the names
print(names)
#names.clear()#clears the names list (removes all items from the list)

"""
names.sort(key=lambda x: len(x))
print(names)
"""
new_list = []
for name in names:
    if len(name) > 5:
        new_list.append(name)
print(new_list)

#list comprehesions
newList = [name for name in names if len(name) > 5]
print(newList)

"""
request for three names from a user and save the names to a list
let the user enter this through through the terminal
call the list personel
"""
personel = []
name1 = input("Enter Personel name: ")
personel.append(name1)

