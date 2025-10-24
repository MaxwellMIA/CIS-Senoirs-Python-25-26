'''
Program: collegeApplicationTrackerPorject.py
Author: Berry Gavigan
Class: CIS
Date:10/24/25
'''

# Import statements
import math

# Constants (ALL_CAPS naming convention)
APPLICATION_FEE = 75.00
AVG_ACCEPTANCE_RATE = 55.0
MAX_IDEAL_DISTANCE = 500

# Welcome message
print("=" * 50)
print("COLLEGE APPLICATION TRACKER")
print("=" * 50)
print("Track your college applications and analyze your options!")
print("=" * 50)


# Variables for student info
student_name = input("What is your name? ")
print(f"Welcome, {student_name}! Let's track your college applications.")
print("Please enter information for 3 colleges you're considering:")
print("\n")

# Lists to store college data

college_one = []
college_two = []
college_three = []

# Data collection loop or individual inputs
print("--- college #1 --- ")
college_name1 = input("College name: ")
location1 = input("Location (City, State): ")
annual_tuition1 = int(input("Annual tuition ($): "))
distance1 = int(input("Distance from home (miles): "))
acceptance_rate1 = int(input("Acceptance rate (%): "))
print("\n")

college_one = [college_name1, location1, annual_tuition1, distance1, acceptance_rate1]

print("--- college #2 --- ")
college_name2 = input("College name: ")
location2 = input("Location (City, State): ")
annual_tuition2 = int(input("Annual tuition ($): "))
distance2 = int(input("Distance from home (miles): "))
acceptance_rate2 = int(input("Acceptance rate (%): "))
print("\n")

college_two = [college_name2, location2, annual_tuition2, distance2, acceptance_rate2]

print("--- college #3 --- ")
college_name3 = input("College name: ")
location3 = input("Location (City, State): ")
annual_tuition3 = int(input("Annual tuition ($): "))
distance3 = int(input("Distance from home (miles): "))
acceptance_rate3 = int(input("Acceptance rate (%): "))
print("\n")

college_three = [college_name3, location3, annual_tuition3, distance3, acceptance_rate3]

print("=" * 50)
print("YOUR COLLEGE APPLICATION SUMMARY")
print("=" * 50)

# college 1 print
four_tuition1 = annual_tuition1 * 4
print(f"College 1: {college_one[0]}")
print(f"Location {college_one[1]}")
print(f"Annual Tuition: ${college_one[2]:.2f}")
print(f"Distance from Home: {college_one[3]:.1f} miles")
print(f"Acceptance Rate: {college_one[4]:.1f}%")
print(f"4-Year Total Cost: ${four_tuition1}")
print("\n")

# college 2 print
four_tuition2 = annual_tuition2 * 4
print(f"College 2: {college_two[0]}")
print(f"Location {college_two[1]}")
print(f"Annual Tuition: ${college_two[2]:.2f}")
print(f"Distance from Home: {college_two[3]:.1f} miles")
print(f"Acceptance Rate: {college_two[4]:.1f}%")
print(f"4-Year Total Cost: ${four_tuition2}")
print("\n")

# college 3 print
four_tuition3 = annual_tuition3 * 4
print(f"College 1: {college_three[0]}")
print(f"Location {college_three[1]}")
print(f"Annual Tuition: ${college_three[2]:.2f}")
print(f"Distance from Home: {college_three[3]:.1f} miles")
print(f"Acceptance Rate: {college_three[4]:.1f}%")
print(f"4-Year Total Cost: ${four_tuition3}")
print("\n")

# Summary report with f-strings
average_annual = (annual_tuition1 + annual_tuition2 + annual_tuition3) / 3
total_four_tuition = (four_tuition1 + four_tuition2 + four_tuition3)
mile_average = (distance1 + distance2 + distance3) /3
total_distance = (distance1 + distance2 + distance3)

'''
print("=" * 50)
print("FINAL ANALYSIS")
print("=" * 50)
print(f"Total Application Fees: ${APPLICATION_FEE * 3}")
print(f"Average Annual Tuition: {average_annual}")
print(f"Total 4-Year Tuition (All Schools): ${total_four_tuition}")
print(f"Average Distance: {mile_average:.1f} miles")
print(f"Total distance (visting all, round trips) {total_distance} miles")
'''