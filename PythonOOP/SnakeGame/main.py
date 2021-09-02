import time
from scoreboard import Score
from turtle import Screen
from snake import Snake
from food import Food

screen = Screen()
screen.bgcolor('black')
screen.setup(height=600, width=600)
screen.title("Snake Game")
screen.tracer(0)

#Object
score = Score()
snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")

#Loop game
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.scoreCount()
    
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        snake.reset()
        score.resetScore()
    
    for tail in snake.segment[1:]:
        if snake.head.distance(tail) < 15:
            score.resetScore
            snake.reset()

screen.exitonclick()
