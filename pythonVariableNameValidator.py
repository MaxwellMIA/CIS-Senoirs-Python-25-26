'''
Program: pythonVariableNameValidator.py
Author: Berry gavigan
Class: CIS
Date:10/7/25
'''

# Python Variable Name Validator
# Student Name: Berry Gavigan
# Date: 10/7/25

# List of Python keywords
python_keywords = [
    'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
    'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
    'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
    'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try',
    'while', 'with', 'yield'
]

# Display welcome message
print("=== PYTHON VARIABLE NAME VALIDATOR ===")
print("This program checks if your variable name is valid in Python.")
print()

# Get user input
variable_name = input("Enter a variable name to validate: ")

# Your validation code goes here

# Check each rule and provide appropriate feedback
#empty string
if variable_name == " ":
    print ("Invalid, variable name cant be empty.")
elif variable_name in python_keywords:
    print("Invalid, '" , variable_name , "' is a python keyword")
else:
    print("HI!")

