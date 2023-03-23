import turtle
wn = turtle.Screen()

elan = turtle.Turtle()

distance = 50
for _ in range(100):
    elan.forward(distance)
    elan.right(90)
    distance = distance + 10
