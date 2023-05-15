CURRENT_YEAR =2023
class Person:
    def __init__(self , name , year_born):
        self.name = name
        self.year_born = year_born
    def getAge(self):
        return CURRENT_YEAR - self.year_born
    def __str__(self):
        return '{} ({}) ' .format(self.name , self.getAge())

class Student(Person):
    def __init__(self , name , year_born):
        Person.__init__(self , name , year_born)
        self.knowledge = 0
    def study(self):
        self.knowledge += 1

moon = Student('Moon' , 2002)
moon.study()
print(moon)
print(moon.knowledge)
print(moon.getAge())
