#main
from turtle import Screen
from paddles import Paddles
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")

screen.tracer(0)
r_paddle = Paddles((370,0))
l_paddle = Paddles((-370,0))
ball = Ball()

screen.onkey(fun=r_paddle.up, key="Up")
screen.onkey(fun=r_paddle.down, key="Down")
screen.onkey(fun=l_paddle.up, key="w")
screen.onkey(fun=l_paddle.down, key="s")
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()



screen.exitonclick()

#paddles
from turtle import Turtle

UP = 90
DOWN = -270

class Paddles(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def up(self):
        y_pos = self.ycor() + 20
        self.goto(x=self.xcor(),y=y_pos)

    def down(self):
        y_pos = self.ycor() - 20
        self.goto(x=self.xcor(), y=y_pos)

#ball
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        # self.goto(x=380, y=288)

    def move(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10

        # self.goto(new_x, new_y)

        while self.ycor() != 590:
            self.goto(new_x, new_y)
        # self.goto(self.xcor() - 20, self.ycor() - 20)
        self.right(20)
        self.goto(new_x - 10, new_y - 10)
