print("Math flascard game\n")
print("Welcome! What is your name?")
name = input().lower() # User types their name, then it is converted to lowercase
print(f"{name.capitalize()}, your name is {len(name)} characters long.") #len() counts the number of characters in the name
print("What is your last name?")
last_name = input().lower()
print(f"Your last name is {len(last_name)} characters long.")
print(f"What is {len(name)} + {len(last_name)}?") # this inserts the numbers instead of the names, creating a math problem
answer = int(input())  # Convert the input to an integer
if answer == len(name) + len(last_name):
    print("Correct!")
else:
    print("Actually, the answer is", len(name) + len(last_name))