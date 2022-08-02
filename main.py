from turtle import Screen
import time
from Snake import Snake
from food import Food
from score_board import ScoreBoard


screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

# Detect food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()

# Detect Collision
    if snake.head.xcor() < -280 or snake.head.xcor() > 290 or snake.head.ycor() < -280 or snake.head.ycor() > 295:
        game_is_on = False
        score.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
