"""
The sys module in Python is a built-in module that provides access to some variables used or maintained by the Python interpreter and functions that interact strongly with the interpreter. It is used for manipulating the Python runtime environment.
"""

import sys
import HelloWorld

path_locations = sys.path

print("This program using these paths for interpreting the program!")
for location in path_locations:
    print(location)

# Importing local file using path.insert of sys module
sys.path.insert(1, r'E:\Programming\Data Science & Python\Python-Projects\Normal Projects')

print(HelloWorld)
