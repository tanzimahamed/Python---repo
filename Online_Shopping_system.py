#  Online Shopping System

#  Class: Product

# We're creating a class for online products. Along with product details, we want to:

# Calculate discounts on any price (not tied to one product) ✅ Static method

# Store product info using instance methods 

# Track total number of products using a class method 




class Product:
    total_products = 0  # Class variable

    def __init__(self, name, price):
        self.name = name        # Instance variable
        self.price = price      # Instance variable
        Product.total_products += 1

    # Instance Method: Show product details
    def show_info(self):
        print(f"Product Name: {self.name}")
        print(f"Original Price: {self.price} Tk")

    # Class Method: Count how many products created
    @classmethod
    def show_total_products(cls):
        print("Total Products Added:", cls.total_products)

    # Static Method: Calculate discount
    @staticmethod
    def calculate_discount(price, discount_percent):
        if price < 0 or discount_percent < 0:
            return "Invalid Input"
        discount = price * (discount_percent / 100)
        new_price = price - discount
        return round(new_price, 2)


# Creating product objects
p1 = Product("Laptop", 70000)
p2 = Product("Phone", 35000)

# Using instance methods
p1.show_info()
p2.show_info()

# Using class method
Product.show_total_products()

# Using static method (calculate discount)
print("Laptop after 10% discount:", Product.calculate_discount(p1.price, 10), "Tk")
print("Phone after 15% discount:", Product.calculate_discount(p2.price, 15), "Tk")

# You can also use it for general pricing:
print("New Shoes after 20% discount:", Product.calculate_discount(3000, 20), "Tk")