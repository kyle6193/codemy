
num = 0
while num < 10:
    print(num)
    num += 1

names = ["Alice", "Bob", "Charlie"]
for i in names: # The For Variable can be named anything, like i
    print(i) #The first loop will end at Charlie, and not be reset. So the next loop will start at Charlie
for x in i:
    print(x) #This will print the letters of Charlie