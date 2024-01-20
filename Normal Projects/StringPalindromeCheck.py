def is_palindrome(input_string):
    new_string = ""
    reverse_string = ""

    for letter in input_string:
        # Check if the letter is not a space
        if letter != " ":
            # Add the letter to the end of new_string and to the front of reverse_string
            new_string += letter.lower()
            reverse_string = letter.lower() + reverse_string

    # Compare new_string to reverse_string in a case-insensitive manner
    if new_string == reverse_string:
        # If True, the input_string contains a palindrome.
        return True

    # Otherwise, return False.
    return False


# Test the function
print(is_palindrome("Never Odd or Even"))  # Should be True
print(is_palindrome("abc"))  # Should be False
print(is_palindrome("kayak"))  # Should be True
