
from os import system
system("clear")
print("Welcome to Python Princess!")
print("The goal is to find the princess!")
name = input("What is your name? ")
name = name.lower()
system("clear")
print("You're standing in front of two doors.")
print("Do you want to go through the left door or the right door?")
question = input().lower()
if question == "left":
    system("clear")
    print("You fell into a pit and died! GAME OVER...")
elif question == "right":
    system("clear")
    print(f'Congratulations {name.capitalize()}, you found \nthe Python Princess! YOU WIN!')
else:
    system("clear")
    print("Incorrect response. GAME OVER...")
    