class Item:
        # Constructor.
        def __init__(self, name, price, quantity):
                self.name = name
                self.price = price
                self.quantity = quantity

        # Help with equality comparison.
        def __eq__(self, other):
                if not isinstance(other, Item):
                        return False
                return self.name == other.name

        # Help with less than comparison.
        def __lt__(self, other):
                return self.name < other.name

        #Help with pretty printing the object.
        def __str__(self):
                return f"Item Name:{self.name}\nItem Price:{self.price}\nItem Quantity:{self.quantity}"

