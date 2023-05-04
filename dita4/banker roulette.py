import random


# Split string method
names_string = input("Give me everybody's names, separated by a comma and a space.\n")
names = names_string.split(", ")


numberList = len(names)

# Use -1 bec len() starts counting from 1 not 0.
randomN = random.randint(0, numberList - 1)

sorryBuddy = names[randomN]

print(f"{sorryBuddy} is going to buy the meal today!")





