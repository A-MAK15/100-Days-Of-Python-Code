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

#ball

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

