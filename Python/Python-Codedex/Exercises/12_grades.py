import random

# Example

grade = 100

# IF
if grade > 60:
    print("You passed!")

# ELSE
if grade > 60:
    print("You passed.")
else:
    print("You failed.")

# Exercise

grade = random.randint(0, 100)

if grade >= 55:
    print("You passed.")
    print(grade)
else:
    print("You failed.")
    print(grade)
