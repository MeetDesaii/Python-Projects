import string
import random

password_list = []
password = ""

letters = list(string.ascii_lowercase) + list(string.ascii_uppercase)
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', '{', ']', '}', '|', ';', ':', "'", '"', ',', '<', '.', '>', '/', '?']

print("Welcome to the Password Generator!\n")

for let in range(1, 9):
    password_list += random.choice(letters)

for num in range(1, 9):
    password_list += random.choice(numbers)

for sym in range(1, 9):
    password_list += random.choice(symbols)

"""
In Python, shuffle is used to randomly rearrange the elements of a list in place. This means that the original list is modified, and the elements are reordered in a random order. The shuffle function is part of the random module, so you need to import this module before you can use it.
"""
random.shuffle(password_list)

for char in password_list:
    password += char

print(f"Generated Password: {password}")
