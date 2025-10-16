'''
Program: mins2hours.py
Author: Berry gavigan
Class: CIS
Date:10/14/25
'''

minutes = int(input("Enter minutes: "))
hours = minutes // 60
mins_remaining = minutes % 60

print (mins_remaining, "minutes(s) is" , hours , "hour(s) and" , mins_remaining , "minutes(s)")