gifts = []

while True:
    print("\n--- List ---")
    for index, gift in enumerate(gifts, start=1):
        print(f"{index}. {gift}")

    print("\nOptions:")
    print("\033[32m1. Add gift")
    print("2. Remove gift")
    print("\033[31m3. Quit\033[0m")

    choice = input("Enter your choice: ")

    if choice == '1':
        gift = input("Enter the gift: ")
        gifts.append(gift)
    elif choice == '2':
        index = int(input("Enter the gift number to remove: "))
        if 1 <= index <= len(gifts):
            removed_gift = gifts.pop(index - 1)
            print(f"Removed: {removed_gift}")
        else:
            print("Invalid gift number.")
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
