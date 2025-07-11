class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print(f"Product Name: {self.name}")
        print(f"Product Price: ₹{self.price}")

# 🛍️ Creating product objects
p1 = Product("Laptop", 55000)
p2 = Product("Smartphone", 20000)

p1.display()
p2.display()