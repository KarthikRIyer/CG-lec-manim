from manimlib import *


class ShadowRay(Scene):

    def construct(self):
        surfaceLine = Line(5 * LEFT + 2 * DOWN, 5 * RIGHT + 2 * DOWN)
        surfaceText = Text("Surface", font_size=24)
        surfaceText.move_to(surfaceLine.get_end() + RIGHT)
        lightText = Text("Directional Light", font_size=24)
        lightText.move_to(surfaceLine.get_center() + 5 * UP)
        # VGroup(surfaceLine, surfaceText).arrange(RIGHT, buff=1)
        self.play(ShowCreation(surfaceLine), FadeIn(surfaceText))

        circle = Circle()
        circle.set_fill(BLUE, opacity=0.5)
        circle.set_stroke(BLUE_E, width=4)
        circle.move_to(surfaceLine.get_center() + 2 * UP)
        self.play(FadeIn(circle))

        rayStartPoint = surfaceLine.get_center() + 4.5 * UP
        rayCenter = Arrow()
        rayCenter.set_stroke(color=YELLOW)
        rayCenter.set_fill(color=YELLOW)
        rayCenter.set_points_by_ends(start=rayStartPoint,
                                     end=rayStartPoint)
        rayRight1 = Arrow()
        rayRight1.set_stroke(color=YELLOW)
        rayRight1.set_fill(color=YELLOW)
        rayRight1.set_points_by_ends(start=rayStartPoint + RIGHT,
                                     end=rayStartPoint + RIGHT)
        rayRight2 = Arrow()
        rayRight2.set_stroke(color=YELLOW)
        rayRight2.set_fill(color=YELLOW)
        rayRight2.set_points_by_ends(start=rayStartPoint + 2 * RIGHT,
                                     end=rayStartPoint + 2 * RIGHT)
        rayLeft1 = Arrow()
        rayLeft1.set_stroke(color=YELLOW)
        rayLeft1.set_fill(color=YELLOW)
        rayLeft1.set_points_by_ends(start=rayStartPoint + LEFT,
                                    end=rayStartPoint + LEFT)
        rayLeft2 = Arrow()
        rayLeft2.set_stroke(color=YELLOW)
        rayLeft2.set_fill(color=YELLOW)
        rayLeft2.set_points_by_ends(start=rayStartPoint + 2 * LEFT,
                                    end=rayStartPoint + 2 * LEFT)
        shadowLine = Line(LEFT + 2 * DOWN, RIGHT + 2 * DOWN)
        shadowLine.set_stroke(GREY_E)
        realWorldText = Text("Real World", font_size=18)
        realWorldText.move_to(shadowLine.get_center() + DOWN)
        cgWorldText = Text("CG World", font_size=18)
        cgWorldText.move_to(shadowLine.get_center() + DOWN)

        self.play(rayCenter.animate.set_points_by_ends(start=rayCenter.get_start(),
                                                       end=rayCenter.get_end() + 1.5 * DOWN),
                  rayRight1.animate.set_points_by_ends(start=rayRight1.get_start(),
                                                       end=rayRight1.get_end() + 4 * DOWN),
                  rayRight2.animate.set_points_by_ends(start=rayRight2.get_start(),
                                                       end=rayRight2.get_end() + 4 * DOWN),
                  rayLeft1.animate.set_points_by_ends(start=rayLeft1.get_start(),
                                                      end=rayLeft1.get_end() + 4 * DOWN),
                  rayLeft2.animate.set_points_by_ends(start=rayLeft2.get_start(),
                                                      end=rayLeft2.get_end() + 4 * DOWN),
                  FadeIn(shadowLine),
                  FadeIn(realWorldText),
                  FadeIn(lightText)
                  )

        self.wait(2)

        self.play(FadeOut(realWorldText))

        rayStartPoint = surfaceLine.get_center()

        rayCenter.set_points_by_ends(start=rayStartPoint,
                                     end=rayStartPoint)
        rayRight1.set_points_by_ends(start=rayStartPoint + RIGHT,
                                     end=rayStartPoint + RIGHT)
        rayRight2.set_points_by_ends(start=rayStartPoint + 2 * RIGHT,
                                     end=rayStartPoint + 2 * RIGHT)
        rayLeft1.set_points_by_ends(start=rayStartPoint + LEFT,
                                    end=rayStartPoint + LEFT)
        rayLeft2.set_points_by_ends(start=rayStartPoint + 2 * LEFT,
                                    end=rayStartPoint + 2 * LEFT)

        hitDot = Dot()
        hitDot.set_fill(color=BLACK)
        hitDot.scale(1.1)
        hitDot.move_to(rayCenter.get_end() + 1 * UP)

        self.play(rayCenter.animate.set_points_by_ends(start=rayCenter.get_start(),
                                                       end=rayCenter.get_end() + 1 * UP),
                  rayRight1.animate.set_points_by_ends(start=rayRight1.get_start(),
                                                       end=rayRight1.get_end() + 4 * UP),
                  rayRight2.animate.set_points_by_ends(start=rayRight2.get_start(),
                                                       end=rayRight2.get_end() + 4 * UP),
                  rayLeft1.animate.set_points_by_ends(start=rayLeft1.get_start(),
                                                      end=rayLeft1.get_end() + 4 * UP),
                  rayLeft2.animate.set_points_by_ends(start=rayLeft2.get_start(),
                                                      end=rayLeft2.get_end() + 4 * UP),
                  FadeIn(cgWorldText),
                  )
        self.add(hitDot)

        # ray = Arrow()
        # ray.set_stroke(color=BLACK)
        # ray.set_fill(color=BLACK)
        # ray.set_points_by_ends(start=lightSrcDot.get_center(),
        #                        end=lightSrcDot.get_center())
        # self.play(ray.animate.set_points_by_ends(start=lightSrcDot.get_center(),
        #                                          end=intersectionDot.get_center()))
        #
        # self.add(intersectionDot)
        # self.add(intersectionMoveDot)
        # self.wait()
        #
        # shadowRay = Arrow()
        # shadowRay.set_fill(color=BLACK)
        # shadowRay.set_points_by_ends(start=intersectionDot.get_center(),
        #                              end=intersectionDot.get_center())
        # shadowRayText = Text("Shadow Ray", font_size=18)
        # shadowRayText.move_to(
        #     (intersectionDot.get_center() + ORIGIN) * 0.5 + RIGHT)
        #
        # self.play(
        #     shadowRay.animate.set_points_by_ends(start=intersectionDot.get_center(),
        #                                          end=ORIGIN), FadeIn(shadowRayText))
        # self.wait()
        # self.play(FadeOut(shadowRay), FadeOut(shadowRayText))
        # self.wait()
        # moveArrow = CurvedArrow(start_point=intersectionDot.get_center(),
        #                         end_point=0.3 * UP)
        # moveArrow.set_fill(BLACK)
        # moveArrow.set_stroke(BLACK)
        # displacePointText = Text("Displace by ε", font_size=18)
        # displacePointText.move_to(
        #     (intersectionDot.get_center() + ORIGIN) * 0.5 + 1.5 * RIGHT)
        # self.play(FadeIn(moveArrow), FadeIn(displacePointText))
        # self.play(intersectionMoveDot.shift, 1.3 * UP)
        # # self.play(moveArrow.animate.put_start_and_end_on(
        # #     start=intersectionDot.get_center(), end=0.3 * UP))
