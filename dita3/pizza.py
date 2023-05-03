print("welcome to Python Pizaa delivers ")
size = input("Whst size pizza do you want ? S,M or L?")
add_pepperoni = input("do you want pepperoni ?Y or N")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0
if size == "S":
    bill += 2
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is $ {bill}")