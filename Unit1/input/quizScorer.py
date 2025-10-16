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
    ! Use a for loop to ask for each answer (True/False or 1/0)
    ! Use a for loop to ask for each correct answer
    ! Calculate and display:
    ! Total correct answers (using +=)
    ! Quiz percentage
    ! Pass/Fail status (70% to pass)
'''

print("\n==QUIZ SCORER==")
print("This programm will score a true or false quiz \n")

name = input("What is your name? ")
questions = int(input("How many questions are there? (5-10) "))
lst = []
correctLst = []
totalCorrectAnswers = 0

print("\nScoreing quiz for" , name , "with" , questions , "qustions.")

print("\nEnter students answers (1 for true, 0 for false)")
for counter in range(1, questions +1):
    answer = list(input("Question " + str(counter) + ": "))
    lst.append(answer)


print("\nEnter correct answers (1 for true, 0 for false)")
for counter in range(1, questions + 1):
    correctAnswer = list(input("Question " + str(counter) + ": "))
    correctLst.append(correctAnswer)

print("\n")

for counter in range(1, questions + 1):
    if lst[counter - 1] == correctLst[counter - 1]:
        print("Question " + str(counter) + ": Correct")
        totalCorrectAnswers += 1
    elif lst[counter - 1] != correctLst[counter - 1]:
            print("Question " + str(counter) + ": Incorrect")

print("\nQuiz results for" , name)
print("Correct answers:" , totalCorrectAnswers)

totalCorrectAnswers = (totalCorrectAnswers / questions) * 100

print("Quiz percentage:" , totalCorrectAnswers)

if totalCorrectAnswers >= 70:
    print("Final statuts: Pass")
else:
     print("Final statuts: Fail")
