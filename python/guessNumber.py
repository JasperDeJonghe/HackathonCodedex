import random

number = random.randint(1, 10)
guesses = 1

print("\033[32m---Welcome to guess a number!---\033[0m")

while guesses <= 5:
    answer = input("Guess a number (1-10): ")

    if answer == number:
        print(f"\033[32mWell done! you guessed number {number}\033[0m")
    else:
        print("\033[31mLet's try again!\033[0m")
        guesses += 1

print(f"\033[31mYou didn't guessed number {number}\033[0m")