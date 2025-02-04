from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

#setting up the screen
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

game_is_on = True
def turn_off():
    global game_is_on
    game_is_on = False

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right,"Right")
screen.onkey(turn_off, "q")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.add_score()

    #detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset_score()
        snake.reset()

    #detect collision with tail excluding first element, which is head
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset_score()
            snake.reset()































