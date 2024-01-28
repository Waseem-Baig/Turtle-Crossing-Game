import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
player = Player()
car_manager = CarManager()
score_board = Scoreboard()
screen.setup(width=500, height=500)
screen.tracer(0)

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # Detect the collision with cars
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            score_board.game_over()

        if player.is_at_finish_line():
            player.go_to_start()
            score_board.increase_level()
            car_manager.level_up()

screen.exitonclick()
