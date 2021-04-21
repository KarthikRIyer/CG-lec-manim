from manimlib import *


class RayTriangle(Scene):

    def construct(self):
        to_isolate = ["P", "O", "+", "t", "R", "A", "B", "C", "D",
                      "x", "y", "z", "0", "*", "(", ")", "\over"]
        lines = VGroup(
            Tex("P = O + tR", isolate=to_isolate),
            Tex("Ax + By + Cz + D = 0", isolate=to_isolate),
            Tex("A * P_x  + B * P_y + C * P_z + D = 0", isolate=to_isolate),
            Tex("A * (O_x + tR_x) + B * (O_y + tR_y) + C * (O_z + tR_z) + D = 0",
                isolate=to_isolate),
            Tex(
                "t = -{{{ A * O_x + B * O_y + C * O_z + D }} \over {{ A * R_x + B * R_y + C * R_z }}}",
                isolate=to_isolate)
        )
        lines.arrange(DOWN, buff=LARGE_BUFF)
        for line in lines:
            line.set_color_by_tex_to_color_map({
                "P": BLUE_E,
                "O": TEAL_E,
                "R": GREEN_E,
                "A": BLUE,
                "B": TEAL,
                "C": GREEN,
                "D": DARK_BROWN,
                "x": RED_E,
                "y": RED_E,
                "z": RED_E,
                "t": YELLOW_E,
                "*": LIGHT_PINK,
                "+": LIGHT_PINK,
                "(": LIGHT_PINK,
                ")": LIGHT_PINK,
                "-": LIGHT_PINK,
                "=": PINK,
                "0": LIGHT_BROWN,
                "\over": LIGHT_BROWN
            })
        self.play(FadeIn(lines[0]), FadeIn(lines[1]))
        play_kw = {"run_time": 2}
        self.play(
            TransformMatchingTex(
                lines[1].copy(), lines[2],
                path_arc=90 * DEGREES,
            ),
            **play_kw
        )
        self.wait()
        self.play(
            TransformMatchingTex(
                lines[2].copy(), lines[3],
                path_arc=90 * DEGREES,
            ),
            **play_kw
        )
        self.wait()
        self.play(
            TransformMatchingTex(
                lines[3].copy(), lines[4],
                path_arc=90 * DEGREES,
            ),
            **play_kw
        )
        self.wait()
