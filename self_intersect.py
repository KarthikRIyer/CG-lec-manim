from manimlib import *


class SelfIntersect(Scene):

    def construct(self):
        intersectionDot = Dot()
        intersectionDot.set_fill(RED)
        intersectionDot.shift(DOWN)
        intersectionMoveDot = Dot()
        intersectionMoveDot.set_fill(RED)
        intersectionMoveDot.shift(DOWN)

        lightSrcDot = Dot()
        lightSrcDot.set_fill(YELLOW)
        lightSrcDot.shift(3 * UP + 3 * LEFT)
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
        lightSrcText = Text("Light Src", font_size=18)
        lightSrcText.move_to(lightSrcDot.get_center() + 0.5 * UP)

        surfaceLine = Line(5 * LEFT, 5 * RIGHT)
        surfaceText = Text("Surface", font_size=24)
        VGroup(surfaceLine, surfaceText).arrange(RIGHT, buff=0.5)
        self.play(ShowCreation(surfaceLine), ShowCreation(lightSrcDot),
                  ShowCreation(lightSrcGlare1), ShowCreation(lightSrcGlare2),
                  ShowCreation(lightSrcGlare3), ShowCreation(lightSrcGlare4))
        self.play(FadeIn(surfaceText), FadeIn(lightSrcText))

        ray = Arrow()
        ray.set_stroke(color=BLACK)
        ray.set_fill(color=BLACK)
        ray.set_points_by_ends(start=lightSrcDot.get_center(),
                               end=lightSrcDot.get_center())
        self.play(ray.animate.set_points_by_ends(start=lightSrcDot.get_center(),
                                                 end=intersectionDot.get_center()))

        self.add(intersectionDot)
        self.add(intersectionMoveDot)
        self.wait()

        shadowRay = Arrow()
        shadowRay.set_fill(color=BLACK)
        shadowRay.set_points_by_ends(start=intersectionDot.get_center(),
                                     end=intersectionDot.get_center())
        shadowRayText = Text("Shadow Ray", font_size=18)
        shadowRayText.move_to(
            (intersectionDot.get_center() + ORIGIN) * 0.5 + RIGHT)

        self.play(
            shadowRay.animate.set_points_by_ends(start=intersectionDot.get_center(),
                                                 end=ORIGIN), FadeIn(shadowRayText))
        self.wait()
        self.play(FadeOut(shadowRay), FadeOut(shadowRayText))
        self.wait()
        moveArrow = CurvedArrow(start_point=intersectionDot.get_center(),
                                end_point=0.3 * UP)
        moveArrow.set_fill(BLACK)
        moveArrow.set_stroke(BLACK)
        displacePointText = Text("Displace by ε", font_size=18)
        displacePointText.move_to(
            (intersectionDot.get_center() + ORIGIN) * 0.5 + 1.5 * RIGHT)
        self.play(FadeIn(moveArrow), FadeIn(displacePointText))
        self.play(intersectionMoveDot.shift, 1.3 * UP)
        # self.play(moveArrow.animate.put_start_and_end_on(
        #     start=intersectionDot.get_center(), end=0.3 * UP))
