#turples
numbers = (1,2,4,5,6,7)
names = "David",
print(type(numbers))
print(type(names))

#indexing and slicing (same as lists) e.g
print(numbers[2])
print(numbers[1:4])
#number[:4] -> start to 4 | numbers[0:4]
#iteration through turple is same as list and string 
for item in numbers: print(item)

#in the event of adding items to the turple
new = list(numbers)
new.append(100)
new = tuple(new)
print(new)

#create a list having numbers which are multiples of 2 from the numbers
multiples = tuple([x for x in numbers if x % 2 == 0])
print(multiples)

odds = tuple([x for x in numbers if x % 2 == 1])
print(odds)

"""
Create an dict called personelData, intially empty!, 
request for the following user data
name, address, location
update personelData with the entered information!
print the registered data to your cmd / terminal
"""

personelData = dict()
name = input("Enter a name: ")
address = input("Enter an address: ")
location = input("Enter a location: ")
personelData.update({
    "name":name,
    "address":address,
    "location":location
})
print(personelData)