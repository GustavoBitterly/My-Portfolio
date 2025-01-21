# Example

# Relational Operators
# == equal to
# '!=' not equal to
# > greater than
# < less than
# >= greater than or equal to
# <= less than or equal to

# ELIF
grade = 89

if grade > 90:
    print("A")
elif grade > 80:
    print("B")
elif grade > 70:
    print("C")
elif grade > 60:
    print("D")
else:
    print("F")

# Exercise
ph = int(input("Enter a pH value (0-14): "))

if ph > 7:
    print("Basic")
elif ph < 7:
    print("Acidic")
else:
    print("Neutral")
