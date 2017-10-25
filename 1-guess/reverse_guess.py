# Think of a number between 0 and 99. Then write a python program
# to guess the number you have thought of
import random

min = 0
max=99
user_input = None

while user_input != "c":
    guess = random.randint(min, max)
    print ("My guess is "+ str(guess))
    user_input = input ("h/l/c ?")
    if user_input == "h":
        max = guess - 1
    elif user_input == "l":
        min  = guess + 1



