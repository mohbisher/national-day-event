import cv2
import turtle
import numpy as np
from matplotlib import pyplot as plt
import time

from Gaussian import gaussian
from Pointer import get_next

class ExecuterClass:


    def execute(self, speed, color):

        win = turtle.Screen()
        win.bgcolor('white')
        point = '/Users/mohbisher/Desktop/folder/pen.png'
        controller = cv2.imread(point, 0)
        th3 = gaussian(point)
        plt.show()

        WIDTH = controller.shape[1]
        HEIGHT = controller.shape[0]
        print(WIDTH, HEIGHT)

        CUTOFF_LEN = ((WIDTH + HEIGHT) / 2) / 60
        iH, iW = np.where(th3 == [0])
        iW = iW - WIDTH / 2
        iH = -1 * (iH - HEIGHT / 2)
        positions = [list(iwh) for iwh in zip(iW, iH)]

        t = turtle.Turtle()
        t.color("brown")
        t.shapesize(1)
        t.pencolor(color)
        turtle.tracer(0, 0)
        t.penup()
        t.goto(positions[0])
        t.pendown()

        time.sleep(3)
        p = positions[0]
        counter = 0
        while (p):
            p = get_next(p, positions)
            if p:
                counter += 1
                print('Drawing direction:', counter)
                if counter % speed == 0:
                    turtle.update()



                current_pos = np.asarray(t.pos())
                new_pos = np.asarray(p)
                length = np.linalg.norm(new_pos - current_pos)
                if length < CUTOFF_LEN:
                    t.goto(p)
                else:
                    t.penup()
                    t.goto(p)
                    t.pendown()
                positions.remove(p)

        turtle.done()


obj = ExecuterClass()
obj.execute(30, 'black')