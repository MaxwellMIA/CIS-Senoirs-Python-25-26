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

print("\n==GRADE TRACKER SYSTEM==")
print("Welcome to the grade tracker!")
print("This program will help you analyze student grades.\n")

students = int(input("How many students are in your class? (1-20): "))

print("You will enter grades for", students , "students.")
print("\nPlease enter student infomation:")
print("-" * 20)

nameLst = []
scoreLst = []

#List for student names and test scores

for student in range (1, students + 1):
    print("Student #" , student , ":")
    name = str(input("  Enter student name: "))
    score = int(input("  Enter test score (0-100): "))
    nameLst.append(name)
    scoreLst.append(score)

print("\n==GRADE TRACKER SYSTEM==\n")
print("Class summary")
print("  Total Students:" , students)
# getting the total points
pointTotal = sum(scoreLst)
print("  Total Points:" , pointTotal)




