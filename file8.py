#sets

electronics = set()
print(type(electronics))
electronics = {'computers','phones','speakers'}

#iteration through a loop 
for item in electronics:
    print(item)

#membership operator 
print("computers" in electronics)

#set methods
electronics.add("air pods")
print(electronics)

cars = ('subaru', 'mark x', 'computers')
electronics.update(cars)

#update can take on a set, turple or a list (any iterable)
print(electronics)

#removal of content 
electronics.remove("computers")
print(electronics)

electronics.discard("david")
electronics.discard("mark x")
print(electronics)

furniture = {'chairs', 'tables', 'desks', 'subaru'}
union = electronics.union(furniture)
print(union)

intersected = electronics.intersection(furniture)
print(intersected)

electronics.intersection_update(furniture)
print(electronics)

electronics = {'computers','phones','speakers', 'desks'}
diff = electronics.difference(furniture)
print(diff)

electronics.difference_update(furniture)
print(electronics)

electronics = {'computers','phones','speakers', 'desks'}

sym_diff = electronics.symmetric_difference(furniture)
print(sym_diff)

electronics.symmetric_difference_update(furniture)
print(electronics)

copied = furniture.copy()
print(copied)

furniture.clear()
print(furniture)

names = {'dave', 'mark'}
names2 = {'dave', 'ivan', 'mercy', 'jacinta'}

print(names.issubset(names2))#returns a boolean
print(names.issuperset(names2))
print(names.isdisjoint(names2))

popped = names2.pop()
print(f"{popped} was removed from set names")
print(names2)