#A class inherits from a child class, which itself inherits from a parent class.

# Parent
#   ↓
# Child1
#   ↓
# Child2


class ParentClass:
    def method1(self):
        print("This method1 is in ParentClass.")

class ChildClass1(ParentClass):
    def method2(self):
        print("This method2 is in ChildClass1.")

class ChildClass2(ChildClass1):
    def method3(self):
        print("This method3 is in ChildClass2.")

ch1 = ChildClass2()
ch1.method1()
ch1.method2()
ch1.method3()

#===========================================================

#parent class
class Animal:
    def eat(self):
        print("Animal eats food")

# child class1
class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Child class2
class Puppy(Dog):
    def weep(self):
        print("Puppy weeps")

# Object of Puppy class
p = Puppy()
p.eat()   # From Animal
p.bark()  # From Dog
p.weep()  # From Puppy


