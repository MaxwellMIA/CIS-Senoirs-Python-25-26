'''
Filename: personalFitnessTracker
Author: Berry Gavigan
Class: CIS
Date: 9/23/25

1.
    Collects the user's personal fitness information using
    Stores all data in appropriately named variables
    Performs calculations on the collected data
    Displays a formatted fitness report using

2. 
    User's name
    Age (integer)
    Weight in pounds (float)
    Height in inches (integer)
    Weekly exercise hours (float)
    Fitness goal (string)

3.
    Calculate BMI (Body Mass Index)
    Determine daily exercise minutes
    Calculate calories burned per week (estimate)

BMI formal
    BMI = (weight_in_pounds / (height_in_inches²)) × 703


Calories burned
    Weekly calories = exercise_hours × 300 (simplified estimate)
'''

print("\n\n=PERSONAL FITNESS TRACKER=")
print("\nWelcome to you personalized fitness tracker!\n")

# inputs

name = input("What is your name? ")
age = int(input("What is your age? "))
weightInPounds = float(input("What is your weight in pounds? "))
heightInInches = int(input("What is you height in inches? "))
hoursOfExercise = float(input("How many hours do you exercise a week? "))
fitnessGoal = str(input("What is your main fitness goal? "))

# calculations

bmi = (weightInPounds / (heightInInches * heightInInches)) * 703
dailyExercise = (hoursOfExercise * 60) / 7
weeklyCalories = hoursOfExercise * 300

# printing
print("\n")
print("=" * 30)
print("FITNESS REPORT FOR" , name)
print("=" * 30)
print("\n")

print("Personal information:")
print("Name :" , name)
print("Age :" , age , "years old")
print("Weight :" , weightInPounds , "lbs")
print("Height :", heightInInches , "\n")

print("Fitness metrics")
print("BMI" , bmi)
print("weekly exercise" , hoursOfExercise , "hours")
print("Daily exercise" , dailyExercise , "minutes")
print("Estimated weekly caloires burned" , weeklyCalories , "calories" , "\n")

print("Fitness goal:" , fitnessGoal , "\n")

print("Keep up the geart work with your fitness journey!")
print("=" * 40)