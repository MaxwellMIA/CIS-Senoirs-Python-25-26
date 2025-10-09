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
invalid_start_chara = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
invalid_chara = [' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '`', '{', '|', '}', '~']

# Check each rule and provide appropriate feedback
# Empty name
if variable_name == "" or variable_name == " ":
    print ("Invalid, variable name cant be empty.")
# Python keyword
elif variable_name in python_keywords:
    print("Invalid, '" , variable_name , "' is a python keyword")
# Starting with numbers
elif variable_name.startswith(tuple(invalid_start_chara)):
    first_char = variable_name[0]
    print("Invaild, variables can not start with a number(s).")
# Invaild charaters
elif any(item in variable_name for item in invalid_chara):
    print("Invaild, you can only use underscores, numbers, and letters in your variable")
# vaild
else:
    print("Vaild!")