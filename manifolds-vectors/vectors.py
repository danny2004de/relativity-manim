from manim import *
import numpy as np

class Vectors1(ThreeDScene, Scene):
    def construct(self):
        texTemplate = TexTemplate()
        texTemplate.add_to_preamble(r'\usepackage{amsmath}')
        self.set_camera_orientation(phi=60*DEGREES, theta=-30*DEGREES)

        axes = ThreeDAxes()
        example_vector1 = Arrow3D([0,0,0], [2,2,2], color=YELLOW)
        sphere = Sphere(radius=3, checkerboard_colors=False, fill_opacity=0.5, stroke_color=BLUE, stroke_width=0)
        curve = CurvedArrow([3, 0 ,0], [3*np.cos(np.pi/4), 0, 3*np.sin(np.pi/4)], angle=np.pi/4, radius=3, color=YELLOW, tip_shape=StealthTip)
        p_pos = np.array([3*np.cos(np.pi/4), 0, 3*np.sin(np.pi/4)])
        p = Dot3D(p_pos, color=GREEN)
        p_label = MathTex(r'p', color=GREEN)
        p_label.rotate(np.pi/2, axis=[0,0,1])
        p_label.rotate(np.pi/4, axis=[0,1,0])
        p_label.next_to(p_pos, DR*0.3+IN*0.3)
        s1 = np.array([1/np.sqrt(2), -1, -1/np.sqrt(2)]) + p_pos
        s2 = np.array([1/np.sqrt(2), 1, -1/np.sqrt(2)]) + p_pos
        s3 = np.array([-1/np.sqrt(2), -1, 1/np.sqrt(2)]) + p_pos
        s4 = np.array([-1/np.sqrt(2), 1, 1/np.sqrt(2)]) + p_pos
        plane = Polygon(s1, s2, s4, s3, color = ORANGE, fill_color=ORANGE, fill_opacity=0.4)
        plane_label = MathTex(r'T_p', color=ORANGE)
        plane_label.rotate(np.pi/2, axis=[0,0,1])
        plane_label.rotate(np.pi/4, axis=[0,1,0])
        plane_label.next_to(plane, DOWN)
        vector1 = Arrow(start=p_pos, end=s4, color=YELLOW, buff=0, tip_shape=StealthTip)
        v_label = MathTex(r'\textbf{V}', color=YELLOW)
        v_label.rotate(np.pi/2, axis=[0,0,1])
        v_label.rotate(np.pi/4, axis=[0,1,0])
        v_label.next_to(vector1, UP)
        m1 = MathTex(r'\textbf{V}', r'\equiv \partial_{\textbf{V}}')
        m1[0].set_color(YELLOW)
        m1.set_opacity(0)
        self.add_fixed_in_frame_mobjects(m1)
        m1.to_edge(LEFT)

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
        self.play(FadeIn(p), Write(p_label))
        self.wait()
        self.play(DrawBorderThenFill(plane), Write(plane_label), run_time=0.75)
        self.wait()
        self.play(DrawBorderThenFill(vector1), Write(v_label), run_time=0.75)
        self.wait()
        m1.set_opacity(1)
        self.play(Write(m1), run_time=0.75)
        self.wait()
        self.remove(m1, vector1, v_label, plane_label, p_label)
        self.wait()

        sphere2 = Sphere(radius=3, checkerboard_colors=False, fill_opacity=0, stroke_color=WHITE, stroke_width=0.6)
        p1, p2, p3 = [3*np.cos(-np.pi/6), 3*np.sin(-np.pi/6), 0], [3*np.cos(-np.pi/12), 3*np.sin(-np.pi/12), 0], [3*np.cos(-np.pi/6)*np.cos(np.pi/12), 3*np.sin(-np.pi/6)*np.cos(np.pi/12), 3*np.sin(np.pi/12)]
        longitude = Arrow(start=p1, end=p2, color=RED, tip_shape=StealthTip, buff=0)
        latitude = Arrow(start=p1, end=p3, color=RED, tip_shape=StealthTip, buff=0)
        varphi = MathTex(r'\varphi', color=RED)
        varphi.rotate(np.pi/2, [1,0,0])
        varphi.rotate(np.pi/3, [0,0,1])
        theta = MathTex(r'\theta', color=RED)
        theta.rotate(np.pi/2, [1,0,0])
        theta.rotate(np.pi/3, [0,0,1])
        varphi.next_to(longitude, IN)
        theta.next_to(latitude, DOWN)

        self.play(DrawBorderThenFill(sphere2), run_time=0.3)
        self.wait()
        self.play(Create(longitude), Write(varphi), run_time=0.75)
        self.wait()
        self.play(Create(latitude), Write(theta), run_time=0.75)
        self.wait()
        self.move_camera(phi=np.pi/4, theta=0, frame_center=p_pos, added_anims=[Write(p_label), Write(plane_label)])
        self.wait()

        ephi = Vector(direction=[0, 1, 0], buff=0, tip_shape=StealthTip, color=YELLOW)
        etheta = Vector(direction=[-np.sqrt(2)/2, 0, np.sqrt(2)/2], buff=0, tip_shape=StealthTip, color=YELLOW)
        ephi_label = MathTex(r'\text{\textbf{e}}', r'_\varphi')
        etheta_label = MathTex(r'\text{\textbf{e}}', r'_\theta')
        for l in [ephi_label, etheta_label]:
            l[0].set_color(YELLOW)
            l[1].set_color(RED)
            l.rotate(np.pi/2, [0, 0, 1])
            l.rotate(np.pi/4, [0, 1, 0])
        ephi_label.next_to(ephi, RIGHT/np.sqrt(2) + IN/np.sqrt(2))
        etheta_label.next_to(etheta, DOWN)
        ephi_def = MathTex(r'\text{\textbf{e}}', r'_\varphi', r'={\partial \over \partial', r'\varphi', r'}\bigg|', r'_p')
        etheta_def = MathTex(r'\text{\textbf{e}}', r'_\theta', r'={\partial \over \partial', r'\theta', r'}\bigg|', r'_p')
        for i, textcolor in [(0, YELLOW), (1, RED), (3, RED), (5, GREEN)]:
            ephi_def[i].set_color(textcolor)
            etheta_def[i].set_color(textcolor)
        self.add_fixed_in_frame_mobjects(ephi_def, etheta_def)
        ephi_def.to_corner(UL)
        etheta_def.next_to(ephi_def, DOWN)

        self.play(Create(ephi), Create(etheta), Write(ephi_label), Write(etheta_label), Write(ephi_def), Write(etheta_def))
        self.wait()


