# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 ==0:
#         print(f"{i} FizzBuzz")
#     elif i % 3 == 0:
#         print(f"{i} Fizz")
#     elif i % 5 == 0:
#         print(f"{i} Buzz")
#     else:
#         print(i)

#The above can be shortened to:
for i in range(1, 101):
    print(f"{i} " + ("Fizz" * (i % 3 ==0) + "Buzz" * (i % 5 == 0) or ""))
'''
This approach builds the output string by multiplying "Fizz" and "Buzz" by the result of the modulo checks 
(which are either 0 for false or 1 for true, so the string is included or not).
'''