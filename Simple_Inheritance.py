#  1. Single Inheritance
# One child class inherits from one parent class.

# Structure:
# Parent
#   ↓
# Child



class Parent_Class:
    def method_1(self):
        print("this method_1 is an Parent_Class.")
    def method_2(self):
        print("this method_2 is an Parent_Class.")
class Child_class(Parent_Class):
    def method_3(self):
        print("this method_3 is in Child_class")

ch_1= Child_class()
ch_1.method_1()
ch_1.method_2()
ch_1.method_3()

#===============================================================
# Parent class
class Animal:
    def sound(self):
        print("Animal makes a sound")  # Base method

# Child class inheriting from Animal
class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Object of Dog class
d = Dog()
d.sound()  # Inherited from Animal
d.bark()   # Defined in Dog
#===============================================



