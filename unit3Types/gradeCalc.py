'''
Program: gradeCalc.py
Author: Berry gavigan
Class: CIS
Date:11/6/25
'''

exam1_grade = float(input("Enter score on Exam 1 (out of 100): "))
exam2_grade = float(input("Enter score on Exam 2 (out of 100): "))
exam3_grade = float(input("Enter score on Exam 3 (out of 100): "))


examAvg = (exam1_grade + exam2_grade + exam3_grade) / 3

print("\n\nStudent Versions:")

# Calculates the overall grade for four equally weighted programming assignments, in which each assignment is graded out of 50 points. Hint: First calculate the percentage for each assignment (e.g., score / 50), then calculate the overall grade percentage (be sure to multiply the result by 100).
def calulate_grade(points):
    total_points = int(input("Please enter the total numebr of points for this assignment: "))
    grade = points / total_points
    return grade

program1 = int(input("Enter number of points on program 1: "))
program2 = int(input("Enter number of points on program 2: "))
program3 = int(input("Enter number of points on program 3: "))
program4 = int(input("Enter number of points on program 4: "))

# Calculate each grade percentage (score/50)
grade1 = calulate_grade(program1) # call the function and pass arguments
grade2 = calulate_grade(program2)
grade3 = calulate_grade(program3)
grade4 = calulate_grade(program4)

# Calculate the overall average
progAvg = (((grade1 + grade2 + grade3 + grade4) / 4) * 100)

# Calculates the overall grade for four equally weighted programming assignments, in which assignments 1 and 2 are graded out of 50 points and assignments 3 and 4 are graded out of 75 points.

assign1 = int(input("Total number of points for assignment 1: "))
assign2 = int(input("Total number of points for assignment 2: "))
assign3 = int(input("Total number of points for assignment 3: "))
assign4 = int(input("Total number of points for assignment 4: "))

assignGrade1 = calulate_grade(assign1)
assignGrade2 = calulate_grade(assign2)
assignGrade3 = calulate_grade(assign3)
assignGrade4 = calulate_grade(assign4)

assignAvg = (((assignGrade1 + assignGrade2 + assignGrade3 + assignGrade4) / 4) * 100)

# Calculates the overall grade for a course with three equally weighted exams (graded out of 100 points) that account for 60% of the overall grade and four equally weighted programming assignments (graded out of 50 points) that account for 40% of the overall grade. Hint: The overall grade can be calculated as 0.6 * averageExamScore + 0.4 * averageProgScore.

print("\n\n Section 3 of the assigment:\n")

overallAvg = (examAvg * 0.5) + (progAvg * 0.4) + (assignAvg * 0.1)
print(f"Student exam average: {examAvg:.2f}")
print(f"Student's programming average: {progAvg:.2f}")
print(f"Student assignment average: {assignAvg:.2f}")
print(f"The students overall average is: {overallAvg:.2f}")