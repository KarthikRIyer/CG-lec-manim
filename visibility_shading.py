from manimlib import *


class VisibilityShading(Scene):
    CONFIG = {
        "camera_class": ThreeDCamera,
    }

    # def set_background(self):
    #     background = Rectangle(
    #         width=100 * FRAME_WIDTH,
    #         height=100 * FRAME_HEIGHT,
    #         stroke_width=0,
    #         fill_color="#000000",
    #         fill_opacity=1)
    #     background2 = Rectangle(
    #         width=100 * FRAME_WIDTH,
    #         height=100 * FRAME_HEIGHT,
    #         stroke_width=0,
    #         fill_color="#000000",
    #         fill_opacity=1)
    #     background3 = Rectangle(
    #         width=100 * FRAME_WIDTH,
    #         height=100 * FRAME_HEIGHT,
    #         stroke_width=0,
    #         fill_color="#000000",
    #         fill_opacity=1)
    #     background2.rotate_about_origin(90, 0)
    #     background2.shift(50 * RIGHT)
    #     background3.rotate_about_origin(90, 0)
    #     background3.shift(50 * LEFT)
    #     background.shift(5 * IN)
    #     self.add(background)
    #     self.add(background2)
    #     self.add(background3)

    def construct(self):
        # circle = Circle()
        # circle.set_fill(BLUE, opacity=0.5)
        # circle.set_stroke(BLUE_E, width=4)
        # square = Square()
        # self.set_background()
        # self.camera.background_color = BLACK
        triangle = Triangle()
        triangle.set_fill(GREY, opacity=0.0)
        triangle.set_stroke(BLACK, width=4)
        triangle.stretch(2, 0)
        triangle.stretch(3, 1)
        triangle.shift(LEFT)
        triangle2 = Triangle()
        triangle2.set_fill(GREY, opacity=0.0)
        triangle2.set_stroke(BLACK, width=4)
        triangle2.stretch(3, 0)
        triangle2.stretch(2, 1)
        triangle2.shift(OUT)
        self.play(ShowCreation(triangle), ShowCreation(triangle2))
        self.wait(2)
        self.play(triangle.animate.set_opacity(1.0), triangle2.animate.set_opacity(1.0))
        self.wait(2)
        self.play(triangle.animate.set_fill(RED), triangle2.animate.set_fill(BLUE))
        self.wait(2)
        # self.play(triangle.rotate, PI/4, about_point=OUT)
        frame = self.camera.frame
        self.play(frame.animate.set_euler_angles(theta=-30 * DEGREES,
                                                 phi=70 * DEGREES, ))
        # line = Line(triangle2.get_center()+OUT, triangle.get_center()+IN)
        # self.play(ShowCreation(line))
