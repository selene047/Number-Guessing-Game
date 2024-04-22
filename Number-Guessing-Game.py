# Number Guessing Game from QuickStart Python Guide - Chapter 3
from random import seed
from random import randint

number = randint(1, 10)
# The input() function waits for the user to input a value and press Enter
# The int() function is used to convert the user input, which is initially a string,
# into an integer. This conversion ensures that the input is treated as a numerical 
# value rather than text. If not a number entered, Python will raise a ValueError.

guess = int(input("I'm thinking of a number! Which do you think it is? "))

if guess > number:
    print("Nice Try! But your guess was too high!")
    print(f"The number was actually: {number}")
elif guess < number:
    print("Aw man! You guessed too low!")
    print(f"The number was actually: {number}")
else:
    print("You guessed correctly. Congratulations! You win!")