class Vectors2(Scene):
    def construct(self):
        texTemplate = TexTemplate()
        texTemplate.add_to_preamble(r'\usepackage{amsmath}')
        ax = Axes(x_range=(0, 10), y_range=(0, 10), tips = False)
        def f(x):
            return 0.2*((x-5)**2)
        parabola = ax.plot(f, color=MAROON)
        t = ValueTracker(0)
        initial = [ax.c2p(t.get_value(), f(t.get_value()))]
        dot = Dot(point=initial)
        dot.add_updater(lambda y: y.move_to(ax.c2p(t.get_value(), f(t.get_value()))))
        vel = always_redraw(lambda: Arrow(
            start=[ax.c2p(t.get_value(), f(t.get_value()))],
            end=[ax.c2p(1 + t.get_value(), 0.4*(t.get_value()-5) + f(t.get_value()))], 
            color=YELLOW, 
            buff=0,
            tip_shape=StealthTip
            )
        )

        m1 = MathTex(r'\phi ( p ) &= (x^\mu( p ))', substrings_to_isolate=['x', ' p '])
        m2 = MathTex(r'\text{\textbf{e}}_\mu &= {\partial \over \partial x^\mu}\bigg|_{ p }', substrings_to_isolate=['x', r'\text{\textbf{e}}', r'_{ p }'])
        m1.set_color_by_tex('x', BLUE)
        m1.set_color_by_tex(' p ', GREEN)
        m2.set_color_by_tex('x', BLUE)
        m2.set_color_by_tex(r'\text{\textbf{e}}', YELLOW)
        m2.set_color_by_tex(r'_{ p }', GREEN)
        m_group = VGroup(m1, m2)
        m_group.arrange(DOWN)

        self.play(DrawBorderThenFill(ax), Create(parabola), Create(vel), FadeIn(dot), run_time = 0.75)
        self.wait()
        self.play(t.animate.set_value(9.5))
        self.wait()
        self.play(FadeOut(parabola), FadeOut(ax), FadeOut(dot), FadeOut(vel), run_time = 0.5)
        self.play(Write(m_group), run_time = 1)
        self.wait()

class Vectors3(Scene):
    def construct(self):
        texTemplate = TexTemplate()
        texTemplate.add_to_preamble(r'\usepackage{amsmath}')
        m1 = MathTex(r'\text{\textbf{V}}', r'=\sum_\mu', r'V', r'^\mu', r'\text{\textbf{e}}', r'_\mu', r'=\sum_\mu', r'V', r'^\mu', r'{\partial \over \partial', r'x', r'^\mu}')
        for i, textcolor in [(0, YELLOW), (4, YELLOW), (-2, BLUE)]:
            m1[i].set_color(textcolor)
        m2 = MathTex(r'\text{\textbf{V}}', r'=', r'V', r'^\mu', r'\text{\textbf{e}}', r'_\mu', r'=', r'V', r'^\mu', r'{\partial \over \partial', r'x', r'^\mu}')
        for i, textcolor in [(0, YELLOW), (4, YELLOW), (-2, BLUE)]:
            m2[i].set_color(textcolor)
        r1 = SurroundingRectangle(m2[3], buff=0.02)
        r2 = SurroundingRectangle(m2[5], buff=0.02)
        r3 = SurroundingRectangle(m2[-4], buff=0.02)
        r4 = SurroundingRectangle(m2[-1], buff=0.02)
        for r in [r1,r2,r3,r4]:
            r.set_stroke(TEAL, 1)
            r.set_fill(TEAL, 0.25)

        self.play(Write(m1), run_time=1)
        self.wait()
        self.play(TransformMatchingTex(m1, m2, transform_mismatches=True), run_time=0.75)
        self.wait()
        self.play(DrawBorderThenFill(r1), DrawBorderThenFill(r2), run_time=0.75)
        self.play(DrawBorderThenFill(r3), DrawBorderThenFill(r4), run_time=0.75)



