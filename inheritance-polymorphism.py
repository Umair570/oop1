# '''Single Inheritance'''

class Car:
    @staticmethod
    def start():
        print("Car started")

    @staticmethod
    def stop():
        print("Car stopped")

class HondaCar(Car):
    def __init__(self,name):
        self.name=name

'''Multilevel Inheritance'''

class Car:
    @staticmethod
    def start():
        print("Car started")

    @staticmethod
    def stop():
        print("Car stopped")

class HondaCar(Car):
    def __init__(self,type):
        self.type=type

class Civic(HondaCar):
    def __init__(self,name):
        self.name=name

'''Multiple Inheritance'''

class A:
    varA="welcome to class A"

class B:
    varB="welcome to class B"

class C(A,B):
    varC="welcome to class C"  


# SUPER METHOD
class Car:
    def __init__(self,type):
        self.type=type

    @staticmethod
    def start():
        print("Car started")

    @staticmethod
    def stop():
        print("Car stopped")

class HondaCar(Car):
    def __init__(self,name,type):
        self.name=name
        super().__init__(type)

car1=HondaCar("Civic","Petrol") 
print(car1.type)       


#Class Method
class Person:
    name="anonymous"

    @classmethod
    def changeName(cls,name):   #here cls is referring to class it is not self because we are using it directly for class
        cls.name=name

#Property Decorator
class Student:
    def __init__(self,phy,chem,math):
        self.phy=phy        
        self.chem=chem        
        self.math=math
        self.percentage=str((self.phy + self.chem + self.math)/3) +"%"

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math)/3) +"%"   #here if we change the marks of any subject then property decorator
                                                                #automatically change those marks and calculate the percentage for us.
    
                 

class Animal:
    def __init__(self,name,sound):
        self.name=name
        self.sound=sound
    def __str__(self):
        return f"Name: {self.name} , Sound: {self.sound}"
    
class Dog(Animal):
    def __init__(self,name,sound,breed):
        Animal.__init__(self,name,sound)              #we can do it like that or we can also use super method
        self.breed=breed

    def __str__(self):
        return Animal.__str__(self)+f" , Breed: {self.breed}"


a1=Animal("Max","Bark")
print(a1)
d1=Dog("Jack","Bark","German Shepherd")
print(d1)


# #IMP!!!!!  whenever  we use inheritance then it becomes obvious that we use the parent class in our child classes

#POLYMORPHISM
'''Operator overloading:
when same operator have is allowed to have different meaning according to the context.
eg. + operator has different meaning for integers,string and lists
eg. in complex numbers real and imaginary parts are added separately

DUNDER FUNCTIONS:

'''

class Complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag

    def showNumber(self):
        return f"{self.real}i + {self.imag}j"
    
    # def addNumbers(self,num2):
    #     newReal=self.real + num2.real
    #     newImag=self.imag + num2.imag
    #     return Complex(newReal,newImag)
    
    def __add__(self,num2):  #this is operator overloading by using dunder functions
        newReal=self.real + num2.real
        newImag=self.imag + num2.imag
        return Complex(newReal,newImag)
    
    def __sub__(self,num2):  #this is operator overloading by using dunder functions
        newReal=self.real - num2.real
        newImag=self.imag - num2.imag
        return Complex(newReal,newImag)
    
    

num1=Complex(1,3)
print(num1.showNumber())
num2=Complex(4,9)
print(num2.showNumber())
added_number=num1 + num2
subtracted_number=num1 - num2
print(added_number.showNumber())
print(subtracted_number.showNumber())
        

#PRACTICE BY APNA COLLEGE
#q1
#SIMPLE OOP
class Circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        area=(3.14)*((self.radius)**2)
        return f"Area: {area}"

    def perimeter(self):
        perimeter=2*(3.14)*(self.radius)
        return f"Perimeter: {perimeter}"  

c1=Circle(21)
print(c1.area())
print(c1.perimeter())              

#q2
#INHERITANCE
class Employee:
    def __init__(self,role,department,salary):
        self.role=role
        self.department=department
        self.salary=salary

    def showDetails(self):
        return f"Employee details:\nRole: {self.role} , Department: {self.department} , Salary: {self.salary}"
    
class Engineer(Employee):
    def __init__(self,name,age,role,department,salary):
        self.name=name
        self.age=age
        super().__init__(role,department,salary)

    def showDetails(self):
        return f"{super().showDetails()} , " + f"Name: {self.name} , Age: {self.age}"

engg=Engineer("Elon Musk","40","Engineer","IT","50,000")
print(engg.showDetails())        

#q3
#POLYMORPHISM
class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price

    def __gt__(self,odr2):
        return self.price> odr2.price    
    
odr1=Order("Chips","50")    
odr2=Order("Pepsi","90")

print(odr1>odr2)