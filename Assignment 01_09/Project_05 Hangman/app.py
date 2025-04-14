import random

# Word list
words = ["python", "developer", "hangman", "challenge", "notebook"]

def get_valid_word(words):
    word = random.choice(words)
    while '_' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) 
    alphabet = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    used_letters = set() 

    lives = 6

    print("Welcome to Hangman!")

    while len(word_letters) > 0 and lives > 0:
        print("\nYou have", lives, "lives left.")
        print("Used letters: ", ' '.join(used_letters))

        # Current state of the word
        word_display = [letter if letter in used_letters else '_' for letter in word]
        print("Current word: ", ' '.join(word_display))

        user_letter = input("Guess a letter: ").upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("Nice guess!")
            else:
                lives -= 1
                print("Wrong guess.")
        elif user_letter in used_letters:
            print("You already guessed that letter.")
        else:
            print("Invalid character. Please enter a valid letter.")

    if lives == 0:
        print(f"\nYou died, the word was {word}")
    else:
        print(f"\nCongrats! You guessed the word: {word} 🎉")


hangman()
