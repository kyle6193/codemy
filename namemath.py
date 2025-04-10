print("Math flascard game\n")
print("Welcome! What is your name?")
name = input().lower()
print(f"{name.capitalize()}, your name is {len(name)} characters long.")
print("What is your last name?")
last_name = input().lower()
print(f"Your last name is {len(last_name)} characters long.")
print(f"What is {len(name)} + {len(last_name)}?")
answer = int(input())  # Convert the input to an integer
if answer == len(name) + len(last_name):
    print("Correct!")
else:
    print("Actually, the answer is", len(name) + len(last_name))