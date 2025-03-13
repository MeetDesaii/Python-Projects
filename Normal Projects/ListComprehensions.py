# This is how List comprehensions works, For loop directly implemented in list variable!
# List Comprehensions let us create new lists based on sequences or ranges.
# This is how logic adding in for loop in one line
# List Comprehension: [<expression> for x in <sequence> if <condition>]
# Dictionary Comprehension: {key:value for key, value in <sequence> if <condition>}
multiples = [x * 7 for x in range(1, 11)]
print(multiples)

"""
OR

multiples = []
for x in range(1,11):
  multiples.append(x*7)

print(multiples)
"""

z = [x for x in range(0, 101) if x % 3 == 0]
print(z)

# Example with input -- Square of Entered number to hundred
square_in = int(input("Enter the number: "))
input_to_hun = [num ** 2 for num in range(square_in, 101)]

print(input_to_hun)