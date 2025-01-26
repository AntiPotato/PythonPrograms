class CharacterNode:
    def __init__(self, character = None, frequency = 0):
        self.character = character
        self.frequency = frequency
        self.right = None
        self.left = None
        self.parent = None

    def set_left(self, left):
        self.left = left
        self.left.set_parent(self)

    def set_right(self, right):
        self.right = right
        self.right.set_parent(self)

    def set_parent(self, parent):
        self.parent = parent

    def get_frequency(self):
        return self.frequency

    def get_character(self):
        return self.character

    def __lt__(self, other):
        return self.frequency < other.frequency

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
