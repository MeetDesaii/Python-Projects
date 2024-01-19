"""
While self is a convention, it's not a keyword in Python. You could technically name it anything, but it's strongly recommended to stick to self for readability and consistency with the Python community.
"""


class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def __add__(self, other):
        return self.area() + other.area()


first_triangle = Triangle(35, 50)
second_triangle = Triangle(12, 56)

print(f"Area of the first triangle is: {first_triangle.area()}")
print(f"Area of the second triangle is: {second_triangle.area()}")
print(f"Area of both triangles is: {first_triangle+second_triangle}")
