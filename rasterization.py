from manimlib import *


class Rasterization(Scene):
    def sign(self, p1, p2, p3):
        return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])

    def PointInTriangle(self, pt, v1, v2, v3):
        d1 = self.sign(pt, v1, v2)
        d2 = self.sign(pt, v2, v3)
        d3 = self.sign(pt, v3, v1)
        has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
        has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)
        return not (has_neg and has_pos)

    def construct(self):
        triangle = Triangle()
        triangle.set_fill(GREEN, opacity=1.0)
        triangle.set_stroke(GREEN, width=0)
        triangle.stretch(2, 0)
        triangle.stretch(3, 1)
        self.add(triangle)
        squares = Group()
        coloredSquares = Group()
        for i in range(-20, 20):
            for j in range(-12, 12):
                square = Square()
                square.set_stroke(color=BLACK, width=2)
                square.set_width(FRAME_WIDTH / 60)
                square.set_height(FRAME_WIDTH / 60)
                square.shift(
                    np.array((i * square.get_width(), j * square.get_width(), 0.)))
                squares.add(square)
                if self.PointInTriangle(square.get_center(), triangle.get_vertices()[0],
                                        triangle.get_vertices()[1],
                                        triangle.get_vertices()[2]):
                    cSquare = square.deepcopy()
                    cSquare.set_fill(GREEN, opacity=1.0)
                    coloredSquares.add(cSquare)
        self.play(FadeIn(squares))
        self.wait(2)
        self.play(FadeOut(triangle), FadeIn(coloredSquares))
        self.wait(2)
