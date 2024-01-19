"""
Bracket notation, [ ], is used to specify the start of the index, ending index, or both. If you do not include the starting index, then the slice contains everything from the beginning of the string to the ending index.
"""

intro = "Hello World, Myself Meet Desai"

"""
When you specify an ending index, Python slices everything up to, but not including the ending index. Notice in the second example the ending index is 11, but the characters sliced are 6–10.
"""

print(intro[0])
print(intro[6:11])
print(intro[20:])
print(intro[:5])

"""
You can also use the join() function, which is very useful when you want to concatenate elements from a list of strings with a specific delimiter.
"""
greetings = ["Hello", "World"]
print(" ".join(greetings))
