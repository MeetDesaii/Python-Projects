"""
This Match-Case is the Switch Case of Python which was introduced in Python 3.10.

It provides a concise and expressive way to perform pattern matching on data structures, such as tuples, lists, and classes. It allows you to match the value of an expression against a series of patterns and execute the corresponding block of code for the matched pattern.


Python pass Statement
The pass statement is used as a placeholder for future code. When the pass statement is executed, nothing happens, but you avoid getting an error when empty code is not allowed. Empty code is not allowed in loops, function definitions, class definitions, or in if statements.
"""

try:
    http_status = int(input("Http response: "))

    match http_status:
        case 200 | 201:
            print("Status: Success")
        case 400:
            print("Status: Not Found")
        case 500 | 501:
            print("Status: Server Error")
        case _:
            pass
            print("Unknown")
except:
    print("Invalid input!")
