from manim import *
import random
import math

class GraphNetworks(Scene):
    def construct(self):
        FRAME_HEIGHT = 8.0
        FRAME_RATIO = 16.0/9.0
        FRAME_WIDTH = FRAME_HEIGHT * FRAME_RATIO
        background = Rectangle(width = FRAME_WIDTH, height = FRAME_HEIGHT, stroke_width = 0, fill_opacity = 1).set_color_by_gradient([RED, ORANGE])
        self.add(background)

        dotCount = 100
        dots = []
        directionX = []
        directionY = []
        speed = []
        
        alpha = ValueTracker(0)
        alphaLimit = 2
        def set_random_dots():
            for i in range(dotCount):
                directionX.append(random.uniform(-1, 1))
                directionY.append(random.uniform(-1, 1))
                speed.append(random.uniform(-2, 2))
                dots.append(Dot([(random.random()*FRAME_WIDTH)-FRAME_WIDTH/2, (random.random()*FRAME_HEIGHT)-FRAME_HEIGHT/2.0, 0]))
                   
        def generate_moving_dots():
            for i in range(dotCount):
                self.add(always_shift(dots[i], [directionX[i], directionY[i], 0], speed[i]))

        def lines_draw():
            lines = VGroup()
            for i in range(dotCount):
                for j in range(i+1, dotCount):
                    dist = math.sqrt(math.pow(dots[j].get_x() - dots[i].get_x(), 2) + math.pow(dots[j].get_y() - dots[i].get_y(), 2))
                    if dist >= alphaLimit:
                        alpha.set_value(0)
                    elif dist >= 0 and dist < alphaLimit:
                        alpha.set_value(-((dist / alphaLimit)) + 1)
                    else:
                        alpha.set_value(1)
                    lines.add(Line(start = [dots[i].get_x(), dots[i].get_y(), 0], end = [dots[j].get_x(), dots[j].get_y(), 0], stroke_width = 10, stroke_opacity = alpha.get_value()))

                if dots[i].get_x() < -(FRAME_WIDTH/2.0 + 1):
                    dots[i].set_x((FRAME_WIDTH/2.0 + 1))
                elif dots[i].get_x() > (FRAME_WIDTH/2.0 + 1):
                    dots[i].set_x(-(FRAME_WIDTH/2.0 + 1))

                if dots[i].get_y() < -(FRAME_HEIGHT/2.0 + 1):
                    dots[i].set_y((FRAME_HEIGHT/2.0 + 1))
                elif dots[i].get_y() > (FRAME_HEIGHT/2.0 + 1):
                    dots[i].set_y(-(FRAME_HEIGHT/2.0 + 1))
                    
            return lines
        
        set_random_dots()
        generate_moving_dots()
        self.add(always_redraw(lines_draw))

        self.wait(10)

