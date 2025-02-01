from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()

# timmy_the_turtle.shape("triangle")
timmy_the_turtle.color("DarkMagenta")

timmy_the_turtle.pensize(10)

random_list = [timmy_the_turtle.forward(100), timmy_the_turtle.right(90), timmy_the_turtle.forward(100)]

for direction in range(1, 30):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(50)

screen = Screen()
screen.exitonclick()
