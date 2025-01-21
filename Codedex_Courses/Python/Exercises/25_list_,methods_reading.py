# Example

# Here are all 11 list methods to save in your notes:

# List Method	Description
# .append()	Add an item to the end of the list
# .clear()	Remove all items from the list
# .copy()	Return a shallow copy of the list
# .count()	Return the number of times the value appears in the list
# .extend()	Appends another list to the current list by extending it
# .index()	Returns the index of a value inside the list
# .insert()	Insert an item at a specified position in the list
# .pop()	Remove an item from a specified position in the list
# .remove()	Remove an item from the list based on the value of the item
# .reverse()	Reverses the list in place
# .sort()	Sorts the list in place

dna = ["AUG", "AUC", "UCG"]

dna.append("UAA")  # ['AUG', 'AUC', 'UCG', 'UAA']
dna.insert(2, "GAU")  # ['AUG', 'AUC', 'GAU', 'UCG', 'UAA']
dna.remove("AUC")  # ['AUG', 'GAU', 'UCG', 'UAA']
dna.pop(0)  # ['GAU', 'UCG', 'UAA']

# Exercise

book_list = [
    "Zero to One",
    "The Lean Startup",
    "The Mom Test",
    "Make It Stick",
    "Life in Code",
]

print(book_list)

book_list.append("Zero to Sold")
print(book_list)

book_list.insert(6, "Zero to Insert")
print(book_list)

book_list.remove("Zero to One")
print(book_list)

book_list.pop(0)
print(book_list)
