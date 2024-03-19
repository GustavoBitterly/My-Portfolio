# Example

# Let's say we want to make the song more personalized.
# For example, say the person's name instead of just “dear friend”, then we can do this:


def happy_birthday(name):
    print("Happy birthday to you")
    print("Happy birthday to you")
    print("Happy birthday dear " + name)
    print("Happy birthday to you")


happy_birthday("Lillian")

# The output would be:

# Happy birthday to you
# Happy birthday to you
# Happy birthday dear Lillian
# Happy birthday to you

# Exercise


def distance_to_miles(distance):
    miles = distance / 1.609
    print(f"The distance in miles is: {miles}")


distance_to_miles(10000)
