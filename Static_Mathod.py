"""A static method is a method inside a class tha dose not take self or cls as its first argument .
It does not need access to  instance or class variable - it behaves like a normal function but is logically grouped inside the class ."""

# it defined using the @staticmethod decorrator.


# class Class_Name:
#     @staticmethod
#     def method_name(Args):
#         # logic here/ body 

class Calculator:
    @staticmethod
    def add(x, y):
        return x + y

# Call without creating object
print(Calculator.add(10, 5))  # Output: 15



class BankAccount:
    @staticmethod
    def convert_currency(taka):
        usd = taka / 110
        print(f"{taka} Taka = {usd:.2f} USD")

# Use static method without object
BankAccount.convert_currency(2200)  # Output: 2200 Taka = 20.00 USD


