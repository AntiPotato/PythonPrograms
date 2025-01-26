from queue import Queue
from CharacterNode import CharacterNode
from queue import PriorityQueue

class CharacterNodeTree:
    def __init__(self, character_node_list):
        self.character_node_list = character_node_list
        self.tree_root = None
        self.code_table = {}
        self.__build_character_node_tree__()

    def __build_character_node_tree__(self):
        nodes_min_heap = PriorityQueue()
        for node in self.character_node_list.copy():
            nodes_min_heap.put(node)

        for i in range(len(self.character_node_list)-1):

            # Find the two min frequency nodes so that we can connect them with a common parent.
            min_frequency_node = nodes_min_heap.get()
            second_min_frequency_node = nodes_min_heap.get()

            # Create a new node with combined frequencies.
            parent_node = CharacterNode(character = f'{second_min_frequency_node.character}{min_frequency_node.character}', frequency =  min_frequency_node.frequency + second_min_frequency_node.frequency)
            parent_node.set_left(second_min_frequency_node)
            parent_node.set_right(min_frequency_node)

            # Add it to the heap to be able to run the next round of matching.
            nodes_min_heap.put(parent_node)
            
            self.tree_root = parent_node

        self.__extract_code_table__(tree_root = self.tree_root, path = f'')


    def __extract_code_table__(self, tree_root, path):
        if tree_root.left == None and tree_root.right == None:
            self.code_table[tree_root.character] = path
            return
        if tree_root.left != None:
            self.__extract_code_table__(tree_root = tree_root.left, path = f'{path}0')
        if tree_root.right != None:
            self.__extract_code_table__(tree_root = tree_root.right, path = f'{path}1')
            
                
    def print_character_node_tree(self):
        character_queue = Queue(maxsize=pow(2,len(self.character_node_list)+1))
        character_queue.put(self.tree_root)

        count = 0
        level = 1
        all_none = True

        while(not character_queue.empty()):
            element = character_queue.get()
            if element == None:
                character_queue.put(None)
                character_queue.put(None)
            else:
                character_queue.put(element.left)
                character_queue.put(element.right)
                all_none = False
            
            print(element, end = ' ')
            
            count = count + 1
            if pow(2, level) - 1 == count:
                print()
                level = level + 1
                if all_none:
                    print()
                    return
                all_none = True
        print()
            

if __name__ == "__main__":
    node1 = CharacterNode('P', 1)
    node2 = CharacterNode('a', 2)
    node3 = CharacterNode('s', 1)

    tree = CharacterNodeTree([node1, node2, node3])
    tree.print_character_node_tree()
    
        
        
