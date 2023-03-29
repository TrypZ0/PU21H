import random

# Lista av ord som spelet kan be efter
words = ['python', 'computer', 'algorithm', 'guitar', 'hamburger',
         'rainbow', 'jazz', 'ocean', 'umbrella', 'television']

# Väljer ett slumpmässigt ord ur listan med hjälp av random modulen
word = random.choice(words)

# Rita ut understräcken (_) för att representera bokstäver som inte gissats än
hidden_word = ['_'] * len(word)

# håller koll på vilka bokstäver spelaren redan missat
guessed_letters = []

# Hur många gissningar en spelare har före spelet är över
max_guesses = 6

# Håller koll på hur många gånger spelaren gissat fel, kan sedan jämföras med max_guesses övanför
num_guesses = 0

# Otroligt vacker ASCII grafik för spelet så att man visuellt ser gubben ritas ut. hoppar framåt ett steg i array:n för varje fel gissning.
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

# Spelets gång
while True:
    # Printar ut dom osynliga bokstäverna (_)
    print(' '.join(hidden_word))

    # Ritar ut den framen av ascii konst som motsvarar antalet felaktiga gissningar
    print(hangman[num_guesses])

    # Ber spelaren att gissa en bokstav
    guess = input('Guess a letter: ').lower()

    # Kolla ifall bokstaven redan gissats, om ja så upplyses spelaren att den redan gissat bokstaven.
    if guess in guessed_letters:
        print('You already guessed that letter!')
        continue

    # lägger till felaktiga gissningar till listan av gissade bokstäver
    guessed_letters.append(guess)

    # Koller ifall gissningen finns i ordet, alltså ifall gissningen är rätt
    if guess in word:
        # byter ut motsvarande tomma bokstäverna med dom riktiga rättgissade bokstäverna
        for i in range(len(word)):
            if word[i] == guess:
                hidden_word[i] = guess
    else:
        # Spelaren gissar fel
        num_guesses += 1
        print('Incorrect guess!')

        # Håller koll på ifall spelaren använt upp alla sina gissningar
        if num_guesses == max_guesses:
            print('You lose! The word was', word)
            print(hangman[num_guesses])
            

# Håller koll på om ordet blivit gissat
    if ''.join(hidden_word) == word:
        print('Congratulations, you guessed the word!')
        play_again = input(
            "Press ENTER to play again or press escape to exit game: ")
        if play_again.lower() == "escape":
            break
        else:
            # Väljer ett nytt ord att spela med och återställer variabler
            word = random.choice(words)
            hidden_word = ['_'] * len(word)
            guessed_letters = []
            num_guesses = 0
            continue
