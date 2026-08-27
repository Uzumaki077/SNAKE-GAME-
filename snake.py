from turtle import Turtle
import random
import time
class Snake:
    def __init__(self):
        self.positions=((-40,0),(-20,0),(0,0))
        self.turtles=[]
        self.create_snake()
        self.snake_head=self.turtles[-1]
    def create_snake(self):
        for i in range(len(self.positions)):
            new=Turtle()
            new.color("white")
            new.penup()
            new.shape("square")
            new.goto(self.positions[i])
            self.turtles.append(new)
    def extend(self):
        new=Turtle()
        new.color("white")
        new.penup()
        new.shape("square")
        new.goto(self.turtles[0].pos())
        self.turtles.insert(0,new)
    def movee(self):
        for i in range(len(self.turtles)-1):
            self.turtles[i].goto(self.turtles[i+1].pos())
        self.snake_head.forward(20)
    def up(self):
        self.snake_head.setheading(90)
    def down(self):
        self.snake_head.setheading(270)    
    def right(self):
        self.snake_head.setheading(0)
    def left(self):
        self.snake_head.setheading(180)



            