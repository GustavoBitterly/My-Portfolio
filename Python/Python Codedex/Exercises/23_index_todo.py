# Example

vowels = ["a", "e", "i", "o", "u"]
# Index:   0    1    2    3    4

# The item at index 0 is 'a'.
# The item at index 1 is 'e'.
# The item at index 2 is 'i'.
# The item at index 3 is 'o'.
# The item at index 4 is 'u'.

print(vowels[0])  # Output: a
print(vowels[1])  # Output: e
print(vowels[2])  # Output: i
print(vowels[3])  # Output: o
print(vowels[4])  # Output: u

# Negative Index

# Another thing to note about index is that it can be positive or negative.
# If the index is negative, it starts from -1 (which is the last item of a list) and it goes backwards from there.

vowels = ["a", "e", "i", "o", "u"]
# Index:   0    1    2    3    4
# Index:  -5   -4   -3   -2   -1

# Slicing

# Slicing is where we can access certain parts of a sequence.
# Instead of accessing an item using a single index like name[index],
# we can get multiple items by specifying where to start and where to end the range like name[start : end].

vowels = ["a", "e", "i", "o", "u"]

print(vowels[0:3])
print(vowels[1:3])

# Output:
# ['a', 'e', 'i']
# ['e', 'i']

# IndexError

# This is what happens when the index is out of the range of a list.
# For example, when we try to do vowels[5], we will get something like:

# Traceback (most recent call last):
#     print(vowels[5])
# IndexError: list index out of range

# Exercise

todo_list = [
    "🏦 Get quarters.",
    "🧺 Do laundry.",
    "🌳 Take a walk.",
    "💈 Get a haircut.",
    "🍵 Make some tea.",
    "💻 Complete Lists chapter.",
    "💖 Call mom.",
    "📺 Watch My Hero Academia.",
]

print(todo_list[0])
print(todo_list[1])

print(todo_list[2:6])

print(todo_list[9])
