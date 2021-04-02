from turtle import Turtle, Screen
from player import Player
from ball import Ball
import time
import random

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)


def seperator():
    t = Turtle()
    t.color("white")
    t.hideturtle()
    t.setheading(90)
    t.pensize(10)
    y = -300
    while y < 300:
        t.penup()
        t.goto(0, y)
        t.pendown()
        t.forward(20)
        y += 40


seperator()
player1 = Player(side='left')
player2 = Player(side='right')
ball = Ball()
screen.update()

screen.listen()
game_on=True
games=1
while game_on:
    screen.update()
    time.sleep(0.1)
    ball.move()
    for c in player1.paddle:
        if c.distance(ball)<10:
            ball.change_direction()
    for c in player2.paddle:
        if c.distance(ball)<10:
            ball.change_direction()
    if ball.collide_wall():
        ball.setheading(360-ball.heading())
    if ball.xcor()>390:
        player1.score+=1
        player1.write_score()
        ball.refresh()
    if ball.xcor()<-390:
        player2.score+=1
        player2.write_score()
        ball.refresh()
    if player1.score>=10 or player2.score>=10:
        t=Turtle()
        t.color("white")
        t.hideturtle()
        if player1.score>=10:
            t.write("Player1 win. Game Over.",align="center",font=('Arial', 30, 'bold'))
        else:
            t.write("Player2 win. Game Over.",align="center",font=('Arial', 30, 'bold'))
        game_on=False
    screen.onkey(player2.up,'Up')
    screen.onkey(player2.down, 'Down')
    screen.onkey(player1.up,'w')
    screen.onkey(player1.down, 's')
    screen.update()


screen.exitonclick()
