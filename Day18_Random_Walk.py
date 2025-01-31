from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()

timmy_the_turtle.shape("triangle")
timmy_the_turtle.color("DarkMagenta")

left = timmy_the_turtle.left(10)
right = timmy_the_turtle.right(10)

for random_walk in range(0, 50):
    timmy_the_turtle.forward(10)
    direction = [left, right]
    random.choice(direction)
  
screen = Screen()
screen.exitonclick()
