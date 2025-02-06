from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

x_position = 0

snakes = []

for _ in range(3):
    new_turtle = Turtle("square")
    new_turtle.penup()
    new_turtle.color("white")
    new_turtle.setpos(x_position, 0)
    snakes.append(new_turtle)
    x_position -= 20

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for snake_num in range(len(snakes) - 1, 0, -1):
        new_x = snakes[snake_num - 1].xcor()
        new_y = snakes[snake_num - 1].ycor()
        snakes[snake_num].goto(new_x, new_y)









screen.exitonclick()
