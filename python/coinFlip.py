import random

def coin_flip_game():
    print("Welcome to the Coin Flip Game!")

    score = 0

    while True:
        print("\nChoose your guess:")
        print("1. Heads")
        print("2. Tails")
        print("3. Quit")

        try:
            choice = int(input("Enter your choice (1, 2, or 3): "))
        except ValueError:
            print("Invalid choice. Please enter 1, 2, or 3.")
            continue

        if choice == 3:
            print("Thanks for playing! Your final score is:", score)
            break

        if choice not in [1, 2]:
            print("Invalid choice. Please enter 1 for Heads, 2 for Tails, or 3 to Quit.")
            continue

        coin_result = random.choice(["Heads", "Tails"])
        print("Coin is flipping...")
        print("It's", coin_result + "!")

        if (choice == 1 and coin_result == "Heads") or (choice == 2 and coin_result == "Tails"):
            print("\033[32mCorrect guess! You earned a point.\033[0m")
            score += 1
        else:
            print("\033[31mWrong guess! Better luck next time.\033[m")

coin_flip_game()
