import random
from turtle import Turtle

class Car(Turtle):

    def __init__(self, Yposition,carcolor, carspeed):
        super().__init__()
        self.carspeed = carspeed
        self.penup()
        self.shape("square")
        self.color(carcolor)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.goto(350+random.randint(0,300),Yposition)

    def move(self):
        self.penup()
        self.backward(self.carspeed)
        self.pendown()