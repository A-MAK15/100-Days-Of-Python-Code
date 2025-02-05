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

## Hirst

from turtle import Turtle, Screen
import random

tim = Turtle()

screen = Screen()
screen.colormode(255)

color_list = [(223, 232, 241), (245, 231, 238), (231, 243, 236), (204, 159, 107), (231, 213, 109), (134, 168, 192), (44, 105, 144), (152, 78, 53), (199, 142, 164), (15, 32, 53), (181, 159, 42), (148, 65, 87), (141, 178, 155), (205, 91, 70), (64, 117, 92), (195, 89, 118), (225, 170, 187), (15, 38, 27), (59, 34, 19)]

row_length = 0
row_height = 0
teleportation = 0

def dot_draw():
    tim.dot(20, random.choice(color_list))
    tim.penup()
    tim.forward(100)

def row():
    global row_length
    while row_length < 5:
        # random_color =
        dot_draw()
        row_length += 1

while row_height < 5:
    row()
    teleportation += 70
    tim.teleport(0, teleportation)
    row_height += 1
    row_length = 0


screen = Screen()
screen.exitonclick()
