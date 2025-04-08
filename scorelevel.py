from turtle import Turtle

class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setposition(-220, 250)
        self.level = 1
        self.color("orange")
        self.write(arg=f"level {self.level}", align="center", font=("Arial", 20, "bold"))

    def increse_level(self):
        self.clear()
        self.level += 1
        self.write(arg=f"level {self.level}", align="center", font=("Arial", 20, "bold"))

    def gameover(self):
        self.setposition(0,0)
        self.color("red")
        self.write(arg=f"Game Over", align="center", font=("Arial", 20, "bold"))