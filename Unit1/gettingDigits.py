'''
Program: GettingDigits.py
Author: Berry gavigan
Class: CIS
Date:10/14/25

given a number, % and // can be used to get each digit, for the three-digit number user_val like 927
'''

myDigit = int(input("Enter a 3 digit number: "))

ones_digit = myDigit % 10
tmp_val = myDigit // 10

tens_digit = tmp_val % 10
tmp_val = tmp_val // 10

hundreds_digit = tmp_val % 10

print("The ones place is" , ones_digit , ", the tens place is" , tens_digit , ", and the hundreds place is" , hundreds_digit)