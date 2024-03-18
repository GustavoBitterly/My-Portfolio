# Example

guess = 0

while guess != 6:
    guess = int(input("Guess the number: "))
# This will run over and over again until the user guesses the number 6.

# Exercise

guess = 0
tries = 0

while guess != 6 and tries < 5:
    guess = int(input("Guess the number:  "))
    tries += 1

print("You got it!")
