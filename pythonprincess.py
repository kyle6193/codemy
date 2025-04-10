from os import system  # Import the system function from the os module to execute shell commands
system("clear")  # Clear the terminal screen
print("Welcome to Python Princess!")  
print("The goal is to find the princess!") 

# Ask the player for their name and convert it to lowercase for consistency
name = input("What is your name? ")
name = name.lower()

system("clear")  
print("You're standing in front of two doors.")  
print("Do you want to go through the left door or the right door?")  

# Get the player's choice and convert it to lowercase for case-insensitive comparison
question = input().lower()

if question == "left": #Beginning of if statement
    system("clear")  
    print("You fell into a pit and died! GAME OVER...")  
elif question == "right": #Second option in if statement
    system("clear")  
    print(f'Congratulations {name.capitalize()}, you found \nthe Python Princess! YOU WIN!') #inserts name into the string and capitalizes the first letter
else: #Final option in if statement if nothing above is typed
    system("clear")  
    print("Incorrect response. GAME OVER...")  