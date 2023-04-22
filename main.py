from turtle import Turtle, Screen
import turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time


score=Score()
score.speed("fastest")
score.ht()
score.penup()
score.left(90)
score.forward(240)
score.left(90)
score.forward(50)
x=score.xcor()
y=score.ycor()
score.color('white')
score.write("0",align="center",font=("Arial",40,"normal"))
score1=Score()
score1.speed("fastest")
score1.ht()
score1.penup()
score1.left(90)
score1.forward(240)
score1.right(90)
score1.forward(50)
x1=score1.xcor()
y1=score1.ycor()
score1.color('white')
score1.write("0",align="center",font=("Arial",40,"normal"))
screen=Screen()
screen.tracer(0)
screen.title("pong game")
screen.setup(width=800,height=600)
screen.bgcolor("black")
r_paddle=Paddle(350,0)
l_paddle=Paddle(-350,0)
line=Turtle()
line.hideturtle()
line.penup()
line.right(90)
line.forward(300)
line.right(180)
line.pendown()
line.color("white")
for i in range(300):
    line.pendown()
    line.forward(20)
    line.penup()
    line.forward(20)
ball=Ball()
turtle.onkeyrelease(r_paddle.up,"Up",)
turtle.onkey(r_paddle.down,"Down")
turtle.onkeyrelease(l_paddle.up,"w",)
turtle.onkey(l_paddle.down,"s")
turtle.listen()
game_is_on=True
while(game_is_on):
    time.sleep(0.011)
    screen.update()
    ball.move()
    if(ball.ycor()>280 or ball.ycor()<-280 ):
        ball.bounce()
    if(ball.xcor()>330 and ball.distance(r_paddle)<50):
        ball.paddle_bounce()
    if (ball.xcor() < -330 and ball.distance(l_paddle) < 50):
        ball.paddle_bounce()
    if(ball.xcor() < -400):
        ball.refresh()
        score1.increment(x1,y1)
    if(ball.xcor()>400):
        ball.refresh()
        score.increment(x, y)







screen.exitonclick()