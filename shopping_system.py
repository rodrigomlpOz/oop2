class Product:
    def __init__(self, product_id, name, price):
        """
        Initializes the Product class.

        Args:
        - product_id (str): A unique identifier for the product.
        - name (str): Name of the product.
        - price (float): Price of the product.
        """
        self.product_id = product_id
        self.name = name
        self.price = price

    def __str__(self):
        """Return a string representation of the Product."""
        return f"Product(ID: {self.product_id}, Name: {self.name}, Price: {self.price})"


class ShoppingCart:
    def __init__(self):
        """Initializes the ShoppingCart class."""
        self.products = {}  # Use a dictionary to store product: quantity pairs.

    def add_product(self, product, quantity=1):
        """
        Add a product to the cart. If the product is already in the cart, increase its quantity.

        Args:
        - product (Product): Product instance to be added.
        - quantity (int): The quantity of the product. Defaults to 1.
        """
        # TODO: Implement this method.

    def remove_product(self, product_id, quantity=1):
        """
        Remove a product from the cart or decrease its quantity.

        Args:
        - product_id (str): ID of the product to be removed.
        - quantity (int): The quantity of the product to be removed. Defaults to 1.
        """
        # TODO: Implement this method.

    def calculate_total(self):
        """Calculate the total price of products in the cart."""
        # TODO: Implement this method.

    def list_products(self):
        """List all products in the cart along with their quantities."""
        # TODO: Implement this method.


class Inventory:
    def __init__(self):
        """Initializes the Inventory class."""
        self.products = {}  # Use a dictionary to store products by their product_id.

    def add_product(self, product):
        """
        Add a product to the inventory.

        Args:
        - product (Product): Product instance to be added.
        """
        # TODO: Implement this method.

    def remove_product(self, product_id):
        """
        Remove a product from the inventory.

        Args:
        - product_id (str): ID of the product to be removed.
        """
        # TODO: Implement this method.


if __name__ == "__main__":
    # This is a place for you to experiment with your classes if you wish.
    pass
