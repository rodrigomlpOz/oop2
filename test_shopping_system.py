import unittest
from shopping_system import Product, ShoppingCart, Inventory

class TestProduct(unittest.TestCase):

    def setUp(self):
        self.product = Product("P001", "Sample Product", 10.99)

    def test_product_creation(self):
        self.assertEqual(self.product.product_id, "P001")
        self.assertEqual(self.product.name, "Sample Product")
        self.assertEqual(self.product.price, 10.99)

class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        self.cart = ShoppingCart()
        self.product1 = Product("P001", "Sample Product 1", 10.99)
        self.product2 = Product("P002", "Sample Product 2", 5.49)

    def test_add_product(self):
        self.cart.add_product(self.product1, 2)
        self.assertIn(self.product1, self.cart.products)
        self.assertEqual(self.cart.products[self.product1], 2)

    def test_remove_product(self):
        self.cart.add_product(self.product1, 2)
        self.cart.remove_product("P001", 1)
        self.assertEqual(self.cart.products[self.product1], 1)

    def test_calculate_total(self):
        self.cart.add_product(self.product1, 2)
        self.cart.add_product(self.product2, 1)
        total = self.cart.calculate_total()
        self.assertEqual(total, 27.47)  # 2*10.99 + 1*5.49

    def test_list_products(self):
        self.cart.add_product(self.product1, 2)
        self.cart.add_product(self.product2, 3)
        products_list = self.cart.list_products()

        # Check that the list has the expected length.
        self.assertEqual(len(products_list), 2)

        # Check for product1 details in the list.
        product1_str = "Sample Product 1 (ID: P001) - Quantity: 2"
        self.assertIn(product1_str, products_list)

        # Check for product2 details in the list.
        product2_str = "Sample Product 2 (ID: P002) - Quantity: 3"
        self.assertIn(product2_str, products_list)


class TestInventory(unittest.TestCase):

    def setUp(self):
        self.inventory = Inventory()
        self.product = Product("P001", "Sample Product", 10.99)

    def test_add_product(self):
        self.inventory.add_product(self.product)
        self.assertIn("P001", self.inventory.products)

    def test_remove_product(self):
        self.inventory.add_product(self.product)
        self.inventory.remove_product("P001")
        self.assertNotIn("P001", self.inventory.products)

if __name__ == '__main__':
    unittest.main()
