import turtle
wn=turtle.Screen()
t1=turtle.Turtle()

width= wn.window_width()
print width


w3=(width-160)/4
x1=0.0-w3
x2=0.0
x3=0.0+w3
print x1,x2,x3


def drawTriangleAt(size,at):
    t1.penup()
    t1.goto(at,0)
    t1.setheading(0)
    t1.pendown()
    t1. write(t1.pos())
    t1.fd(size)
    t1.lt(120)
    t1.fd(size)
    t1.lt(120)
    t1.fd(size)


def drawPentagon(size,at):
    t1.penup()
    t1.goto(at,0)
    t1.setheading(0)
    t1.pendown()
    t1. write(t1.pos())
    t1.fd(size)
    t1.rt(72)
    t1.fd(size)
    t1.rt(72)
    t1.fd(size)
    t1.rt(72)
    t1.fd(size)
    t1.rt(72)
    t1.fd(size)
    t1.rt(72)

def drawStarAt(size,at):
    t1.penup()
    t1.goto(at,0)
    t1.setheading(0)
    t1.pendown()
    t1. write(t1.pos())
    t1.fd(size)
    t1.rt(144)
    t1.fd(size)
    t1.rt(144)
    t1.fd(size)
    t1.rt(144)
    t1.fd(size)
    t1.rt(144)
    t1.fd(size)
    t1.rt(144)
    t1.fd(size)

drawTriangleAt(100,x1)
drawPentagon(100,x2)
drawStarAt(100,x3)
