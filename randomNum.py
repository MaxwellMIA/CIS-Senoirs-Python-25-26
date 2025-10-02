'''
Program: whileLoop.py
Author: Berry Gavigan
Class: CIS
Date:10/2/25

python has a module called random. it needs to imported to use it
'''

import random
for roll in range(10):
    print (random.randint(1, 6), end=" ")

#second example
smaller = int(input("enter the smaller number: "))
larger = int(input("Enter the larger number: "))
myNumber = random.randint(smaller, larger)
count = 0

while True:
    count += 1
    userNumber = int(input("Enter your guess: "))
    if userNumber < myNumber:
        print("too small")
    elif userNumber > myNumber:
        print("too large")
    else:
        print("congrats! you got it in" , count)
        break