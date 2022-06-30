from turtle import *
from math import sqrt

# parameetrid
speed(0)
colormode(255) # rgb
bgcolor("lightskyblue")
algne_x, algne_y = -150, -150

def algusesse(x=algne_x, y=algne_y):
    penup()
    goto(x, y)
    setheading(0)
    pen(fillcolor="black", pencolor="black", pensize=1)
    pendown()

def alus(laeva_pikkus=450, ma_ei_tea=255, aluse_värv="saddlebrown"):
    pen(fillcolor=aluse_värv, pencolor="black", pensize=3)
    begin_fill()
    forward(laeva_pikkus)
    setheading(45)
    forward(ma_ei_tea)
    setheading(180)
    forward(laeva_pikkus+ma_ei_tea*sqrt(2))
    setheading(270)

    i = 0
    while i < 92:
        forward(9.2)
        left(3)
        i+=3

    end_fill()

    algusesse()

# natukene loll funktsioon, aga hetkel töötab
def aknad(mitu, x=0, y=0, vahe=125):
    #mitu_akent = ??
    pen(fillcolor="blue", pencolor="black", pensize=4)

    # esimene aken
    penup()
    goto(xcor()+65+x, ycor()+30+y)
    pendown()
    algus=xcor()
    
    for i in range(mitu+1):
        begin_fill()
        circle(20)
        end_fill()
        
        penup()
        goto(algus+i*vahe, ycor())
        pendown()

    algusesse()

def mastid():

    for k,i,j in [(300, 150, 30), (180, 380, 25)]:
        penup()
        goto(xcor()+i, ycor())
        setheading(90)
        forward(255*sqrt(2)/2)
        pendown()

        pen(pencolor="black", fillcolor="black")
        begin_fill()
        forward(k)
        left(90)
        forward(j)
        left(90)
        forward(k)
        left(90)
        forward(j)
        end_fill()

        algusesse()

def kapteni_ruum():
    penup()
    goto(xcor()-(255*sqrt(2)/2), ycor()+(255*sqrt(2)/2))
    pendown()

    pen(fillcolor="saddlebrown", pencolor="black", pensize=3)
    begin_fill()
    setheading(90)
    forward(140)
    setheading(0)
    forward(200)
    setheading(270)
    forward(140)
    end_fill()

    algusesse()

def meri():
    penup()
    goto(xcor()-4000, ycor())
    pendown()

    pen(pencolor="blue", fillcolor="blue")
    begin_fill()
    for i in range(4):
        forward(10000)
        right(90)
    end_fill()

    algusesse()


algusesse()
alus()
aknad(5, x=-105, vahe=105)
aknad(6, x=-160, y=80, vahe=105)
mastid()
kapteni_ruum()
meri()
exitonclick()
