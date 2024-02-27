#classes - a blueprint used to create object 

class Person():
    species = "mamal"

person1 = Person()
print(person1.species)

#__init__() - constructor for the class
class Person():
    def __init__(self, name, dob, gender):
        self.name = name
        self.dob = dob
        self.gender = gender
        self.email = f"{name}.{gender[0:2]}@upf.co.ug"

    def greeting(self, timeOfDay):
        return f"Hello {self.name}, {timeOfDay}"
    
    def computeAge(self):
        age = 2024 - self.dob
        return f"{self.name} is {age} years old"
    
    def workingHours(self):
        return "works during day hours!"

person1 = Person("David", 1994, "Male")
person2 = Person("Hope", 1995, "Female")

print(person1.name, person1.dob, person1.gender)
print(person1.__dict__)

#modifying the attributes 
person1.__setattr__("name","Mafabi")
print(person1.__dict__)
#method 2 - setting attribute
setattr(person1, "dob", 1997)
print(person1.__dict__)
person1.gender = "Female"
print(person1.__dict__)
print(person1.greeting("afternoon"))
print(person1.computeAge())
print(person1.email)


#Class Inheritance
class Developers(Person):
    def __init__(self, name, dob, gender, language, salary, allowances):
        super().__init__(name, dob, gender)
        self.language = language
        self.salary = salary
        self.allowances = allowances

    def computeGrossPay(self):
        gross = self.salary + self.allowances
        return f"{self.name} gross salaray is {gross}"
    
    def workingHours(self):
        return "works during night hours!"

person3 = Developers("Aggrey",1990,"Male","Python",100000,40000)
print(person3.greeting("good evening"))
print(person3.computeAge())
print(person3.computeGrossPay())

#polymorphism
print(person1.workingHours())
print(person3.workingHours())