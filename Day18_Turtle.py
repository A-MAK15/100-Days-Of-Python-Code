from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()

# timmy_the_turtle.shape("triangle")
timmy_the_turtle.color("DarkMagenta")

timmy_the_turtle.pensize(10)

screen = Screen()
screen.colormode(255)

def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb

# print(random_colour())

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

for direction in range(1, 200):
    random_num = random.randint(1, 100)
    timmy_the_turtle.color(random_colour())
    timmy_the_turtle.speed(100)
    zigzag(random_num)
    zongzeng(random_num)
    timmy_the_turtle.left(90)

screen = Screen()
screen.exitonclick()
