from CharacterFrequencyCalculator import CharacterFrequencyCalculator
from CharacterNode import CharacterNode
from CharacterNodeTree import CharacterNodeTree
import os
import math

# Read input from a data file.
characters = ""
with open('data.txt', 'r') as file:
    characters = file.read()
file_size = os.path.getsize("data.txt")

print("\nInput File Size in Bytes:", file_size)
print("\nInput is as follows: \n")
print(characters)

# Generate frequency map
calculator = CharacterFrequencyCalculator(characters)
character_map = calculator.get_character_frequency_map()
print("\nFrequency Map generated is as follows: \n")
print(character_map)

# Convert into nodes.
character_node_list = []
for i, (k, v) in enumerate(character_map.items()):
    character_node_list.append(CharacterNode(k, v))

# Create a tree from the nodes to help get the encoded table.
tree = CharacterNodeTree(character_node_list)

print("\nFollowing is the tree representation in level order format: \n")
tree.print_character_node_tree()
print("\nFollowing is the Encoding table generated: \n")
print(tree.code_table)


# Encode the characters.
encoded_characters = ""
for char in characters:
    encoded_characters = f'{encoded_characters}{tree.code_table[char]}'

print("Encoded_characters are as follows: \n", encoded_characters)
output_size = int(math.ceil(len(encoded_characters)/8))
print("\nExpected output File Size in Bytes: \n", output_size)


print("\nCompression % is as follows: \n",int(math.floor(100*((file_size-output_size)/file_size))))


# Decode using the reversed encoding table.
key = ''
decoding_map = {v: k for k, v in tree.code_table.items()}
print("\nDecoding table is as follows: \n", decoding_map)

# Print the decoded value to cross check loss less transformations.
print("\nOutput to prove loss less transformations across cycles of endoing and decoding. \n")
for char in encoded_characters:
    key = f'{key}{char}'
    if key in decoding_map:
        print(decoding_map[key], end='')
        key = ''
print()




