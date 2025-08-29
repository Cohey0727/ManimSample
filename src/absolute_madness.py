from manim import *
import numpy as np
import random

class AbsoluteMadness(Scene):
    def construct(self):
        self.camera.background_color = BLACK
        
        # 画面全体を震わせる
        def shake_camera():
            self.camera.frame.shift(np.array([random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5), 0]))
            
        # 1000個のオブジェクトを同時生成
        chaos_objects = VGroup()
        for _ in range(1000):
            obj_type = random.choice([Circle, Square, Triangle, Star])
            obj = obj_type(
                radius=random.uniform(0.01, 0.3),
                color=random.choice([RED, BLUE, YELLOW, GREEN, PURPLE, ORANGE, PINK, TEAL]),
                fill_opacity=random.uniform(0.3, 1)
            )
            obj.move_to([
                random.uniform(-10, 10),
                random.uniform(-6, 6),
                0
            ])
            obj.rotate(random.uniform(0, 2*PI))
            chaos_objects.add(obj)
        
        # 全てを0.1秒で投入
        self.play(
            *[GrowFromCenter(obj) for obj in chaos_objects[:100]],
            run_time=0.1
        )
        
        # 狂気の回転と色変更を50回
        for i in range(50):
            shake_camera()
            animations = []
            for obj in chaos_objects[:100]:
                animations.append(
                    obj.animate
                    .rotate(random.uniform(-PI, PI))
                    .scale(random.uniform(0.5, 2))
                    .set_color(random.choice([RED, BLUE, YELLOW, GREEN, PURPLE, ORANGE, PINK, TEAL]))
                    .move_to([
                        random.uniform(-10, 10),
                        random.uniform(-6, 6),
                        0
                    ])
                )
            
            # 100個のFlashを同時発生
            flashes = []
            for _ in range(100):
                flashes.append(
                    Flash(
                        [random.uniform(-8, 8), random.uniform(-4, 4), 0],
                        color=random.choice([RED, BLUE, YELLOW, GREEN, PURPLE, WHITE, GOLD]),
                        flash_radius=random.uniform(0.5, 3),
                        num_lines=random.randint(10, 50)
                    )
                )
            
            self.play(
                *animations,
                *flashes,
                run_time=0.05
            )
        
        # 巨大文字の乱れ打ち
        for _ in range(30):
            text = Text(
                random.choice(["爆", "炸", "轟", "烈", "激", "狂", "乱", "破", "砕", "滅"]),
                font_size=random.randint(100, 300),
                color=random.choice([RED, YELLOW, ORANGE, WHITE]),
                weight=BOLD
            )
            text.move_to([
                random.uniform(-6, 6),
                random.uniform(-3, 3),
                0
            ])
            text.rotate(random.uniform(-PI/4, PI/4))
            
            self.play(
                Write(text),
                text.animate.scale(random.uniform(5, 10)).set_opacity(0),
                Flash(text.get_center(), color=random.choice([RED, YELLOW, WHITE]), 
                      flash_radius=random.uniform(5, 15), num_lines=random.randint(50, 150)),
                run_time=0.1
            )
        
        # 数式の暴走
        formulas = [
            "∞^∞^∞",
            "π!!!!",
            "e^(e^(e^e))",
            "∇×∇×∇",
            "∫∫∫∫∫",
            "Σ^∞_∞",
            "∂^n/∂x^n",
            "lim_{x→∞}",
            "∏∏∏",
            "√√√√√"
        ]
        
        formula_objects = VGroup()
        for formula in formulas:
            for _ in range(10):
                f = Text(formula, font_size=random.randint(30, 150), 
                        color=random.choice([GOLD, WHITE, CYAN, PINK]))
                f.move_to([
                    random.uniform(-8, 8),
                    random.uniform(-4, 4),
                    0
                ])
                formula_objects.add(f)
        
        self.play(
            *[Write(f) for f in formula_objects],
            run_time=0.5
        )
        
        # 全てが回転しながら中心に収束
        self.play(
            *[obj.animate.move_to(ORIGIN).rotate(10*PI).scale(0.01) for obj in chaos_objects[:100]],
            *[f.animate.move_to(ORIGIN).rotate(10*PI).scale(0.01) for f in formula_objects],
            run_time=1
        )
        
        # 最終大爆発 - 500個のFlash同時発火
        mega_flashes = []
        for _ in range(500):
            mega_flashes.append(
                Flash(
                    ORIGIN,
                    color=random.choice([RED, BLUE, YELLOW, GREEN, PURPLE, WHITE, GOLD, ORANGE, PINK]),
                    flash_radius=random.uniform(1, 30),
                    num_lines=random.randint(10, 200)
                )
            )
        
        self.play(
            *mega_flashes,
            run_time=0.5
        )
        
        # 画面全体を白で塗りつぶす
        white_screen = Rectangle(width=30, height=20, color=WHITE, fill_opacity=1)
        self.play(
            FadeIn(white_screen),
            run_time=0.1
        )
        
        # 超巨大END
        end_text = Text("終", font_size=500, color=BLACK, weight=BOLD)
        self.play(
            Write(end_text),
            run_time=0.2
        )
        
        # ENDも爆発
        self.play(
            end_text.animate.scale(50).set_opacity(0),
            FadeOut(white_screen),
            *[Flash(
                [random.uniform(-10, 10), random.uniform(-6, 6), 0],
                color=BLACK,
                flash_radius=random.uniform(5, 20),
                num_lines=random.randint(50, 150)
            ) for _ in range(100)],
            run_time=0.5
        )