from turtle import Turtle
import random
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.speed("fastest")
        self.color("white")
        self.shapesize(stretch_wid=1,stretch_len=1)
        r_num=random.randint(1,4)
        if(r_num==1):
            r_heading=random.randint(5,85)
            self.setheading(r_heading)
        elif(r_num==2):
            r_heading = random.randint(95,175)
            self.setheading(r_heading)
        elif (r_num == 3):
            r_heading = random.randint(185,265)
            self.setheading(r_heading)
        elif (r_num == 4):
            r_heading = random.randint(275,355)
            self.setheading(r_heading)
        self.go=1

    def move(self):
        self.forward(self.go)
    def bounce(self):
        heading=self.heading()
        self.setheading(-heading)
    def paddle_bounce(self):
        self.go+=1
        heading=self.heading()
        if(heading>0 and heading<90):
            self.setheading(90 + heading)
        if(heading>180 and heading<270):
            theta=self.heading()-180
            self.setheading(360-theta)
        if (heading > 90 and heading < 180):
            self.setheading(heading-90)
        if (heading > 270 and heading < 360):
            theta=self.heading()-270
            self.setheading(270-theta)
    def refresh(self):
        self.go=1
        r_num = random.randint(1, 2)
        self.goto(0,0)
        if (r_num == 1):
            r_heading = random.randint(95, 265)
            self.setheading(r_heading)
        elif (r_num == 2):
            r_heading = random.randint(-85, 85)
            self.setheading(r_heading)







