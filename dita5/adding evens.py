total = 0
for number in range(2, 101, 2):
    total += number
print(number)
#  we can do like this
total2 = 0
for number in range(1, 101):
    if number % 2 == 0:
        total2 += number
print(total2)