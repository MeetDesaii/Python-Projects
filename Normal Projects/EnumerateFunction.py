"""
Enumerate is a built-in function in python that allows you to keep track of the number of iterations (loops) in a loop. This enumerate object contains a count (from the start, which always defaults to 0) and a value obtained from iterating over the iterable object.

The enumerate() function takes a list as a parameter and returns a tuple for each element in the list. The first value of the tuple is the index and the second value is the element itself.
"""

names = ["Vishal Bhanderi", "Dhara Bhanderi", "Meet Desai", "Mital Bhanderi", "Preet Desai", "Zeel Bhanderi", "Abhi Bhanderi", "Fenil Bhanderi"]

print("We are siblings! This is one type of ladder based on age!")

for index, name in enumerate(names):
    print(f"{index+1} - {name}")
