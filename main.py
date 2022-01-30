import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_cars()
    cars.drive()

    for car in cars.all_cars:
        if player.distance(car) < 20:
            score.game_over()
            game_is_on = False

    if player.is_at_finish_line():
        player.go_to_start()
        cars.level += 1
        score.level_up()

screen.exitonclick()
