# TABIND Scrabble project
# Olivia
# 2024/10/23
# Description: The objective of this project is to develop a program that takes the letter combination “tabind” and creates an alphabetical list of all the words that can be found with those letters. 


import itertools

# Load dictionary of valid English words
def load_dictionary():
    with open("words.txt", "r") as file:
        words = set(word.strip().lower() for word in file)
    return words

# Generate all possible words
def generate_words(letters, dictionary):
    words = set()
    for i in range(1, len(letters) + 1):  
        for combination in itertools.permutations(letters, i):
            word = "".join(combination)
            if word in dictionary:  # Check if the word is valid
                words.add(word)
    return sorted(words)  # Return the words in alphabetical order

def main():
    letters = "tabind"  # The given letters
    dictionary = load_dictionary() 
    valid_words = generate_words(letters, dictionary)  
    print("Words found:")
    for word in valid_words:
        print(word)

# Run the program
if __name__ == "__main__":
    main()
