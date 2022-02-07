from turtle import Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

game_is_on = True
time_to_regenerate = 0
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
score_board = ScoreBoard()
cars = []


def new_car(speed):
    car = CarManager(speed)
    cars.append(car)


speed = 5
screen.onkeypress(player.move, "Up")
while game_is_on:
    time.sleep(0.1)
    screen.update()
    time_to_regenerate += 1
    if time_to_regenerate > 6:
        new_car(speed)
        time_to_regenerate = 0
    if player.ycor() > 280:
        player.reposition()
        score_board.increase_level()
        for car in cars:
            speed = car.increase_speed()
    else:
        for car in cars:
            car.move()
            if player.distance(car) < 20:
                game_is_on = False
                score_board.game_over()

screen.exitonclick()
