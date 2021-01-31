#!/usr/bin/env python3
import sys, random
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"


print("Hello!")
n = input ("What is your name? ")
print("Nice to meet you, {}!".format(n))

Answer = ["Yes", "No"]
for x in Answer:
    x = input("Would you like to play a game? (Y/N) ")
    if x == "Yes":
        print("Great!")
        break
    elif x == "No":
        print("Oh, that's too bad. See you later!")
        exit()
    else:
        print("I'm sorry, I didn't understand that.") 
        

number = random.randrange(1,11)
count = 0
guess = -1
while guess != number:
    count = count + 1
    guess = input("Guess a number from 1 to 10: ") 
    try:
        guess = int(guess) 
        if guess != number:
            print("Not quite, please try again!")
    except:
        print("Please enter a number!")
print("Great job! You got it! You were able to guess the number in " + str(count) + " tries.")
print("Let's play again soon!")