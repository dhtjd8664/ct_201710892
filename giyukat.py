import turtle
wn= turtle.Screen()
t1=turtle.Turtle()

def giyukat(x,y,z):
    t1.penup()
    t1.goto(x,y)
    t1.pendown()
    t1.fd(z)
    t1.rt(90)
    t1.fd(z)

giyukat(100,100,100)

wn.exitonclick()
