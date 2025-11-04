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

def calculate_average(students): 
    math1 = grade_book[0]["math_grade"]
    english1 = grade_book[0]["english_grade"]
    science1 = grade_book[0]["science_grade"]
    history1 = grade_book[0]["history_grade"]

    total1 = (math1 + english1 + science1 + history1)
    average1 = (total1 / 4)
    return average1

average1 = calculate_average(grade_book)
print(f"{grade_book[0]["name"]}s average grade: {average1:.2f}")

def print_class_report(students):
    """Prints a formatted report for all students"""
    # Your code here
    pass

def find_top_student(students):
    """Returns the student with the highest average"""
    # Your code here
    pass

def count_honor_students(students):
    """Counts students with average >= 90"""
    # Your code here
    pass

# Test your functions
print_class_report(grade_book)
top_student = find_top_student(grade_book)
honor_count = count_honor_students(grade_book)