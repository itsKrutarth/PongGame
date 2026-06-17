from turtle import Screen, Turtle
from paddle import Paddle

screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
game_is_on = True

RightPaddle = Paddle()
RightPaddle.goto(350, 0)


LeftPaddle = Paddle()
LeftPaddle.goto(-350, 0)

def go_up():
    RightPaddle.goto(RightPaddle.xcor(), RightPaddle.ycor()+20)

def go_down():
    RightPaddle.goto(RightPaddle.xcor(), RightPaddle.ycor()-20)

screen.listen()
screen.onkey(go_up(), "Up")
screen.onkey(go_down(), "Down")
# screen.onkey()

while game_is_on:
    screen.update()

screen.exitonclick()