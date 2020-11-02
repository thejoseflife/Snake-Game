import turtle
import time
import random

delay = 0.1
speed = 20

window = turtle.Screen()
window.bgcolor("limegreen")
window.title("Josef's Snake Game in Python!")
window.setup(500, 500)
window.tracer(0)

snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color("red")
snake.penup()
snake.goto(0, 0)
snake.direction = ""

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("brown")
food.penup()
food.goto(random.randint(-250, 230), random.randint(-250, 230))

segments = []

def go_up():
    if snake.direction != "down":
        snake.direction = "up"

def go_down():
    if snake.direction != "up":
        snake.direction = "down"

def go_left():
    if snake.direction != "right":
        snake.direction = "left"

def go_right():
    if snake.direction != "left":
        snake.direction = "right"

def move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + speed)
    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - speed)
    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - speed)
    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + speed)

def resetsnake():
    time.sleep(1)
    snake.goto(0, 0)
    snake.direction = ""
    for segment in segments:
        segment.goto(1000, 1000)
    segments.clear()

window.listen()
window.onkeypress(go_up, "Up")
window.onkeypress(go_down, "Down")
window.onkeypress(go_left, "Left")
window.onkeypress(go_right, "Right")

while True:
    window.update()

    if(snake.xcor() < -240 or snake.xcor() > 240 or snake.ycor() < -240 or snake.ycor() > 240):
        resetsnake()
    
    if food.distance(snake) < 20:
       food.goto(random.randint(-250, 250), random.randint(-250, 250))
       
       segment = turtle.Turtle()
       segment.speed(0)
       segment.shape("square")
       segment.color("yellow")
       segment.penup()
       segments.append(segment)
       
    for index in range(len(segments)-1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = snake.xcor()
        y = snake.ycor()
        segments[0].goto(x, y)

  
    move()

    for segment in segments:
        if segment.distance(snake) < 20:
            resetsnake()
    time.sleep(delay)

    

window.mainloop()
