import random

print("Welcome to Rock, Paper, Scissors!")

while True:
    # Get user choice
    print("Enter your choice: Rock, Paper, or Scissors")
    user_choice = input().capitalize()
    while user_choice not in ['Rock', 'Paper', 'Scissors']:
        print("Invalid choice. Please enter Rock, Paper, or Scissors.")
        user_choice = input().capitalize()

    # Get computer choice
    computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])

    # Determine winner
    print(f"You chose {user_choice}.")
    print(f"The computer chose {computer_choice}.")

    if user_choice == computer_choice:
        print("\033[33mIt's a tie!\033[0m")
    elif (
        (user_choice == 'Rock' and computer_choice == 'Scissors') or
        (user_choice == 'Paper' and computer_choice == 'Rock') or
        (user_choice == 'Scissors' and computer_choice == 'Paper')
    ):
        print("\033[32mYou win!\033[0m")
    else:
        print("\033[31mComputer wins!\033[0m")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing! Goodbye.")
        break
