import turtle
from turtle import Screen, Turtle

num_sides = 6
side_length = 70
angle = 360.0 / num_sides 

screen = turtle.Screen()

polygon = turtle.Turtle()

for _ in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)

polygon.hideturtle() # Hide the arrow mark

turtle.done() #Hold the screen from quitting