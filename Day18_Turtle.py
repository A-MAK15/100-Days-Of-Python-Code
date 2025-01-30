from turtle import Turtle, Screen

timmy_the_turtle = Turtle()

timmy_the_turtle.shape("triangle")
timmy_the_turtle.color("DarkMagenta")


for triangle in range(0, 3):
    timmy_the_turtle.left(120)
    timmy_the_turtle.forward(100)
    timmy_the_turtle.color("DarkSeaGreen")

for square in range(0, 3):
    timmy_the_turtle.left(90)
    timmy_the_turtle.forward(100)
    timmy_the_turtle.color("CadetBlue")

timmy_the_turtle.left(180)
timmy_the_turtle.forward(100)

timmy_the_turtle.right(200)
timmy_the_turtle.forward(100)

for pentagon in range(0, 4):
    timmy_the_turtle.left(72)
    timmy_the_turtle.forward(100)
    timmy_the_turtle.color("DarkGrey")

for hexagon in range(0, 6):
    timmy_the_turtle.left(60)
    timmy_the_turtle.forward(100)
    timmy_the_turtle.color("cyan3")

for heptagon in range(0, 7):
    timmy_the_turtle.left(51)
    timmy_the_turtle.forward(100)
    timmy_the_turtle.color("DarkSlateBlue")

for octagon in range(0, 8):
    timmy_the_turtle.left(45)
    timmy_the_turtle.forward(100)
    timmy_the_turtle.color("aquamarine4")

for nonagon in range(0, 9):
    timmy_the_turtle.left(40)
    timmy_the_turtle.forward(100)
    timmy_the_turtle.color("aquamarine")

for decagon in range(0, 10):
    timmy_the_turtle.left(36)
    timmy_the_turtle.forward(100)
    timmy_the_turtle.color("CornFlowerBlue")

screen = Screen()
screen.exitonclick()
