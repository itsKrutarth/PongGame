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
screen.onkey(LeftPaddle.go_up, "w")
screen.onkey(LeftPaddle.go_down, "s")
screen.onkey(RightPaddle.go_up, "Up")
screen.onkey(RightPaddle.go_down, "Down") 

while game_is_on:
    time.sleep(0.1)
    ball.move()
    ball.checkWallCollision()
    if(ball.distance(RightPaddle)<25 or ball.distance(LeftPaddle)<25):
        ball.paddleCollision()
    if(ball.xcor()>390):
        game_is_on= False
        Player = "Left Player"
        turtle2 = Turtle()
        turtle2.penup()
        turtle2.hideturtle()
        turtle2.color("white")
        turtle2.goto(0, 0)
        turtle2.write(f"GAME OVER! {Player} WON!! ", False, align="center", font=("Arial", 24, "normal"))

    elif(ball.xcor()<-390):
        game_is_on= False
        Player = "Right Player"
        turtle2 = Turtle()
        turtle2.penup()
        turtle2.hideturtle()
        turtle2.color("white")
        turtle2.goto(0, 0)
        turtle2.write(f"GAME OVER! {Player} WON!! ", False, align="center", font=("Arial", 24, "normal"))

    screen.update()



screen.exitonclick()