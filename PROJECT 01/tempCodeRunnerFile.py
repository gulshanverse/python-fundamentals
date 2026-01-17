import random

choices = {"s": 1, "w": -1, "g": 0}
reverse = {1: "Snake", -1: "Water", 0: "Gun"}

while True:
    computer = random.choice([-1, 0, 1])

    youstr = input("Enter your choice (s = Snake, w = Water, g = Gun): ").lower().strip()

    if youstr not in choices:
        print("Invalid input! Please enter only s, w, or g.\n")
        continue

    you = choices[youstr]

    print(f"\nYou chose {reverse[you]}")
    print(f"Computer chose {reverse[computer]}")

    result = you - computer

    if result == 0:
        print("Result: Draw!")
    elif result in (1, -2):
        print("Result: You Win!")
    else:
        print("Result: You Lose!")

    play_again = input("\nPlay again? (y/n): ").lower().strip()
    if play_again != "y":
        print("Thanks for playing. Game over.")
        break

