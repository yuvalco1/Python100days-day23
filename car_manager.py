import random
from turtle import Turtle

from car import Car

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 10
MOVE_INCREMENT = 5


class CarManager():

    def __init__(self):
        self.car_list = []

    def create_car(self):
        random_chance = random.randint(1,5)
        if random_chance == 1:
            car = Car(random.randint(-9,9)*25, random.choice(COLORS), STARTING_MOVE_DISTANCE)
            self.car_list.append(car)

    def move(self):
        for car in self.car_list:
            car.move()


    def level_up(self):
        for car in self.car_list:
            car.carspeed += MOVE_INCREMENT




