def tower_of_hanoi(n, source, target, auxiliary):
    if n > 0:
        tower_of_hanoi(n - 1, source, auxiliary, target)
        print(f"Move disk {n} from {source} to {target}")
        tower_of_hanoi(n - 1, auxiliary, target, source)

def manual_tower_of_hanoi(num_disks):
    pegs = {'A': list(range(num_disks, 0, -1)), 'B': [], 'C': []}
    target_pegs = ['A', 'B', 'C']

    while pegs['C'] != list(range(num_disks, 0, -1)):
        print("\nCurrent state of pegs:")
        for peg, disks in pegs.items():
            print(f"{peg}: {disks}")

        try:
            user_input = input("Enter source peg (A, B, C), target peg (A, B, C), or 'D' for the solution: ").upper()

            if user_input == 'D':
                print("\nSolution to the Tower of Hanoi puzzle:")
                tower_of_hanoi(num_disks, 'A', 'C', 'B')
                break

            source_peg, target_peg = user_input[0], user_input[1]

            if source_peg not in pegs or target_peg not in pegs:
                print("Invalid peg. Please enter A, B, or C.")
                continue

            if not pegs[source_peg]:
                print("Source peg is empty. Choose a different source.")
                continue

            source_disk = pegs[source_peg][-1]
            if pegs[target_peg] and source_disk > pegs[target_peg][-1]:
                print("Invalid move. Cannot place a larger disk on a smaller one.")
                continue

            pegs[source_peg].pop()
            pegs[target_peg].append(source_disk)

        except KeyboardInterrupt:
            print("\nExiting the game. Goodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

    if pegs['C'] == list(range(num_disks, 0, -1)):
        print("\n\033[31mCongratulations! You have successfully moved all disks to the target peg (C).")
        print("You have won the Tower of Hanoi game!\033[0m")

print("\033[32mWelcome to the Manual Tower of Hanoi game!")
print("To play the game, follow these instructions:")
print("1. Enter the number of disks.")
print("2. Enter the source peg (A, B, C) and target peg (A, B, C) for each move.")
print("3. The game will display the current state of the pegs after each move.")
print("4. Enter '4' to get the solution to the Tower of Hanoi puzzle.")
print("5. You win the game by successfully moving all disks to the target peg (C). ")
print("6. You can exit the game at any time by pressing Ctrl+C.\033[0m")

try:
    num_disks = int(input("Enter the number of disks: "))
    if num_disks <= 0:
        print("Please enter a positive integer.")
    else:
        manual_tower_of_hanoi(num_disks)
except ValueError:
    print("Invalid input. Please enter a valid integer.")
