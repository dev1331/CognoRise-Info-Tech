while True:

    import random

    # Define the possible moves
    moves = ["rock", "paper", "scissors"]

    # Take user input
    user_action = input("Enter a choice (rock, paper, scissors): ")

    # Make the computer choose a random action
    computer_action = random.choice(moves)

    # Determine the winner
    if user_action == computer_action:
        print(f"It's a tie! Both chose {user_action}.")
    elif (user_action == "rock" and computer_action == "scissors") or (user_action == "paper" and computer_action == "rock") or (user_action == "scissors" and computer_action == "paper"):
        print(f"You win! {user_action} beats {computer_action}.")
    else:
        print(f"You lose! {computer_action} beats {user_action}.")
