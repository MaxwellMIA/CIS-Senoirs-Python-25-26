'''
Program: whileLoop.py
Author: Berry gavigan
Class: CIS
Date:10/2/25

set the sum to 0.0
input a string
while the string is not the empty string
    convert the string to a float
    add the float to the sum
    input a string
print the sum

loop control variable - the first input statment that initializes a variable to a value that the loop condidtion can test

theSum = 0.0
data = input("Enter a number or just enter to quit: ")
while data != "":
    number = float(data)
    theSum += number
    data = input("Enter a number or just enter to quit: ")

print("The sum is" , theSum)
'''

print("\n\nA count controlled while loop")

#summation with a for loop
theSum = 0
for count in range (1, 100001):
    theSum += count
print(theSum, "\n\n")

#summation wth a while loop
theSum = 0
count = 1
while count <= 10000:
    theSum += count
    count += 1 #control variable needs to increment
print(theSum)


print("\n\ncounting down with loops")

#counting down with a forloop
for count in range (10, 0 ,-1):
    print(count, end= " ")

#counting down with a while loop
count = 10 
while count >= 1:
    print(count, end=" ")
    count -= 1

print("\n\nThe ehilr true statment with a break statment")

theSum = 0.0
while True:
    data = input("enter a number or just enter to quit: ")
    if data == "": #termination condition
        break # THE BREAK STATEMNET WILL END THE LOOP
    number = float(data)
    theSum += number
print("the sum is", theSum)

print("\n\ngradeing example")
while True:
    number = int(input("enter the numeric grade:"))
    if number >= 0 and number <= 100:
        break
    else:
        print("error, grade must be between 100 and 0")
print(number) #echo the vaild input

print("\n\nDifferant grading explame\n")
done = False
while not done: #while not == false
    number = int(input("enter a number grade: "))
    if number >= 0 and number <= 100:
        done = True
    else:
        print("error, grade must be between 100 and 0")
print(number)