import time
from turtle import Screen

from car import Car
from car_manager import CarManager
from player import Player
#from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Yuval's frog game")
screen.tracer(0)

player = Player()
screen.listen()
screen.onkeypress(key="Up", fun=player.player_move_up)

cars = CarManager()
score = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    cars.create_car()
    cars.move()
    screen.update()
    for car in cars.car_list:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()
    if player.is_at_finish_line():
        player.go_to_start()
        cars.level_up()
        score.level_up()
screen.exitonclick()
