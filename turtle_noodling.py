import turtle
import time

t = turtle.Pen()

#drawing a cornerless box
for n in range(0,4):
    t.forward(100)
    t.up()
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.down()

#letters
def drawU(t):
    t.left(90)
    t.forward(100)
    t.up()
    t.left(180)
    t.forward(100)
    t.left(90)
    t.down()
    t.forward(90)
    t.left(90)
    t.forward(100)
    t.up()
    t.left(180)
    t.forward(100)
    t.left(90)
    t.forward(50)
    t.down()
    
time.sleep(5)
