# PDX Code Guild Fullstack Course
# Lab 07 Rock Paper Scissors Lizard Spock
# Samuel Purdy
# 4/8/2020

# Imports Random Module.
import random
import string

# Custom Module used to verify inputs when using input().
import verify

# Moveset: R = Rock, P = Paper, S = Scissors.
possible_moves = ["R", "P", "S", "L", "K"]

correct_inputs = ["Yes", "No"]

# Predifined wins and losses
wins = {
    "R": ["D", "L", "W", "W", "L"],
    "P": ["W", "D", "L", "L", "W"],
    "S": ["L", "W", "D", "W", "L"],
    "L": ["L", "W", "L", "D", "W"],
    "K": ["W", "L", "W", "L", "D"]
}

# Used to print the correct moves base on what character string is used.
moves_printed = {
    "R": "Rock",
    "P": "Paper",
    "S": "Scissors",
    "L": "Lizard",
    "K": "Spock"
}

# Defining variables.
user_input = "Yes"
user_move = None


def check_valid_move(str1):
    for move in possible_moves:
        if str1 == move:
            return True
    return False


# Keeps playing the game if the user wants to.
while user_input == "Yes":
    # Prints the choices.
    print("--------------------------------------")
    print("Rock Paper Scissors Lizard Spock Game!")
    print("R = Rock")
    print("P = Paper")
    print("S = Scissors")
    print("L = Lizard")
    print("K = Spock")

    # Checks to make sure the user uses the correct moves.
    # verify.valid_input(user_move, possible_moves, against_string = True, against_list = True)
    while not verify.valid_input(user_move, possible_moves, against_string = True, against_list = True):
        user_move = input("Choose one: ")
        user_move = user_move.upper()

    # Prints User move and computer move
    print(f"You chose {moves_printed[user_move]}")

    # Generates a random move for the computer to use.
    computer_move = random.randint(0, 4)

    # Prints the computers move
    print(f"The computer chose {moves_printed[possible_moves[computer_move]]}")

    # Checks to see what combination victory is made based on the computer
    # move and the user move, then prints the correct victory message.
    if wins[user_move][computer_move] == "D":
        print("It's a draw!")
    elif wins[user_move][computer_move] == "W":
        print("You win!")
    else:
        print("The computer wins!")

    # Resets inputs incase the player wishes to play again.
    user_move = None
    user_input = None

    # Asks the user if they want to play again.
    while not verify.valid_input(user_input, correct_inputs, against_string = True, against_list = True):
        user_input = input("Play again? (Yes/No) ")
