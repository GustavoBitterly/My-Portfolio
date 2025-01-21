# Example

# Now you might be wondering, is there a way to iterate over a list? 🔁
# Yep, there are multiple ways to iterate over a list in Python! In this exercise, we are going to show you different ways to do so.

# FOR-IN
# The first way is using a for-in loop. Here's an example:

snowfall = [0.3, 0.0, 0.0, 1.2, 3.9, 2.2, 0.8]

for i in snowfall:
    print(i)

# The i is a variable which represents an item inside the list, each time the loop iterates.
# This is saying for every item in the snowfall list, print out the item. The output will be:

0.3
0.0
0.0
1.2
3.9
2.2
0.8

# for-in with range() and len()
# We can also loop through a list using the index (position). To do so, we need the range() function and the len() function.

# As a reminder:
# range() function returns a sequence of numbers, from 0 to a number.
# len() function returns the length of the list.

snowfall = [0.3, 0.0, 0.0, 1.2, 3.9, 2.2, 0.8]

for i in range(len(snowfall)):
    print(snowfall[i])

# The i here is an index. This is saying for every index from 0 to the length of snowfall minus 1 (7 - 1 = 6),
# print out the item at that index.

# Exercise

# 💿 Theme: Indie Travel Songs

playlist = [
    "Porches - rangerover",
    "Mount Eerie - You Swan, Go On",
    "Carolyn Polachek - Look at Me Now",
    "Pinegrove - Darkness",
    "LVP UP - Spirit Was",
    "Mitski - First Love / Late Spring",
]

print(playlist)

for i in playlist:
    print(i)
