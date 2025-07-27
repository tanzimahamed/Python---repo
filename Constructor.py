"""A constructor is a special method that is automatically 
called when a new object of a class is created.
In Python, the constructor method is:"""
#class Class_Name:
#def __init__(self):




# #Types__
#     1.Default Constructor
#       Constructor with no parameters other than self.
#     2. Parameterized Constructor
#        Constructor that takes arguments to initialize object data.




#Default Constructor
class Demo:
    def __init__(self):
        print("Default Constructor Called")

d = Demo() 



#Parameterized Constructor
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("Name:", self.name)
        print("Age:", self.age)

s1 = Student("Alice", 20)
s1.show()

#  Summary:
# Constructor = __init__(self)

# Called automatically when object is created

# Used to initialize data

# Can be default or parameterized

# You can simulate overloading using default values

