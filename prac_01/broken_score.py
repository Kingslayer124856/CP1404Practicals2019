"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

score = float(input("Enter Score: "))
if score < 0:
    print("Invalid Score")
elif score > 100:
    print("Invalid Score")
elif score < 50:
    print("Bad")
elif score >= 90:
    print("Excellent")
else:
    print("Passable")