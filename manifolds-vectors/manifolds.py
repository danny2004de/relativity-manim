from manim import *

class Manifolds(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi = 60*DEGREES, theta=45*DEGREES)
        torus = Torus(major_radius=2, minor_radius=2/3)
        self.play(Create(torus), run_time=1)
        self.wait()