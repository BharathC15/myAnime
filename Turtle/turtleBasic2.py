# https://realpython.com/beginners-guide-python-turtle/

import turtle

def quitfn():
    turtle.bye()

if __name__=="__main__":
    turtle.onkey(quitfn,'q') #call quit function when q key is pressed


    s = turtle.getscreen()
    #t = turtle.Turtle(visible=False)
    t = turtle.Turtle()

    #t.goto(100,100) #goto a particular direction

    t.right(90)
    t.forward(90)
    t.left(90)
    t.forward(90)

    t.hideturtle()
    turtle.listen() #Listen to the input commands
    turtle.done()
