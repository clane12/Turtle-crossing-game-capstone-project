from turtle import *
from mainturtle import Char
from cars import Cars
from scorelevel import Level
import time


screen = Screen()
screen.setup(600, 600)
screen.listen()
screen.tracer(0)



player = Char()
screen.onkey(fun=player.movefor, key="w")
screen.onkey(fun=player.moveback, key="s")

cars = Cars()


level = Level()

game = True
while game:
    screen.update()
    time.sleep(0.02)
    cars.buildcars()
    cars.drive()

    if player.ycor() >= 280:
        player.resetpos()
        level.increse_level()
        cars.nextlevel()

    for car in cars.cars:
        if car.distance(player) <= 22:
            print("game over")
            level.gameover()
            game = False















screen.exitonclick()