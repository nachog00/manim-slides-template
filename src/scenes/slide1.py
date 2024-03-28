from manim_slides import Slide
from manim import *

def slide1(scene:Slide):
    scene.play(Write(Text("Slide 1")))
    scene.next_slide(notes="Don't forget to tell about this!!!!!")