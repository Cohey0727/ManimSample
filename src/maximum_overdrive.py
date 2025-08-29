from manim import *
import numpy as np

class MaximumOverdrive(Scene):
    def construct(self):
        self.camera.background_color = BLACK
        
        # 1秒で1000個のオブジェクトを爆発的に生成
        for frame in range(60):  # 1秒 = 60フレーム
            # 各フレームで20個のFlash
            self.play(*[
                Flash(
                    [np.random.uniform(-8, 8), np.random.uniform(-4, 4), 0],
                    color=np.random.choice([RED, YELLOW, ORANGE, WHITE, BLUE, GREEN, PURPLE, GOLD, PINK]),
                    flash_radius=np.random.uniform(1, 10),
                    num_lines=np.random.randint(20, 100)
                ) for _ in range(20)
            ], run_time=0.016)  # 1/60秒
        
        self.wait(0.01)