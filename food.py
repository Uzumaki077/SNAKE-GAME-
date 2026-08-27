from turtle import Turtle 
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.color('red')
        self.shape("circle")
        self.shapesize(0.5,0.5)
        self.penup()
        self.food_pos()
    def food_pos(self):
        self.xpos=random.randint(-380,380)
        self.ypos=random.randint(-350,350)
        self.goto(self.xpos,self.ypos)    

            
