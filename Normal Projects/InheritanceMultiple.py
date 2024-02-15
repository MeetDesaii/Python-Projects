class A:
    a = 1


class B(A):
    a = 2


class C(B):
    pass


c = C()
print(c.a)

"""
There are two built-in functions that can come in handy when trying to find the relationship between different classes and objects: issubclass() and isinstance().
"""

"""
This can be read as: “Is B subclass of A?“ You can see the result is "True" in the second case where child B is the subclass.
"""
print(issubclass(B, A))

"""
Another built-in function similar to this one is isinstance() that determines if some object is an instance of some class. So if I write:
"""
print(isinstance(c, C))
