from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.shape("square")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.goto(x,y)
        self.y=60

        self.x=x
    def up(self):
        self.goto(self.x,self.ycor()+self.y)
    def down(self):
        self.goto(self.x,self.ycor()-self.y)



