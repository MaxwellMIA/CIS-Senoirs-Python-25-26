'''
Program: carpetSales.py
Author: Berry gavigan
Class: CIS
Date:10/16/25

1: Read from input the carpet price per square foot (float), room width (int) and room length (int). Calculate the room area in square feet. Calculate the carpet price based on square feet with an additional 20% for waste. Output square feet and carpet cost. Submit for grading to confirm 1 test passes.
'''

# initialize constants
TAX_RATE = 0.07
WASTE_PCT = 1.2
LABOR_RATE = 0.75

totalSales = 0

# order 1
# input price per qr foot, room width and room length
price = float(input("Enter the price per sqaure foot: "))
width = int(input("Enter the width of the room: "))
length = int(input("Enter the length of the room: "))

# calculate room squarefeet
sq_feet = width * length

# calculate carpet cost including 20% waste
carpet = (sq_feet * WASTE_PCT) * price

# calculate labor (0.75 per sq ft)
labor = sq_feet * LABOR_RATE

# calculate sales tax
tax = (carpet + labor) * TAX_RATE

# calculate the total cost
cost = carpet + tax + labor

# output results
print("Order #1")
print(f"Square feet: {sq_feet} sq ft")
print(f"Cost of carpet: ${carpet:.2f}")
print(f"Labor: ${labor:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Cost: ${cost:.2f}")
totalSales += cost

# order 2

# input
print("\nFor order 2, add the price per sq ft, width, and length all seperated be a space. ex 2.45 16 10")
price, width, length = input().split()
price = float(price)
width = int(width)
length = int(length)

#calcs
sq_feet = width * length
carpet = (sq_feet * WASTE_PCT) * price
labor = sq_feet * LABOR_RATE
tax = (carpet + labor) * TAX_RATE
cost = carpet + tax + labor

#outpur results
print("Order #2")
print(f"Square feet: {sq_feet} sq ft")
print(f"Cost of carpet: ${carpet:.2f}")
print(f"Labor: ${labor:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Cost: ${cost:.2f}")
totalSales += cost

#order 3

# input
print("\nFor order 3, add the price per sq ft, width, and length all seperated be a space. ex 2.45 16 10")
price, width, length = input().split()
price = float(price)
width = int(width)
length = int(length)

#calcs
sq_feet = width * length
carpet = (sq_feet * WASTE_PCT) * price
labor = sq_feet * LABOR_RATE
tax = (carpet + labor) * TAX_RATE
cost = carpet + tax + labor

#outpur results
print("Order #3")
print(f"Square feet: {sq_feet} sq ft")
print(f"Cost of carpet: ${carpet:.2f}")
print(f"Labor: ${labor:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Cost: ${cost:.2f}")
totalSales += cost

# output tatal sales
print(f"your total Carpet sales is: ${totalSales:.2f}")