import turtle
t = turtle.Turtle()
t.speed(0)
t.pensize(2)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
for i in range(360):
    t.pencolor(colors[i % 6])
    t.forward(i)
    t.right(59)

t.hideturtle()
turtle.done()
