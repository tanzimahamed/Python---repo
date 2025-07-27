# #OOP_in_Python

# """What is a Class?
# A class is a blueprint for creating objects. 
# It defines a set of attributes (variables) and methods (functions)."""

# # class Class_name:
# #     name="Tanzim Ahamed"   #class variable
# #     age=25



# # class Student:


# """ __init__() Method (Constructor)
# __init__() is a special method called when a new object is created.
#  It’s used to initialize object variables."""
    
#     # def __init__(self,name,roll):
#     #     self.name=name
#     #     self.roll=roll
   
   
# """What is an Object?
# An object is an instance of a class.
#  When you create an object, Python allocates memory and allows you to access the class members."""

# # s1= Class_name()
    


   
# class Student:      #creat a class
#     def __init__(self, name, roll):   #method is like constructor
#         self.name = name
#         self.roll = roll

# s1 = Student("Tanzim Ahamed", 2)  #objec
# print(s1.name)   
# print(s1.roll)   
# class Student:
#     colleg_name = "ABC College"

#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def Welcome(self):
#         print("Welcome Student:", self.name)

#     def get_marks(self):
#         return self.marks        

# # Create objects
# Std_1 = Student("Tanzim", 242)
# Std_2 = Student("Arunima", 232)

# # You forgot to add () after method calls!
# Std_1.Welcome()  # <- Add ()
# Std_2.Welcome()  # <- Add ()
# print(Std_2.get_marks())  # <- Add ()
# print(Std_1.get_marks())  # <- Add ()


# class Student:
#     college_name = "ABC College"

#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def welcome(self):
#         print(f"Welcome Student: {self.name}")

#     def get_marks(self):
#         return self.marks


# # Object তৈরি
# s1 = Student("Tanzim", 242)
# s2 = Student("Arunima", 232)

# # Method Call
# s1.welcome()
# s2.welcome()

# # Mark Access
#  print("Arunima's Marks:", s2.get_marks())
#  print("Tanzim's Marks:", s1.get_marks())


# """Create student class that takes name & marks of 3 subject as arguments in constructor.
# then create a mathod to print the average"""
# class Student:
#     def __init__(self,Name, Marks): # Constructor: name & 3 subject marks list
#         self.Name=Name
#         self.Marks=Marks
#     def get_ave(self):     # Method to calculate average
#         sum=0
#         for val in self.Marks:
#             sum+=val
#         print('Hi,',self.Name,'Your avg Marks is :',sum/3)    
# # Object create kore method call
# S1=Student("Tanzim Ahamed",[99,87,97])
# S1.get_ave()
class Dog:
    def __init__(self,name ,color ):
        self.name = name 
        self.color = color
    def poke( self):
        print(self.color,self.name,'is Smilling')
    def update_color(self,color):
        self.color= color
#________________________________

d1= Dog('Rover','Brown')
d2 = Dog('tomy','white')
#d1.poke()
#d2.poke()
d1.update_color("black")
#d1.poke()
print(d1.__dict__)
print(d2.__dict__)