from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()

# timmy_the_turtle.shape("triangle")
timmy_the_turtle.color("DarkMagenta")

random_list = [timmy_the_turtle.forward(100), timmy_the_turtle.right(90), timmy_the_turtle.forward(100)]

random.choice(random_list)



screen = Screen()
screen.exitonclick()
