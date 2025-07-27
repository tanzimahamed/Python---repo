# Base class
class Animal:
    def make_sound(self):
        print("Animals make different sounds.") 
# Derived class
class Dog(Animal):
    def make_sound(self):
        # Override 
        super().make_sound()  
        print("Dog barks!")   

# Create an object of Dog
d = Dog()
d.make_sound()

