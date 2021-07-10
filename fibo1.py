# https://www.geeksforgeeks.org/python-plotting-fibonacci-spiral-fractal-using-turtle/



import turtle
from random import randint

def quitfn():
    turtle.bye()

def goLoc(x,y):
    t.penup()
    t.goto(x*scaleFactor,y*scaleFactor)
    t.pendown()

def drawRect(a,b):
    t.color(randint(0, 255),randint(0, 255),randint(0, 255))
    a_ = a * scaleFactor
    b_ = b * scaleFactor
    #t.begin_fill()
    t.forward(a_)
    t.left(90)
    t.forward(b_)
    t.left(90)
    t.forward(a_)
    t.left(90)
    t.forward(b_)
    t.left(90)
    t.forward(a_)
    t.left(90)
    #t.end_fill()

def fibSquare(a,b):
    a_ = a * scaleFactor
    b_ = b * scaleFactor
    t.backward(a_ * scaleFactor)
    t.right(90)
    t.forward(b_ * scaleFactor)
    t.left(90)
    t.forward(b_ * scaleFactor)
    t.left(90)
    t.forward(b_ * scaleFactor)



if __name__ == "__main__":

    scaleFactor = 5
    turtle.colormode(255)

    turtle.onkey(quitfn,'q') #call quit function when q key is pressed

    turtle.title("Fibonacci Series")

    s = turtle.Screen()
    t = turtle.Turtle()

    t.width(3)

    #drawRect(1,1)
    #goLoc(1,0)
    #drawRect(1,1)

    fibA = 1
    fibB = 1

    for fib in range(10):
        #goLoc(scaleFactor,0)
        drawRect(fibA,fibB)
        #fibSquare(fibA,fibB)
        fibA,fibB = fibB,fibA+fibB

    #t.hideturtle() # Hide the arrow mark
    turtle.listen() #Listen to the input commands
    turtle.done() #Hold the screen from quitting