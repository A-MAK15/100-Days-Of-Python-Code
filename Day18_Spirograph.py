from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)

timmy_the_turtle = Turtle()

# timmy_the_turtle.shape("triangle")
timmy_the_turtle.color("DarkMagenta")

timmy_the_turtle.home()

timmy_the_turtle.circle(100)

def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb

timmy_the_turtle.speed("fastest")

for circle in range(int(360/10)):
    timmy_the_turtle.color(random_colour())
    timmy_the_turtle.circle(100)
    timmy_the_turtle.right(10)

screen = Screen()
screen.exitonclick()
