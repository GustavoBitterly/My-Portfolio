# Example

# and returns True if both conditions are True, and returns False otherwise.
# or returns True if at least one of the conditions is True, and False otherwise.
# not returns True if the condition is False, and vice versa.

hunger = 4
anger = 1

if hunger > 4 and anger > 1:
    print("Hangry")


coffee = 1
bubble_tea = 1

if coffee > 0 or bubble_tea > 0:
    print("😊")

tired = False

if not tired:
    print("Time to code!")

# Exercise

height = int(input("What is your height (cm)? = "))
credits = int(input("How many credits do you have? = "))

if height >= 137 and credits >= 10:
    print("Enjoy the ride!")
elif height < 137 and credits >= 10:
    print("You are not tall enough to ride.")
elif height >= 137 and credits < 10:
    print("You dont have enough credits.")
else:
    print("you have not met either requirement")
