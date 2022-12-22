from turtle import Turtle, Screen

def triangle():
    for i in range(0,3):
        jimmy.forward(60)
        jimmy.right(120)
    jimmy.forward(60)
    jimmy.right(90)

def square():
    for i in range(0,4):
        jimmy.forward(60)
        jimmy.right(90)
    jimmy.right(270)

def pentagon():
    for i in range(0,4):
        jimmy.right(72)
        jimmy.forward(60)
    jimmy.right(72)
    jimmy.forward(60)

def hexagon():
    for i in range(0,5):
        jimmy.right(60)
        jimmy.forward(60)
    jimmy.right(60)
    jimmy.forward(60)

def heptagon():
    for i in range(0,6):
        jimmy.right(51.42)
        jimmy.forward(60)
    jimmy.right(51.42)
    jimmy.forward(60)

def octagon():
    for i in range(0,7):
        jimmy.right(45)
        jimmy.forward(60)
    jimmy.right(45)
    jimmy.forward(60)

def nanogon():
    for i in range(0,8):
        jimmy.right(40)
        jimmy.forward(60)
    jimmy.right(40)
    jimmy.forward(60)


def decagon():
    for i in range(0,9):
        jimmy.right(36)
        jimmy.forward(60)
    jimmy.right(36)
    jimmy.forward(60)


jimmy = Turtle()
triangle()
square()
pentagon()
hexagon()
heptagon()
octagon()
nanogon()
decagon()




screen = Screen()
screen.exitonclick()

