'''
Filename: gradeTracker.py
Author: Berry Gavigan
Class: CIS
Date 10/1/25

Welcome Interface: Display a professional welcome message
Student Count Input: Ask how many students' grades to track (1-20 students)
Grade Collection Loop: Use a for loop to collect each student's information:
Student name (string input)
Test score (numeric input, 0-100 range)
Statistics Calculations: 
Calculate and display:
Total points earned by all students
Average class score
Highest score achieved
Lowest score achieved
Number of students who passed (≥70%)
Results Display: Format and display all statistics clearly
Input Validation: Handle basic input errors gracefully
'''


import math

print("\nWELCOME TO THE GRADE TRACKER\n")

numStudents = int(input("How many students are in your class? "))
print("You will enter grades for", numStudents, "students")
print("=" * 20)

print("\nEnter student data")
# list
names = []
numScores =[]
letScore = []
# get info
for count in range (1, numStudents + 1):
    print("Student #" , count)
    name = input("Enter Students name: ")
    score = int(input("Enter their score: "))
    names.append(name)
    numScores.append(score)
    
#get letter grades
for count in range (1, numStudents + 1):
    if numScores[count - 1] >= 90:
        letter = "A"
    elif numScores[count - 1] >= 80:
        letter = "B"
    elif numScores[count - 1] >= 70:
        letter = "C"
    elif numScores[count - 1] >= 60:
        letter = "D"
    else:
        letter = "F"
    
    letScore.append(letter)

classTotal = 0
for numbers in range(1, numStudents + 1):
    classTotal += numScores[numbers - 1]
    
classAvg = classTotal / numStudents
passing = []
passTimes = 0

for see in range(0, numStudents):
    if numScores[see]  >= 70:
        test = True
        passTimes += 1
    else: 
        test = False
    passing.append(test)

gradeA = 0
gradeB = 0
gradeC = 0
gradeD = 0
gradeF = 0
for loop in range(0, numStudents):
    if letScore[loop] == "A":
        gradeA += 1
    elif letScore[loop] == "B":
        gradeB += 1
    elif letScore[loop] == "C":
        gradeC += 1
    elif letScore[loop] == "D":
        gradeD += 1
    elif letScore[loop] == "F":
        gradeF += 1

passPecent = passTimes / numStudents * 100

print("Class Summary")
print('Total Students:', numStudents)
print('Total Points:', classTotal)
print('Class Avrage:', classAvg)
print('Highest Score:', max(numScores))
print('Lowest Score:', min(numScores))
print('Passing students: ' , passTimes , "/" , numStudents)
print('Passing rate:', passPecent , "\n")

print("Grade distbuation")
print("Grade A:", gradeA)
print("Grade B:", gradeB)
print("Grade C:", gradeC)
print("Grade D:", gradeD)
print("Grade F:", gradeF)

gradOkay = []

for avrage in range(0, numStudents):
    if numScores[avrage] >= 80:
        okay = "Above average"
    else:
        okay = "Below average"
    gradOkay.append(okay)
    
print("\nIndivdual Scores")

for last in range (0, numStudents):
    print(names[last] , ": " , numScores[last] , " (" , letScore[last] , ") - " , gradOkay[last])