from turtle import Turtle
import random


x = -360
y = 0
positions = []

class Wall(Turtle):

    def __init__(self):
        super().__init__()
        self.all_bricks = []
        self.build_wall()

    def create_brick(self, position):
        for pos in position:
            new_brick = Turtle("square")
            new_brick.shapesize(stretch_wid=1.2, stretch_len=4)
            new_brick.penup()
            new_brick.goto(pos[0], pos[1])
       
            if positions.index(position) < 2:
                new_brick.color("blue")
            elif 1 < positions.index(position) < 4:
                new_brick.color("orange")
            else:
                new_brick.color("green")
            self.all_bricks.append(new_brick)
