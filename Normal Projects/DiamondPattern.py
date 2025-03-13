"""
Diamond Pattern
Problem Description:

You are given an integer n. Your task is to return a diamond pattern of '*' with n rows for the upper part (the widest row will have 2n - 1 stars), and the lower part is the mirrored version of the upper part. Each row should be centered with appropriate spaces.

Input:
A single integer n, where 1 <= n <= 100.

Output:
A list of strings where each string represents a row in the diamond pattern.

Example:

Input: 3
Output: ['  *  ', ' *** ', '*****', ' *** ', '  *  ']
 
Input: 5
Output: ['    *    ', '   ***   ', '  *****  ', ' ******* ', '*********', ' ******* ', '  *****  ', '   ***   ', '    *    ']
"""

def diamond_pattern(n):
    for i in range(1, n+1):
        stars = "*" * (2*i-1)
        spaces = " " * (n-i)
        print(spaces + stars + spaces)
    for i in range(n-1, 0, -1):
        stars = "*" * (2*i-1)
        spaces = " " * (n-i)
        print(spaces + stars + spaces)

diamond_pattern(5)  

