from turtle import Turtle, Screen

timmy_the_turtle = Turtle()

timmy_the_turtle.shape("triangle")
timmy_the_turtle.color("DarkMagenta")


for triangle in range(0, 3):
    timmy_the_turtle.left(120)
    timmy_the_turtle.forward(100)

for square in range(0, 3):
    timmy_the_turtle.left(90)
    timmy_the_turtle.forward(100)

timmy_the_turtle.left(180)
timmy_the_turtle.forward(100)

# for pentagon in range(0, 4):

timmy_the_turtle.right(200)
timmy_the_turtle.forward(100)

timmy_the_turtle.left(60)
timmy_the_turtle.forward(100)

timmy_the_turtle.left(72)
timmy_the_turtle.forward(100)

timmy_the_turtle.left(72)
timmy_the_turtle.forward(100)

# timmy_the_turtle.left(60)
# timmy_the_turtle.forward(100)
#
# timmy_the_turtle.left(60)
# timmy_the_turtle.forward(100)
#
# timmy_the_turtle.left(60)
# timmy_the_turtle.forward(120)







screen = Screen()
screen.exitonclick()
