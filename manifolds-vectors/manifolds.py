from manim import *
import numpy as np

class Manifolds1(ThreeDScene, Scene):
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
        self.wait()

class Manifolds2(Scene):
    def construct(self):
        rect = Rectangle(color=YELLOW, height=5, width=5)
        rect.move_to(DOWN)
        r_label = MathTex(r'M', color=YELLOW).next_to(rect, RIGHT, buff=0.2)
        axes = NumberPlane(x_range=(-4, 4), y_range=(-4, 4), tips = False, x_length=5, y_length=5).move_to(DOWN)
        polarplane = PolarPlane(radius_max=4, azimuth_step=8, azimuth_units="PI radians", size=5).move_to(DOWN)
        t1 = MathTex(r'p\to ', r'(x,y)', substrings_to_isolate=['p', 'x', 'y'])
        t2 = MathTex(r'p\to ', r'(r,\theta)', substrings_to_isolate=['p', 'r', r'\theta'])
        t1.set_color_by_tex('p', GREEN)
        t1.set_color_by_tex('x', BLUE)
        t1.set_color_by_tex('y', BLUE)
        t2.set_color_by_tex('p', GREEN)
        t2.set_color_by_tex('r', BLUE)
        t2.set_color_by_tex(r'\theta', BLUE)
        for t in t1, t2:
            t.next_to(rect, UP)
        p = Dot(axes.coords_to_point(2, 1), color=GREEN)
        p_label = MathTex(r'p', color=GREEN).next_to(p, DR, buff=0.1)


        self.add(rect, r_label)
        self.wait()
        self.play(DrawBorderThenFill(axes), run_time=1.5)
        self.wait()
        self.play(FadeIn(p), FadeIn(p_label), run_time=0.5)
        self.play(Write(t1), run_time=0.5)
        self.wait()
        self.play(FadeOut(axes), run_time=0.5)
        self.play(DrawBorderThenFill(polarplane), run_time=1.5)
        self.wait()
        self.play(
            FadeOut(t1[3], shift=0.5*UP),
            FadeIn(t2[3], shift=0.5*UP),
            FadeOut(t1[5], shift=0.5*UP),
            FadeIn(t2[5], shift=0.5*UP),
            run_time=0.5
        )
        t2.set_opacity(0)
        for i in 3,5:
            t1[i].set_opacity(0)
            t2[i].set_opacity(1)
        self.wait()
        self.play(
            FadeOut(rect),
            FadeOut(polarplane),
            FadeOut(t1),
            FadeOut(t2),
            FadeOut(p),
            FadeOut(p_label),
            run_time=0.75
            )
        
        base = MathTex(r'\phi:M\to\mathbb{R}^n')
        lhs_phi = MathTex(r'\phi:')
        lhs_phi.align_to(base, LEFT)
        rhs_phi = MathTex(r'\to \mathbb{R}^n')
        lhs_p = MathTex(r'\phi(', 'p', ')')
        lhs_p[1].set_color(GREEN)
        rhs_p = MathTex(r'=(x^1(p),\hdots,x^n(p))', substrings_to_isolate=['x', 'p'])
        simplified_rhs_p = MathTex(r'=(x^\mu (p))', substrings_to_isolate=['x', 'p'])
        mu = MathTex(r'\mu = (1,\hdots, n)')
        for r in rhs_p, simplified_rhs_p:
            r.set_color_by_tex('x', BLUE)
            r.set_color_by_tex('p', GREEN)
        r_label.generate_target()
        r_label.target.next_to(lhs_phi, RIGHT, SMALL_BUFF)
        rhs_phi.next_to(r_label.target, RIGHT, SMALL_BUFF)
        lhs_p.next_to(lhs_phi, DOWN)
        rhs_p.next_to(lhs_p, RIGHT, SMALL_BUFF)
        simplified_rhs_p.next_to(lhs_p, RIGHT, SMALL_BUFF)
        mu.next_to(lhs_p, DOWN).align_to(lhs_p, LEFT)

        self.play(MoveToTarget(r_label))
        self.play(Write(lhs_phi), Write(rhs_phi), run_time=0.75)
        self.play(Write(lhs_p), Write(rhs_p), run_time=0.75)
        self.wait()
        self.play(TransformMatchingTex(rhs_p, simplified_rhs_p, transform_mismatches=True, fade_transform_mismatches=True), run_time=0.75)
        self.play(Write(mu), run_time=0.75)
        self.wait()
        


