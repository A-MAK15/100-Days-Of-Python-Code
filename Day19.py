from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(100)

def move_backwards():
    tim.backward(100)

def counter_clockwise():
    tim.left(10)

def clockwise():
    tim.right(10)

def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear_drawing)

screen.exitonclick()

## Turtle race
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
color = ["red", "orange", "yellow", "green", "blue", "purple"]
is_race_on = False
all_turtles = []

user_bet = screen.textinput(title="Place your bet", prompt="Which turtle will win the race ? Enter color : ")
# print(user_input)

y = -100

for turtle in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color[turtle])
    new_turtle.penup()
    new_turtle.goto(x=-238, y=y)
    all_turtles.append(new_turtle)
    y += 40

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won!!!!The {winning_color} turtle is the winner")
            else:
                print(f"You have lost. The {winning_color} turtle won")
        rand_distance = random.randint(1,10)
        turtle.forward(rand_distance)


screen.exitonclick()
