# Shopping Cart System

Welcome to the "Shopping Cart System" exercise. Your task is to design and implement a simple shopping cart system using object-oriented programming principles, focusing on the use of classes, dictionaries, and functions.

## Problem Description:

Imagine you're building a basic online shopping system. This system needs to be able to manage products and user shopping carts.

### Requirements:

1. **Product Class**:
   - Each product has the following attributes: `product_id`, `name`, `price`.
   - The `product_id` should be a unique identifier for each product.

2. **ShoppingCart Class**:
   - Each shopping cart has a collection of products.
   - Implement the following methods:
        - `add_product`: Add a product to the cart. If the product is already in the cart, increase its quantity.
        - `remove_product`: Remove a product from the cart or decrease its quantity.
        - `calculate_total`: Calculate the total price of products in the cart.
        - `list_products`: List all products in the cart along with their quantities.

3. **Inventory Class**:
   - Holds a collection of products available for sale.
   - Implement the following methods:
        - `add_product`: Add a product to the inventory.
        - `remove_product`: Remove a product from the inventory.

## Getting Started:

1. **Setting up**:
   - Ensure you have Python installed on your machine.
   - Clone this repository or download the project files.
   - Navigate to the project directory using your terminal or command prompt.

2. **Files**:
   - `shopping_system.py`: Contains the initial stubs for the `Product`, `ShoppingCart`, and `Inventory` classes.
   - `test_shopping_system.py`: Contains unit tests to validate your solution.

3. **Implementation**:
   - Open `shopping_system.py` in your favorite text editor or IDE.
   - Complete the implementation of the provided methods and add any additional methods or attributes you deem necessary.

4. **Testing**:
   - Once your implementation is complete, run the tests using the command: `python test_shopping_system.py`
   - Make sure all tests pass to confirm the correctness of your solution.

5. **Submission**:
   - After you've finished the implementation and tested your solution, follow the submission instructions provided by your instructor or the platform.

## Tips:

- Use dictionaries to efficiently manage products in both the shopping cart and inventory.
- Ensure you handle edge cases, such as attempting to remove more products than are available in the cart or inventory.
- Think about the user experience. For example, when listing products in the cart, it's helpful to also show the quantity and total price for each product.

Happy coding and enjoy building your shopping cart system!
