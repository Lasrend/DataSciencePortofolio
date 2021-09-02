# Snake Game Using Python
This is my old project while learning Object Oriented Programming in Python. 

## How to use:
If you want to try this project, you need:
* Python 3 
* Clone or download repository
* Open SnakeGame folder and execute __main.py__

## Contents:
* __SnakeGame__: A folder containing all Python program
    * __food.py__: Display food objects randomly
    * __scoreboard.py__: Count score, reset score, and save the highest score in __Highscore.txt__
    * __snake.py__: Create snake object and the movement
    * __main.py__: Combine all object
* __Result.JPG__: Result of this project

## Object based considerations:
* Class Snake:
    * attributes:
        * segment
        * head
    * methods:
        * createSnake
        * addSegement
        * extend
        * move
        * up
        * down
        * left
        * right
        * reset

* Class Score:
    * attributes:
        * track
        * highscore
    * methods:
        * scoreCount
        * updateScore
        * resetScore

* Class Food:
    * methods:
        * refresh