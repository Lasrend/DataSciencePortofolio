from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.color("blue")
        self.refresh()
    
    def refresh(self):
        randomX = random.randint(-280,280)
        randomY = random.randint(-280,280)
        self.goto(randomX, randomY)