import random

# Example

# To define a function, we need a function definition. A function definition begins with the def keyword,
# followed by the function name, a set of parentheses, and a colon in that order.


# Here’s what a function definition looks like:
def say_hello():
    print("Howdy! 🤠")
    print("How are you?")


# To call a function, we use the function name followed by parentheses somewhere in the code:
def say_hello():
    print("Howdy! 🤠")
    print("How are you?")


say_hello()

# So the output would be:

# Howdy! 🤠
# How are you?

# Exercise

fortune_cookie = [
    "Dont pursue happiness – create it.",
    "All things are difficult before they are easy.",
    "The early bird gets the worm, but the second mouse gets the cheese.",
    "Someone in your life needs a letter from you.",
    "Dont just think. Act!",
    "Your heart will skip a beat.",
    "The fortune you search for is in another cookie.",
    "Help! Im being held prisoner in a Chinese bakery!",
]


def fortune():
    random_fortune = random.choice(fortune_cookie)
    print(random_fortune)


fortune()
