## Create a Product class for a small e-commerce application.

class Product:
    """Represent a product in an e-commerce application."""

    def __init__(self, product_id, name, price, category, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.category = category
        self.stock_quantity = stock_quantity

    def display_product(self):
        """Display product details."""

        print("Product ID:", self.product_id)
        print("Name:", self.name)
        print("Price:", self.price)
        print("Category:", self.category)
        print("Stock Quantity:", self.stock_quantity)

    def update_stock(self, quantity):
        """Update product stock."""

        self.stock_quantity += quantity

        print("Stock updated successfully.")
        print("New Stock Quantity:", self.stock_quantity)

    def calculate_total_price(self, quantity):
        """Calculate total price for the given quantity."""

        total_price = self.price * quantity

        print("Quantity:", quantity)
        print("Total Price:", total_price)

        return total_price

    @staticmethod
    def is_valid_price(price):
        """Check whether the price is valid."""

        return price > 0


# Create 5 Product objects

product1 = Product(
    101,
    "Laptop",
    55000,
    "Electronics",
    10
)

product2 = Product(
    102,
    "Smartphone",
    25000,
    "Electronics",
    15
)

product3 = Product(
    103,
    "Headphones",
    2000,
    "Accessories",
    20
)

product4 = Product(
    104,
    "Backpack",
    1500,
    "Bags",
    25
)

product5 = Product(
    105,
    "Keyboard",
    1200,
    "Accessories",
    30
)


# Display products

print("===== Product 1 =====")
product1.display_product()

print("\n===== Product 2 =====")
product2.display_product()

print("\n===== Product 3 =====")
product3.display_product()

print("\n===== Product 4 =====")
product4.display_product()

print("\n===== Product 5 =====")
product5.display_product()


# Demonstrate buying a product

print("\n===== Buying Product =====")

product1.calculate_total_price(2)

# Reduce stock after buying 2 laptops
product1.update_stock(-2)


# Demonstrate adding stock

print("\n===== Adding Stock =====")

product2.update_stock(5)


# Demonstrate static method

print("\n===== Price Validation =====")

print("Price 5000:", Product.is_valid_price(5000))
print("Price 0:", Product.is_valid_price(0))
print("Price -100:", Product.is_valid_price(-100))