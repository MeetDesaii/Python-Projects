# This is a recursive method to reverse a string!

def reverse_string(string):
    if len(string) == 0:
        return string
    else:
        return reverse_string(string[1:]) + string[0]


print(reverse_string("This is a recursive method to reverse a string!"))


# This is a shortest method to reverse a string using string[start:stop:step]

name = "Meet Desai"

reversed_name = name[::-1]
print(reversed_name)
