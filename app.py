#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
import random
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")


def play_game():
    """
    Play a game of rock-paper-scissors against the computer.

    The function prompts the user to enter their choice (rock, paper, or scissors),
    generates a random choice for the computer, and determines the winner based on
    the game rules. The result is printed to the console.

    Parameters:
    None

    Returns:
    None
    """
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    user_choice = input("Enter your choice (rock/paper/scissors): ").lower()

    print(f"Computer chooses: {computer_choice}")
    print(f"You choose: {user_choice}")

    if user_choice not in choices:
        print("Invalid choice. Please try again.")
        return

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
            (user_choice == "paper" and computer_choice == "rock") or \
            (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("Computer wins!")

play_game()
