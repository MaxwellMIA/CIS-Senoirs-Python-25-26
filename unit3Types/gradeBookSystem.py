'''
Program: gradeBookSystem.py
Author: Berry gavigan
Class: CIS
Date:11/4/25
'''

# Challenge: Complete Grade Book System

# Create a list of student dictionaries
grade_book = [
    {
        "name":"Emma Rodriguez",
        "id":"S12345",
        "math_grade":95,
        "english_grade":91,
        "science_grade":92,
        "history_grade":89
    },

    {
        "name":"Marcus Chen",
        "id":"S12346",
        "math_grade":87,
        "english_grade":90,
        "science_grade":85,
        "history_grade":88
    },

    {
        "name":"Sophia Patel",
        "id":"S12347",
        "math_grade":98,
        "english_grade":96,
        "science_grade":94,
        "history_grade":97
    }
]

def get_average(student): 
    grades = [
        student["math_grade"],
        student["english_grade"],
        student["science_grade"],
        student["history_grade"],
    ]
    return sum(grades) / len(grades)

def print_class_report(students):
    """Prints a formatted report for all students"""
    print("class report")
    for student in students:
        avg = get_average(student)
        print(f"Name: {student["name"]}")
        print(f"Id: {student["id"]}")
        print(f"Math: {student["math_grade"]}")
        print(f"English: {student["english_grade"]}")
        print(f"Science: {student["science_grade"]}")
        print(f"History: {student["history_grade"]}")
        print(f"Average: {avg:.2f}")
        print()
    print()

def find_top_student(students):
    """Returns the student with the highest average"""
    return max(students, key=get_average)

def count_honor_students(students):
    """Counts students with average >= 90"""
    return sum(1 for s in students if get_average(s) >= 90)

# Test your functions
print_class_report(grade_book)
top_student = find_top_student(grade_book)
print(f"Top students: {top_student['name']} (ID: {top_student['id']}) with an average of {get_average(top_student):.2f}")
honor_count = count_honor_students(grade_book)
print(f"Number of honor students (avg >= 90): {honor_count}")