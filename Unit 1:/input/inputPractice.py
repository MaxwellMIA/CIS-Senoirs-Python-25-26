'''
Filename: inputPractice
Author: Berry Gavigan
Class: CIS
Date: 9/19/25

Ask:
First name
Last name
Favorite color
First number
Second number
Favortie tv show
Favortie movie
Favorite song
Favorite food

- write out a paragraph outlining user data useing varibles. Using the first and second numbers, create 3 separate math equations, and print out the values
'''

firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
favoriteColor = input("Whats your favorite color? ")
firstNumber = input("First number: ")
secondNumber = input("Second number: ")
favoriteTvShow = input("Whats your favorite tv show? ")
favoriteMovie = input("Whats your favorite movie? ")
favoriteSong = input("Whats your favorite song? ")
favoriteFood = input("Whats your favorite food? ")

print("Your name is" , firstName , lastName , ". Your favorite color is" , favoriteColor , "while your favorite tv show and movie is" , favoriteTvShow , "and" , favoriteMovie , "respectively. Your favorite song is" , favoriteSong , ", while your favorite food is" , favoriteFood , ".")

adding = int(firstNumber) + int(secondNumber)
subtracting = int(firstNumber) - int(secondNumber)
mulitping = int(firstNumber) * int(secondNumber)

print(firstNumber , "+" , secondNumber , "=" , adding )
print(firstNumber , "-" , secondNumber , "=" , subtracting )
print(firstNumber , "*" , secondNumber , "=" , mulitping )


