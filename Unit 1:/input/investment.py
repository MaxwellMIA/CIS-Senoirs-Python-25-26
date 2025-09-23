'''
Program: investment.py
Author: Berry Gavigan
Class: CIS
Date: 9/22/25

compute an investment report

1. inputs
    starting investment amount
    number of years
    interest rate (int)

2. the report is displated in tabulr form with a header

3. computations and outputs:
    for each year of the investment
        compute the interst and add it to the investment
        print a formatted row of results for that year
4. the ending investment and intreest you have paid in total are also displayed
'''
print("\n\nMy investment calc")
print("=" * 25)
# accept the inputs

investmentAmount = float(input("Starting investment amount: "))
numOfYears = float(input("Number of years: "))
interestRate = int(input("interest rate: "))

# convert the investment rate to a decial number

interestRate = interestRate / 100

#loop

loop = 0
investmentTotal = investmentAmount
while loop < numOfYears:
    loop = loop + 1
    investmentTotal = (investmentTotal * interestRate) + investmentTotal
    print("In year" , loop , "you will have $" , investmentTotal)