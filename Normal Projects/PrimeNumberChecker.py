# Prime Number Checker

print("- Prime Number Checker -")
number = int(input("Enter the number: "))

prime_status = False

for i in range(2, number):
    if number % i == 0:
        prime_status = True

if prime_status:
    print(f"{number} is not a Prime Number!")
else:
    print(f"{number} is a Prime Number!")
