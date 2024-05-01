from manim import *
import numpy as np

class inner1(ThreeDScene, Scene):
    def construct(self):
        texTemplate = TexTemplate()
        texTemplate.add_to_preamble(r'\usepackage{amsmath}')

        m1 = MathTex(r'\phi(', r'p', r') = (', r'x', r'^\mu(', 'p', r'))')
        m2 = MathTex(r' g', r' _{\alpha \beta}=\begin{bmatrix} g _{11}&\cdots& g _{1n}\\ \vdots & \ddots & \vdots\\ g _{n1} & \cdots & g _{nn}\end{bmatrix}')
        m3 = MathTex(r'\text{\textbf{V}}', r'\cdot', r"\text{\textbf{V}}'", r'=') 
        m3_rhs1 = MathTex(r'\sum_\alpha \sum_\beta', r"g_{\alpha\beta} V^\alpha {V'}^\beta")
        m3_rhs2 = MathTex(r"g_{\alpha\beta} V^\alpha {V'}^\beta")
        m4 = MathTex(r'ds', r'^2=', r'g_{\alpha\beta} dx^\alpha dx^\beta', substrings_to_isolate=['dx'])
        for i, textcolor in [(1, GREEN), (3, BLUE), (5, GREEN)]:
            m1[i].set_color(textcolor)
        for i, textcolor in [(0, YELLOW), (2, YELLOW)]:
            m3[i].set_color(textcolor)
        m4[0].set_color(ORANGE)
        m4.set_color_by_tex('x', BLUE)
        v0 = VGroup(m3, m3_rhs1)
        v0.arrange(RIGHT, SMALL_BUFF, center=True)
        m3_rhs1.shift(DOWN*0.25)
        v1 = VGroup(m1, m2, v0, m4)
        v1.arrange(DOWN, aligned_edge = LEFT)
        # m3_rhs1.next_to(m3, RIGHT, SMALL_BUFF)
        m3_rhs2.next_to(m3, RIGHT, SMALL_BUFF)

        self.play(Write(m1), Write(m2))
        self.wait()
        self.play(Write(v0))
        self.wait()
        self.play(TransformMatchingTex(m3_rhs1, m3_rhs2))
        self.wait()
        self.play(Write(m4))
        self.wait()