import turtle
import random
screen = turtle.Screen()
screen.setup(400,600)
# Background
screen.bgpic("background.gif")
turtle.penup()
turtle.goto(-175, 275)
turtle.color("white")
Score = 0
Lives = 3
score_turtle = turtle.Turtle()
# score_turtle.write(f"SCORE: {Score}", font = ('Arial', 6, 'bold'))
score_turtle.penup()
score_turtle.goto(-190, 230)
score_turtle.color("white")
score_turtle.pendown()
score_turtle.hideturtle()
lives_turtle = turtle.Turtle()
# score_turtle.write(f"SCORE: {Score}", font = ('Arial', 6, 'bold'))
lives_turtle.penup()
lives_turtle.goto(80, 230)
lives_turtle.color("white")
lives_turtle.pendown()
lives_turtle.hideturtle()
# score_turtle.write(f"LIVES: {Lives}", font = ('Arial', 6, 'bold'))
# Spaceship
spaceship = turtle.Turtle()
screen.register_shape("spaceship.gif")
spaceship.shape("spaceship.gif")
spaceship.penup()
spaceship.goto(0,-225)
#Asteroid
asteroid = turtle.Turtle()
screen.register_shape("asteroid.gif")
asteroid.shape("asteroid.gif")
asteroid.penup()
asteroid.goto(0,270)
# Spaceship controls
def move_right():
    x = spaceship.xcor()
    y = spaceship.ycor()
    if spaceship.xcor() < 101:
        spaceship.goto(x + 50, y)
def move_left():
    x = spaceship.xcor()
    y = spaceship.ycor()
    if spaceship.xcor() > -101:
        spaceship.goto(x - 50, y)
def move_asteroid():
    x = asteroid.xcor()
    y = asteroid.ycor()
    asteroid.penup()
    asteroid.goto(x, y - 3)
def reset_asteroid():
    if asteroid.ycor() <= -330:
        asteroid.hideturtle()
        x = random.randint(-125,125)
        asteroid.goto(x,300)
        asteroid.showturtle()
def display_score():
    global Score
    score_turtle.clear()
    score_turtle.write(f"SCORE: {Score}", font = ('Arial', 6, 'bold'))
screen.tracer(0)
screen.listen()
screen.onkey(move_right, "Right")
screen.onkey(move_left, "Left")
while asteroid.ycor() > -330:
    move_asteroid()
    reset_asteroid()
    distance = spaceship.distance(asteroid)
    display_score()
    if distance <= 20:
        if Lives >= 0:            
            Lives -= 1
            print(Lives)
            asteroid.hideturtle()
            x = random.randint(-125,125)
            asteroid.goto(x,300)
            asteroid.showturtle()
    if Lives == 0:
        asteroid.hideturtle()
        turtle.goto(-150, 0)
        turtle.write(f"GAME OVER", font = ('Arial', 50, 'bold'))
screen.update()
turtle.mainloop()