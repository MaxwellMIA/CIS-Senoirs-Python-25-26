'''
Program: quizOne.py
Author: Berry Gavigan
Class: CIS
Date: 10/2/25
'''

#1

for count in range(1, 5 +1):
    print(count)
print("\n")

#2

for counting in range(3, 8 +1):
    print(counting)
print("\n")

#3

for skip in range(0, 11, +2):
    print(skip)
print("\n")

#4

for counts in range(10, 0, -1):
    print(counts)
print("\n")

#5

numberOne = 5*1
numberTwo = 5*2
numberThree = 5*3
numberFour = 5*4
numberFive = 5*5

print("5 x 1 =" , numberOne)
print("5 x 2 =" , numberTwo)
print("5 x 3 =" , numberThree)
print("5 x 4 =" , numberFour)
print("5 x 5 =" , numberFive)

print("\n")
#6

age = int(input("Enter your age: "))

if age >= 18:
    print("You are a adult")
else:
    print("You are a minor")

print("\n")

#7

for odd in range(1, 11):
    if odd == 1 or 3 or 5 or 7 or 9:
        print("Odd")
    else:
        print("Even")

print("\n")

#8

for countdown in range(20, -1, -5):
    print("Countdown:", countdown)

print("\n")

#9

for small in range(1, 7):
    if small <= 3:
        print("Number", small, "is small")
    else:
        print("Number", small, "is large")

print("\n")

#10
number = int(input("Enter your number "))
for numbers in range(1, number, +2):
    if numbers <= 3:
        print(numbers, "low")
    else:
        print(numbers, "high")

print("\n")

#10 bonus
for countdowns in range(15, -1, -3):
    if countdowns >= 1:
        print(countdowns)
    else:
        print("Blastoff!")