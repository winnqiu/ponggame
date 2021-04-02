from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.games=1
        self.change_heading()


    def move(self):
        self.forward(20)

    #touch paddle and change direction
    def change_direction(self):
        old=self.heading()
        self.setheading(180-old)

    def collide_wall(self):
        if self.ycor()>=280 or self.ycor()<=-280:
            return True

    def refresh(self):
        self.games += 1
        self.goto(0,0)
        self.change_heading()


    def change_heading(self):
        if self.games % 2 == 1:
            angle=random.randint(-35,35)
            while -5<angle<5:
                angle=random.randint(-35,35)
            self.setheading(angle)
        else:
            angle=random.randint(145, 215)
            while 175<angle<185:
                angle = random.randint(145, 215)
            self.setheading(angle)