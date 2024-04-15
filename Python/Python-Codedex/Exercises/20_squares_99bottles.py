# Example

# String concatenation

for i in range(5):
    print("The square of " + str(i) + " is " + str(i * i))

# String interpolation

for i in range(5):
    print(f"The square of {i} is {i*i}")

# Exercise

for i in range(99, 0, -1):
    print(
        f"{i} bottles of beer on the wall {i} bottles of beer Take one down, pass it around"
    )
