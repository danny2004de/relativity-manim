from manim import *
import numpy as np

class Vectors1(ThreeDScene, Scene):
    def construct(self):
        texTemplate = TexTemplate()
        texTemplate.add_to_preamble(r'\usepackage{amsmath}')
        self.set_camera_orientation(phi=60*DEGREES, theta=-30*DEGREES)

        axes = ThreeDAxes()
        example_vector1 = Arrow3D([0,0,0], [2,2,2], color=ORANGE)
        sphere = Sphere(radius=3, checkerboard_colors=False, fill_opacity=0.5, stroke_color=BLUE, stroke_width=0)
        curve = CurvedArrow([3, 0 ,0], [3*np.cos(np.pi/4), 0, 3*np.sin(np.pi/4)], angle=np.pi/4, radius=3, color=ORANGE)
        p = Dot3D([[3*np.cos(np.pi/4), 0, 3*np.sin(np.pi/4)]], color=GREEN)
        p_label = MathTex(r'p', color=GREEN)
        p_label.set_opacity(0)
        self.add_fixed_in_frame_mobjects(p_label)
        # p_label.next_to(axes.c2p(3*np.cos(np.pi/4), 0, 3*np.sin(np.pi/4)), IN*0.1)
        p_label.shift(UR*1.45)
    
        self.play(Create(axes), run_time=0.5)
        self.wait()
        self.play(DrawBorderThenFill(example_vector1), run_time=0.75)
        self.wait()
        self.play(FadeOut(example_vector1), FadeOut(axes), run_time = 0.3)
        self.play(DrawBorderThenFill(sphere), run_time=0.75)
        self.wait()
        self.play(Create(curve))
        self.wait()
        self.play(FadeOut(curve), run_time=0.5)
        self.play(FadeIn(p), p_label.animate.set_opacity(1))
        self.wait()