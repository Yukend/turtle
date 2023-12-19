import turtle 
import time

sample = turtle.Screen().bgcolor("green")

t = turtle.Turtle()
t.speed(10)
t.color("red")
for i in range(0, 24):
    t.forward(50)
    t.right(15)
    t.forward(50)
    t.right(165)
    t.forward(50)
    t.right(15)
    t.forward(50)
t.forward(50)
t.right(15)
t.forward(50)
t.right(15)
for i in range(0, 24):
    t.forward(50)
    t.right(150)
    t.forward(50)
    t.left(135)
time.sleep(5)

