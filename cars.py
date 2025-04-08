from turtle import *
import random
import time

COLOR = ["red", 'blue', 'green', 'yellow', 'orange', 'purple', 'pink']

class Cars:
    def __init__(self):
        self.cars = []
        self.speed = 1


    def buildcars(self):
        chance = random.randint(1,16)
        if chance == 6:
            self.car = Turtle("square")
            self.car.shapesize(1, 2)
            self.car.penup()
            self.car.color(random.choice(COLOR))
            self.car.setposition(random.randint(320, 350), random.randint(-220, 250))
            self.cars.append(self.car)

    def drive(self):
        for car in self.cars:
            car.back(self.speed)

    def newposition(self):
        for car in self.cars:
            if car.position() >= 320:
                self.cars.pop(car)

    def nextlevel(self):
        self.speed += 0.7
