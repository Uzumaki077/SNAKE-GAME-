from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        with open("high score.txt","r") as file:
            high_score=file.read()
        self.score=5
        self.high_score=high_score
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(0,350)
        self.show_score()
    def show_score(self):
        self.write(f"Score: {self.score}    High score: {self.high_score}",align="center",font=("arial",22,"normal"))
    def increase_score(self):
        self.score+=1
        self.clear()
        self.show_score()
    def end_game(self):
        self.clear()
        self.screen.bgcolor("Red")
        self.goto(0,0)
        if self.score>int(self.high_score):
            self.high_score=self.score
            with open("high score.txt","w+") as file:
                file.write(str(self.high_score))
        self.write(f"-----GAME OVER-----\n\n FINAL SCORE: {self.score} \n High Score: {self.high_score}",align="center",font=("arial",24,"normal"))            

