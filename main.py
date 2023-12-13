from datetime import datetime
import json
import subprocess

with open("./text/once_opened.txt", "r") as file:
    json_data = file.read()
    once_opened_data = json.loads(json_data)

with open("./text/data_file.txt", "r") as file:
    json_data = file.read()
    file_data = json.loads(json_data)

with open("./text/recipe_ingr.txt", "r") as file:
    recipe_Ingredients = file.read()

with open("./text/recipe_inst.txt", "r") as file:
    recipe_Instructions = file.read()

with open("./text/story.txt", "r") as file:
    story = file.read()

with open("./text/Guess_story.txt", "r") as file:
    guessStory = file.read()

with open("./text/calculator_story.txt", "r") as file:
    calculator_story = file.read()

with open("./text/treeStory.txt", "r") as file:
    tree_story = file.read()

with open("./text/songStory.txt", "r") as file:
    song_story = file.read()

with open("./text/lastDay.txt", "r") as file:
    last_day = file.read()

with open("./text/diceStory.txt", "r") as file:
    dice_story = file.read()




current_date = datetime.now()
early = input("Do you want to get acces to every gift? (y/n) ").lower()
if early == "y":
    current_day = 24
else:
    current_day = current_date.day

answer = input("Do you want to check the advent calendar? (y/n) ").lower()

if answer == 'y':
    for i in range(1, 25):
        if once_opened_data[str(i)] != file_data[str(i)]:
            print(f"\033[31m{i}\033[0m {once_opened_data[str(i)]}")
        else:
            print(f"\033[31m{i}\033[0m \033[32m{once_opened_data[str(i)]}\033[0m")

    day_to_open = input("\nWhich day do you want to open? ")
    if int(day_to_open) < current_day:
        if day_to_open != "" and day_to_open.isdigit():
            parsed_day = int(day_to_open)
            if 1<= parsed_day <= 24:
                print(f"\033[31mYou chose to open day {day_to_open}")
                print(f"{file_data[day_to_open]}\033[0m")

                once_opened_data[day_to_open] = file_data[day_to_open]
                with open("./text/once_opened.txt", "w") as json_file:
                    json.dump(once_opened_data, json_file, indent=4)
                
                if parsed_day == 1:
                    print(f"\033[32m{story}\033[0m")

                if parsed_day == 1:
                    print(f"\033[32m{guessStory}\033[0m")

                elif parsed_day == 3:
                    subprocess.run(["python", "./python/guessNumber.py"])

                elif parsed_day == 3:
                    subprocess.run(["python", "./python/cookieClicker.py"])

                elif parsed_day == 5:
                    print(f"\033[32m{recipe_Ingredients}\033[0m")
                    print(f"\033[31m{recipe_Instructions}\033[0m")

                elif parsed_day == 6:
                    subprocess.run(["python", "./python/higherLower.py"])

                elif parsed_day == 7:
                    subprocess.run(["python", "./python/pythonQuiz.py"])

                elif parsed_day == 8:
                    subprocess.run(["python", "./python/christmas_tree.py"])

                elif parsed_day == 9:
                    subprocess.run(["python", "./python/santaGame.py"])

                elif parsed_day == 10:
                    subprocess.run(["python", "./python/snake.py"])

                elif parsed_day == 11:
                    subprocess.run(["python", "./python/RPS.py"])

                elif parsed_day == 12:
                    print(f"\033[32m{calculator_story}\033[0m")

                elif parsed_day == 13:
                    subprocess.run(["python", "./python/calculator.py"])

                elif parsed_day == 14:
                    subprocess.run(["python", "./python/gift.py"])

                elif parsed_day == 15:
                    subprocess.run(["python", "./python/TowerofHanoi.py"])

                elif parsed_day == 16:
                    print(f"\033[32m{song_story}\033[0m")

                elif parsed_day == 17:
                    print(f"\033[32m{tree_story}\033[0m")

                elif parsed_day == 18:
                    subprocess.run(["python", "./python/coinFlip.py"])

                elif parsed_day == 19:
                    subprocess.run(["python", "./python/hangman.py"])
                    
                elif parsed_day == 20:
                    subprocess.run(["python", "./python/TicTacToe.py"])

                elif parsed_day == 21:
                    subprocess.run(["python", "./python/song.py"])

                elif parsed_day == 22:
                    subprocess.run(["python", "./python/diceGame.py"])

                elif parsed_day == 23:
                    print(f"\033[32m{dice_story}\033[0m")
                
                elif parsed_day == 24:
                    print(f"\033[32m{last_day}\033[0m")

            else:
                print("This isn't a date in the advent calender, please enter a number between 1 and 24.")
        else:
            print("Invalid input. Please enter a valid number next time!")
    else:
        print("Don't open it to early!")
    
elif answer != "n" and answer != "y":
        print("Invalid input. Please enter a valid character next time!")
else:
    exit("Marry Christmas! See you tomorrow!")

