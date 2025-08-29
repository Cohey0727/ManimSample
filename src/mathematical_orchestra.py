from manim import *
import numpy as np
from math import *

class MathematicalOrchestra(Scene):
    def construct(self):
        # 🎼 序曲: 指揮者登場
        self.conductor_entrance()
        
        # 🎵 第1楽章: 調和の数列（ハーモニック・セリーズ）
        self.first_movement_harmonic_series()
        
        # 🎶 第2楽章: フーリエの舞踏会
        self.second_movement_fourier_dance()
        
        # 🎵 第3楽章: フラクタルの狂詩曲
        self.third_movement_fractal_rhapsody()
        
        # 🎼 第4楽章: 黄金比のワルツ
        self.fourth_movement_golden_waltz()
        
        # 🔥 グランドフィナーレ: 宇宙の大合唱
        self.grand_finale_cosmic_chorus()

    def conductor_entrance(self):
        # ステージライト
        spotlight = Circle(radius=8, fill_color=YELLOW, fill_opacity=0.1, stroke_width=0)
        self.play(FadeIn(spotlight), run_time=2)
        
        # 指揮者（指揮棒）
        conductor_stick = Line(ORIGIN, UP*2, color=GOLD, stroke_width=8)
        conductor_hand = Circle(radius=0.3, color=PINK, fill_opacity=1)
        conductor_hand.move_to(conductor_stick.get_end())
        conductor = VGroup(conductor_stick, conductor_hand)
        
        # ドラマティック登場
        self.play(
            GrowFromCenter(conductor),
            Flash(ORIGIN, color=GOLD, flash_radius=5, num_lines=30),
            run_time=2
        )
        
        # オーケストラ・タイトル
        title = Text("🎼 MATHEMATICAL ORCHESTRA 🎼", font_size=40, color=GOLD)
        title.set_stroke(WHITE, width=2)
        title.to_edge(UP)
        
        self.play(Write(title), conductor.animate.scale(0.5).to_corner(UR))
        self.wait(1)
        self.play(FadeOut(title), FadeOut(spotlight))

    def first_movement_harmonic_series(self):
        # 第1楽章のタイトル
        movement_title = Text("第1楽章: 調和の数列", font_size=32, color=BLUE)
        self.play(Write(movement_title))
        self.wait(1)
        self.play(movement_title.animate.scale(0.7).to_corner(UL))
        
        # 楽器たち（音符として表現）
        instruments = VGroup()
        frequencies = [1, 1/2, 1/3, 1/4, 1/5, 1/6, 1/7, 1/8]  # 倍音列
        colors = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE, PINK, WHITE]
        
        for i, (freq, color) in enumerate(zip(frequencies, colors)):
            # 音符の大きさは周波数に比例
            note = Circle(
                radius=freq * 2,
                color=color,
                fill_opacity=0.6,
                stroke_width=4
            )
            note.move_to([i*1.5 - 5, sin(i*0.5)*2, 0])
            instruments.add(note)
        
        # 楽器たちが登場（リズミカルに）
        for i, instrument in enumerate(instruments):
            self.play(
                GrowFromCenter(instrument),
                Flash(instrument.get_center(), color=instrument.color, flash_radius=1),
                run_time=0.3
            )
        
        # ハーモニック・ダンス（調和運動）
        for beat in range(8):
            self.play(
                *[instrument.animate.scale(1 + 0.3*sin(beat + i)).rotate(PI/4)
                  for i, instrument in enumerate(instruments)],
                run_time=0.5
            )
        
        # 調和的収束
        self.play(
            *[instrument.animate.move_to(ORIGIN).scale(0.5).set_opacity(0.3) 
              for instrument in instruments],
            run_time=2
        )
        
        self.play(FadeOut(instruments), FadeOut(movement_title))

    def second_movement_fourier_dance(self):
        movement_title = Text("第2楽章: フーリエの舞踏会", font_size=32, color=GREEN)
        self.play(Write(movement_title))
        self.wait(1)
        self.play(movement_title.animate.scale(0.7).to_corner(UL))
        
        # ダンサーたち（回転する円）
        dancers = VGroup()
        num_dancers = 7
        
        for i in range(num_dancers):
            radius = 2 / (i + 1)
            dancer_circle = Circle(
                radius=radius,
                color=interpolate_color(RED, BLUE, i/num_dancers),
                stroke_width=6,
                fill_opacity=0.1
            )
            
            # ダンサーのポイント
            dancer_dot = Dot(
                color=interpolate_color(YELLOW, PINK, i/num_dancers),
                radius=0.1
            )
            
            dancer = VGroup(dancer_circle, dancer_dot)
            if i == 0:
                dancer.move_to(ORIGIN)
            else:
                dancer.move_to(dancers[i-1][1].get_center())  # 前のダンサーの点に
            
            dancers.add(dancer)
        
        # ダンサー登場
        self.play(*[Create(dancer) for dancer in dancers], run_time=2)
        
        # フーリエ級数のダンス（エピサイクル）
        trail = VMobject(color=GOLD, stroke_width=4)
        trail.start_new_path(dancers[-1][1].get_center())
        
        def update_dancers_and_trail(mob, dt):
            total_angle = mob.time * 2
            current_pos = ORIGIN
            
            for i, dancer in enumerate(dancers):
                freq = i + 1
                angle = total_angle * freq
                radius = 2 / freq
                
                # 現在のダンサーの中心を更新
                dancer[0].move_to(current_pos)
                
                # ダンサー上の点の位置
                point_pos = current_pos + radius * np.array([cos(angle), sin(angle), 0])
                dancer[1].move_to(point_pos)
                
                # 次のダンサーの中心は現在の点
                current_pos = point_pos
            
            # トレイルを更新
            trail.add_line_to(current_pos)
        
        # 時間を追跡
        self.time = 0
        def update_time(mob, dt):
            self.time += dt
        
        dancers.add_updater(update_dancers_and_trail)
        self.add_updater(update_time)
        self.add(trail)
        
        # 美しいフーリエのダンス
        self.wait(8)
        
        # アップデーターを停止
        dancers.clear_updaters()
        self.clear_updaters()
        
        # ダンサーたちがお辞儀
        self.play(
            *[dancer.animate.scale(0.3).set_opacity(0.5) for dancer in dancers],
            trail.animate.set_opacity(0.5),
            run_time=2
        )
        
        self.play(FadeOut(dancers), FadeOut(trail), FadeOut(movement_title))

    def third_movement_fractal_rhapsody(self):
        movement_title = Text("第3楽章: フラクタルの狂詩曲", font_size=32, color=PURPLE)
        self.play(Write(movement_title))
        self.wait(1)
        self.play(movement_title.animate.scale(0.7).to_corner(UL))
        
        # ドラゴン曲線（フラクタル）を生成
        def dragon_curve(order, start, end, turn_left=True):
            if order == 0:
                return [Line(start, end, stroke_width=3)]
            
            # 中点を計算
            mid = (start + end) / 2
            
            # 垂直ベクトルを計算
            direction = end - start
            perpendicular = np.array([-direction[1], direction[0], 0])
            
            if turn_left:
                bend_point = mid + perpendicular * 0.5
            else:
                bend_point = mid - perpendicular * 0.5
            
            # 再帰的に曲線を生成
            left_curve = dragon_curve(order-1, start, bend_point, True)
            right_curve = dragon_curve(order-1, bend_point, end, False)
            
            return left_curve + right_curve
        
        # フラクタル・オーケストラ
        fractal_instruments = VGroup()
        
        # 複数のドラゴン曲線を異なる色で作成
        for i in range(4):
            order = 6 + i
            angle = i * PI / 2
            start_point = 2 * np.array([cos(angle), sin(angle), 0])
            end_point = start_point + np.array([cos(angle + PI/4), sin(angle + PI/4), 0])
            
            dragon_lines = dragon_curve(min(order, 8), start_point, end_point)
            
            color = interpolate_color(RED, BLUE, i/3)
            for line in dragon_lines:
                line.set_color(color)
                line.set_stroke_width(2)
            
            dragon = VGroup(*dragon_lines)
            fractal_instruments.add(dragon)
        
        # フラクタル楽器たちの登場（爆発的に）
        for dragon in fractal_instruments:
            self.play(
                *[Create(line) for line in dragon[:20]],  # 最初の20本だけ
                Flash(dragon.get_center(), color=dragon[0].color, flash_radius=2),
                run_time=1
            )
        
        # フラクタル・ダンス（自己相似性を表現）
        for iteration in range(3):
            self.play(
                *[dragon.animate.rotate(PI/3).scale(1.2) for dragon in fractal_instruments],
                run_time=1.5
            )
            
            # スケールを元に戻しながら色を変更
            self.play(
                *[dragon.animate.scale(1/1.2).set_color(
                    interpolate_color(dragon[0].color, YELLOW, 0.5)
                ) for dragon in fractal_instruments],
                run_time=1
            )
        
        # フラクタルの集約
        self.play(
            *[dragon.animate.move_to(ORIGIN).scale(0.5).set_opacity(0.3) 
              for dragon in fractal_instruments],
            run_time=2
        )
        
        self.play(FadeOut(fractal_instruments), FadeOut(movement_title))

    def fourth_movement_golden_waltz(self):
        movement_title = Text("第4楽章: 黄金比のワルツ", font_size=32, color=GOLD)
        self.play(Write(movement_title))
        self.wait(1)
        self.play(movement_title.animate.scale(0.7).to_corner(UL))
        
        # 黄金比 φ = (1 + √5) / 2
        phi = (1 + sqrt(5)) / 2
        
        # 黄金螺旋
        def golden_spiral(t):
            r = exp(t * log(phi) / (PI/2))
            return np.array([r * cos(t), r * sin(t), 0])
        
        spiral = ParametricFunction(
            golden_spiral,
            t_range=[0, 4*PI],
            color=GOLD,
            stroke_width=6
        )
        
        # 黄金矩形のシーケンス
        rectangles = VGroup()
        golden_rectangles = VGroup()
        
        # フィボナッチ数列
        fib = [1, 1]
        for i in range(8):
            fib.append(fib[-1] + fib[-2])
        
        # 黄金矩形を作成
        current_pos = ORIGIN
        for i in range(6):
            width = fib[i] * 0.3
            height = fib[i+1] * 0.3
            
            rect = Rectangle(
                width=width,
                height=height,
                color=interpolate_color(GOLD, ORANGE, i/5),
                stroke_width=3,
                fill_opacity=0.1
            )
            rect.move_to(current_pos)
            golden_rectangles.add(rect)
            
            # 次の矩形の位置
            if i % 4 == 0:
                current_pos += RIGHT * width / 2
            elif i % 4 == 1:
                current_pos += UP * height / 2
            elif i % 4 == 2:
                current_pos += LEFT * width / 2
            else:
                current_pos += DOWN * height / 2
        
        # ワルツのリズムで登場（3拍子）
        for i in range(0, len(golden_rectangles), 3):
            batch = golden_rectangles[i:i+3]
            self.play(
                *[GrowFromCenter(rect) for rect in batch],
                run_time=1
            )
            self.wait(0.5)
        
        # 黄金螺旋の登場
        self.play(Create(spiral), run_time=3)
        
        # ワルツ・ダンス（回転運動）
        waltz_group = VGroup(golden_rectangles, spiral)
        
        for beat in range(6):
            # 3拍子のリズム
            self.play(
                waltz_group.animate.rotate(2*PI/3).scale(1.1),
                run_time=1
            )
            self.play(
                waltz_group.animate.scale(1/1.1),
                run_time=0.5
            )
        
        # 黄金比の美しい収束
        self.play(
            waltz_group.animate.scale(0.7).set_opacity(0.5),
            run_time=2
        )
        
        self.play(FadeOut(waltz_group), FadeOut(movement_title))

    def grand_finale_cosmic_chorus(self):
        # 🔥 究極のフィナーレ
        finale_title = Text("🔥 GRAND FINALE: 宇宙の大合唱 🔥", font_size=36, color=WHITE)
        finale_title.set_stroke(GOLD, width=3)
        
        self.play(
            Write(finale_title),
            Flash(ORIGIN, color=GOLD, flash_radius=10, num_lines=50),
            Flash(ORIGIN, color=WHITE, flash_radius=8, num_lines=30),
            Flash(ORIGIN, color=RED, flash_radius=6, num_lines=20),
            run_time=3
        )
        
        self.wait(1)
        self.play(finale_title.animate.scale(0.6).to_edge(UP))
        
        # 全ての数学的要素が一斉に登場！
        
        # 1. フィボナッチ螺旋群
        fibonacci_spirals = VGroup()
        for i in range(5):
            spiral = ParametricFunction(
                lambda t: np.array([
                    (1+i*0.3) * t * cos(t + i*PI/3),
                    (1+i*0.3) * t * sin(t + i*PI/3),
                    0
                ]) / 5,
                t_range=[0, 3*PI],
                color=interpolate_color(RED, BLUE, i/4),
                stroke_width=4
            )
            fibonacci_spirals.add(spiral)
        
        # 2. 数学定数たち
        constants = VGroup(
            Text("π", font_size=60, color=RED),
            Text("e", font_size=60, color=GREEN),
            Text("φ", font_size=60, color=GOLD),
            Text("∞", font_size=60, color=PURPLE),
            Text("i", font_size=60, color=CYAN),
        )
        
        for i, const in enumerate(constants):
            angle = i * 2*PI/5
            const.move_to(3 * np.array([cos(angle), sin(angle), 0]))
        
        # 3. 幾何学的図形のオーケストラ
        geometric_orchestra = VGroup()
        shapes = [Circle, Square, Triangle, RegularPolygon, RegularPolygon]
        shape_args = [{'radius': 1}, {'side_length': 1.5}, {'fill_opacity': 0.3}, 
                     {'n': 5}, {'n': 6}]
        
        for i, (shape_class, args) in enumerate(zip(shapes, shape_args)):
            if shape_class == RegularPolygon:
                shape = shape_class(**args)
            else:
                shape = shape_class(**args)
            
            shape.set_color(interpolate_color(YELLOW, PINK, i/4))
            shape.set_stroke_width(3)
            shape.set_fill_opacity(0.2)
            
            # 円形に配置
            angle = i * 2*PI/5 + PI/2
            shape.move_to(2 * np.array([cos(angle), sin(angle), 0]))
            geometric_orchestra.add(shape)
        
        # 全要素の登場（クライマックス！）
        all_elements = VGroup(fibonacci_spirals, constants, geometric_orchestra)
        
        self.play(
            *[Create(spiral) for spiral in fibonacci_spirals],
            *[GrowFromCenter(const) for const in constants],
            *[GrowFromCenter(shape) for shape in geometric_orchestra],
            run_time=4
        )
        
        # 究極の大合唱・ダンス
        for climax_beat in range(10):
            animations = []
            
            # スパイラルの回転
            animations.extend([
                Rotating(spiral, angle=PI/2, about_point=ORIGIN)
                for spiral in fibonacci_spirals
            ])
            
            # 定数の脈動
            animations.extend([
                const.animate.scale(1.3 + 0.5*sin(climax_beat + i))
                for i, const in enumerate(constants)
            ])
            
            # 図形の変身
            animations.extend([
                shape.animate.rotate(PI/3).set_color(
                    interpolate_color(shape.color, WHITE, sin(climax_beat*0.7 + i))
                )
                for i, shape in enumerate(geometric_orchestra)
            ])
            
            self.play(*animations, run_time=0.8)
        
        # 最終的な統合（全てが一つに）
        self.play(
            all_elements.animate.scale(2).move_to(ORIGIN).set_opacity(0.8),
            Flash(ORIGIN, color=WHITE, flash_radius=15, num_lines=100),
            Flash(ORIGIN, color=GOLD, flash_radius=12, num_lines=80),
            Flash(ORIGIN, color=RED, flash_radius=10, num_lines=60),
            run_time=3
        )
        
        # 宇宙への昇華
        final_message = VGroup(
            Text("MATHEMATICS", font_size=48, color=GOLD),
            Text("THE UNIVERSAL LANGUAGE", font_size=32, color=WHITE),
            Text("数学は宇宙の言語", font_size=28, color=CYAN),
            Text("🎼 ∞ 🎵", font_size=40, color=PINK)
        )
        
        final_message.arrange(DOWN, buff=0.5)
        
        self.play(
            Transform(all_elements, final_message),
            Transform(finale_title, Text("♪ BRAVO! ♪", font_size=60, color=GOLD)),
            run_time=3
        )
        
        # 美しいカーテンコール
        self.wait(2)
        self.play(
            final_message.animate.scale(1.5).set_color(WHITE),
            run_time=2
        )
        
        self.wait(1)
        
        # 全てが星になって消えていく
        self.play(
            *[obj.animate.scale(0.01).move_to([
                8*cos(i*0.7), 8*sin(i*0.7), 0
            ]).set_color(WHITE) for i, obj in enumerate(final_message)],
            finale_title.animate.scale(0.01).set_color(WHITE),
            run_time=4
        )
        
        self.wait(2)