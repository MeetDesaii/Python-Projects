print("Let's calculate individual's bill easily using this program!")

# Type Conversion
total_bill = float(input("Total bill: "))
tip_percentage = float(input("Percentage for a tip: "))
people = float(input("Number of people to split the bill: "))

tip_amount = (total_bill * tip_percentage) / 100
individual_bill = (total_bill + tip_amount) / people

# Round function to round up the number
print(f"Each person should pay: {round(individual_bill, 2)}")
