import turtle
from random import randint
forw = 1
t = turtle.Turtle()
t.speed(0) #0 #10
turtle.colormode(255)
#turtle.bgcolor('Black')
#t.color('White')

def quitfn():
    turtle.bye()

turtle.onkey(quitfn,'q')
turtle.listen()

while True:
    #t.color(randint(0, 255),randint(0, 255),randint(0, 255))
    t.forward(forw)
    t.left(120)
    t.left(2) #1
    forw += 1
turtle.done()