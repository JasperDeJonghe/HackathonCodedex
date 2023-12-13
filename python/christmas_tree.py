import random

tree_height = int(input("Enter the height of the Christmas tree: "))

for i in range(tree_height):
    spaces = " " * (tree_height - i - 1)
    stars = "*" * (2 * i + 1)

    decorated_stars = ""
    for char in stars:
        color_code = random.choice(["\033[91m", "\033[92m", "\033[93m"]) 
        decorated_stars += f"{color_code}{char}\033[0m"

    print(f"{spaces}{decorated_stars}")

trunk_width = tree_height // 3
trunk_height = tree_height // 2

for _ in range(trunk_height):
    spaces = " " * (tree_height - trunk_width // 2)
    trunk = "\033[93m#" * trunk_width
    print(f"{spaces}{trunk}\033[0m")
