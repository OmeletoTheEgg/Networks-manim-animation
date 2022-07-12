from manim import *
import random
import math

class Graph(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        arrow = Arrow3D(start=np.array([0, 0, 0]), end=np.array([2, 2, 2]))
        m0 = Matrix([[, ], [-1, 1]])
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.add(axes)
        self.add_fixed_in_frame_mobjects(m0)
        m0.to_corner(UL)
        self.wait(PI/2)
        self.stop_3dillusion_camera_rotation()

