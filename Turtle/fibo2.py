# Fibonacci spiral
import turtle
from random import randint
import math

def quitfn():
    turtle.bye()


if __name__ == "__main__":

    scaleFactor = 3
    resolution = 30
    turtle.colormode(255)

    turtle.onkey(quitfn,'q') #call quit function when q key is pressed

    turtle.title("Fibonacci Series")

    s = turtle.Screen()
    t = turtle.Turtle()

    t.speed(0)
    t.width(3)

    #drawRect(1,1)
    #goLoc(1,0)
    #drawRect(1,1)

    fibA = 1
    fibB = 2

    for fib in range(1,10):
        move  = ((math.pi / 2) * fibB * scaleFactor) / resolution
        t.color(randint(0, 255),randint(0, 255),randint(0, 255))
        for _ in range(resolution):
            t.forward(move)
            t.left(90/resolution)

        fibA,fibB = fibB,fibA+fibB

    #t.hideturtle() # Hide the arrow mark
    turtle.listen() #Listen to the input commands
    turtle.done() #Hold the screen from quitting