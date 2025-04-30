#functions are created with def instead of func in python
#this is the same as the fizzbuzz.py file, but inside a function
def fizz_buzz(i):
    if i % 3 == 0 and i % 5 == 0: #if i is divisible by 3 and also by 5
        print(f"{i} FizzBuzz")
    elif i % 3 == 0:
        print(f"{i} Fizz")
    elif i % 5 == 0:
        print(f"{i} Buzz")
    else:
        print(f"{i} is boring")

prompt = int(input("Enter a number: "))
fizz_buzz(prompt)
#you call a function by typing its name out. You can add a (parameter) if needed

def is_even(x): #calling for 1 parameter
    if x % 2 == 0:
        return True #return doesn't print to the screen. You will still need to print() in order to see the answer
    else:
        return False
    
my_variable = is_even(99)
print(my_variable) 

def namer(first = "John", last = "Elder"): #These 2 parameters have default values that are used if you call the function empty
    print(f"First Name: {first}")
    print(f"Last Name: {last}")

namer("Kyle") #This only changes the first parameter. I didn't find a way to only change the second one. Figure out later

for i in range(1, 101):
    fizz_buzz(i)
'''
The above does the same fizz buzz but by calling the function 100 times, instead of just printing out each line.
It uses a for loop to change the integer each line
'''

def seven_things(one, two, three, four, five, six, seven):
    answer = one+two+three+four+five+six+seven
    return answer #this function needs 7 parameters. It adds all of them together and returns the sum

print("Enter 7 numbers below:")
one = int(input("First number: "))
two = int(input("Second number: "))
three = int(input("Third number: "))
four = int(input("Fourth number: "))
five = int(input("Fifth number: "))
six = int(input("Sixth number: "))
seven = int(input("Seventh number: "))

'''
The above is how you get 7 consecutive inputs and then send those inputs to a function. 
The numbers have to be defined outside of the initial function definition for them to exist
They are then used below to complete the function
'''

result = seven_things(one, two, three, four, five, six, seven)
print("The sum is:", result)