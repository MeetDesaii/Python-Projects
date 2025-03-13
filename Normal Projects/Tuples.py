# Tuples are immutable means It can't be modified by changing the value of the element

numbers = (1, 2, 3, 4, 5)
print(type(numbers))
print(numbers)

tuple_ex = ("Meet", 135520, 350.2, 24222.24, "1 BTC")
tuple_creation = "Meet", "Desai", 1, 3, 5, 5, 2, 0

print(type(tuple_creation), tuple_creation)

print(tuple_ex)

# Now let's try to change the value of 1 BTC

tuple_ex[-1] = "0.1 BTC"
# TypeError: 'tuple' object does not support item assignment and in real life, 1 BTC can't be replace by any other digit because 1 BTC will always be 1 BTC :) 

print(tuple_ex)