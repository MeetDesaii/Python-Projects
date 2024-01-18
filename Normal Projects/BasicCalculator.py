print("Welcome to the basic calculator!")
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
exponential = num1 ** num2
floor_division = num1 // num2

print(f"\nAddition of {num1} and {num2} is {addition}")
print(f"Subtraction of {num1} and {num2} is {subtraction}")
print(f"Multiplication of {num1} and {num2} is {multiplication}")
print(f"Division of {num1} and {num2} is {division}")
print(f"Exponential of {num1} rest to {num2} is {exponential}")
print(f"Floor Division of {num1} and {num2} is {floor_division}")
