from turtle import Turtle

class Char(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.setheading(90)
        self.penup()
        self.setposition(0, -280)

    def movefor(self):
        self.forward(20)

    def moveback(self):
        self.back(20)

    def resetpos(self):
        self.setposition(0, -280)