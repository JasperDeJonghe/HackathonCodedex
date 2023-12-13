import random

score = 0
current_number = random.randint(1, 100)

print("Welcome to the Higher-Lower Game!")
print(f"Current number: {current_number}")

while True:
    user_guess = input("Predict the next number - higher (H) or lower (L): ").upper()

    while user_guess not in ['H', 'L']:
        print("Invalid input. Please enter 'H' for higher or 'L' for lower.")
        user_guess = input("Predict the next number - higher (H) or lower (L): ").upper()

    next_number = random.randint(1, 100)

    print(f"Next number: {next_number}")

    if (next_number > current_number and user_guess == 'H') or (next_number < current_number and user_guess == 'L'):
        print("\033[32mCorrect! You guessed it right.\033[0m")
        score += 1
    else:
        print("\033[31mIncorrect. Game over!\033[0m")
        break

    current_number = next_number

print(f"\033[32mYour final score: {score}\033[0m")
