import turtle
wn=turtle.Screen()
t1=turtle.Turtle()

def drawSquare(size):
    for i in range(0,4):
        t1.fd(size)
        t1.rt(90)
drawSquare(100)
wn.exitonclick()
