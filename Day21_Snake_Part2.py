#scorebord
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.score = 0
        self.write(f"Score : {self.score}", True, align="center", font=("Arial", 20, "normal"))
        self.penup()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!!!", True, align="center", font=("Arial", 20, "normal"))

    def score_increase(self):
        self.score += 1
        self.goto(0, 270)
        self.clear()
        self.write(f"Score : {self.score}", True, align="center", font=("Arial", 20, "normal"))
        self.penup()

#food
import random
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
#snake
from turtle import Turtle, Screen

POSITIONS = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 30
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
screen = Screen()

class Snake:

    def __init__(self):
        self.x_position = 0
        self.snakes = []
        self.snake_creation()
        self.head = self.snakes[0]

    def snake_creation(self):
        for position in POSITIONS:
            self.add_segments(position)

    def add_segments(self, position):
        new_turtle = Turtle("square")
        new_turtle.penup()
        new_turtle.color("white")
        new_turtle.goto(position)
        self.snakes.append(new_turtle)
        # self.x_position -= 20

    def extend(self):
        self.add_segments(self.snakes[-1].position())

    def move(self):
        for snake_num in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[snake_num - 1].xcor()
            new_y = self.snakes[snake_num - 1].ycor()
            self.snakes[snake_num].goto(new_x, new_y)
        self.snakes[0].forward(10)

    def up(self):
        if self.snakes[0].heading() != DOWN:
            self.snakes[0].setheading(UP)

    def down(self):
        if self.snakes[0].heading() != UP:
            self.snakes[0].setheading(DOWN)

    def left(self):
        if self.snakes[0].heading() != RIGHT:
            self.snakes[0].setheading(LEFT)

    def right(self):
        if self.snakes[0].heading() != LEFT:
            self.snakes[0].setheading(RIGHT)
#main
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food) < 15:
        scoreboard.score_increase()
        food.refresh()
        snake.extend()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    for segment in snake.snakes[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
