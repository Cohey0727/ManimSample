from manim import *
import numpy as np

class NuclearExplosion(Scene):
    def construct(self):
        self.camera.background_color = BLACK
        
        # 画面全体フラッシュ爆発を1000回
        for i in range(1000):
            color = interpolate_color(RED, WHITE, (i % 100) / 100)
            self.add(Flash(ORIGIN, color=color, flash_radius=20, num_lines=200))
            self.wait(0.001)
            self.remove(*self.mobjects)
        
        # 終