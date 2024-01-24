# Beginner - Modifying content of a list!
fruits = ['Pineapple', 'Banana', 'Apple', 'Melon', 'Kiwi']

# fruits.append("Grapes")
fruits.insert(0, "Orange")
fruits.remove('Banana')
fruits.pop(3)
fruits[2] = "Strawberry"
print(fruits)

"""
Python tuples are a type of data structure that is very similar to lists. The main difference between the two is that tuples are immutable, meaning they cannot be changed once they are created. This makes them ideal for storing data that should not be modified, such as database records.

# Convert a list to a tuple
my_list = [1, 2, 3, 4]
my_tuple = tuple(my_list)

print(my_tuple)  # Outputs: (1, 2, 3, 4)
"""


def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - (hours * 3600)) // 60
    remaining_seconds = (seconds - (hours * 3600) - (minutes * 60))
    return hours, minutes, remaining_seconds


# Results will be in Tuple
print(convert_seconds(5000))
print(type(convert_seconds(5000)))

# We can change it into three variables because we know the order won't change so!

con_hours, con_minutes, con_seconds = convert_seconds(5000)
print(f"{con_hours} hour(s), {con_minutes} minute(s), {con_seconds} second(s) left!")
