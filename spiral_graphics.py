#this is a spiral which can be used on web designs, and as either wall paper or screen saver for mobile devices.

import turtle
import math
import random
wn = turtle.Screen()   #this specify the screen on which the design is displayed
wn.bgcolor('black')      #this is the background color of the screen
Theo = turtle.Turtle()
Theo.speed(0)             #this determines the speed of the circles
Theo.color('green')
rotate=int(360)
def drawCircles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-4
def drawSpecial(t,size,repeat):
  for i in range (repeat):
    drawCircles(t,size)
    t.right(360/repeat)
drawSpecial(Theo,100,10)
Henry = turtle.Turtle()
Henry.speed(0)
Henry.color('white')
rotate=int(90)
def drawCircles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-10
def drawSpecial(t,size,repeat):
    for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)
drawSpecial(Henry,100,10)

Iyke = turtle.Turtle()
Iyke.speed(0)
Iyke.color('Red')
rotate=int(90)
def drawCircles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-10
def drawSpecial(t,size,repeat):
    for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)
drawSpecial(Iyke,100,10)


for i in range (20):
    drawSpecial(Henry,100,10)
    drawSpecial(Theo,100,10)
    drawSpecial(Iyke,100,10)
