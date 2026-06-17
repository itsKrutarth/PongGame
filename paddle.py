from turtle import Screen, Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)

    def goto(self, x, y):
        return super().goto(x, y)
    
    def go_up(self):
        self.goto(self.xcor(), self.ycor()+20)
    
    def go_down(self):
        self.goto(self.xcor(), self.ycor()-20)