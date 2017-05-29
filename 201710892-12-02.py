
import turtle
wn=turtle.Screen()
t1=turtle.Turtle()




def drawTriangle(size):
    t1.fd(size)
    t1.lt(120)
    t1.fd(size)
    t1.lt(120)
    t1.fd(size)


def drawTriangleAt(size,x,y):
    t1.penup()
    t1.goto(x,y)
    t1.setheading(0)
    t1.pendown()
    t1. write(t1.pos())
    drawTriangle(size)


def drawSquare(size):
    t1.fd(size)
    t1.rt(90)
    t1.fd(size)
    t1.rt(90)
    t1.fd(size)
    t1.rt(90)
    t1.fd(size)


def drawSquareAt(size,x,y):
    t1.penup()
    t1.goto(x,y)
    t1.setheading(0)
    t1.pendown()
    t1. write(t1.pos())
    drawSquare(size)



def drawStar(size):
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
def drawStarAt(size,x,y):
    t1.penup()
    t1.goto(x,y)
    t1.setheading(0)
    t1.pendown()
    t1. write(t1.pos())
    drawStar(size)

drawTriangleAt(100,-200,0)
drawSquareAt(100,0,0)
drawStarAt(100,200,0)
