from manim import *
import numpy as np

class MathematicalSymphony(Scene):
    def construct(self):
        # タイトル
        title = Text("Mathematical Symphony", font_size=48, color=GOLD)
        subtitle = Text("A Visual Journey Through Mathematics", font_size=24, color=BLUE)
        subtitle.next_to(title, DOWN, buff=0.5)
        
        self.play(Write(title), Write(subtitle))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(subtitle))
        
        # Part 1: フーリエ級数による円の描画
        self.fourier_epicycles()
        
        # Part 2: 複素平面での変換
        self.complex_transformations()
        
        # Part 3: 3Dフラクタル
        self.fractal_patterns()
        
        # Part 4: 微分方程式の可視化
        self.differential_flow()
        
        # フィナーレ
        self.finale()

    def fourier_epicycles(self):
        # フーリエ級数でハートを描く
        def heart_function(t):
            x = 16 * np.sin(t)**3
            y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
            return np.array([x/20, y/20, 0])
        
        # エピサイクル（円周上を回る円）を作成
        epicycles = VGroup()
        num_epicycles = 8
        
        for i in range(num_epicycles):
            radius = 1 / (2*i + 1)
            circle = Circle(radius=radius, color=BLUE, stroke_width=2)
            dot = Dot(color=RED, radius=0.05)
            line = Line(ORIGIN, RIGHT * radius, color=YELLOW, stroke_width=1)
            
            epicycle = VGroup(circle, dot, line)
            epicycles.add(epicycle)
        
        title = Text("Fourier Epicycles", font_size=36, color=GOLD)
        title.to_edge(UP)
        
        self.play(Write(title))
        self.play(Create(epicycles))
        
        # アニメーション: エピサイクルが回転してハートを描く
        path = VMobject()
        path.set_color(PINK)
        
        def update_path(mob, alpha):
            # 複雑なフーリエ級数計算をシンプルに
            point = heart_function(alpha * 2 * PI)
            if hasattr(mob, 'points') and len(mob.points) > 0:
                mob.add_line_to(point)
            else:
                mob.start_new_path(point)
        
        self.play(
            UpdateFromAlphaFunc(path, update_path),
            *[Rotating(epi, angle=2*PI*(i+1), run_time=4) for i, epi in enumerate(epicycles)],
            run_time=4
        )
        
        self.wait(1)
        self.play(FadeOut(epicycles), FadeOut(title), FadeOut(path))

    def complex_transformations(self):
        title = Text("Complex Transformations", font_size=36, color=GOLD)
        title.to_edge(UP)
        
        # 複素数平面のグリッド
        grid = ComplexPlane(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            background_line_style={
                "stroke_color": BLUE,
                "stroke_width": 2,
                "stroke_opacity": 0.6,
            }
        )
        
        # 複素数の点群
        points = VGroup(*[
            Dot(grid.n2p(complex(x, y)), color=interpolate_color(RED, YELLOW, (x+y)/8), radius=0.05)
            for x in range(-2, 3) for y in range(-2, 3)
        ])
        
        self.play(Write(title))
        self.play(Create(grid), Create(points))
        
        # 変換: z → z²
        def square_transform(point):
            z = grid.p2n(point.get_center())
            z_squared = z ** 2
            return grid.n2p(z_squared)
        
        self.play(
            *[point.animate.move_to(square_transform(point)) for point in points],
            run_time=3
        )
        self.wait(1)
        
        # 変換: z → e^z
        def exp_transform(point):
            z = grid.p2n(point.get_center())
            z_exp = np.exp(z)
            if abs(z_exp) < 10:  # 発散を防ぐ
                return grid.n2p(z_exp)
            return point.get_center()
        
        self.play(
            *[point.animate.move_to(exp_transform(point)) for point in points],
            run_time=3
        )
        
        self.wait(1)
        self.play(FadeOut(grid), FadeOut(points), FadeOut(title))

    def fractal_patterns(self):
        title = Text("Fractal Geometry", font_size=36, color=GOLD)
        title.to_edge(UP)
        
        # シェルピンスキの三角形を生成
        def sierpinski_triangle(depth, size=4, position=ORIGIN):
            if depth == 0:
                triangle = Polygon(
                    position + UP * size / 2,
                    position + DOWN * size / 2 + LEFT * size / 2,
                    position + DOWN * size / 2 + RIGHT * size / 2,
                    fill_color=interpolate_color(BLUE, RED, depth/5),
                    fill_opacity=0.7,
                    stroke_color=WHITE,
                    stroke_width=1
                )
                return VGroup(triangle)
            
            triangles = VGroup()
            new_size = size / 2
            
            # 上の三角形
            triangles.add(*sierpinski_triangle(depth-1, new_size, position + UP * new_size / 2))
            # 左下の三角形
            triangles.add(*sierpinski_triangle(depth-1, new_size, position + DOWN * new_size / 2 + LEFT * new_size / 2))
            # 右下の三角形
            triangles.add(*sierpinski_triangle(depth-1, new_size, position + DOWN * new_size / 2 + RIGHT * new_size / 2))
            
            return triangles
        
        self.play(Write(title))
        
        # 段階的にフラクタルを構築
        for depth in range(5):
            fractal = sierpinski_triangle(depth)
            if depth == 0:
                self.play(Create(fractal))
            else:
                self.play(Transform(previous_fractal, fractal))
            previous_fractal = fractal
            self.wait(0.5)
        
        # 回転とスケーリング
        self.play(
            Rotating(fractal, angle=2*PI, run_time=4),
            fractal.animate.scale(1.5),
        )
        
        self.wait(1)
        self.play(FadeOut(fractal), FadeOut(title))

    def differential_flow(self):
        title = Text("Vector Field Flow", font_size=36, color=GOLD)
        title.to_edge(UP)
        
        # ベクトル場の定義 (渦状の流れ)
        def vector_field_func(point):
            x, y, _ = point
            return np.array([-y + 0.1*x, x + 0.1*y, 0])
        
        # ベクトル場を作成
        vector_field = ArrowVectorField(
            vector_field_func,
            x_range=[-3, 3, 0.5],
            y_range=[-3, 3, 0.5],
            colors=[BLUE, GREEN, YELLOW, RED],
            vector_config={"stroke_width": 2}
        )
        
        # 流線上を移動する粒子
        particles = VGroup(*[
            Dot(radius=0.03, color=interpolate_color(PINK, ORANGE, i/10))
            for i in range(20)
        ])
        
        # 粒子を円周上に配置
        for i, particle in enumerate(particles):
            angle = i * 2 * PI / 20
            particle.move_to([2 * np.cos(angle), 2 * np.sin(angle), 0])
        
        self.play(Write(title))
        self.play(Create(vector_field))
        self.play(Create(particles))
        
        # 粒子がベクトル場に沿って流れる
        def update_particle(particle, dt):
            velocity = vector_field_func(particle.get_center())
            particle.shift(velocity * dt * 0.5)
        
        for particle in particles:
            particle.add_updater(update_particle)
        
        self.wait(8)
        
        for particle in particles:
            particle.clear_updaters()
        
        self.play(FadeOut(vector_field), FadeOut(particles), FadeOut(title))

    def finale(self):
        # 全ての要素を組み合わせたフィナーレ
        finale_text = Text("Mathematics: The Language of the Universe", 
                          font_size=32, color=GOLD)
        finale_text.to_edge(DOWN)
        
        # 複数の数学要素を同時に表示
        circle = Circle(radius=2, color=BLUE)
        square = Square(side_length=3, color=RED).rotate(PI/4)
        triangle = Triangle(color=GREEN).scale(2)
        
        # 黄金比の螺旋
        golden_spiral = ParametricFunction(
            lambda t: np.array([
                np.exp(t * 0.1) * np.cos(t),
                np.exp(t * 0.1) * np.sin(t),
                0
            ]),
            t_range=[0, 4*PI],
            color=GOLD,
            stroke_width=4
        )
        
        shapes = VGroup(circle, square, triangle)
        
        self.play(Write(finale_text))
        self.play(Create(shapes))
        self.play(Create(golden_spiral))
        
        # 最終的な変換とフェードアウト
        self.play(
            *[shape.animate.scale(2).set_opacity(0.3) for shape in shapes],
            golden_spiral.animate.scale(1.5).set_opacity(0.8),
            run_time=3
        )
        
        # 全てを美しくフェードアウト
        everything = VGroup(finale_text, shapes, golden_spiral)
        self.play(
            everything.animate.scale(0.1).set_opacity(0),
            run_time=2
        )
        
        # 最後のメッセージ
        final_message = Text("Created with Manim & uv", font_size=24, color=WHITE)
        self.play(Write(final_message))
        self.wait(2)
        self.play(FadeOut(final_message))