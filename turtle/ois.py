from turtle import *
from random import choice
from math import sqrt, cos, radians
from time import sleep

c = ["darkgreen", "olive", "darkcyan", "darkblue", "navy",
         "blue", "cadetblue", "darkkhaki", "plum", "gold",
         "limegreen", "aqua"]
speed(0)
sirge = 200
bgcolor("black")
ht()

def poolring(n, sirge):
    save_heading = heading()
    left(a/2)
    circle(sirge*sqrt(2*(1-cos(radians(a))))//2, 180)
    setheading(save_heading)

for n in range(3, 100+1):
   
    a = 360/n
    pencolor(choice(c))
    
    for i in range(n):
        forward(sirge)
        poolring(n, sirge)
        
        penup()
        goto(0, 0)
        pendown()

        right(a)

    sleep(0.5)
    clear()


exitonclick()
