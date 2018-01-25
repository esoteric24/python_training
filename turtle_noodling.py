import turtle
import time

t = turtle.Pen()

#drawing a cornerless box
# for n in range(0,4):
#     t.forward(100)
#     t.up()
#     t.forward(50)
#     t.left(90)
#     t.forward(50)
#     t.down()

#letters
def drawU(self):
    self.left(90)
    self.forward(80)
    self.up()
    self.left(180)
    self.forward(80)
    self.left(90)
    self.down()
    self.forward(70)
    self.left(90)
    self.forward(80)
    self.up()
    self.left(180)
    self.forward(80)
    self.left(90)
    self.forward(30)
    self.down()

t.drawU()

time.sleep(5)
