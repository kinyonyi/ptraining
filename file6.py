#dictionary 
person = {
    "name":"David Hope",
    "age":45,
    "location":"mbale",
    "bobbies":['swimming','outings']
}

#dictionary methods
print(person['name'])
"""
class approach!
name = getattr(person, "name")
print(name)
age = person.__getattribute__("age")
print(age)
"""

#updating dictionary keys / attributes
person['name'] = "Mafabi Ivan"
print(person['name'])

age = person.setdefault("age", 50)
print(age)

person.update({"age":60})
print(person['age'])

address = person.setdefault("address", "kikandwa")
print(address)
print(person)

#removal of item from dict
person.pop("address")#removes address from person
print(person)

person.popitem()#deletes the last item in the dictionary 
print(person)

del person['name']#deletes the specified key value pair from dict
print(person)

copied = person.copy()

#getting all keys from the dictionary 
keys = person.keys()
print(keys)

#geting values
values = person.values()
print(values)

#getting items 
items = person.items()
print(items)

#iterating through the dictionary 
for item in person.items():
    print(item)

for key, value in person.items():
    print(key, value)
