# Example

# Control flow is the order in which the program's code executes.
# if statement tests a condition for truth and executes the code if it's True.
# elif clause can be added between if and else.
# else executes the code if none of the above is True.
# Relational operators are used to compare two values: ==, !=, >, >=, <, <=.
# Logical operators are used to combine two or more conditions: and, or, not.

review = 3

if review >= 4.5:
    print("Extraordinary")
elif review >= 4:
    print("Excellent")
elif review >= 3:
    print("Good")
else:
    print("Eh")
