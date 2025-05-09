#from satellite import *
# from grid import *
import turtle
import random
pen = turtle.Turtle()
screen = turtle.Screen()
pen.speed(100)
screen.setup(600,600)
screen.bgcolor("black")
def draw_stars():
    for j in range(30):
        pen.penup()
        size = random.randint(10,11)
        x = random.randint(-250,250)
        y = random.randint(-130,350)
        color = "white"
        pen.goto(x,y)
        pen.pendown()
        pen.fillcolor(color)
        pen.begin_fill()
        for i in range(5):
            pen.forward(size)
            pen.right(144)
        pen.end_fill()
def moon():
    pen.penup()
    pen.goto(0,-380)
    pen.dot(560, "wheat")
def craters(x,y,size,color):
    pen.penup()
    pen.goto(x,y)
    pen.pendown()
    pen.dot(size, color)
moon()
draw_stars()
craters(160,-220, 40, "peru")
craters(-160,-200, 80, "peru")
craters(50,-250, 50, "peru")
craters(20,-150, 60, "peru")
def draw_satellite():
    pen.penup()
    pen.goto(-40,0)
    pen.pendown()
    #top triangle
    pen.fillcolor("orange")
    pen.begin_fill()
    pen.right(-60)
    for i in range(3):
        pen.forward(80)
        pen.right(120)
    pen.end_fill()
    # body rectangle
    pen.fillcolor("blue")
    pen.begin_fill()
    pen.left(-150)
    for j in range(2):
        pen.forward(120)
        pen.left(90)
        pen.forward(80)
        pen.left(90)
    pen.end_fill()
    #wings A
    pen.penup()
    pen.goto(-40,-40)
    pen.pendown()
    pen.right(90)
    pen.fillcolor("lightblue")
    pen.begin_fill()
    for k in range(4):
        pen.forward(40)
        pen.left(90)
    pen.penup()
    pen.goto(-80,-40)
    pen.pendown()
    for l in range(4):
        pen.forward(40)
        pen.left(90)
    pen.end_fill()
    #wing B
    pen.penup()
    pen.goto(120,-80)
    pen.pendown()
    pen.right(90)
    pen.fillcolor("lightblue")
    pen.begin_fill()
    for m in range(4):
        pen.forward(40)
        pen.left(90)
    pen.penup()
    pen.goto(80,-80)
    pen.pendown()
    for n in range(4):
        pen.forward(40)
        pen.left(90)
    pen.end_fill()
    #booster
    pen.penup()
    pen.goto(-20,-120)
    pen.pendown()
    pen.right(180)
    pen.fillcolor("red")
    pen.begin_fill()
    for o in range(2):
        pen.forward(65)
        pen.left(90)
        pen.forward(40)
        pen.left(90)
    pen.end_fill()
draw_satellite()
pen.penup()
pen.goto(-160,230)
pen.color("yellow")
pen.write("GALAXY SURFER", font = ('Arial', 30, 'bold'))
pen.hideturtle()
turtle.mainloop()