import turtle
from random import choice, randint


class Background(object):

    WIDTH = HEIGHT = 1000

    def __init__(self):
        #turtle.delay(0) # change this to change speed
        turtle.setup(self.WIDTH, self.HEIGHT)
        turtle.setworldcoordinates(0, 0, 500, 500)  # easier control of field and sizes

        # testing
        self.draw_map()

    def draw_road(self):
        d = turtle.Turtle()
        d.speed(0)
        d.begin_fill()
        for _ in range(4):
            d.fd(500)
            d.lt(90)
        d.end_fill()

    def draw_grass(self):
        d = turtle.Turtle()
        d.speed(0)
        d.width(10)
        starts = [(0, 300), (300, 500), (500, 200), (200, 0)]
        angles = [0, 270, 180, 90]
        for start, angle in zip(starts, angles):
            d.pu()
            d.setpos(*start)
            d.seth(angle)
            d.pd()

            d.color('gray', 'green')
            d.begin_fill()
            for _ in range(4):
                d.fd(200)
                d.lt(90)
            d.end_fill()


        d.ht()
        turtle.turtles().pop(0)  # remove turtle from memory

    def draw_map(self):
        self.draw_road()
        self.draw_grass()

"""
1) Current system is pretty buggy
2) Facing rows should move simultaneously
3) Turtles should keep a distance between each other
"""
class TurtleTraffic(object):

    STARTS = [(0, 0, 225), (90, 275, 0), (180, 500, 275), (270, 225, 500)]
    COLORS = ["yellow", "red", "blue", "green", "coral", "cyan", "hotpink", "indigo", "navy"]

    row_can_move = {0: 1, 90: 1, 180: 1, 270: 1}
    turtle_queue = []

    def __init__(self):
        turtle.delay(0)
        turtle.onscreenclick(self.print_pos)
        self.mainloop()

    def mainloop(self):
        while 1:
            if randint(0, 100) == 50:
                self.turtle_queue.append(self.make_turtle())

            # needs some rework
            for t in self.turtle_queue:

                current_pos = t.position()
                if 350 >= current_pos[0] >= 150 and 350 >= current_pos[1] >= 150:
                    for head in self.row_can_move:
                        if head != t.heading():
                            self.row_can_move[head] = 0

                else: # some unexpected behaviour will arise
                    self.row_can_move[t.heading()] = 1

                if current_pos[0] > 500 or current_pos[1] > 500:
                    t.ht()
                    self.turtle_queue.remove(t)
                    continue

                # move
                if self.row_can_move[t.heading()]:

                    """
                    for tx in self.turtle_queue:
                        if tx.heading() == t.heading():
                            p1 = tx.position()
                            p2 = t.position()
                            if (0 < p1[0]-p2[0] < 20) or (0 < p1[1]-p2[1] < 20):
                                print(p1, p2)
                                break
                    else: # road is clear
                    """
                    t.fd(1)


    @staticmethod
    def print_pos(a, b):
        print(a, b)

    def make_turtle(self, speed=1):
        p = choice(self.STARTS)
        color = choice(self.COLORS)

        turt = turtle.Turtle()
        turt.shapesize(3)
        turt.color(color)
        turt.shape("turtle")
        turt.speed(0)
        turt.pu()
        turt.seth(p[0])
        turt.setpos(p[1], p[2])
        turt.st()
        turt.speed(speed)
        return turt


if __name__ == "__main__":
    b = Background()
    t = TurtleTraffic()
