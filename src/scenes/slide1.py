from manim_slides import Slide
from manim import *

def slide1(scene:Slide):
    slide_title = Text("Slide 1")
    scene.play(Write(slide_title))
    scene.next_slide(notes="Don't forget to tell about this!!!!!")
    scene.play(slide_title.animate.scale(0.5).to_edge(UP))