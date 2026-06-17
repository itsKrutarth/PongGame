from turtle import Screen, Turtle

screen = Screen()
# screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
game_is_on = True

RightPaddle = Turtle()
RightPaddle.penup()
RightPaddle.shape("square")
RightPaddle.color("white")
RightPaddle.goto(350, 0)
RightPaddle.shapesize(stretch_wid=5, stretch_len=1)


LeftPaddle = Turtle()
LeftPaddle.penup()
LeftPaddle.shape("square")
LeftPaddle.color("white")
LeftPaddle.goto(-350, 0)
LeftPaddle.shapesize(stretch_wid=5, stretch_len=1)


screen.exitonclick()