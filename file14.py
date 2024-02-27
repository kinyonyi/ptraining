from file13 import *
msg = "Hello Dave, how are you!"
nums = [2,4,5,6,7]

print(changed(msg))
print(multipleNumbers(nums))
print(reversedString(msg))
returned = reversedString(msg.split())
print(returned)
#optimal method
print(" ".join(returned))

#Method two
new_msg = ""
for item in returned:
    new_msg += item + " "
print(new_msg.strip())