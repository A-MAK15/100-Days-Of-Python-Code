from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()

# timmy_the_turtle.shape("triangle")
timmy_the_turtle.color("DarkMagenta")

timmy_the_turtle.pensize(10)

color = ["DarkMagenta", "bisque3", "CadetBlue", "blue4", "chocolate1", "coral"]

# print(random_color)

def zigzag(num):
    timmy_the_turtle.forward(num)
    timmy_the_turtle.right(90)
    timmy_the_turtle.forward(num)
    timmy_the_turtle.left(90)

def zongzeng(no):
    timmy_the_turtle.forward(no)
    timmy_the_turtle.left(90)
    timmy_the_turtle.forward(no)
    timmy_the_turtle.right(90)

for direction in range(1, 101):
    random_num = random.randint(1, 100)
    random_color = random.choice(color)
    timmy_the_turtle.color(random_color)
    timmy_the_turtle.speed(100)
    zigzag(random_num)
    zongzeng(random_num)
    timmy_the_turtle.left(90)

screen = Screen()
screen.exitonclick()
