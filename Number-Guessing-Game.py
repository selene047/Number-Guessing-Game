# Number Guessing Game from QuickStart Python Guide - Chapter 3
#number = randint(1, 10)
# The input() function waits for the user to input a value and press Enter
# The int() function is used to convert the user input, which is initially a string,
# into an integer. This conversion ensures that the input is treated as a numerical 
# value rather than text. If not a number entered, Python will raise a ValueError.
'''

guess = int(input("I'm thinking of a number! Which do you think it is? "))

if guess > number:
    print("Nice Try! But your guess was too high!")
    print(f"The number was actually: {number}")
elif guess < number:
    print("Aw man! You guessed too low!")
    print(f"The number was actually: {number}")
else:
    print("You guessed correctly. Congratulations! You win!")
'''

#Attempting a more enhanced version with a function that utilizes a loop 
import random

def guess_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while attempts < 3:
        guess = int(input("I'm thinking of a number between 0 and 100! Which do you think it is? You have 3 chances!"))

        if guess == number_to_guess:
            print("You guessed correctly! Congratulations! You win!")
        elif guess < number_to_guess:
            print("Aw man! You guessed too low! Try again!")
        else:
            print("Nice Try! But your guess was too high!")

        attempts += 1

    if attempts == 3:
        print(f"Sorry, you've used all of your attempts. The number was {number_to_guess}.")

    play_again = input("Do you want to play again? (yes/no)")
    if play_again.lower == "yes":
        guess_number()
    else:
        print("Thank you for playing!")

guess_number()