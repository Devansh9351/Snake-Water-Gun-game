import random

computer=random.choice([1,2,3])

devanshstr=input("Enter your choice from R P S : ")

devanshdict={"r":1, "p":2, "s":3}

reversedict={1:"r", 2:"p", 3:"s"}

devansh=devanshdict[devanshstr]

print(f"Devansh choose: {reversedict[devansh]} \ncomputer choose: {reversedict[computer]}")

if(computer == devansh):

    print("The match is draw:")
else:
    
    if(computer == 1 and devansh == 2):
        print("Devansh wins:")

    elif(computer == 1 and devansh == 3):
        print("Computer wins:")

    elif(computer == 2 and devansh == 1):
        print("Computer wins:")

    elif(computer == 2 and devansh == 3):
        print("Devansh wins:")

    elif(computer == 3 and devansh == 1):
        print("Devansh wins: ")

    elif(computer == 3 and devansh == 2):
        print("computer wins:")

    else:
        print("Something went wrong")

