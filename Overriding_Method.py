#Overriding = same mathod name & parameters in child class 
#Overloading = same method name diffrent parameter using default args ot *args

class Bank_Accout:
    def Interest_rate(self):
        return 5
class Student_Account(Bank_Accout):
    def Interest_rate(self):  # override with special rate 
        return 8
normal= Bank_Accout()
Student = Student_Account()

print("Normal:",normal.Interest_rate())
print("Student:",Student.Interest_rate())


#==========================================================================


class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

# Create objects
a = Animal()
d = Dog()

a.speak()  # Output: Animal makes a sound
d.speak()  # Output: Dog barks (overrides parent method)


#==============================================================================



class Payment:
    def process_payment(self, amount):
        print(f"Processing payment of {amount} in generic way")

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing credit card payment of {amount}")

class PayPalPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of {amount}")

p1 = CreditCardPayment()
p2 = PayPalPayment()

p1.process_payment(100)
p2.process_payment(200)

