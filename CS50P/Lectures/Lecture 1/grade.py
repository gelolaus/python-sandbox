# Ask for score input
score = int(input("Score: "))

"""
Print letter if score = number
A = 90-100
B = 80-89
C = 70-79
D = 60-69
F = <60
"""

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
