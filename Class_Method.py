#  What is a Class Method?

# A class method is a method that:
# Works with the class itself, not the instance.
# Can access or modify class variables.
# Uses @classmethod decorator.
# Takes cls as the first parameter (not self).



class Student:
    university = "Daffodil International University"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_university(cls, new_university):   #class method, (cls)not self
        cls.university = new_university

    def display(self):
        print("Name:", self.name)
        print("University:", Student.university)

# Before changing university
s1 = Student("Tanzim")
s1.display()

# Change university using class method
Student.change_university("AIUB")

# Check change for new student
s2 = Student("Arif")
s2.display()


#=================================================================
class Car:
    wheels = 4

    @classmethod
    def set_wheels(cls, number):
        cls.wheels = number

Car.set_wheels(6)
print(Car.wheels)  # Output: 6

