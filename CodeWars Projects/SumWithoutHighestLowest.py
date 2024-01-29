"""
Sum all the numbers of a given array ( cq. list ), except the highest and the lowest element ( by value, not by index! ).

The highest or lowest element respectively is a single element at each edge, even if there are more than one with the same value.

Mind the input validation.
If an empty value ( null, None, Nothing etc. ) is given instead of an array, or the given array is an empty list or a list with only 1 element, return 0.
"""


# My Solution
def sum_array(arr):
    try:
        arr_sum = 0
        for num in arr:
            arr_sum += num
        if max(arr) != min(arr):
            final_sum = arr_sum - max(arr) - min(arr)
            return final_sum
        else:
            final_sum = arr_sum - max(arr)
            return final_sum
    except:
        return 0


print(sum_array([]))

"""
3 BEST SOLUTIONS:

def sum_array(arr):
    if arr == None or len(arr) < 3:
        return 0
    return sum(arr) - max(arr) - min(arr)
    
    
def sum_array(arr):
    return sum(sorted(arr)[1:-1]) if arr and len(arr) > 1 else 0
    
    
def sum_array(arr):
    return 0 if arr == None else sum(sorted(arr)[1:-1])
"""
