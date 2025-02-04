from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.high_score = 0
        self.read_high_score()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.print_score()

    def read_high_score(self):
        """reads high score from data.txt and returns the value"""
        # If a highscore already exists
        try:
            with open("data.txt") as file:
                high_score = int(file.read())
                self.high_score = high_score
        # if user has not played yet
        except FileNotFoundError:
            pass

    def update_high_score(self):
        """updates high score to data.txt or creates it if first time playing"""
        with open("data.txt", mode="w") as file:
            file.write(str(self.score))
        self.high_score = self.score

    def print_score(self):
        self.teleport(0, 270)
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align = ALIGNMENT,font = FONT)

    def add_score(self):
        self.score += 1
        self.print_score()

    def reset_score(self):
        if self.score > self.high_score:
            self.update_high_score()
        self.score = 0
        self.print_score()



















