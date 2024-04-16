from manim import *
import numpy as np

class Manifolds(ThreeDScene, Scene):
    def construct(self):
        texTemplate = TexTemplate()
        texTemplate.add_to_preamble(r'\usepackage{amsmath}')
        header1 = Tex(r'Manifolds', color=ORANGE, font_size=40)
        blist = BulletedList('No inherent coordinates or measure of distance', 'Charts ascribe coordinates to manifolds', font_size=40)
        blist.set_opacity(0)
        text = VGroup()
        text.add(header1, blist)
        text.arrange(DOWN, center=False, aligned_edge=LEFT)
        text.to_corner(UL)
        self.set_camera_orientation(phi=60*DEGREES, theta=45*DEGREES)
        torus = Torus(major_radius=2, minor_radius=1, checkerboard_colors=False)
        axes = ThreeDAxes(axis_config={"include_ticks": False})
        sphere = Sphere((-7,7,0), radius=2, checkerboard_colors=False)
        self.add_fixed_in_frame_mobjects(header1, blist)
        self.play(FadeIn(torus), run_time=0.5)
        self.wait()
        self.move_camera(phi=90*DEGREES, theta=45*DEGREES, zoom=2.5)
        self.wait()
        self.move_camera(phi=60*DEGREES, theta=45*DEGREES, zoom=1)
        self.wait()
        self.move_camera(phi=60*DEGREES, theta=45*DEGREES, zoom=0.5, run_time=0.5, added_anims=[torus.animate.move_to((7,-7,0))])
        self.wait()
        self.play(Create(axes), run_time=0.5)
        self.wait()
        self.play(FadeIn(sphere), run_time=0.5)
        self.wait()
        blist[0].set_opacity(1)
        self.play(Write(blist[0]), run_time=1)
        self.wait()
        blist[1].set_opacity(1)
        self.play(Write(blist[1]), run_time=1)

    # def make_fixed(*mobs):
    #     for mob in mobs:
    #         mob.fixed = True
    #         for submob in mob.family_members_with_points():
    #             submob.fixed = True
