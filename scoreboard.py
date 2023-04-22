from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
    def increment(self,x,y):
        self.score += 1
        self.clear()
        self.goto(x, y)
        self.write(self.score, move=False, align="center", font=("Arial", 40, "normal"))