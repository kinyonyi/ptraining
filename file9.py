#conditionals
"""
if(condition):
    do this
else:
    do something else
"""

today = 'thursday'
if today == 'thursday':
    print('we have a session')
else:
    print('its a free day!')

print('we have a session') if today == 'thursday' else print('its a free day!')


if today == 'thursday':
    print('we have a session')

if today == 'thursday': print('we have a session')

#multiple conditions
if today == 'thursday':
    print('we have a session')
elif today == 'friday':
    print('a gyming day!')
else:
    print('its a free day!')

print('we have a session') if today == 'thursday' else print('a gyming day!') if today == 'friday' else print("its a free day!")
#conditions can be nested!
num = 30
if num > 5:
    print(f"{num} is > 5")
    if num % 2 == 0:
        num /= 5
        print(f"{num} is also a mukltiple of 2")
        if num > 10:
            print(f"{num} is greater than 10")
else:
    print(f"{num} is < 5")

name = "david"
msg = "Hello david, how are u"
msg = "hello "+ name + " how are you"
msg = "Hello {}, how are you".format(name)
msg = "Hello {name}, how are you".format(name = name)
