from turtle import Turtle

X = 380
Y = 20
FONT = ('Arial', 30, 'bold')


class Player:
    def __init__(self, side):
        self.paddle = []
        self.side = side
        self.create_paddle()
        self.score = 0
        if self.side == 'right':
            self.scoreboard_x = 50
        else:
            self.scoreboard_x = -50
        self.scoreboard = Turtle()
        self.scoreboard_detail()
        self.write_score()

    def create_paddle(self):
        if self.side == 'right':
            x = X
        else:
            x = -X
        y = Y
        for i in range(3):
            seg = Turtle(shape='square')
            seg.speed('fastest')
            seg.color("white")
            seg.penup()
            seg.goto(x, y)
            y -= 20
            self.paddle.append(seg)

    def scoreboard_detail(self):
        self.scoreboard.hideturtle()
        self.scoreboard.color('white')
        self.scoreboard.penup()

    def write_score(self):
        self.scoreboard.goto(self.scoreboard_x, 200)
        self.scoreboard.clear()
        self.scoreboard.write(self.score, align='center', font=FONT)

    def up(self):
        if self.paddle[0].ycor()<220:
            for i in range(3):
                self.paddle[i].setheading(90)
                self.paddle[i].forward(60)
        else:
            pass

    def down(self):
        if self.paddle[-1].ycor()>-220:
            for i in range(3):
                self.paddle[i].setheading(270)
                self.paddle[i].forward(60)
        else:
            pass
