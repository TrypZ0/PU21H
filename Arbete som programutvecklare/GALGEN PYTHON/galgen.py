import random

# List of words to choose from
words = ['python', 'computer', 'algorithm', 'guitar', 'hamburger', 'rainbow', 'jazz', 'ocean', 'umbrella', 'television']

# Select a random word from the list
word = random.choice(words)

# Create a list of underscores to represent the hidden word
hidden_word = ['_'] * len(word)

# Keep track of the guessed letters
guessed_letters = []

# Maximum number of incorrect guesses
max_guesses = 6

# Keep track of the number of incorrect guesses
num_guesses = 0

# Hangman ASCII art
hangman = [
    """
    +---+
    |   |
        |
        |
        |
        |
  =========
    """,
    """
    +---+
    |   |
    O   |
        |
        |
        |
  =========
    """,
    """
    +---+
    |   |
    O   |
    |   |
        |
        |
  =========
    """,
    """
    +---+
    |   |
    O   |
   /|   |
        |
        |
  =========
    """,
    """
    +---+
    |   |
    O   |
   /|\  |
        |
        |
  =========
    """,
    """
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
  =========
    """,
    """
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
  =========
    """
]

# Main game loop
while True:
    # Print the current state of the hidden word
    print(' '.join(hidden_word))
    
    # Print the hangman ASCII art
    print(hangman[num_guesses])
    
    # Ask the user for a guess
    guess = input('Guess a letter: ').lower()
    
    # Check if the guess has already been made
    if guess in guessed_letters:
        print('You already guessed that letter!')
        continue
    
    # Add the guess to the list of guessed letters
    guessed_letters.append(guess)
    
    # Check if the guess is in the word
    if guess in word:
        # Replace the underscores with the guessed letter
        for i in range(len(word)):
            if word[i] == guess:
                hidden_word[i] = guess
    else:
        # Incorrect guess
        num_guesses += 1
        print('Incorrect guess!')
        
        # Check if the maximum number of guesses has been reached
        if num_guesses == max_guesses:
            print('You lose! The word was', word)
            print(hangman[num_guesses])
            break
    
    # Check if the word has been guessed
    if ''.join(hidden_word) == word:
        print('Congratulations, you guessed the word!')
        break
