
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

x=("X")
c=int(position[0])
r=int(position[1])
if (r==1):
 row1[c-1]=x
elif (r==2):
 row2[c-1]=x
else:
 row3[c-1]=x

print(f"{row1}\n{row2}\n{row3}")