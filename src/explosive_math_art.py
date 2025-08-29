from manim import *
import numpy as np
from math import *

class ExplosiveMathArt(Scene):
    def construct(self):
        # 超ド派手なオープニング！
        self.explosive_opening()
        
        # パート1: カラフル爆発フラクタル
        self.explosive_fractals()
        
        # パート2: ダンシング・マセマティクス
        self.dancing_mathematics()
        
        # パート3: 宇宙的変身シーン
        self.cosmic_transformation()
        
        # パート4: 究極フィナーレ
        self.ultimate_finale()

    def explosive_opening(self):
        # 画面全体が虹色に爆発！
        explosion_circles = VGroup(*[
            Circle(radius=0.1, color=color, fill_opacity=0.8, stroke_width=0)
            for color in [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE, PINK] * 20
        ])
        
        for i, circle in enumerate(explosion_circles):
            angle = i * 2 * PI / len(explosion_circles)
            circle.move_to(ORIGIN)
        
        # タイトルが劇的に登場
        title = Text("🎆 EXPLOSIVE MATH ART 🎆", font_size=40, color=GOLD)
        title.set_stroke(WHITE, width=3)
        
        # 爆発アニメーション！
        self.add(explosion_circles)
        self.play(
            *[circle.animate.scale(50).set_opacity(0).move_to([
                10 * cos(i * 2 * PI / len(explosion_circles)),
                10 * sin(i * 2 * PI / len(explosion_circles)),
                0
            ]) for i, circle in enumerate(explosion_circles)],
            run_time=2
        )
        
        # タイトル登場と同時に虹色パルス
        self.play(
            Write(title),
            *[Flash(title, color=color, flash_radius=3) for color in [RED, GREEN, BLUE]],
            run_time=2
        )
        self.wait(1)
        self.play(title.animate.scale(0.1).set_opacity(0))

    def explosive_fractals(self):
        # マンデルブロ集合風の爆発的フラクタル
        def mandelbrot_color(c, max_iter=50):
            z = 0
            for n in range(max_iter):
                if abs(z) > 2:
                    # カラフルな色付け
                    colors = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE, PINK]
                    return colors[n % len(colors)]
                z = z*z + c
            return BLACK

        # フラクタルパーティクル群
        particles = VGroup()
        for x in np.linspace(-2, 2, 30):
            for y in np.linspace(-2, 2, 30):
                c = complex(x, y)
                color = mandelbrot_color(c)
                if color != BLACK:
                    dot = Dot(
                        point=[x, y, 0],
                        color=color,
                        radius=0.05
                    )
                    particles.add(dot)
        
        # 爆発的登場
        self.play(
            *[FadeIn(dot, scale=10) for dot in particles[:50]],  # 最初の50個
            run_time=2
        )
        
        # パーティクルが踊り狂う！
        self.play(
            *[dot.animate.shift([
                2 * sin(i * 0.5),
                2 * cos(i * 0.3),
                0
            ]).set_color(interpolate_color(RED, BLUE, sin(i)))
            for i, dot in enumerate(particles[:50])],
            run_time=3
        )
        
        # 消失エフェクト
        self.play(
            *[FadeOut(dot, scale=0.1) for dot in particles[:50]],
            run_time=1
        )

    def dancing_mathematics(self):
        # 数式が踊る！
        formulas = VGroup(
            Text("∫ e^(ix) dx = -ie^(ix)", color=PINK),
            Text("∇²φ = 4πGρ", color=CYAN),
            Text("E = mc²", color=YELLOW),
            Text("∂²u/∂t² = c²∇²u", color=GREEN),
            Text("ℏ ∂ψ/∂t = Ĥψ", color=PURPLE),
        )
        
        # 円形に配置
        for i, formula in enumerate(formulas):
            angle = i * 2 * PI / len(formulas)
            formula.move_to([3 * cos(angle), 3 * sin(angle), 0])
            formula.scale(0.8)
        
        # 劇的登場
        self.play(
            *[FadeIn(formula, shift=DOWN*3, scale=3) for formula in formulas],
            run_time=2
        )
        
        # 数式が回転しながら色が変わる
        for _ in range(3):
            self.play(
                Rotating(formulas, angle=2*PI/3, about_point=ORIGIN),
                *[formula.animate.set_color(
                    interpolate_color(RED, BLUE, sin(i + _))
                ) for i, formula in enumerate(formulas)],
                run_time=2
            )
        
        # 中央に集合して消失
        self.play(
            *[formula.animate.move_to(ORIGIN).scale(0.1).set_opacity(0) 
              for formula in formulas],
            run_time=2
        )

    def cosmic_transformation(self):
        # 宇宙的スケールの変換アニメーション
        
        # 銀河の螺旋
        def galaxy_spiral(t, arm=0):
            r = t * 0.5
            theta = t * 2 + arm * 2*PI/3
            return np.array([
                r * cos(theta),
                r * sin(theta),
                0
            ])
        
        # 3本の螺旋腕
        galaxies = VGroup()
        for arm in range(3):
            spiral = ParametricFunction(
                lambda t: galaxy_spiral(t, arm),
                t_range=[0, 10],
                color=interpolate_color(BLUE, PINK, arm/2),
                stroke_width=8
            )
            galaxies.add(spiral)
        
        # 星のパーティクル
        stars = VGroup(*[
            Dot(
                point=[4*cos(i*0.7), 4*sin(i*0.7), 0],
                color=interpolate_color(WHITE, YELLOW, sin(i)),
                radius=0.03
            )
            for i in range(100)
        ])
        
        # 宇宙の創生！
        self.play(
            *[Create(spiral) for spiral in galaxies],
            run_time=3
        )
        
        self.play(
            *[FadeIn(star, scale=20) for star in stars[:30]],
            run_time=2
        )
        
        # 全てが回転・拡大・縮小を繰り返す
        cosmic_group = VGroup(galaxies, stars)
        self.play(
            Rotating(cosmic_group, angle=4*PI),
            cosmic_group.animate.scale(2).set_opacity(0.7),
            run_time=4
        )
        
        # 超新星爆発エフェクト！
        explosion_flashes = VGroup(*[
            Flash(ORIGIN, color=color, flash_radius=8, num_lines=20)
            for color in [WHITE, YELLOW, ORANGE, RED] * 5
        ])
        
        self.play(
            *[flash for flash in explosion_flashes],
            cosmic_group.animate.scale(0.01).set_opacity(0),
            run_time=2
        )

    def ultimate_finale(self):
        # 究極のフィナーレ - 全ての要素を同時に！
        
        # 虹色の背景グラデーション
        background = Rectangle(width=20, height=20, fill_opacity=0.3)
        background.set_color([RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE])
        self.add(background)
        
        # 最終メッセージ
        messages = [
            Text("MATHEMATICS", font_size=60, color=GOLD),
            Text("IS", font_size=40, color=CYAN),
            Text("BEAUTIFUL", font_size=80, color=PINK),
            Text("& EXPLOSIVE!", font_size=50, color=RED),
        ]
        
        for i, msg in enumerate(messages):
            msg.set_stroke(WHITE, width=3)
            msg.move_to([0, 2-i*1.2, 0])
        
        # 爆発的な登場とパーティクル効果
        particles = VGroup(*[
            Dot(
                point=[8*cos(i*0.3), 8*sin(i*0.3), 0],
                color=interpolate_color(RED, BLUE, sin(i*0.5)),
                radius=0.1
            )
            for i in range(200)
        ])
        
        # 全てが同時に起こる大フィナーレ！
        self.play(
            *[Write(msg) for msg in messages],
            *[FadeIn(p, scale=5) for p in particles[::5]],  # 一部のパーティクル
            Flash(ORIGIN, color=WHITE, flash_radius=15, num_lines=50),
            Flash(ORIGIN, color=GOLD, flash_radius=10, num_lines=30),
            Flash(ORIGIN, color=PINK, flash_radius=8, num_lines=25),
            run_time=3
        )
        
        # 最終的なカオス！全部が動く
        all_objects = VGroup(*messages, *particles)
        self.play(
            Rotating(all_objects, angle=4*PI),
            *[obj.animate.set_color(
                interpolate_color(RED, BLUE, sin(i*0.7))
            ).scale(1 + 0.5*sin(i*0.5)) for i, obj in enumerate(all_objects)],
            run_time=5
        )
        
        # 美しいフェードアウト
        self.play(
            *[FadeOut(obj, scale=0.1) for obj in all_objects],
            FadeOut(background),
            run_time=3
        )
        
        # 最後の一言
        final_text = Text("Created with 🔥 Passion & ⚡ Manim", 
                         font_size=36, color=WHITE)
        self.play(Write(final_text))
        self.wait(2)
        self.play(FadeOut(final_text))