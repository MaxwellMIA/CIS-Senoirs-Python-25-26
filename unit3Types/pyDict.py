'''
Program: pyDict.py
Author: Berry gavigan
Class: CIS
Date:11/4/25

Student Grade Book Manager

- Name: Emma Rodriguez
- Student ID: "S12345"
- Grade Level: 12
- Email: "emma.r@school.edu"
- Math grade: 95
- English grade: 88
- Science grade: 92
- Homework completed: True

Tasks:
1. Create a dictionary called student1 with all the information above
2. Print the entire dictionary.
3. Print Emma's email address.
4. Print Emma's math grade.
'''

# part 1: create the dictorany

student1 = {
    "name":"Emma Rodriguez",
    "student_id":"S12345",
    "grade_level":12,
    "email":"emma.r@school.edu",
    "math_grade":95,
    "english_grade":88,
    "science_grade":92,
    "homework_completed":True
}

# print the entire dictoanry
print("Complete student record:")
print(student1)

# print specific values
print("\nStudent Email:", student1["email"])
print("\nMath Grade:", student1["math_grade"])

# part 2

# modify emmas homework statuts
student1["homework_completed"] = False

# update english grade
student1["english_grade"] = 91

# add a history grade
student1["history_grade"] = 89

# add clubs
student1["clubs"] = ["debate team", "math club"]

# print the updated dictoanry
print("\nUpdated student record")
print(student1)

# part 3: Create a function to calcuate average grade
# python fuction structure: def (keyword) func_name(arguments)
def calculate_average(student): 
    # Get all grades
    math = student1["math_grade"]
    english = student1["english_grade"]
    science = student1["science_grade"]
    history = student1["history_grade"]

    # Calculate average
    total = (math + english + science + history)
    average = (total / 4)

    # Return average
    return average

# Test your function
# Function call:
average = calculate_average(student1)
print(f"\n{student1["name"]}'s average grade: {average:.2f}")

#part 4: Using dictionary methods
# 1. print all keys
print("\nAll values in the dictonary:")
print(student1.keys())

# 2. print all values
print("\nAll the values in the dictonary")
print(student1.values())

# 3. Print all key:value pairs
print("\n All the key-value pairs:")
print(student1.items())

# 4. Safely get phone number (doesnt exist)
6
# Function call:
average = calculate_average(student1)
print(f"\n{student1["name"]}'s average grade: {average:.2f}")

#part 4: Using dictionary methods
# 1. print all keys
print("\nAll values in the dictonary:")
print(student1.keys())

# 2. print all values
print("\nAll the values in the dictonary")
print(student1.values())

# 3. Print all key:value pairs
print("\n All the key-value pairs:")
for key, value in student1.items():
    print(f"{key}: {value}")

# 4. Safely get phone number (doesnt exist)
phone = student1.get("phone_number", "Not Available")
print("\nPhone number:", phone)

# 5. Create new student and use update
student2 = {
    "name":"Marks Chen",
    "student_id":"S12346",
}

# use .update() to add these fields all at once:
# grade_level 11, math_grade: 87, english, 90, seiecne_grade: 85
student2.update({"grade_level":11,
                 "math_grade":87,
                 "english_grade":90,
                 "science_grade":85
})

print("\nNew student record:")
print(student2)