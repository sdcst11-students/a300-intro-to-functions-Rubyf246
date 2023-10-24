"""
Task 2:
Create a program to play a number guessing game
There should be a function:
title()
displays instructions and how to play

game()
plays the games
"""
def title():
    print("WELCOME TO KIMMIE'S GUESSING NUMBER GAME!!! \n You have to guess a number from 0 to 50, then Kimmie will tell you if your number is too high or too low. \n You have 7 guesses! \n GOOD LUCK ")
title()
num=47
def game():
    for i in range(1, 8):
        numguess= int(input(f"put in your {i} guess"))
        if  numguess==num:
            print("YOU GOT IT!")
            break 
        elif numguess>num:
            print("Guess is too high")
        elif numguess<num:
            print("Guess is too low")
game()