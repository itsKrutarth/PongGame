from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

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

ball = Ball()

screen.listen()
screen.onkey(RightPaddle.go_up, "Up")
screen.onkey(RightPaddle.go_down, "Down") 
screen.onkey(LeftPaddle.go_up, "w")
screen.onkey(LeftPaddle.go_down, "s")

while game_is_on:
    time.sleep(0.1)
    ball.move()
    ball.checkWallCollision()
    if(ball.distance(RightPaddle)<5 or ball.distance(LeftPaddle)<5):
        
    screen.update()

screen.exitonclick()