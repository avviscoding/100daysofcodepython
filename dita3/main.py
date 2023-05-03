print ("welcome to rollercoaster!")
height=int(input("what is your height in cm ?"))
bill= 0
if height>120:
    print ("yes you can ride ")
    age=int(input("what is your age "))
    if age <12 :
        bill=5
        print("pay 5  dollare ")
    elif age <=18:
        bill=7
        print("pay 7 dollare ")
    else:
        bill=12
        print("pay 12 dollare ")
    wants_photo = input("do you want photos yes or no type y for yes and n for no")
    if wants_photo == "Y":
      bill += 3

    print(f"your bill is {bill} bill")

else:
    print("can't ride")