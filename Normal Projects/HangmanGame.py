# Hangman Game

import random
import ListsData

indian_cricketers = ListsData.indian_cricket_players

chosen_cricketer = random.choice(indian_cricketers)
word_length = len(chosen_cricketer)

print(chosen_cricketer)

# Printing the "_" based on the name of the cricketer!
cricketer_name = str.split(chosen_cricketer, " ")
print("Guess the name of an Indian Cricketer: ")

display = []
for _ in range(word_length):
    display += "_"

end_of_game = False
lives = 6

# Looping till user will guess right cricketer name and user is alive!
while not end_of_game:

    user_guess = input("\nGuess a letter: ")

    for position in range(word_length):
        letter = chosen_cricketer[position]
        if letter == user_guess:
            display[position] = letter

    if user_guess not in chosen_cricketer:
        if lives == 0:
            print(f"\nBetter luck next time! You loose the game! The name of the cricketer is {chosen_cricketer}")
            end_of_game = True
            break
        else:
            lives -= 1
            print(f"Wrong guess! Lives left: {lives}")

    print(" ".join(display))

    if "_" not in display:
        end_of_game = True
        print(f"\nCongratulations! You won the game! The name of the cricketer is {chosen_cricketer}")
