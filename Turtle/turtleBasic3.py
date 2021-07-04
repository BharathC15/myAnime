import turtle
import time

def quitfn():
    turtle.bye()

if __name__=="__main__":
    turtle.onkey(quitfn,'q') #call quit function when q key is pressed

    turtle.title("Bharath's programming")

    s = turtle.Screen()
    t = turtle.Turtle()

    t.goto(100,100) # Go to the given location

    t.setpos(-100,100) # Go to the given location


    t.right(90)
    t.forward(90)
    t.left(90)
    t.forward(90)

    t.penup() # stop drawing

    t.setx(-150)
    t.sety(-150)
    
    t.pendown() # start drawing

    t.circle(25)


    t.pensize(5) #Change the pen size
    t.goto(-75,175)

    t.dot(25)

    s.bgcolor(0.5,0,0.5)
    #print(s.colormode()) -> Default = 1
    

    # fill
    t.goto(75,-200)

    t.pencolor("Green")
    t.fillcolor("orange")

    t.begin_fill()
    t.fd(100)
    t.lt(120)
    t.fd(100)
    t.lt(120)
    t.fd(100)
    t.end_fill()

    #Cloning Turtles
    s.bgcolor('white')
    t.home() # goto origin
    c = t.clone()
    t.color("magenta")
    c.color("red")
    t.circle(100)
    c.circle(60)

    t.hideturtle() # Hide the arrow mark
    turtle.listen() #Listen to the input commands
    turtle.done() #Hold the screen from quitting