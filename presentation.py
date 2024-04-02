from manim import *
from manim_slides import Slide
from src.scenes.intro import intro
from src.scenes.slide1 import slide1
from src.scenes.slide2 import slide2


class Presentation(Slide):
    def construct(self):
        # INTRO
        intro(self)
        # SLIDE 1
        slide1(self)
        slide2(self)