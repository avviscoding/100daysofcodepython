# while something_is_true:
#     do this
#     then do this
#     then do this
#     deri kur condition becomes false athr mbaron loop

# kur condition nuk behet false athere kemi te bejme me infinite loop fik laptopin n at mom
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()