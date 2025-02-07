#main
from turtle import Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

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

screen.exitonclick()

#snake
from turtle import Turtle, Screen

POSITIONS = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 30
screen = Screen()

class Snake:

    def __init__(self):
        self.x_position = 0
        self.snakes = []
        self.snake_creation()

    def snake_creation(self):
        for coor in POSITIONS:
            new_turtle = Turtle("square")
            new_turtle.penup()
            new_turtle.color("white")
            new_turtle.goto(coor)
            self.snakes.append(new_turtle)
            # self.x_position -= 20

    def move(self):
        for snake_num in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[snake_num - 1].xcor()
            new_y = self.snakes[snake_num - 1].ycor()
            self.snakes[snake_num].goto(new_x, new_y)
        self.snakes[0].forward(10)

    def up(self):
        self.snakes[0].setheading(90)

    def down(self):
        self.snakes[0].setheading(270)

    def left(self):
        self.snakes[0].setheading(180)

    def right(self):
        self.snakes[0].setheading(0)









screen.exitonclick()
