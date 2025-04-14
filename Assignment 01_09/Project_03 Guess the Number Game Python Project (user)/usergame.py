## 3 project : Guess the number game user 

import random

def guess_the_number():
    secret_number = random.randint(1, 100)
    attempts = 6

    print("Welcome to Guess the Number Game!")
    print("Guess a number between 1 and 100.")
    print(f"You have {attempts} attempts. Let's begin!\n")

def guess_the_number():
    secret_number = 47 
    attempts = 6

    while attempts > 0:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input! Please enter a number.\n")
            continue

        if guess == secret_number:
            print(f"Congratulations! You guessed the right number: {guess}")
            break
        else:
            attempts -= 1
            difference = abs(secret_number - guess)

           
            if difference >= 40:
                hint = "Too High! ⬆" if guess > secret_number else "Too Low! ⬇"
            elif difference >= 20:
                hint = "Medium Range 📉"
            elif difference >= 10:
                hint = "Very Close!"
            else:
                hint = "Almost There!"

            print(f"{hint} | Attempts left: {attempts}\n")

            if attempts == 0:
                print(f" Game Over! The correct number was {secret_number}")
                print("Try Again!")


guess_the_number()


