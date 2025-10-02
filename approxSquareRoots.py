'''
Program: approxSquareRoots.py
Author: Berry gavigan
Class: CIS
Date:10/2/25

request: write a progam the cpmputes square roots. you will use pythons math module. pythons math module has a functions call sqrt - math.sqrt - will only b used at the end to comare your calculation with pythons calculation

compute the square root of a number: 
1. The input is a number
2. the outputs are program estimate of the sqaure root using newtons method of succssive approximations, and pythons own estimate using math.sqrt()
'''

import math

#receive the input number from the user
x = float(input("enter a postive number: "))

#initialize the tolerance and estimate
tolerance = 0.000001
estimate = 1.0

#perform with successive approimations
while True:
    estimate = (estimate + x / estimate) / 2
    difference = abs(x - estimate ** 2)
    if difference <= tolerance:
        break

#output the result
print("the programs estimate:" , estimate)
print("pythons estimate.    :" , math.sqrt(x))