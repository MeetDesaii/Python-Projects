"""
Take an array and remove every second element from the array. Always keep the first element and start removing with the next element.

Example:
["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> ["Keep", "Keep", "Keep", ...]

None of the arrays will be empty, so you don't have to worry about that!
"""


# My Solution
def remove_every_other(my_list):
    return my_list[::2]


print(remove_every_other(['Hello', 'Goodbye', 'Hello Again']))
print(remove_every_other([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(remove_every_other([['Goodbye'], {'Great': 'Job'}]))

"""
The expression my_list[::2] is a form of list slicing in Python, which is a powerful feature for accessing parts of lists (or any sequence type, like strings and tuples). Let's break down the slicing syntax my_list[start:end:step]:

start: This is the index where the slice starts. If omitted, as in your case (my_list[::2]), it defaults to the start of the list, which is index 0.

end: This is the index where the slice ends. The slice will include up to but not including this index. If omitted, the slice extends to the end of the list.

step: This is the step size or stride. It determines the increment between indices in the slice. If omitted, it defaults to 1, meaning every element is included. In your case, the step is 2, so the slice includes every second element.
"""


"""
3 BEST SOLUTIONS

def remove_every_other(my_list):
    r = []
    for i in range(len(my_list)):
        if i % 2 == 0:
            r.append(my_list[i])
    return r
    
    
def remove_every_other(my_list):
    return [v for c,v in enumerate(my_list) if not c%2]
    
    
def remove_every_other(my_list):
    del my_list[1::2]
    return my_list
"""
