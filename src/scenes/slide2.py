from manim_slides import Slide
from manim import *

def slide2(scene:Slide):
    slide_title = Text("Slide 2")
    scene.play(Write(slide_title))
    scene.next_slide(notes="Don't forget to tell about this!!!!!")
    scene.play(slide_title.animate.scale(0.5).to_edge(UP))
    
    header = scene.canvas["header"]
    content = VGroup().next_to(header, DOWN)
    
    content.add(Square(color=BLUE))
    content.add(Square(color=RED))
    content.add(Square(color=GREEN))
    content.arrange(RIGHT, buff=2)
    
    scene.add(content)
    scene.play(Write(content))
    
    scene.next_slide()
    
    # scene.wipe()