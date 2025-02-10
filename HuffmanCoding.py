from CharacterFrequencyCalculator import CharacterFrequencyCalculator
from CharacterNode import CharacterNode
from CharacterNodeTree import CharacterNodeTree
import os
import math

def to_binary_32(num):
  """Converts an integer to a 32-bit binary string.

  Args:
    num: The integer to convert.

  Returns:
    A 32-bit binary string representation of the integer.
  """
  return bin(num & 0xFFFFFFFF)[2:].zfill(32)

def write_binary_string_to_file(binary_string, filename):
    """Writes a string of 0s and 1s to a binary file.

    Args:
        binary_string: The string of 0s and 1s to write.
        filename: The name of the file to write to.
    """
    with open(filename, 'wb') as f:
        # Convert the binary string to bytes
        byte_array = bytearray()
        for i in range(0, len(binary_string), 8):
            byte = binary_string[i:i+8]
            byte_array.append(int(byte, 2))
        f.write(bytes(byte_array))

def binary_string_from_file(file_path):
    """Reads a binary file and returns a string of 1s and 0s."""
    try:
        with open(file_path, 'rb') as file:
            binary_data = file.read()
            binary_string = ''.join(format(byte, '08b') for byte in binary_data)
            return binary_string
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occurred: {e}"


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
# Not printing the tree, as it is taking a lot of space. Please uncomment to see this.
#tree.print_character_node_tree()
print("\nFollowing is the Encoding table generated: \n")
print(tree.code_table)


# Encode the characters.
# We first write a 4 bytes to represent the number of characters present.
# This will help us during decoding by ignoring the padding that will be added to write in a binary file.
encoded_characters = ''.join(to_binary_32(len(characters)))
print("We start with the number of characters", len(characters) ," written inside the encoded characters to help with decoding:", encoded_characters)
for char in characters:
    encoded_characters = f'{encoded_characters}{tree.code_table[char]}'


print("Encoded_characters are as follows: \n", encoded_characters)
output_size = int(math.ceil(len(encoded_characters)/8))
print("\nExpected output File Size in Bytes without padding: \n", output_size)

# Pad the encoded characters to become proper byte sized.
for padding_count in range(len(encoded_characters)%8):
    encoded_characters = f'{encoded_characters}{0}'
print("Encoded_characters after padding with 0s to right are as follows: \n", encoded_characters)


filename = "binary_file.bin"
write_binary_string_to_file(encoded_characters, filename)
encoded_file_size = os.path.getsize(filename)
print(f"File Size of the encoded file in Bytes: {encoded_file_size}")


print("\nCompression % is as follows: \n",int(math.floor(100*((file_size-encoded_file_size)/file_size))))


# Decode using the reversed encoding table.
key = ''
decoding_map = {v: k for k, v in tree.code_table.items()}
print("\nDecoding table is as follows: \n", decoding_map)

# Print the decoded value to cross check loss less transformations.
print("\nOutput to prove loss less transformations across cycles of endoing and decoding. This prints the padding as well.\n")
for char in encoded_characters[32:]:
    key = f'{key}{char}'
    if key in decoding_map:
        print(decoding_map[key], end='')
        key = ''
print()


# Decode by reading the encoded file now.
encoded_characters_from_file = binary_string_from_file(filename).strip()
number_of_characters = int(encoded_characters_from_file[:32],2)
print("No. of characters to decode:",number_of_characters)

print("\nOutput to prove loss less transformations across cycles of endoing and decoding and saving to files. \n")
for char in encoded_characters_from_file[31:]:
    if (number_of_characters == 0):
        break
    key = f'{key}{char}'
    if key in decoding_map:
        number_of_characters = number_of_characters - 1
        print(decoding_map[key], end='')
        key = ''
print()






