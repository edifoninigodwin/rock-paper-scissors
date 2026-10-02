import random

choices = ["rock", "paper", "scissors"]
player_score = 0
computer_score = 0

print("Rock, Paper, Scissors! Type 'quit' to stop.")


while True:
    player = input("\nYour choice (rock/paper/scissors): ").lower().strip()

    if player == "quit":
        break

    
    if player not in choices:
        print("Invalid choice. Try again.")
        continue

    computer = random.choice(choices)
    print(f"Computer chose: {computer}")

    if player == computer:
        print("It's a tie!")
    elif (
        (player == "rock" and computer == "scissors")
        or (player == "paper" and computer == "rock")
        or (player == "scissors" and computer == "paper")
    ):
        print("You win!")
        player_score += 1
    else:
        print("Computer wins!")
        computer_score += 1

    print(f"Score -> You: {player_score} | Computer: {computer_score}")

print(f"\nFinal score -> You: {player_score} | Computer: {computer_score}")
print("Thanks for playing!")