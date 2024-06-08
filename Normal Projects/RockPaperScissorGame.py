import random

choices = ["Rock", "Paper", "Scissor"]
computer_choice = random.randint(0, 2)

print("Welcome to Rock, Paper and Scissor Game:\n")

try:
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor!\n"))

    if user_choice > 2 or user_choice < 0:
        print("Input error! Please enter a valid input!")
    elif user_choice == 0 and computer_choice == 2:
        print(f"Congratulations! you won!\nYou chose {choices[user_choice]} and computer chose {choices[computer_choice]}!")
    elif user_choice == 2 and computer_choice == 0:
        print(f"Oops! you lose!\nYou chose {choices[user_choice]} and computer chose {choices[computer_choice]}!")
    elif computer_choice > user_choice:
        print(f"Oops! you lose!\nYou chose {choices[user_choice]} and computer chose {choices[computer_choice]}!")
    elif user_choice > computer_choice:
        print(f"Congratulations! you won!\nYou chose {choices[user_choice]} and computer chose {choices[computer_choice]}!")
    elif computer_choice == user_choice:
        print(f"Game draw!\nYou chose {choices[user_choice]} and computer chose {choices[computer_choice]}!")

except ValueError:
    print("Input error! Please enter a valid input!")
