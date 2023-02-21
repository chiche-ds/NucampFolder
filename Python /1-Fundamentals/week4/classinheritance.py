class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


x = Person("John", "Doe")
x.printname()

#child class 

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname,lname)
        self.graduationyear = year
    


x = Student("Mike", "Olsen", 2019)
x.printname()