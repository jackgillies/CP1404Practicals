"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


score = float(input("Enter score: "))
if score <= 0:
    print("Invalid score")
elif score >= 50 and score <= 89:
    print("Passable")
elif score >= 90 and score <= 100:
    print("Excellent")
else:
    print("Bad")