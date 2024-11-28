class ItemToPurchase:
	# Parameterized constructor with default values helping to act like a default constructor
	def __init__(self, item_name: str = "none", item_price: float = 0, item_quantity: int = 0):
		self.item_name = item_name
		self.item_price = item_price
		self.item_quantity = item_quantity
	
	# Method to calculate and print the cost.
	def print_item_cost(self):
		print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.0f} = ${(self.item_price * self.item_quantity):.0f}")

	# Method to calculate and print the total cost.
	def print_total(self, other_item):
		print("\nTOTAL COST\n")
		self.print_item_cost()
		other_item.print_item_cost()
		print(f"Total: ${((self.item_price * self.item_quantity) + (other_item.item_price * other_item.item_quantity)):.0f}")

# Taking user's input for creating two items.
print("\nItem1\n")
item1 = ItemToPurchase(input("\nEnter the item name:\n"), float(input("\nEnter the item price:\n")), int(input("\nEnter the item quantity:\n")))

print("\nItem2\n")
item2 = ItemToPurchase(input("\nEnter the item name:\n"), float(input("\nEnter the item price:\n")), int(input("\nEnter the item quantity:\n")))

# Printing total
item1.print_total(item2)

 


	