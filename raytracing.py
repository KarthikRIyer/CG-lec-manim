from manimlib import *


class Raytracing(Scene):

    def construct(self):
        box = Rectangle(width=FRAME_WIDTH * 0.9, height=FRAME_HEIGHT * 0.9)
        box.set_stroke(color=BLACK, width=4)

        boxObject = Rectangle(width=FRAME_WIDTH * 0.05, height=FRAME_HEIGHT * 0.4)
        boxObject.set_stroke(color=BLACK, width=4)
        boxObject.set_fill(color=BLUE_E, opacity=1)
        boxObject.move_to(box.get_center() + 3 * LEFT)

        lightSrcDot = Dot()
        lightSrcDot.set_fill(YELLOW)
        lightSrcDot.move_to(box.get_center() + 5 * RIGHT + 3 * UP)
        lightSrcGlare1 = Line(lightSrcDot.get_center() + 0.3 * LEFT,
                              lightSrcDot.get_center() + 0.3 * RIGHT)
        lightSrcGlare2 = Line(lightSrcDot.get_center() + 0.3 * UP,
                              lightSrcDot.get_center() + 0.3 * DOWN)
        lightSrcGlare3 = Line(lightSrcDot.get_center() + 0.2 * LEFT + 0.2 * UP,
                              lightSrcDot.get_center() + 0.2 * RIGHT + 0.2 * DOWN)
        lightSrcGlare4 = Line(lightSrcDot.get_center() + 0.2 * LEFT + 0.2 * DOWN,
                              lightSrcDot.get_center() + 0.2 * RIGHT + 0.2 * UP)
        lightSrcGlare1.set_stroke(color=YELLOW, width=4)
        lightSrcGlare2.set_stroke(color=YELLOW, width=4)
        lightSrcGlare3.set_stroke(color=YELLOW, width=4)
        lightSrcGlare4.set_stroke(color=YELLOW, width=4)
        lightSrcText = Text("Light\n\nSrc", font_size=18)
        lightSrcText.move_to(lightSrcDot.get_center() + 0.8 * RIGHT)

        cameraTri = Triangle()
        cameraTri.set_stroke(color=BLACK, width=4)
        cameraTri.stretch(2, 1)
        cameraTri.scale(0.3)
        cameraTri.move_to(boxObject.get_center() + 2 * LEFT + 2 * UP)
        cameraTri.rotate(angle=45 * DEGREES, axis=OUT)
        cameraText = Text("Camera", font_size=18)
        cameraText.move_to(cameraTri.get_vertices()[0] + 0.5 * UP)

        self.play(ShowCreation(box), ShowCreation(boxObject), ShowCreation(lightSrcDot),
                  ShowCreation(lightSrcGlare1), ShowCreation(lightSrcGlare2),
                  ShowCreation(lightSrcGlare3), ShowCreation(lightSrcGlare4),
                  ShowCreation(cameraTri), FadeIn(cameraText), FadeIn(lightSrcText))
        realWorldText = Text("Real World", font_size=24, opacity=0.8)
        self.play(FadeIn(realWorldText))
        self.wait(0.5)
        self.play(FadeOut(realWorldText))
        self.wait(1.0)

        ray1 = Line()
        ray1.set_stroke(color=GREY, width=4)
        ray1.set_points_by_ends(start=lightSrcDot.get_center(),
                                end=lightSrcDot.get_center())
        rayNoCam = Line()
        rayNoCam.set_stroke(color=BLACK, width=4)
        rayNoCam.set_fill(color=BLACK)
        rayNoCam.set_points_by_ends(start=lightSrcDot.get_center(),
                                    end=lightSrcDot.get_center())
        self.play(ray1.animate.set_points_by_ends(start=lightSrcDot.get_center(),
                                                  end=box.get_bottom()),
                  rayNoCam.animate.set_points_by_ends(start=lightSrcDot.get_center(),
                                                      end=box.get_bottom() + 3 * RIGHT)
                  )
        ray1.add_tip()
        ray1.get_tip().scale(0.5)
        ray1.get_tip().set_color(color=GREY)
        rayNoCam.add_tip()
        rayNoCam.get_tip().scale(0.5)
        rayNoCam.get_tip().set_color(color=BLACK)

        ray2 = Line()
        ray2.set_stroke(color=GREY, width=4)
        ray2.set_points_by_ends(start=ray1.get_end(),
                                end=ray1.get_end())
        rayNoCam2 = Line()
        rayNoCam2.set_stroke(color=BLACK, width=4)
        rayNoCam2.set_fill(color=BLACK)
        rayNoCam2.set_points_by_ends(start=rayNoCam.get_end(),
                                     end=rayNoCam.get_end())
        self.play(ray2.animate.set_points_by_ends(start=ray1.get_end(),
                                                  end=box.get_left() + DOWN),
                  rayNoCam2.animate.set_points_by_ends(start=rayNoCam.get_end(),
                                                       end=boxObject.get_right())
                  )
        ray2.add_tip()
        ray2.get_tip().scale(0.5)
        ray2.get_tip().set_color(color=GREY)
        rayNoCam2.add_tip()
        rayNoCam2.get_tip().scale(0.5)
        rayNoCam2.get_tip().set_color(color=BLACK)

        ray3 = Line()
        ray3.set_stroke(color=GREY, width=4)
        ray3.set_points_by_ends(start=ray2.get_end(),
                                end=ray2.get_end())
        rayNoCam3 = Line()
        rayNoCam3.set_stroke(color=BLACK, width=4)
        rayNoCam3.set_fill(color=BLACK)
        rayNoCam3.set_points_by_ends(start=rayNoCam2.get_end(),
                                     end=rayNoCam2.get_end())
        self.play(ray3.animate.set_points_by_ends(start=ray2.get_end(),
                                                  end=boxObject.get_left()),
                  rayNoCam3.animate.set_points_by_ends(start=rayNoCam2.get_end(),
                                                       end=box.get_top())
                  )
        ray3.add_tip()
        ray3.get_tip().scale(0.5)
        ray3.get_tip().set_color(color=GREY)
        rayNoCam3.add_tip()
        rayNoCam3.get_tip().scale(0.5)
        rayNoCam3.get_tip().set_color(color=BLACK)

        ray4 = Line()
        ray4.set_stroke(color=GREY, width=4)
        ray4.set_points_by_ends(start=ray3.get_end(),
                                end=ray3.get_end())
        rayNoCam4 = Line()
        rayNoCam4.set_stroke(color=BLACK, width=4)
        rayNoCam4.set_fill(color=BLACK)
        rayNoCam4.set_points_by_ends(start=rayNoCam3.get_end(),
                                     end=rayNoCam3.get_end())
        self.play(ray4.animate.set_points_by_ends(start=ray3.get_end(),
                                                  end=cameraTri.get_vertices()[0]),
                  rayNoCam4.animate.set_points_by_ends(start=rayNoCam3.get_end(),
                                                       end=box.get_right())
                  )
        ray4.add_tip()
        ray4.get_tip().scale(0.5)
        ray4.get_tip().set_color(color=GREY)
        rayNoCam4.add_tip()
        rayNoCam4.get_tip().scale(0.5)
        rayNoCam4.get_tip().set_color(color=BLACK)

        self.wait(2)
        self.play(FadeOut(ray1), FadeOut(ray2), FadeOut(ray3), FadeOut(ray4),
                  FadeOut(rayNoCam), FadeOut(rayNoCam2), FadeOut(rayNoCam3),
                  FadeOut(rayNoCam4))
        cgWorldText = Text("CG World", font_size=24, opacity=0.8)
        self.play(FadeIn(cgWorldText))
        self.wait(0.5)
        self.play(FadeOut(cgWorldText))
        self.wait(1.0)

        ray1 = Line()
        ray1.set_stroke(color=GREY, width=4)
        ray1.set_points_by_ends(start=cameraTri.get_vertices()[0],
                                end=cameraTri.get_vertices()[0])
        self.play(ray1.animate.set_points_by_ends(start=ray1.get_start(),
                                                  end=boxObject.get_left()))
        ray1.add_tip()
        ray1.get_tip().scale(0.5)
        ray1.get_tip().set_color(color=GREY)

        ray2 = Line()
        ray2.set_stroke(color=GREY, width=4)
        ray2.set_points_by_ends(start=ray1.get_end(),
                                end=ray1.get_end())
        self.play(ray2.animate.set_points_by_ends(start=ray1.get_end(),
                                                  end=box.get_left() + DOWN))
        ray2.add_tip()
        ray2.get_tip().scale(0.5)
        ray2.get_tip().set_color(color=GREY)

        ray3 = Line()
        ray3.set_stroke(color=GREY, width=4)
        ray3.set_points_by_ends(start=ray2.get_end(),
                                end=ray2.get_end())
        self.play(ray3.animate.set_points_by_ends(start=ray2.get_end(),
                                                  end=box.get_bottom()))
        ray3.add_tip()
        ray3.get_tip().scale(0.5)
        ray3.get_tip().set_color(color=GREY)

        ray4 = Line()
        ray4.set_stroke(color=GREY, width=4)
        ray4.set_points_by_ends(start=ray3.get_end(),
                                end=ray3.get_end())
        self.play(ray4.animate.set_points_by_ends(start=ray3.get_end(),
                                                  end=lightSrcDot.get_center()))
        ray4.add_tip()
        ray4.get_tip().scale(0.5)
        ray4.get_tip().set_color(color=GREY)
        self.wait(1)
