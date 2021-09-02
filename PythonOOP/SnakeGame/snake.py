from turtle import Turtle, heading, pos, position

# Constant Variable
STARTING_POS = [(0,0), (-20,0), (-40,0)]
CONSTANT_MOV = 20
## Angle to move snake
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0 

class Snake:
    def __init__(self): ### Initiate when call class
        self.segment = []
        self.createSnake()
        self.head = self.segment[0]
    
    def createSnake(self):
        for i in STARTING_POS:
            self.addSegment(i)

    def addSegment(self, position):
        newTurtle = Turtle(shape="square")
        newTurtle.color("white")
        newTurtle.penup()
        newTurtle.goto(position)
        self.segment.append(newTurtle)

    def extend(self):
        self.addSegment(self.segment[-1].position())

    def move(self):
        for segNum in range(len(self.segment)-1, 0, -1):
            newX = self.segment[segNum-1].xcor()
            newY = self.segment[segNum-1].ycor()
            self.segment[segNum].goto(newX, newY)
        self.head.forward(CONSTANT_MOV)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for seg in self.segment:
            seg.goto(1000,1000)
        self.segment.clear()
        self.createSnake()
        self.head = self.segment[0]
    


