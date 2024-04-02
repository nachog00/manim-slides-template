from src.scenes.intro import intro
from manim_slides import Slide
import subprocess

class TestClass(Slide):

    def construct(self):
        intro(self)

if __name__ == "__main__":
    proccess = subprocess.run(["manim", "render", "driver.py", "-ql", "TestClass"])
    # proccess = subprocess.run(["manim-slides", "convert", "TestClass" , "_site/test.html"])
    