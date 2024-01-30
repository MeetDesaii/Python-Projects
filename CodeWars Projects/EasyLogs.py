"""
Add two logs with base X, with the value of A and B. Example log A + log B where the base is X.
"""

# My Solution

import math


def logs(x, a, b):
    return math.log(a, x) + math.log(b, x)


print(logs(10, 2, 3))
print(logs(5, 2, 3))
print(logs(1000, 2, 3))
print(logs(2, 1, 2))
print(logs(0.00001, 0.002, 0.01))


"""
3 BEST SOLUTIONS

from math import log
def logs(x, a, b):
    # Your code here
    return log(a*b, x)
    
    
from math import log

def logs(x, a, b):
    return log(a,x) + log(b,x)
    
    
import math

def logs(x, a, b):
    return math.log(a*b,x)
"""