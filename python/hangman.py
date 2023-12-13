import random

words = ["python", "hangman", "programming", "computer", "developer", "coding"]
secret_word = random.choice(words).upper()
guessed_letters = []
attempts = 6

print("Welcome to Hangman!")

while "_" in "".join([letter if letter in guessed_letters else "_" for letter in secret_word]) and attempts > 0:
    guess = input("Guess a letter: ").upper()

    if len(guess) == 1 and guess.isalpha():
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
        elif guess in secret_word:
            guessed_letters.append(guess)
            print("Good guess!")
        else:
            attempts -= 1
            print(f"Wrong guess! Attempts left: {attempts}")
    else:
        print("Invalid input. Please enter a single letter.")

    print("".join([letter if letter in guessed_letters else "_" for letter in secret_word]))

if "_" not in "".join([letter if letter in guessed_letters else "_" for letter in secret_word]):
    print("\033[32mCongratulations! You guessed the word.\033[0m")
else:
    print(f"\033[31mSorry, you ran out of attempts. The word was {secret_word}.\033[0m")
