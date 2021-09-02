from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.track = 0
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        with open("Highscore.txt") as file:
            contents = file.read()
        self.highScore = int(contents)
    
    # def gameOver(self):
    #     self.goto(0,0)
    #     self.write("Game Over", move=False, align="center", font=("Arial", 24, "normal"))

    def scoreCount(self):
        self.track += 1
        self.clear()
        self.write(f"Score: {self.track}", move = False, align="center", font=("Arial", 10, "normal"))

    def updateScore(self):
        self.clear()
        self.write(f"Score: {self.track} High Score: {self.highScore}", move=False, 
        align="center", font=("Arial", 10, "normal"))

    def resetScore(self):
        if self.track > self.highScore:
            self.highScore = self.track
        self.track = 0
        with open("Highscore.txt", mode = "w") as file:
            file.write(f"{self.highScore}")
        self.updateScore()
