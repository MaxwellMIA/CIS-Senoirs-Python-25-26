# UNSTRUCTURED PROGRAM - Needs fixing!
print("Fitness Tracker")
print("===============")

exercise = input("What exercise did you do? ")
duration_str = input("How many minutes? ")
duration = int(duration_str)

calories_per_minute = 8  # Average
total_calories = duration * calories_per_minute

print("Exercise: " + exercise)
print("Duration: " + str(duration) + " minutes")
print("Calories burned: " + str(total_calories))

if total_calories >= 300:
    print("Great workout!")
else:
    print("Good start! Try for 30+ minutes next time.")

