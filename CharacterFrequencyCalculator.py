class CharacterFrequencyCalculator:
    # Parameterized constructor to help create a calculator.
    def __init__(self, characters: str):
        self.characters = characters
        self.character_dictionary = {}
        self.calculate()


    # Calculates the frequencies of the characters.
    def calculate(self):
        for char in self.characters:
            self.character_dictionary[char] = self.character_dictionary.get(char, 0) + 1

    # Returns the calculated frequencies.
    def get_character_frequency_map(self):
        return self.character_dictionary



if __name__ == "__main__":
    choice = 'Y'
    while(choice == 'Y'):
        characters = input("Enter a character string: \n")
        calculator = CharacterFrequencyCalculator(characters)
        character_map = calculator.get_character_frequency_map()
        print(character_map)
        choice = input("Enter Y to continue Or anything else to quit.")


    
