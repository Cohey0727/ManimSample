from manim import *
import numpy as np
import random

class AbsoluteChaos(Scene):
    def construct(self):
        self.camera.background_color = BLACK
        
        # 瞬間爆発開始
        for _ in range(20):
            self.play(*[
                Flash(
                    [random.uniform(-8, 8), random.uniform(-4, 4), 0],
                    color=random.choice([RED, YELLOW, ORANGE, WHITE, BLUE, GREEN, PURPLE]),
                    flash_radius=random.uniform(2, 10),
                    num_lines=random.randint(30, 150)
                ) for _ in range(50)
            ], run_time=0.1)
        
        # 数字の暴走
        numbers = VGroup()
        for _ in range(200):
            num = Text(
                str(random.randint(0, 9)),
                font_size=random.randint(20, 200),
                color=random.choice([RED, BLUE, YELLOW, GREEN, PURPLE, ORANGE, PINK, TEAL, WHITE])
            )
            num.move_to([random.uniform(-8, 8), random.uniform(-4, 4), 0])
            numbers.add(num)
        
        self.play(*[FadeIn(n, scale=random.uniform(2, 10)) for n in numbers], run_time=0.2)
        
        # 超高速回転地獄
        for _ in range(30):
            self.play(
                *[n.animate
                  .rotate(random.uniform(-2*PI, 2*PI))
                  .move_to([random.uniform(-8, 8), random.uniform(-4, 4), 0])
                  .scale(random.uniform(0.5, 2))
                  .set_color(random.choice([RED, BLUE, YELLOW, GREEN, PURPLE, ORANGE, PINK, TEAL, WHITE]))
                  for n in numbers],
                run_time=0.05
            )
        
        # 巨大文字爆撃
        giant_chars = ["∞", "π", "e", "φ", "i", "Σ", "∫", "∇", "∂", "√"]
        for char in giant_chars:
            giant = Text(char, font_size=500, color=random.choice([RED, GOLD, WHITE, BLUE]))
            self.play(
                Write(giant),
                giant.animate.scale(10).set_opacity(0),
                *[Flash([random.uniform(-8, 8), random.uniform(-4, 4), 0],
                       color=random.choice([RED, YELLOW, WHITE]),
                       flash_radius=random.uniform(3, 8),
                       num_lines=random.randint(40, 100))
                  for _ in range(20)],
                run_time=0.1
            )
        
        # 全画面フラッシュ連打
        colors = [RED, BLUE, YELLOW, GREEN, PURPLE, ORANGE, PINK, WHITE, GOLD, TEAL]
        for color in colors * 3:
            rect = Rectangle(width=20, height=12, color=color, fill_opacity=0.8)
            self.play(FadeIn(rect), run_time=0.02)
            self.play(FadeOut(rect), run_time=0.02)
        
        # 数式の嵐
        formulas = VGroup()
        formula_texts = [
            "∞!", "π^π^π", "e^∞", "i^i^i^i", "0/0",
            "lim→∞", "∫∫∫", "∂^∞", "∇×∇", "Σ^∞"
        ]
        
        for _ in range(100):
            formula = Text(
                random.choice(formula_texts),
                font_size=random.randint(30, 150),
                color=random.choice([GOLD, WHITE, CYAN, PINK, RED])
            )
            formula.move_to([random.uniform(-8, 8), random.uniform(-4, 4), 0])
            formula.rotate(random.uniform(0, 2*PI))
            formulas.add(formula)
        
        self.play(*[Write(f) for f in formulas], run_time=0.3)
        
        # カオス回転
        for _ in range(10):
            self.play(
                Rotating(numbers, angle=PI, about_point=ORIGIN),
                Rotating(formulas, angle=-PI, about_point=ORIGIN),
                *[Flash(ORIGIN, color=random.choice(colors), 
                       flash_radius=random.uniform(5, 15),
                       num_lines=random.randint(50, 150))
                  for _ in range(30)],
                run_time=0.2
            )
        
        # 全てを中心に吸い込む
        everything = VGroup(numbers, formulas)
        self.play(
            everything.animate.move_to(ORIGIN).scale(0.001),
            *[Flash(ORIGIN, color=random.choice(colors),
                   flash_radius=i,
                   num_lines=200-i*10)
              for i in range(20)],
            run_time=0.5
        )
        
        # 最終究極爆発
        self.play(
            *[Flash(
                [random.uniform(-10, 10), random.uniform(-6, 6), 0],
                color=random.choice(colors),
                flash_radius=random.uniform(5, 20),
                num_lines=random.randint(100, 300)
            ) for _ in range(200)],
            run_time=0.3
        )
        
        # 狂気の終焉
        end = Text("爆", font_size=1000, color=RED, weight=BOLD)
        self.play(
            GrowFromCenter(end),
            *[Flash(ORIGIN, color=RED, flash_radius=30-i, num_lines=300-i*10)
              for i in range(30)],
            run_time=0.5
        )
        
        self.play(
            end.animate.scale(100).set_opacity(0),
            run_time=0.2
        )