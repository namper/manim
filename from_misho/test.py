from manimlib.imports import *


class TestScene(Scene):
    def construct(self):
        t = TextMobject(
            "$ \\displaystyle  \\int_{c} Pdx + Qdy = \\iint\limits_D (Q_x - P_y) dxdy$",
        )

        self.play(Write(t))
        self.wait()
