import turtle

def star():
    t = turtle.Turtle()
    t.pensize(5)
    t.pencolor("yellow")
    for i in range(5):
        t.forward(250)
        t.right(144)
    turtle.done()

def cross_square():
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

def draw_heart(): 
    t = turtle.Turtle()

    t.pensize(5)
    t.fillcolor("red")  
    t.begin_fill() 
    t.left(140)
    t.forward(180)
    t.circle(-90, 200) 
    t.left(120)
    t.circle(-90, 200) 
    t.forward(180)
    t.end_fill()

    turtle.done()

def square():
    t = turtle.Turtle()

    t.pensize(5)
    t.pencolor("purple")
    t.forward(300)

    t.left(180)

    t.right(60)
    t.pencolor("yellow")
    t.forward(300)

    t.left(120)
    t.pencolor("green")
    t.forward(300)

    turtle.done