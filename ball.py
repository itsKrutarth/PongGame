from turtle import Screen, Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.goto(0,0)
        self.x = 10
        self.y = 10
    
    def move(self):
        self.goto(self.xcor()+self.x, self.ycor()+self.y)

    def checkWallCollision(self):
        if(self.ycor()>285 or self.ycor()<-285):
            self.y *= -1