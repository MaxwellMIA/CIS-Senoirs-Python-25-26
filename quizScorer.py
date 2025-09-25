'''
Filename: quizScorer
Author: Berry Gavigan
Class: CIS
Date: 9/25/25

Project Objectives
    Input/Output: Use print() and input() effectively
    For Loops: Implement loops with correct bounds
    Augmented Assignment: Use += and similar operators
    Off-by-One Prevention: Avoid common indexing errors
    Basic Calculations: Convert data types and perform math


Project Requirements
    ! Ask for the student's name 
    ! Ask how many quiz questions there are (5-10) 
    Use a for loop to ask for each answer (True/False or 1/0)
    Use a for loop to ask for each correct answer
    Calculate and display:
    Total correct answers (using +=)
    Quiz percentage
    Pass/Fail status (70% to pass)
'''

print("\n==QUIZ SCORER==")
print("This programm will score a true or false quiz \n")

name = input("What is your name? ")
questions = int(input("How many questions are there? (5-10) "))


print("\nScoreing quiz for" , name , "with" , questions , "qustions.")


lst = []
print("\nEnter students answers (1 for true, 0 for false)")
for question in range(1, questions +1):
    answer = int(input("Question " + str(question) + ": "))
    lst.append(answer)

correctLst = []
print("\nEnter correct answers (1 for true, 0 for false)")
for question in range(1, questions + 1):
    correctAnswer = int(input("Question " + str(question) + ": "))
    correctLst.append(correctAnswer)

if answer == correctAnswer:
    print("Question" , str(question) , "Correct")
else:
    print("Question" , str(question) , "Incorrect")