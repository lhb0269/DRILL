import turtle

def move_up():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()

def movea_left():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()

def move_down():
    turtle.setheading(270)
    turtle.forward(50)
    turtle.stamp()

def moved_right():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()
def restart():
    turtle.home()
    turtle.clear()
    

turtle.shape('turtle')

turtle.onkey(move_up,'w')
turtle.onkey(movea_left,'a')
turtle.onkey(move_down,'s')
turtle.onkey(moved_right,'d')
turtle.onkey(restart,'Escape')
turtle.listen()
