import turtle            # set up alex
wn = turtle.Screen()
alex = turtle.Turtle()

for aColor in ["yellow", "red", "purple", "blue"]:      # repeat four times
    alex.forward(50)
    alex.left(90)

wn.exitonclick()
