class CharacterNode:
    # Parameterized constructor to create a node with appropriate defaults.
    def __init__(self, character = None, frequency = 0):
        self.character = character
        self.frequency = frequency
        self.right = None
        self.left = None
        self.parent = None

    # Sets the left child of the node.
    def set_left(self, left):
        self.left = left
        self.left.set_parent(self)

    # Sets the right child of the node.
    def set_right(self, right):
        self.right = right
        self.right.set_parent(self)

    # Sets the parent of the node.
    def set_parent(self, parent):
        self.parent = parent

    # Returns the frequency of the character represented by the node.
    def get_frequency(self):
        return self.frequency

    # Gets the character for this node.
    def get_character(self):
        return self.character

    # Helps compare less than condition with any other node.
    def __lt__(self, other):
        return self.frequency < other.frequency
    
    # Helps print the node in a human readable format.
    def __str__(self):
        if self == None:
            return '[None]'
        if self.left != None and self.right == None:
            return f'[{self.left.character}]<--[{self.character}:{self.frequency}]'
        if self.left == None and self.right != None:
            return f'[{self.character}:{self.frequency}]-->[{self.right.character}]'
        if self.left == None and self.right == None:
            return f'[{self.character}:{self.frequency}]'   
        return f'[{self.left.character}]<--[{self.character}:{self.frequency}]-->[{self.right.character}]'


if __name__ == "__main__":
    node1 = CharacterNode('P', 1)
    node2 = CharacterNode('a', 2)
    node3 = CharacterNode('s', 1)

    print(node1)
    print(node2)
    print(node3)
