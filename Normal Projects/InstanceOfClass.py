"""
When writing a Python class, you define a method called __init__ to be your constructor. The special name tells Python to use that method as the constructor. Just like any other method, the constructor can take arguments. When making an argument to the class, the first constructor must always be self.

As you might expect, Python classes have many other special methods. Most of these have default implementations provided by the Python standard library, but you are free to override the behavior of any of them. Like the __init__ constructor, special methods begin and end with a double underscore, and this is called dunder method. The word “dunder” combines the “d” in double and the “under” in underscore.
"""


class Apple:
    # Dunder (double underscore) method
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

    # Dunder (double underscore) method
    def __str__(self):
        return "An apple which is {} and {}.".format(self.color, self.flavor)


apple_type = Apple("Red", "Sweet")
print(f"Color: {apple_type.color}\nFlavor: {apple_type.flavor}")
print(apple_type)
