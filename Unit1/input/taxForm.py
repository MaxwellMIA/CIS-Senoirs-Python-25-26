'''
Program: taxForm.py
Author: Berry Gavigan
Class: CIS
Date: 9/22/25

Compute a person's income tax
1. significant constants
    tax rate
    standard deduction
    dedcuction per dependent

2. the inputs are
    gross income
    number of dependents

3. computations:
    taxable income = gross income - the standard deduction - a deduction for each dependent
    income tax = is a fixed percentage of the taxable income

4. the outputs are:
    the income tax
'''
print("\n\nMy Tax Rate Calculator.")
print("=" * 40)

# inititalze the contants
TAX_RATE = 0.20
STANDARD_DEDUCTION = 10000.00
DEPENDENT_DEDUCTION = 3000.00

#request the inputs
grossIncome = float(input("Enter the gross income: "))
numDependents = int(input("Enter the number of dependents: "))

#compute the income tax
taxableIncome = grossIncome - STANDARD_DEDUCTION - \
                DEPENDENT_DEDUCTION * numDependents
incomeTax = taxableIncome * TAX_RATE

#display the income tax
print("The income tax is $" + str(incomeTax) + "\n\n")