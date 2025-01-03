import random

print("Welcome to Rock-Paper-Scissors!")
choices = ["rock", "paper", "scissors"]

def get_user_choice():
  while True:
    user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    if user_choice in ["rock", "paper", "scissors"]:
      return user_choice
    else:
      print("Invalid choice. Please enter (rock/paper/scissors)")

def get_computer_choice():
  return random.choice(choices)

def determine_winner(user_choice, computer_choice):
  if user_choice == computer_choice:
    return "It's a tie!"
  elif (user_choice == "rock" and computer_choice == "scissors") or \
       (user_choice == "scissors" and computer_choice == "paper") or \
       (user_choice == "paper" and computer_choice == "rock"):
    return "You win!"
  else:
    return "Computer wins!"

def play_game():
  user_score = 0
  computer_score = 0

  while True:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)

    if result == "You win!":
      user_score += 1
    elif result == "Computer wins!":
      computer_score += 1

    print(f"Your Score: {user_score}")
    print(f"Computer Score: {computer_score}")

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != 'y':
      break


play_game()