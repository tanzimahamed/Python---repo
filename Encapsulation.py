"""Definition:
Encapsulation means binding the data (variables) and
the code (methods) that operates on the data into
a single unit (class) and restricting direct access 
to some of the object’s components.

 Why Use Encapsulation?
To protect data from outside interference.
To control access to variables.
To make your code modular and secure.
Prevent accidental modification of data.
"""
# Access Level:
#public-self.name
#protected - self._name
#private - self.__name



#-----------------------------------------------------------
# class Student:
#     def __init__(self,name, Id):
#         self.name = name    #public instance variable
#         self.__id = Id      # private variable because self.__id 
#     def details(self):
#         print("name:",self.name,"ID:",self.__id)
# # Create a object 
# s1  = Student("Tanzim",11)
# s2 = Student("arunima " , 12)
# #print(s1.__id)
# s1.details()
# s2.details() 
# ------------------------------------------------------------   



#---------------------------------------------------------------
class Student:
    def __init__(self, name, roll):
        self.name = name         # public
        self._roll = roll        # protected (convention)
        self.__cgpa = 3.85       # private

    def display_info(self):
        print("Name:", self.name)
        print("Roll:", self._roll)
        print("CGPA:", self.__cgpa)  # can access inside the class

    def update_cgpa(self, new_cgpa):
        if 0 <= new_cgpa <= 4.0:
            self.__cgpa = new_cgpa
        else:
            print("Invalid CGPA!")

std = Student("Tanzim", 101)

std.display_info()         # ✔ Works
print(std.name)            # ✔ Public: Works
print(std._roll)           # ⚠ Protected: Works but not recommended
# print(std.__cgpa)        # ❌ Private: Error

# Access private variable via name mangling:
print(std._Student__cgpa)  # ✔ Works (but not recommended)
#---------------------------------------------------------------------------






#--------------------------------------------------------------------------
"""Think of a bank account:
You can deposit/withdraw money using methods.
But you can't directly change the balance.
"""
class Bank_Account:
    def __init__(self,balance):
        self.__balance = balance
    def deposit(self,amount):
        self.__balance += amount
    def get_balance(self):
        return self.__balance

# create Object 
acc = Bank_Account(10000)
acc.deposit(500)
print(acc.get_balance())     
#print(acc.self.__balance)   
#--------------------------------------------------------
