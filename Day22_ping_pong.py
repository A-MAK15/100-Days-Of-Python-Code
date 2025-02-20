#main
from turtle import Screen
from paddles import Paddles
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")

screen.tracer(0)
r_paddle = Paddles((370,0))
l_paddle = Paddles((-370,0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(fun=r_paddle.up, key="Up")
screen.onkey(fun=r_paddle.down, key="Down")
screen.onkey(fun=l_paddle.up, key="w")
screen.onkey(fun=l_paddle.down, key="s")
game_is_on = True


while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280.0 or ball.ycor() < -280.0:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

     #r_paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    # l_paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

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
        self.xmove = 10
        self.ymove = 10
        # self.goto(x=380, y=288)
        self.ball_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove

        self.goto(new_x, new_y)

    def bounce_y(self):
        self.ymove *= -1
        self.ball_speed *= 0.9

    def bounce_x(self):
        self.xmove *= -1
        self.ball_speed *= 0.9

    def reset_position(self):
        self.goto(0,0)
        self.bounce_x()
        self.ball_speed = 0.1

#scoreboard
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.updated_scoreboard()

    def updated_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        self.l_score += 1
        self.updated_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.updated_scoreboard()

