import random

print("Welcome to the Dice Game!")

score = 0

while True:
    input("Press Enter to roll the die...")

    player_roll = random.randint(1, 6)
    computer_roll = random.randint(1, 6)

    print(f"You rolled: {player_roll}")
    print(f"Computer rolled: {computer_roll}")

    if player_roll > computer_roll:
        print("\033[32mYou win this round!\033[0m")
        score += 1
    elif player_roll < computer_roll:
        print("\033[31mComputer wins this round.\033[0m")
        break
    else:
        print("It's a tie! Roll again.")

print(f"Your final score: {score}")
