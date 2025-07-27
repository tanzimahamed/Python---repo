# class Person:
#      def __init__(self, name, age):
#         self.name = name
#         self.age = age

#      def display_details(self):
#         print(f"Name: {self.name}, Age: {self.age}")

#   # Creating an object
# p1 = Person("Alice", 25)

#   # Displaying the details
# p1.display_details()

 
class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author
        self.price = 0

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price

    def details(self):
        print("Book Name:", self.name,
              "\nAuthor:", self.author,
              "\nPrice:", self.price, "Taka")

# Object creation and method calls
b1 = Book("Opekkha", "Humayun Ahmed")
#b1.details()
b1.set_price(255)
b1.details()
