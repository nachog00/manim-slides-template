from manim import *
from manim_slides import Slide
from ..constants import FONT_SIZES, STYLE, PRESENTATION_DETAILS


def intro(scene: Slide):

    pulsing_dot = Dot(color=RED)
    scene.play(Create(pulsing_dot))
    scene.next_slide(loop=True)
    scene.play(Indicate(pulsing_dot, scale_factor=2, color=BLUE, run_time=1.5))
    scene.next_slide()

    initials = Text("IG", font_size=FONT_SIZES["TITLE"], color=BLUE)
    circle = Circle(color=BLUE, radius=0.5).move_to(initials)
    logo = VGroup(pulsing_dot, initials, circle)
    scene.play(Transform(pulsing_dot, initials))
    scene.play(DrawBorderThenFill(circle))

    scene.wait(0.5)
    # move logo to upper right corner
    scene.play(logo.animate.scale(0.5).to_corner(UL))

    module_name = Text(
        PRESENTATION_DETAILS["MODULE_NAME"],
        font_size=FONT_SIZES["TITLE"],
        # font=STYLE["FONT_FAMILY"],
    )
    module_code = Text(
        PRESENTATION_DETAILS["MODULE_CODE"],
        font_size=FONT_SIZES["SUBTITLE"],
        # font=STYLE["FONT_FAMILY"],
    ).next_to(module_name, DOWN)

    header_right = VGroup(module_name, module_code)
    scene.add_to_canvas(header_right=header_right)
    scene.play(Write(module_name), Write(module_code))
    scene.next_slide()
    scene.play(header_right.animate.scale(0.4).to_corner(UR))

    title = Text(
        PRESENTATION_DETAILS["TITLE"],
        font_size=FONT_SIZES["TITLE"],
        # font=STYLE["FONT_FAMILY"],
    )
    subtitle = Text(
        PRESENTATION_DETAILS["SUBTITLE"],
        font_size=FONT_SIZES["SUBTITLE"],
        # font=STYLE["FONT_FAMILY"],
    ).next_to(title, DOWN)

    header_left = VGroup(title, subtitle)
    scene.add_to_canvas(header_left=header_left)
    scene.play(Write(title), Write(subtitle))
    scene.next_slide()
    scene.play(header_left.animate.scale(0.4).next_to(logo, RIGHT, buff=0.2))

    header = VGroup(logo, header_left, header_right)

    header.save_state()
    scene.play(header.animate.set_opacity(0.5))


class TestScene(Slide):
    def construct(self):
        intro(self)


if __name__ == "__main__":
    subprocess.RUN(["manim", "-p", "ql", "src/slides/intro.py", "TestScene"])
