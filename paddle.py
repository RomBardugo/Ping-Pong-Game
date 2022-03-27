from turtle import Turtle

class Paddle(Turtle):

    def __init__(self,dir):
        super().__init__()
        self.initial_paddele(dir)
        
            




    def initial_paddele(self,dir):
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(350,0)
        self.goto(dir)




    def move_up(self):
        self.setposition(self.xcor(), self.ycor() + 20)


    def move_down(self):
        self.setposition(self.xcor(), self.ycor() - 20)

    
        
