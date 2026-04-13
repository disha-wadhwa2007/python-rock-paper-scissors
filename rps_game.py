import random

print("=== Rock Paper Scissors Game ===")

options = ["rock", "paper", "scissors"]

while True:
    user = input("Enter rock, paper, scissors or exit: ").lower()

    if user == "exit":
        print("Thanks for playing!")
        break

    if user not in options:
        print("Invalid choice. Please try again.")
        continue

    computer = random.choice(options)
    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You win!")
    else:
        print("Computer wins!")
