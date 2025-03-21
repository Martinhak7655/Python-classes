import turtle

t = turtle.Turtle()

t.pensize(5)
for i in range(4):
    t.pencolor("yellow")
    t.forward(300)
    t.left(90)

t.pencolor("green")
t.left(45)
t.forward(425)

t.pencolor("yellow")
t.left(135)
t.forward(300)

t.pencolor("green")
t.left(135)
t.forward(425)

turtle.done()