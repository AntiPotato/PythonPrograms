from ItemToPurchase import ItemToPurchase

class ShoppingCart:
    # Parameterized constructor with default values helping to act like a default constructor.
    def __init__(self, customer_name: str = "none", current_date: str = "January 1, 2020", cart_items: list = []):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items

    # Method to find an item's index in the cart by item's name. Returns -1 if there is no match.
    def find_item_index_by_name(self, item_name):
        item_index = -1
        for index, item in enumerate(self.cart_items):
            if item.item_name == item_name:
                item_index = index
        return item_index

    # Method to find an item in the cart by item's name. Returns None if there is no match.   
    def get_item_by_name(self, item_name):
        item_index = self.find_item_index_by_name(item_name)

        if item_index == -1:
            return None
        return self.cart_items[item_index]

    # Method to add an item to the cart.  
    def add_item(self, item):
        self.cart_items.append(item)

    # Method to remove an item by name from the cart. Skips if thers is no match.
    def remove_item(self, item_name):
        item_index = self.find_item_index_by_name(item_name)
                
        if item_index == -1:
            print("Item not found in cart. Nothing removed.")
        else:
            del self.cart_items[item_index]

    # Method to modify an item in the cart. Skips if item is not found.
    # Also skips if price or quantity or description has default values.
    def modify_item(self, item):
        item_index = self.find_item_index_by_name(item.item_name)
                
        if item_index == -1:
            print("Item not found in cart. Nothing modified.")
            return
        
        if item.item_price != 0:
            self.cart_items[item_index].item_price = item.item_price

        if item.item_quantity != 0:
            self.cart_items[item_index].item_quantity = item.item_quantity

        if item.item_description != "none":
            self.cart_items[item_index].item_description = item.item_description


    # Returns number of items in the cart.
    def get_num_items_in_cart(self):
        num_items = 0
        for item in self.cart_items:
            num_items = num_items + item.item_quantity

        return num_items

    # Calculates and returns the cost of the cart.
    def get_cost_of_cart(self):
        cost = 0
        for item in self.cart_items:
            cost = cost + item.get_item_cost()

        return cost

    # Prints the cart total.       
    def print_total(self):
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
            return
        
        print('{: ^100}'.format(f"{self.customer_name}'s Shopping Cart - {self.current_date}"))
        print('{: ^100}'.format(f"Number of Items: {self.get_num_items_in_cart()}"))
        for item in self.cart_items:
            item.print_item_cost()
        print('{: ^100}'.format(f"Total: ${self.get_cost_of_cart()}"))
        print()

    # Prints item descriptions.
    def print_description(self):
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
            return
        
        print('{: ^100}'.format(f"{self.customer_name}'s Shopping Cart - {self.current_date}"))
        print('{: ^100}'.format(f"Item Descriptions"))
        for item in self.cart_items:
            item.print_item_description()
        print()

# Method to print the menu and help take various actions on the shopping cart.
def print_menu(shopping_cart):
    print()
    print('{: ^100}'.format("MENU"))
    print('{: ^100}'.format("a - Add item to cart"))
    print('{: ^100}'.format("r - Remove item from cart"))
    print('{: ^100}'.format("c - Change item quantity"))
    print('{: ^100}'.format("i - Output items' descriptions"))
    print('{: ^100}'.format("o - Output shopping cart"))
    print('{: ^100}'.format("q - Quit"))
    choice = input('{: ^100}'.format("Choose an option:\n"))
    print()
    if choice == 'q':
        return
    elif choice == 'a':
        item = ItemToPurchase(input("\nEnter the item name:\n"), float(input("\nEnter the item price:\n")), int(input("\nEnter the item quantity:\n")), input("\nEnter the item desciption:\n"))
        shopping_cart.add_item(item)
    elif choice == 'r':
        item_name = input("\nEnter item name to remove:\n")
        shopping_cart.remove_item(item_name)
    elif choice == 'c':
        item_name = input("\nEnter item name whose quantity you want to modify:\n")
        quantity = int(input(f"\nEnter the new quantity for the item:\n"))
        modified_item = ItemToPurchase(item_name = item_name, item_quantity = quantity)
        shopping_cart.modify_item(modified_item)
    elif choice == 'i':
        shopping_cart.print_description()
    elif choice == 'o':
        shopping_cart.print_total()
    print_menu(shopping_cart)


if __name__ == "__main__":
    shopping_cart = ShoppingCart(input("\nEnter the customer name:\n"), input("\nEnter the current date:\n"), [])
    print_menu(shopping_cart)
        
            
    
    
    
    





        
