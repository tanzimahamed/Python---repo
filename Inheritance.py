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


#==================================
# 1. Bank Account System (Single Inheritance)
# Imagine a general bank account, and a savings account that inherits from it.

# Concept:
# Base class: BankAccount
# Derived class: SavingsAccount



# Base class
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited. New balance: {self.balance} Tk")

# Derived class
class SavingsAccount(BankAccount):
    def add_interest(self, rate):
        interest = self.balance * rate / 100
        self.balance += interest
        print(f"Interest added: {interest} Tk. Total balance: {self.balance} Tk")

# Object
acc = SavingsAccount("Tanzim", 5000)
acc.deposit(1000)
acc.add_interest(5)


#===================================================================================

# 2. University System (Multilevel Inheritance)
# Suppose we have:
# Person → Student → UniversityStudent

# Base class
class Person:
    def __init__(self, name):
        self.name = name

# Intermediate class
class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id

# Derived class
class UniversityStudent(Student):
    def __init__(self, name, student_id, university):
        super().__init__(name, student_id)
        self.university = university

    def display(self):
        print(f"Name: {self.name}, ID: {self.student_id}, University: {self.university}")

# Object
std = UniversityStudent("Tanzim", "ICE 242", "DIU")
std.display()

#==========================================================================================================


# 4. Employee Payment System (Hybrid Inheritance)
# A mix of inheritance types — combining multiple paths.


class Person:
    def __init__(self,name):
        self.name = name
class Employee(Person):
    def __init__(self, name,employee_id):
        super().__init__(name)
        self.employee_id = employee_id
class Salary:
    def __init__(self, monthly_salary):
        self.monthly_salary = monthly_salary
class FullTimeEmployee(Employee, Salary):
    def __init__(self, name, employee_id, monthly_salary):
        Employee.__init__(self, name, employee_id)
        Salary.__init__(self, monthly_salary)
    def Display(self):
        print(f"Name: {self.name}, ID: {self.employee_id}, Salary: {self.monthly_salary} Tk")

emp = FullTimeEmployee("Tanzim Ahamed","EMP242",40000)
emp_2 = FullTimeEmployee("Arunima Aru","EMP243",35000)    
emp.Display()
emp_2.Display()    