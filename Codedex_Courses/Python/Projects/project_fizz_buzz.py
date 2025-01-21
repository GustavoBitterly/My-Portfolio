# Fizz Buzz

# Technical interview question at countless companies.

# Create a fizz_buzz.py program that outputs numbers from 1 to 100.

# Here's the catch:

# For multiples of 3, print "Fizz" instead of the number.
# For multiples of 5, print "Buzz" instead of the number.
# Here's the tricky part: For multiples of 3 and 5, print "FizzBuzz".

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
