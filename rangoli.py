import turtle

wn = turtle.Screen()
wn.setup(1.0, 1.0)
wn.bgcolor('#000113')

draw=turtle.Pen()

first = turtle.Turtle()
first.speed(0)
first.color('aqua')
first.pensize(1)

rotate=int(360)

# For First Circle
def drawCircles(t,size):
    for i in range(10):
        t.circle(size)
        size=size-4
        draw.width(i/100+0.2)
def drawSpecial(t,size,repeat):
  for i in range (repeat):
    drawCircles(t,size)
    t.right(360/repeat)
drawSpecial(first,100,10)

# For Second Circle
second = turtle.Turtle()
second.speed(0)
second.color('magenta')
second.pensize(1)

rotate=int(90)

def drawCircles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-19
def drawSpecial(t,size,repeat):
    for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)
drawSpecial(second,100,10)


turtle.done()