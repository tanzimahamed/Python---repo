# class Student:
#     # Constructor with instance variables
#     def __init__(self, name, marks):
#         self.name = name          # instance variable
#         self.marks = marks        # instance variable

#     # Instance method
#     def display(self):
#         print("Student Name:", self.name)
#         print("Marks:", self.marks)

# # Creating objects
# s1 = Student("Tanzim", 85)
# s2 = Student("Arunima", 92)

# # Calling instance method
# s1.display()
# s2.display()



class House:
    def __init__(self):
        self.window = 4
        self.door = 2 
         
    def _view_(self):
        print(self.window,"Window",self.door,"door")
#__________________________
H1 = House()
H2 = House()
H1.window= 6
H2.door = 4
H1._view_()
H2._view_()
print(H1)    # self = location of memory 
print(H2)

             
# In Python, self is a reference to the current object (instance).
# It is used inside class methods to access:

# Instance variables
# Instance methods

