#Operators
#arithmetic Operators (+, -, *, /, //, %)
num1 = 10
num2 = 30 

addition = num1 + num2 #result of addition
diff = num1 - num2 #result of subtraction
multiple = num1 * num2 #result of multiplication
division = num1 / num2 #whole number plus fraction
floor_division = num1 // num2 #whole number part of division
modulus = num1 % num2 #remainder of division

print(f"The sum of {num1} and {num2} is {addition}")
print(diff)
print(multiple)
print(f"The division of {num1} and {num2} is {division:.2f}")
print(floor_division)
print(modulus)

#comparison operators - (<, >, <=, >=, !=, ==) ->Return Booleans
print(f"{num1} < {num2} is {num1 < num2}")
print(f"{num1} > {num2} is {num1 > num2}")
print(f"{num1} <= {num2} is {num1 <= num2}")
print(f"{num1} >= {num2} is {num1 >= num2}")
print(f"{num1} != {num2} is {num1 != num2}")
print(f"{num1} == {num2} is {num1 == num2}")

#Identity operators - (is, is not) - Return Booleans
print(f"{num1} is {num2} is {num1 is num2}")
print(f"{num1} is not {num2} is {num1 is not num2}")

#assignment operators - (=, +=, -=, *=, /=, )
number = 20 #assignining number with value 20 
number += 5 #number = number + 5
print(number)
number -= 10
print(number)
#same thing applies to (*=, /=)

#logical operators (and, or, not) - return Booleans
"""
and returns a true only if left and right coparison are true
or return true if either side is true, false if both false
not - reverse of true or a false
"""
print(f"{True} and {True} is {True and True}")
print(f"{True} and {False} is {True and False}")
print(f"{True} or {True} is {True or True}")
print(f"{True} or {False} is {True or False}")
print(f"{False} or {False} is {False or False}")
print(f"not {True} and {True} is {not (True and True)}")

#membership operator - (in, not in)
nums = range(20, 30)
print(25 in nums)
print(20 not in nums)




