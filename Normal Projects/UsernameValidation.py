print("Welcome to the username validation program!")

"""
Here are some username validation rules: 
-> Usernames can only contain alphanumeric characters, such as lowercase and uppercase letters, numbers, and underscores.
-> Usernames must be at least three characters long.
-> Only numbers in the username should be at the end, with zero or more of them.
-> The dot (.), underscore (_), or hyphen (-) must not be the first or last character.
-> A valid username should start with an alphabet so, [A-Za-z].
-> A username can't only be underscores.
-> A username that consists of less than 6 or greater than 30 characters is an invalid username.
"""

username = input("Validate your username: ")
# len() is predefined function to measure length of the string!
if len(username) < 3:
    print("Minimum 3 characters are required for an username!")

