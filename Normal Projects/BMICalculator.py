print("Welcome to the BMI (Body Mass Index) calculator!")

weight_in_kg = float(input("Enter the weight in kg: "))
height_in_cm = float(input("Enter the height in cm: "))

height_in_meters = height_in_cm / 100

bmi = weight_in_kg / (height_in_meters * height_in_meters)

print(f"Your BMI level is {bmi}")

# Conditional operators and control flow
if bmi < 18.5:
    print("Your BMI is Underweight!")
elif 18.5 <= bmi <= 24.99:
    print("Your BMI is Normal!")
elif 25 <= bmi <= 29.99:
    print("Your BMI is Overweight!")
elif 30 <= bmi <= 34.99:
    print("Your BMI is Obese!")
elif bmi >= 35:
    print("Your BMI is Extremely Obese!")
