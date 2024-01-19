# Introduction that how to use while and for loop!

greetings = 0

while greetings < 3:
    print("Welcome user, nice to meet you!\n")
    greetings += 1


def to_celsius(fahrenheit):
    return ((fahrenheit - 32) * 5) / 9


# The range() function can take up to three parameters:  range(start, stop, step)
for feh in range(0, 101, 10):
    print(f"Fahrenheit: {feh} | Celsius: {to_celsius(feh)}")
