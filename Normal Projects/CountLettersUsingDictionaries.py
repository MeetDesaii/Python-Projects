"""
Operations
len(dictionary) - Returns the number of items in a dictionary.

for key, in dictionary - Iterates over each key in a dictionary.

for key, value in dictionary.items() - Iterates over each key,value pair in a dictionary.

if key in dictionary - Checks whether a key is in a dictionary.

dictionary[key] - Accesses a value using the associated key from a dictionary.

dictionary[key] = value - Sets a value associated with a key.

del dictionary[key] - Removes a value using the associated key from a dictionary.
"""


def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result


print(count_letters("Meetkumar Vipulbhai Desai"))
