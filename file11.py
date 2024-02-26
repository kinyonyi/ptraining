#Functions-****
"""
a block of code only executed once called!
"""
def namings():
    print('I am called Dave!')

#to call the function, use the function name
namings()

def namings(name):
    print(f'I am called {name}!')

namings("Isaac")
namings("Mafabi")
namings("Winnie")

def details(name, gender, location):
    print(f'{name} is {gender} located in {location}')

details('dave', 'male', 'kikandwa')

def data(*args):
    print(args)

data(1,2,3,4,5,'dave','mercy','hope')
data('dave','mercy','hope')

def namings(name = 'hope', /):
    print(f'I am called {name}!')

namings()
namings("Vodriko")

#key word arguments
def namings(name):
    print(name)

namings(name = "dave")

def data(name, age):
    print(name, age)

data(name = 'dave', age = 30)

def data(**kwargs):
    print(kwargs, kwargs['age'])

data(name = 'dave', age = 30)
print(data(name = 'dave', age = 30))


#function return 
def data(**kwargs):
    return kwargs

response = data(name = 'dave', 
    age = 30, 
    nationality ='ugandan')

print(response)
print(response['name'])

def namings(*, name):
    print(f'I am called {name}!')

data(name = 'dave')#valid
#data('dave')#not valid


#decorators 
def nameDecorator(func):
    def wrapper(*args, **kwargs):
        print(args)
        print("before the check")
        if len(kwargs['name']) > 10:
            print("Violatiotion of length constraint!")
        else:
            func(*args, **kwargs)
        print("after the check")
    return wrapper

@nameDecorator
def myFunc(name):
    print(f"My name is {name}")

#nameDecorator(named())
myFunc('upf', name = "David Isaac")

#lambda function
nextAge = lambda age: age + 1
newAge = nextAge(25)
print(newAge)
"""
def nextAge(age):
    return age + 1
"""