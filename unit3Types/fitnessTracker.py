'''
Program: fitnessTracker.py
Author: Berry gavigan
Class: CIS
Date:11/18/25
'''

def welcome():
    print("Fitness Tracker")
    print("===============")

def get_duration():
    exercise = input("What exercise did you do? ")
    duration_str = input("How many minutes? ")
    duration = int(duration_str)
    return exercise, duration

def get_calories(duration):
    calories_per_minute = 8  # Average
    total_calories = duration * calories_per_minute
    return total_calories

def print_results(exercise, duration, total_calories):
    print("Exercise: " + exercise)
    print("Duration: " + str(duration) + " minutes")
    print("Calories burned: " + str(total_calories))

    if total_calories >= 300:
        print("Great workout!")
    else:
        print("Good start! Try for 30+ minutes next time.")

def main():
    welcome()
    exercise, duration = get_duration()
    total_calories = get_calories(duration)
    print_results(exercise, duration, total_calories)
    
if __name__ == "__main__":
    main()