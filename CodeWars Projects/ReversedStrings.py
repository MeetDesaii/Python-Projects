"""
Complete the solution so that it reverses the string passed into it.

'world'  =>  'dlrow'
'word'   =>  'drow'
"""


# My Solution

def reverse_string(string):
    pos = -1
    reversed_str = ""
    while pos >= -len(string):
        reversed_str += string[pos]
        pos = pos - 1
    return reversed_str


print(reverse_string("Meet"))


"""
3 BEST SOLUTIONS

def solution(str):
  return str[::-1]
  
  
def solution(string):
    s = list(string)
    j = len(s)-1
    for i in range(len(s)):
        if (i<j):
            s[i], s[j] = s[j], s[i]
            j = j-1
        else:
            continue
    s1 = ''.join(s)
    return s1
    
    
def solution(string):
    return ''.join(i for i in reversed(string))
"""