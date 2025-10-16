'''
File name: variables.py
Auther: Berry Gavigan
Date: 9/17/2025

Practing varible basics
'''

# This is a comment on a single line
# Variables can hold all data types
myInt = 42
myFLoat = 3.1415
myString = "Berry Gavigan"
myBool = True

print("My name is:" , myString)

myAge = myInt

print("My age is :" , myAge)
print("I dont not want to be:" , myInt + myAge) # 84

print(myFLoat)  #3.1415
myFLoat = 6.28210 #reassigned the variable
print(myFLoat) #6.28210

print("\n\n\n")
print("My Ticket App")
print("-------------")

ticketTotal = 43.50 + 43.50 + 43.50
processFee = 2.95
venueFee = 3.95 + 3.95 + 3.95
print("\nMy subtotal is")
print("--------------")
print("$" , ticketTotal + processFee +venueFee)