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
            print('{: ^100}'.format("SHOPPING CART IS EMPTY"))
            return
        
        print('{: ^100}'.format(f"{self.customer_name}'s Shopping Cart - {self.current_date}"))
        print('{: ^100}'.format(f"Number of Items: {self.get_num_items_in_cart()}"))
        for item in self.cart_items:
            item.print_item_cost()
        print('{: ^100}'.format(f"Total: ${self.get_cost_of_cart():.0f}"))
        print()

    # Prints item descriptions.
    def print_description(self):
        if len(self.cart_items) == 0:
            print('{: ^100}'.format("SHOPPING CART IS EMPTY"))
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

    print('{: ^100}'.format("Choose an option:"))
    choice = input('{: <50}'.format(""))
    print()
          
    if choice == 'q':
        return
    
    elif choice == 'a':
        print('{: ^100}'.format("ADD ITEM TO CART"))
        
        print('{: ^100}'.format("Enter the item name:"))
        item_name = input('{: <50}'.format(""))
        
        print('{: ^100}'.format("Enter the item description"))
        item_description = input('{: <50}'.format(""))
        
        print('{: ^100}'.format("Enter the item price:"))
        item_price = float(input('{: <50}'.format("")))
        
        print('{: ^100}'.format("Enter the item quantity"))
        item_quantity = int(input('{: <50}'.format("")))
        
        item = ItemToPurchase(item_name, item_price, item_quantity, item_description)
        
        shopping_cart.add_item(item)
        
    elif choice == 'r':
        print('{: ^100}'.format("REMOVE ITEM FROM CART"))
        
        print('{: ^100}'.format("Enter name of item to remove:"))
        item_name = input('{: <50}'.format(""))
        
        shopping_cart.remove_item(item_name)
        
    elif choice == 'c':
        print('{: ^100}'.format("CHANGE ITEM QUANTITY"))
        
        print('{: ^100}'.format("Enter the item name:"))
        item_name = input('{: <50}'.format(""))

        print('{: ^100}'.format("Enter the new quantity:"))
        item_quantity = int(input('{: <50}'.format("")))
        
        modified_item = ItemToPurchase(item_name = item_name, item_quantity = item_quantity)
        shopping_cart.modify_item(modified_item)
        
    elif choice == 'i':
        print('{: ^100}'.format("OUTPUT ITEMS' DESCRIPTIONS"))
        
        shopping_cart.print_description()
        
    elif choice == 'o':
        print('{: ^100}'.format("OUTPUT SHOPPING CART"))
        
        shopping_cart.print_total()

    # Calling itself to show the menu again.    
    print_menu(shopping_cart)


if __name__ == "__main__":

    print('{: ^100}'.format("Enter customer's name:"))
    customer_name = input('{: <50}'.format(""))
    print('{: ^100}'.format("Enter today's date:"))
    today_date = input('{: <50}'.format(""))

    print()
    print('{: ^100}'.format(f'Customer name: {customer_name}'))
    print('{: ^100}'.format(f'Today\'s date: {today_date}'))
    
    shopping_cart = ShoppingCart(customer_name, today_date)
    
    print_menu(shopping_cart)
        
            
    
    
    
    





        
