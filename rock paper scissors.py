import random

print("Welcome to the Rock, Paper, Scissors game!")

# Define the possible choices
choices = ["rock", "paper", "scissors"]

# Computer's random choice
computer = random.choice(choices)

# User's input
user = input("Enter your choice (rock, paper, or scissors): ").lower()

# Validate user input
if user not in choices:
    print("Invalid choice! Please select 'rock', 'paper', or 'scissors'.")
else:
    print(f"Computer chose: {computer}")

    # Determine the winner
    if user == computer:
        print("It's a tie! 🤝")
    elif (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper") or \
         (user == "rock" and computer == "scissors"):
        print("You have won the game! 🎉")
    else:
        print("You have lost the game. Better luck next time! 😢")
