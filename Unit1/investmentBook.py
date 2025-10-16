'''
Program: investmentBook.py
Author: Berry Gavgian
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
print("\n\n")
print("=" * 50)
print("my investment tracker")
print("=" * 50)

# accpet the imputs

startBalance = float(input("Enter the investment amount: "))
years = int(input("Enter the number of years: "))
rate = int(input("enter the rqate as a percentage: "))

# convert the rate to a decimal number

rate = rate / 100

# initialize the accumlaotr for the interest

totalIntrest = 0.0

# display the header for the table

print("%4s%18s%10s%16s" % ("Year", "starting balance", "interest", "ending balance"))

# compute and display the resuts for each year

for year in range(1, years + 1):
    intrest = startBalance * rate
    endBalance = startBalance + intrest
    print("%4d%18.2f%10.2f%16.2f" % (year, startBalance, intrest, endBalance))
    startBalance = endBalance
    totalIntrest += intrest

# display the totals for the period

print("ending balance: $%0.2f" % endBalance)
print("total intrest earned: $%0.2f" % totalIntrest)