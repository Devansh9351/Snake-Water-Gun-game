import random

choices = ["snake", "water", "gun"]

computer = random.choice(choices)
user = input("Enter Snake, Water, or Gun: ").lower()

print("Computer chose:", computer)

if user == computer:
    print("It's a tie!")

elif user == "snake" and computer == "water":
    print("You win!")

elif user == "water" and computer == "gun":
    print("You win!")

elif user == "gun" and computer == "snake":
    print("You win!")

elif user in choices:
    print("Computer wins!")

else:
    print("Invalid choice!")