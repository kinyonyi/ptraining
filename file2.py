#Data Types 
#string Data Type 
location = "Kikandwa"
city = 'Kampala'

print(type(location))
print(type(city))

#numerical Data Types - int, float, complex
num1 = 5
num2 = 10.5
num3 = 3 + 2j
print(type(num1))
print(type(num2))
print(type(num3))

#sequence Data Types - list, turple, range
mylist = [1,2,3,4,5]
names = ('david','mercy','gerald')
nums = range(10)
#range(10, 20)
#range with step = range(10, 20, 3)
print(type(mylist))
print(type(names))
print(type(nums))

#mapping Data Type - dict
person_details = {
    "name":"Kinyonyi David Hope",
    "gender":"Male",
    "age":45
}
print(type(person_details))

#Boolean Data Type - True & False
rainy = True
chilyMorning = False

print(type(rainy))
print(type(chilyMorning))

#None DataType 
today = None
print(type(today))

#set dataType 
fruits = {'oranges','mangoes','guavas'}
print(type(fruits))