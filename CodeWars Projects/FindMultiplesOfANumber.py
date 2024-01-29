"""
In this simple exercise, you will build a program that takes a value, integer , and returns a list of its multiples up to another value, limit . If limit is a multiple of integer, it should be included as well. There will only ever be positive integers passed into the function, not consisting of 0. The limit will always be higher than the base.

For example, if the parameters passed are (2, 6), the function should return [2, 4, 6] as 2, 4, and 6 are the multiples of 2 up to 6.
"""


# My Solution
def find_multiples(integer, limit):
    # Your code here!
    my_list = []
    for num in range(integer, limit + 1):
        if num % integer == 0:
            my_list.append(num)
    return my_list


print(find_multiples(5, 25))
print(find_multiples(2,6))
print(find_multiples(1, 2))


"""
3 BEST SOLUTIONS

def find_multiples(integer, limit):
    return list(range(integer, limit+1, integer))
    
    
def find_multiples(integer, limit):
    return range(integer,limit+1,integer)
    
    
def find_multiples(integer, limit):
    arr = []
    count = integer
    while count <= limit:
        arr.append(count)
        count += integer
    return arr
"""