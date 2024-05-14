class Car:
    def __init__(self, marc, subname, age):
        self.marc = marc
        self.subname = subname
        self.age = age

    def my(self):
        print("Марка " + self.marc, self.subname, self.age)

p1 = Car("Toyota", "Camry", 2024)
p1.my


class Person:
    def __init__(self,name):
        self.name=name
    def get_info(self):
        print("Аты:",self.name)

class Employee(Person):
    def job(self,job_name):
        print("Аты:",self.name,"жұмыс:",job_name)

employee_obj=Employee("Канат")
employee_obj.job("programmer")


class Color:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        print("shape color:", self.color)

class Triangle(Color):
    def __init__(self, color, side1, side2, side3):
        Color.__init__(self,color)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.a = side1 + side2 + side3

    def get_perimeter(self):
        print("Perimeter:", self.a)

obj1 = Triangle(color="Yellow", side1=8, side2=4, side3=10)
obj1.get_color()
obj1.get_perimeter()
