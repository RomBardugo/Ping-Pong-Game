from turtle import Turtle

class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.r_score = 0
        self.l_score = 0
        self.update_scoreBoard()
        
    def update_scoreBoard(self):
        self.clear()
        self.goto(-100, 220)
        self.write(self.l_score, align="center", font=("Courier", 50, "normal"))
        self.goto(100, 220)
        self.write(self.r_score, align="center", font=("Courier", 50, "normal"))

    
    def increse_l_score(self):
        self.l_score += 1
        self.update_scoreBoard()
        
    def increse_r_score(self):
        self.r_score += 1
        self.update_scoreBoard()