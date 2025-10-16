'''
Program: lucky.py
Author: Berry gavigan
Class: CIS
Date:10/2/25
'''

import random

totalRounds = 0
totalWins = 0
totalGuesses = 0

print("=" * 50)
print("  WELCOME TO THE LUCKY NUMBER GUESSING GAME!")
print("=" * 50)
print()

while True: 
    luckyNum = random.randint(1, 50)
    maxAttempts = 7
    attemps = 0
    totalRounds += 1
    result = ""
   
    print(f"\nRound {totalRounds + 1}")
    print("I'm thinking of a lucky number between 1 and 50...")
    print(f"You have {maxAttempts} attempts to guess it!")
    print()
   
    while attemps < maxAttempts: 
        guess = int(input("Guess:"))
        attemps += 1
        if guess == luckyNum:
            print("You win!")
            totalWins += 1
            result = "win"
            break

        elif guess > luckyNum:
            print("To high")
        else:
            print("To low")
    totalGuesses += attemps
       
    if result != "win":
        print("you lose")
        result = "lost"

    print("\nYou" , result, "with" , attemps, "atetmps")
   
    playAgain = input("Do you want to play again? Type 'No' To stop. ").lower()
    if playAgain == "no":
        break
print("Total wins" , totalWins)
print("total guesses" , totalGuesses)
print("total rounds" , totalRounds)
print("\nThanks for playing! Goodbye!")
