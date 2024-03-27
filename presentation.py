from manim import *
from manim_slides import Slide
from src.slides.intro import intro
from src.slides.slide1 import slide1


class Presentation(Slide):
    def construct(self):
        # INTRO
        intro(self)
        # SLIDE 1
        slide1(self)