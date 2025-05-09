import turtle
import math

screen = turtle.Screen()
screen.setup(560, 560)
screen.bgcolor("white")

msg = turtle.Turtle()
msg.penup()
msg.hideturtle()
#msg.color("#edf1ad")
msg.color("#494947")
msg.speed(0)

grid = turtle.Turtle()
grid.color("dark gray")
grid.speed(0)
grid.penup()
grid.goto(-200,0)
grid.pendown()
grid.right(90)
grid.speed(0)

def grid1():
    for i in range(-280,281,40):
        grid.penup()
        grid.goto(i,280)
        grid.pendown()
        grid.forward(560)
        msg.goto(i-10,-12)
        msg.write(i)
        
    grid.left(90)
        
    for j in range(-280,281,40):
        grid.penup()
        grid.goto(-280,j)
        grid.pendown()
        grid.forward(560)
        if j!=0:
            msg.goto(2,j-3)
            msg.write(j)
        
    #x axis
    grid.penup()
    grid.goto(-280,0)
    grid.pendown()
    grid.pensize(4)
    grid.forward(560)
    
    #y axis
    grid.penup()
    grid.goto(0,280)
    grid.right(90)
    grid.pendown()
    grid.pensize(4)
    grid.forward(560)
    grid.hideturtle()
  
    grid.color("blue")    
    grid.penup()
    grid.goto(-90,60)
    grid.pendown()
    grid.dot(6)
    grid.penup()
    grid.goto(-100,70)
    grid.write("(-90,60)")
    grid.penup()
    grid.goto(170,60)
    grid.pendown()
    grid.dot(6)
    grid.penup()
    grid.goto(160,70)
    grid.write("(170,60)")
'''
    grid.goto(100,20)
    grid.pendown()
    grid.dot(6)
    grid.penup()
    grid.goto(60,10)
    grid.write("(100,20)")
    grid.goto(0,0)
    grid.pendown()
    grid.dot(6)
    grid.penup()
    grid.goto(-25,-20)
    grid.write("(0,0)")
'''
grid1()