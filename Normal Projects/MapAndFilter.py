"""
The map function applies a given function to every item of an iterable and returns a map object (which is an iterator). This map object can then be converted into a list or other iterable types.
"""


def square(number):
    return number ** 2


numbers = [1, 2, 3, 4, 5]
squared_numbers = map(square, numbers)

print(list(squared_numbers))

"""
The filter function applies a given function to each item of an iterable and returns a filter object with the items for which the function returns True. Like map, the filter object can be converted into a list or other iterable types.
"""


def is_even(number):
    return number % 2 == 0


numbers = [1, 2, 3, 4, 5]
even_numbers = filter(is_even, numbers)

print(list(even_numbers))


"""
Key Differences-

Purpose: map transforms each item in an iterable, applying a function to all items. filter, on the other hand, selects items based on a condition, filtering out those that don't meet the criterion.
Return Value: Both return an iterator (map or filter object), but map returns the result of applying the function to each item, while filter returns each item that makes the function return True.
"""
