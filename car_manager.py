from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self, speed):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=2)
        self.color(random.choice(COLORS))
        self.penup()
        self.starting_move_distance = speed
        self.goto(300, random.randint(-230, 250))
        self.setheading(180)

    def move(self):
        self.forward(self.starting_move_distance)

    def increase_speed(self):
        self.starting_move_distance += MOVE_INCREMENT
        return self.starting_move_distance
