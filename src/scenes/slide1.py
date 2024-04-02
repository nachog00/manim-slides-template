from manim_slides import Slide
from manim import *

def slide1(scene:Slide):
    slide_title = Text("Slide 1")
    scene.play(Write(slide_title))
    scene.next_slide(notes="Don't forget to tell about this!!!!!")
    scene.play(slide_title.animate.scale(0.5).to_edge(UP))
    
    header = scene.canvas["header"]
    content = VGroup().next_to(header, DOWN)
    
    content.add(Circle(color=BLUE))
    content.add(Circle(color=RED))
    content.add(Circle(color=GREEN))
    content.arrange(RIGHT, buff=2)
    
    
    scene.add(content)
    scene.play(Write(content))
    
    scene.next_slide()
    
    # scene.wipe()