from Item import Item

items = [Item("Cooking Book", 18, 100),
         Item("Recipies", 33, 200),
         Item("Pen", 4, 1002),
         Item("Pencil", 2, 123),
         Item("Blackboard", 70, 89),
         Item("Recipi Book", 18, 100),
         Item("Gardening", 33, 200),
         Item("Table top", 4, 1002),
         Item("Plant", 2, 123),
         Item("Whiteboard", 70, 89)]

def LinearSearch(items, item_name_to_search):
    item_to_search = Item(item_name_to_search, 0, 1)
    for i in range(len(items)):
        if items[i] == item_to_search:
            return items[i]
    return None


while(True):
    item_found = LinearSearch(items, input("Enter the item name you want to check: "))

    if item_found == None:
        print("Item was not found")
    else:
        print(f"Found item:\n{item_found}")


    choice = input("Do you wish to continue? Press Y or N: ")
    if choice != 'Y':
        break;
    


