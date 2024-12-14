class Bug:
    def __init__(self,position):
        self.position=position
        self.direction=1

    def move(self):
        self.position+=self.direction
       
    def turn(self):
        self.direction*=-1
                                           #5
    def getPosition(self):
        return self.position

cli=Bug(10)
cli.move()
print(cli.getPosition())
cli.turn()
cli.move()                
print(cli.getPosition())  
cli.move()
print(cli.getPosition())              


class Person:
    def __init__(self,name,birthyear):
        self.name=name
        self.birthyear=birthyear

    def __str__(self):
        return f"Name:{self.name} , Birthyear:{self.birthyear}"

class Student(Person):
    def __init__(self,name,birthyear,major):
        Person.__init__(self,name,birthyear)
        self.major=major

    def __str__(self):
        return Person.__str__ (self)+f", Major:{self.major}"

class Instructor(Person):                                        #5
    def __init__(self,name,birthyear,salary):
        Person.__init__(self,name,birthyear)
        self.salary=salary

    def __str__(self):
        return Person.__str__(self)+f", Salary:{self.salary}"

p1=Person("Umair","2005")
print(p1)
s1=Student("Umair","2005","CS")
print(s1)
i1=Instructor("Fakhir","1990","500000")
print(i1)
