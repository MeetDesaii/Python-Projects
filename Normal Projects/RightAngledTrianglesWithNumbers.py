"""
Problem Description:

You are given an integer n. Your task is to return a right-angled triangle pattern where each row contains repeated digits. The first row contains the number 1 repeated once, the second row contains the number 2 repeated twice, and so on until the nth row contains the number n repeated n times.

Input:
A single integer n, where 1 <= n <= 100.

Output:
A list of strings where each string represents a row in the triangle. The ith row contains the digit i repeated i times.

Example:

Input: 5
Output: ['1', '22', '333', '4444', '55555']
 
Input: 3
Output: ['1', '22', '333']
"""

def right_angled_triangle(n):
    for i in range(1, n+1):
        print(str(i) * i)
        
        
right_angled_triangle(5)
