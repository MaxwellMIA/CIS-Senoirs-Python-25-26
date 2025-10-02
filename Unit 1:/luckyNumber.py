'''
Program: lucky.py
Author: Berry gavigan
Class: CIS
Date:10/2/25
'''

import random

# Game statistics
totalRounds = 0
totalWins = 0
totalGuesses = 0

print("=" * 50)
print("  WELCOME TO THE LUCKY NUMBER GUESSING GAME!")
print("=" * 50)
print()

# Main game loop - play multiple rounds
# TODO: Use while True loop with break statement here
while True: 
    # Generate random lucky number
    luckyNum = random.randint(1, 50)
    # Set maximum attempts
    maxAttempts = 7
    # Initialize attempt counter
    attemps = 0
   
    print(f"\nRound {totalRounds + 1}")
    print("I'm thinking of a lucky number between 1 and 50...")
    print(f"You have {maxAttempts} attempts to guess it!")
    print()
   
    # Guessing loop - count-controlled while loop
    while attemps < maxAttempts: 
        # Get user's guess
        guess = int(input("Guess:"))
        # Increment attempt counter
        attemps += 1
        # Check if guess is correct
        if guess == luckyNum:
            # Player wins!
            print("You win!")
            #Update statistics
            totalWins += 1
            break
        # Provide hints
        elif guess > luckyNum:
            print("To high")
        else:
            print("To low")
    totalRounds += 1
    totalGuesses += attemps
        
       
    # If loop completes without break, player lost
    # TODO: Handle case where player runs out of attempts
   
    # Display round statistics
    # TODO: Show attempts used, win/loss for this round
   
    # Ask if player wants to play again
    # TODO: Get input and check if user wants to continue
    # TODO: Use break statement to exit main game loop if done

# Display final statistics
# TODO: Show total rounds, wins, and average guesses per round

print("\nThanks for playing! Goodbye!")
