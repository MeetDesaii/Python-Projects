print("Welcome to Treasure Island!\nYour objective is to find the treasure!\nLET'S START!")

crossroad_move = input("You're at crossroad, where do you want to go? Type 'left' or 'right'. ").lower()

if crossroad_move == "left":
    lake_move = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. ").lower()
    if lake_move == "wait":
        door_choice = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose? ").lower()
        if door_choice == "red":
            print("You entered in a room of full of fire. Game over!")
        elif door_choice == "yellow":
            print("You found the treasure. You won!")
        elif door_choice == "blue":
            print("You entered in a room of beasts. Game over!")
        else:
            print("Something went wrong. Start again!")
    elif lake_move == "swim":
        print("You have attacked by an angry trout. Game over!")
    else:
        print("Something went wrong. Start again!")
elif crossroad_move == "right":
    print("You fall into a hole. Game Over!")
else:
    print("Something went wrong. Start again!")
    