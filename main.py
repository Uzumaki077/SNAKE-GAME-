from turtle import Turtle,Screen
import random
import time
from snake import Snake
from food import Food
from score import Score 
window=Screen()
window.setup(800,800)
window.bgcolor("black")
window.tracer(0)
sam=Snake()
food=Food()
score=Score()
GAME_ON=True
while GAME_ON:
    sam.movee()
    window.update()
    time.sleep(0.07)
    window.listen()
    window.onkey(sam.up,"Up")
    window.onkey(sam.down,"Down")
    window.onkey(sam.right,"Right")
    window.onkey(sam.left,"Left")
    if sam.snake_head.distance(food)<15:
        food.food_pos()
        sam.extend()
        score.increase_score()
    if sam.snake_head.xcor()>380 or sam.snake_head.xcor()<-380 or sam.snake_head.ycor()>380 or sam.snake_head.ycor()<-380:
       score.end_game()
       break
    for segment in sam.turtles[0:-1]:
        if sam.snake_head.distance(segment)<10:
            score.end_game()
            GAME_ON=False       
window.exitonclick()
