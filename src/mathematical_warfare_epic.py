from manim import *
import numpy as np
from math import *

class MathematicalWarfareEpic(Scene):
    def construct(self):
        # 🎬 PROLOGUE: 創世記 - GENESIS (2分)
        self.prologue_genesis()
        
        # ⚡ ACT I: 災厄の始まり (3分30秒)
        self.act1_calamity_begins()
        
        # ⚔️ ACT II: 激闘編 (4分)
        self.act2_great_battle()
        
        # 💀 ACT III: 絶望と犠牲 (3分)
        self.act3_despair_sacrifice()
        
        # 🌟 ACT IV: 希望の降臨 (3分30秒)
        self.act4_advent_hope()
        
        # 🎆 ACT V: 終極決戦 (3分30秒)
        self.act5_ultimate_showdown()
        
        # 🌈 FINALE: 新生と調和 (2分30秒)
        self.finale_rebirth_harmony()

    def prologue_genesis(self):
        """🎬 PROLOGUE: 創世記 - GENESIS (2分)"""
        
        # Scene 0.1: 数学宇宙の誕生 (30秒)
        self.genesis_big_bang()
        
        # Scene 0.2: 黄金時代の数学王国 (1分)
        self.golden_age_kingdom()
        
        # Scene 0.3: 不穏な兆候 (30秒)
        self.ominous_signs()

    def genesis_big_bang(self):
        """Scene 0.1: 数学宇宙の誕生 (30秒)"""
        
        # 完全な闇
        self.camera.background_color = BLACK
        self.wait(2)
        
        # タイトル表示
        title = Text("MATHEMATICAL WARFARE", font_size=60, color=GOLD)
        subtitle = Text("THE EPIC SAGA", font_size=36, color=WHITE)
        subtitle.next_to(title, DOWN, buff=0.5)
        
        # ドラマティック登場
        self.play(
            Write(title),
            Flash(ORIGIN, color=GOLD, flash_radius=8, num_lines=50),
            run_time=2
        )
        self.play(Write(subtitle), run_time=1)
        self.wait(1)
        
        # タイトル消失
        self.play(FadeOut(title), FadeOut(subtitle))
        
        # 数学的特異点（ビッグバン開始）
        singularity = Dot(ORIGIN, radius=0.01, color=WHITE)
        self.add(singularity)
        self.wait(1)
        
        # ビッグバン爆発！
        explosion_circles = VGroup(*[
            Circle(radius=0.1 + i*0.5, stroke_color=interpolate_color(WHITE, BLUE, i/20), 
                   stroke_width=6-i*0.2, fill_opacity=0)
            for i in range(20)
        ])
        
        self.play(
            singularity.animate.scale(100).set_opacity(0),
            *[Create(circle) for circle in explosion_circles[:5]],
            Flash(ORIGIN, color=WHITE, flash_radius=15, num_lines=100),
            Flash(ORIGIN, color=BLUE, flash_radius=10, num_lines=60),
            Flash(ORIGIN, color=GOLD, flash_radius=8, num_lines=40),
            run_time=3
        )
        
        # 基本数字たちが星として誕生
        numbers = VGroup()
        for i in range(1, 10):
            num = Text(str(i), font_size=30, color=interpolate_color(YELLOW, CYAN, i/10))
            angle = i * 2 * PI / 9
            num.move_to([4*cos(angle), 4*sin(angle), 0])
            numbers.add(num)
        
        self.play(
            *[FadeIn(num, scale=5, shift=num.get_center()) for num in numbers],
            *[FadeOut(circle) for circle in explosion_circles],
            run_time=2
        )
        
        # 幾何学図形が惑星として形成
        shapes = VGroup(
            Circle(radius=1, color=BLUE).move_to([-3, 2, 0]),
            Square(side_length=1.5, color=RED).move_to([3, 2, 0]),
            Triangle(color=GREEN).scale(1.2).move_to([0, -3, 0]),
        )
        
        self.play(
            *[GrowFromCenter(shape) for shape in shapes],
            run_time=2
        )
        
        # 壮大なオーケストラBGM表示
        bgm_text = Text("♪ 壮大なオーケストラBGM開始 ♪", font_size=24, color=GOLD)
        bgm_text.to_edge(DOWN)
        self.play(Write(bgm_text), run_time=1)
        
        self.wait(1)
        self.play(FadeOut(numbers), FadeOut(shapes), FadeOut(bgm_text))

    def golden_age_kingdom(self):
        """Scene 0.2: 黄金時代の数学王国 (1分)"""
        
        # ナレーション
        narration = Text("遥か昔、数学宇宙には平和と調和が存在していた...", 
                        font_size=24, color=WHITE)
        narration.to_edge(UP)
        self.play(Write(narration), run_time=2)
        
        # π宮殿: 巨大な円形建造物
        pi_palace = VGroup()
        main_circle = Circle(radius=3, color=BLUE, stroke_width=8, fill_opacity=0.1)
        inner_circles = VGroup(*[
            Circle(radius=1+i*0.5, color=BLUE, stroke_width=3, fill_opacity=0.05)
            for i in range(3)
        ])
        pi_symbol = Text("π", font_size=48, color=BLUE).move_to(main_circle.get_center())
        pi_palace.add(main_circle, inner_circles, pi_symbol)
        pi_palace.move_to([-4, 1, 0])
        
        self.play(Create(pi_palace), run_time=2)
        
        # e神殿: 螺旋階段の神聖な建物
        e_temple = VGroup()
        # 螺旋階段
        spiral = ParametricFunction(
            lambda t: np.array([0.3*t*cos(t*2), 0.3*t*sin(t*2), 0]),
            t_range=[0, 3*PI],
            color=GREEN,
            stroke_width=6
        )
        e_symbol = Text("e", font_size=48, color=GREEN)
        e_temple.add(spiral, e_symbol)
        e_temple.move_to([4, 1, 0])
        
        self.play(Create(e_temple), run_time=2)
        
        # φ庭園: 完璧な比率の美庭
        phi_garden = VGroup()
        # 黄金螺旋
        phi_spiral = ParametricFunction(
            lambda t: np.array([
                0.5*exp(t*0.3)*cos(t),
                0.5*exp(t*0.3)*sin(t),
                0
            ]),
            t_range=[0, 2*PI],
            color=GOLD,
            stroke_width=6
        )
        phi_symbol = Text("φ", font_size=48, color=GOLD)
        phi_garden.add(phi_spiral, phi_symbol)
        phi_garden.move_to([0, -2, 0])
        
        self.play(Create(phi_garden), run_time=2)
        
        # 市民たち: 小数、分数、整数が平和に暮らす
        citizens = VGroup()
        fractions = [
            Text("1/2", font_size=20, color=YELLOW).move_to([-2, 0, 0]),
            Text("3/4", font_size=20, color=YELLOW).move_to([2, 0, 0]),
            Text("0.5", font_size=20, color=CYAN).move_to([-1, -1, 0]),
            Text("2.718", font_size=20, color=CYAN).move_to([1, -1, 0]),
        ]
        citizens.add(*fractions)
        
        self.play(
            *[FadeIn(citizen, scale=2) for citizen in citizens],
            run_time=1.5
        )
        
        # 平和な風景を演出
        peaceful_glow = Circle(radius=8, fill_color=GOLD, fill_opacity=0.05, stroke_width=0)
        self.play(FadeIn(peaceful_glow), run_time=1)
        
        self.wait(2)
        
        # 全てを薄くして次のシーンへ
        all_elements = VGroup(narration, pi_palace, e_temple, phi_garden, citizens, peaceful_glow)
        self.play(all_elements.animate.set_opacity(0.3), run_time=1)

    def ominous_signs(self):
        """Scene 0.3: 不穏な兆候 (30秒)"""
        
        # 不穏なBGM表示
        ominous_bgm = Text("♫ 不安なBGMに転調... ♫", font_size=20, color=RED)
        ominous_bgm.to_edge(DOWN)
        self.play(Write(ominous_bgm), run_time=1)
        
        # 数学王国の外縁部で異変
        edge_distortion = VGroup()
        for i in range(10):
            angle = i * 2 * PI / 10
            distortion = Line(
                [6*cos(angle), 6*sin(angle), 0],
                [7*cos(angle), 7*sin(angle), 0],
                color=RED,
                stroke_width=8
            )
            edge_distortion.add(distortion)
        
        self.play(
            *[Create(dist) for dist in edge_distortion],
            run_time=1.5
        )
        
        # 計算エラーが散発的に発生
        errors = VGroup()
        for i in range(5):
            error = Text("ERROR", font_size=16, color=RED)
            error.move_to([
                np.random.uniform(-5, 5),
                np.random.uniform(-3, 3),
                0
            ])
            errors.add(error)
        
        self.play(
            *[FadeIn(error, scale=3) for error in errors],
            Flash(ORIGIN, color=RED, flash_radius=5, num_lines=20),
            run_time=2
        )
        
        # 数式が不安定に
        unstable_formula = Text("x² + y² = z²", font_size=24, color=WHITE)
        self.play(Write(unstable_formula))
        
        # 数式が歪む
        for _ in range(3):
            self.play(
                unstable_formula.animate.shift([
                    np.random.uniform(-1, 1),
                    np.random.uniform(-1, 1),
                    0
                ]).set_color(interpolate_color(WHITE, RED, np.random.random())),
                run_time=0.5
            )
        
        # 暗雲が王国を覆う
        dark_clouds = Rectangle(
            width=16, height=10,
            fill_color=GRAY,
            fill_opacity=0.7,
            stroke_width=0
        )
        
        self.play(
            FadeIn(dark_clouds),
            *[FadeOut(error) for error in errors],
            FadeOut(unstable_formula),
            FadeOut(edge_distortion),
            FadeOut(ominous_bgm),
            run_time=2
        )
        
        # 不穏な静寂
        warning_text = Text("何かが...来る...", font_size=32, color=RED)
        self.play(Write(warning_text), run_time=1)
        self.wait(2)
        self.play(FadeOut(warning_text), FadeOut(dark_clouds), run_time=1)

    def act1_calamity_begins(self):
        """⚡ ACT I: 災厄の始まり (3分30秒)"""
        
        # ACT I タイトル
        act1_title = Text("ACT I: 災厄の始まり", font_size=48, color=RED)
        act1_subtitle = Text("THE CALAMITY BEGINS", font_size=32, color=WHITE)
        act1_subtitle.next_to(act1_title, DOWN, buff=0.5)
        
        self.play(
            Write(act1_title),
            Write(act1_subtitle),
            Flash(ORIGIN, color=RED, flash_radius=10, num_lines=50),
            run_time=2
        )
        self.wait(1)
        self.play(FadeOut(act1_title), FadeOut(act1_subtitle))
        
        # Scene 1.1: 無限大∞の覚醒
        self.infinity_awakening()
        
        # Scene 1.2: パニックと混乱  
        self.panic_and_chaos()
        
        # Scene 1.3: ∞の破壊開始
        self.infinity_destruction()
        
        # Scene 1.4: 三大定数の招集
        self.three_constants_assembly()

    def infinity_awakening(self):
        """Scene 1.1: 無限大∞の覚醒 (1分)"""
        
        scene_title = Text("Scene 1: 無限大∞の覚醒", font_size=20, color=GRAY)
        scene_title.to_corner(UL)
        self.add(scene_title)
        
        # 数学王国の地下深く
        underground = Rectangle(width=12, height=6, fill_color=DARK_GRAY, 
                               fill_opacity=0.8, stroke_width=0)
        underground.move_to([0, -1, 0])
        self.play(FadeIn(underground), run_time=1)
        
        # 封印された無限大∞
        chains = VGroup()
        for i in range(8):
            angle = i * PI / 4
            chain = Line(
                [2*cos(angle), 2*sin(angle), 0],
                [4*cos(angle), 4*sin(angle), 0],
                color=GRAY,
                stroke_width=8
            )
            chains.add(chain)
        
        infinity_symbol = Text("∞", font_size=80, color=DARK_BLUE)
        infinity_symbol.set_opacity(0.5)
        
        self.play(
            Create(chains),
            FadeIn(infinity_symbol),
            run_time=2
        )
        
        # ∞が目を覚ます
        awakening_text = Text("「何千年もの間...封印されていた...」", 
                            font_size=20, color=DARK_BLUE)
        awakening_text.to_edge(DOWN)
        self.play(Write(awakening_text), run_time=2)
        
        # ∞の怒り
        self.play(
            infinity_symbol.animate.set_color(RED).set_opacity(1).scale(1.5),
            run_time=1
        )
        
        anger_text = Text("「なぜ俺だけが恐れられる！」", 
                         font_size=24, color=RED, weight=BOLD)
        anger_text.to_edge(DOWN)
        self.play(Transform(awakening_text, anger_text), run_time=1)
        
        # 封印破壊
        self.play(
            *[chain.animate.set_color(RED).rotate(PI/4) for chain in chains],
            Flash(ORIGIN, color=RED, flash_radius=8, num_lines=30),
            run_time=2
        )
        
        # 鎖が砕ける
        self.play(
            *[FadeOut(chain, scale=3) for chain in chains],
            Flash(ORIGIN, color=WHITE, flash_radius=6, num_lines=20),
            run_time=1
        )
        
        # 地震: 王国全体が震撼
        earthquake_text = Text("地震発生！王国全体が震撼！", 
                              font_size=20, color=YELLOW)
        self.play(Transform(awakening_text, earthquake_text), run_time=1)
        
        # 画面振動効果
        for _ in range(5):
            self.play(
                infinity_symbol.animate.shift([0.2, 0, 0]),
                underground.animate.shift([0.1, 0, 0]),
                run_time=0.1
            )
            self.play(
                infinity_symbol.animate.shift([-0.2, 0, 0]),
                underground.animate.shift([-0.1, 0, 0]),
                run_time=0.1
            )
        
        # ∞登場: 巨大化して天空に現れる
        self.play(
            infinity_symbol.animate.scale(3).move_to([0, 2, 0]).set_color(DARK_RED),
            FadeOut(underground),
            Flash(infinity_symbol.get_center(), color=DARK_RED, flash_radius=5, num_lines=25),
            run_time=3
        )
        
        final_roar = Text("「俺の時代が来た！」", font_size=32, color=DARK_RED, weight=BOLD)
        self.play(Transform(awakening_text, final_roar), run_time=1)
        
        self.wait(2)
        self.play(FadeOut(awakening_text), FadeOut(scene_title))
        
        # ∞は残しておく（次のシーンで使用）
        self.infinity = infinity_symbol

    def panic_and_chaos(self):
        """Scene 1.2: パニックと混乱 (45秒)"""
        
        scene_title = Text("Scene 2: パニックと混乱", font_size=20, color=GRAY)
        scene_title.to_corner(UL)
        self.add(scene_title)
        
        # 市民たちの恐怖と逃走
        fleeing_numbers = VGroup()
        for i in range(1, 6):
            num = Text(str(i), font_size=24, color=YELLOW)
            num.move_to([np.random.uniform(-4, 4), np.random.uniform(-2, 2), 0])
            fleeing_numbers.add(num)
        
        self.play(
            *[FadeIn(num, scale=2) for num in fleeing_numbers],
            run_time=1
        )
        
        # 数字たちが泣きながら逃げる
        crying_text = Text("「助けて！誰か助けて！」", font_size=20, color=YELLOW)
        crying_text.to_edge(DOWN)
        self.play(Write(crying_text), run_time=1)
        
        # 逃走アニメーション
        self.play(
            *[num.animate.move_to([
                8 * (1 if num.get_center()[0] > 0 else -1),
                num.get_center()[1],
                0
            ]).set_opacity(0) for num in fleeing_numbers],
            run_time=2
        )
        
        # 分数たちがバラバラに
        fractions = VGroup(
            Text("1/2", font_size=20, color=CYAN).move_to([-2, 1, 0]),
            Text("3/4", font_size=20, color=CYAN).move_to([2, 1, 0]),
        )
        
        self.play(*[FadeIn(frac) for frac in fractions], run_time=0.5)
        
        # バラバラ効果
        scattered_parts = VGroup()
        for frac in fractions:
            parts = frac.submobjects.copy() if hasattr(frac, 'submobjects') else [frac]
            for part in parts:
                part.animate.shift([np.random.uniform(-2, 2), np.random.uniform(-2, 2), 0])
                scattered_parts.add(part)
        
        self.play(
            *[FadeOut(frac, scale=0.3) for frac in fractions],
            run_time=1
        )
        
        # 幾何学図形が歪んで崩壊
        distorted_circle = Circle(radius=1, color=BLUE).move_to([-3, 0, 0])
        distorted_square = Square(side_length=1, color=RED).move_to([3, 0, 0])
        
        self.play(
            Create(distorted_circle),
            Create(distorted_square),
            run_time=1
        )
        
        # 歪み効果
        self.play(
            distorted_circle.animate.stretch(2, 0).set_color(DARK_BLUE),
            distorted_square.animate.rotate(PI/4).stretch(1.5, 1).set_color(DARK_RED),
            run_time=1.5
        )
        
        self.play(
            FadeOut(distorted_circle, scale=0.1),
            FadeOut(distorted_square, scale=0.1),
            FadeOut(crying_text),
            FadeOut(scene_title),
            run_time=1
        )

    def infinity_destruction(self):
        """Scene 1.3: ∞の破壊開始 (1分)"""
        
        scene_title = Text("Scene 3: ∞の破壊開始", font_size=20, color=GRAY)
        scene_title.to_corner(UL)
        self.add(scene_title)
        
        # ∞の必殺技「無限拡散波」
        attack_name = Text("「無限拡散波！」", font_size=32, color=DARK_RED, weight=BOLD)
        attack_name.to_edge(DOWN)
        self.play(Write(attack_name), run_time=1)
        
        # 攻撃エフェクト
        expansion_waves = VGroup()
        for i in range(10):
            wave = Circle(
                radius=1 + i*0.8,
                stroke_color=interpolate_color(DARK_RED, RED, i/10),
                stroke_width=8 - i*0.6,
                fill_opacity=0
            )
            expansion_waves.add(wave)
        
        self.play(
            *[Create(wave) for wave in expansion_waves[:3]],
            Flash(self.infinity.get_center(), color=DARK_RED, flash_radius=6, num_lines=40),
            run_time=2
        )
        
        # 建物が無限大に拡散して消滅
        buildings = VGroup()
        for i in range(5):
            building = Rectangle(
                width=0.8, height=2,
                fill_color=GRAY,
                fill_opacity=0.7,
                stroke_color=WHITE
            )
            building.move_to([i*2-4, -2, 0])
            buildings.add(building)
        
        self.play(*[FadeIn(building) for building in buildings], run_time=0.5)
        
        # 拡散消滅エフェクト
        self.play(
            *[building.animate.scale(10).set_opacity(0) for building in buildings],
            *[Create(wave) for wave in expansion_waves[3:6]],
            run_time=2
        )
        
        # 数式破壊
        formula = Text("E = mc²", font_size=32, color=WHITE)
        self.play(Write(formula), run_time=1)
        
        destruction_text = Text("方程式が解けなくなる！", font_size=20, color=RED)
        self.play(Transform(attack_name, destruction_text), run_time=1)
        
        # 数式にエラー表示
        error_overlay = Text("ERROR", font_size=48, color=RED)
        error_overlay.move_to(formula.get_center())
        
        self.play(
            FadeIn(error_overlay, scale=2),
            formula.animate.set_color(RED),
            Flash(formula.get_center(), color=RED, flash_radius=3, num_lines=15),
            run_time=1.5
        )
        
        # 計算不能エラーが王国中に拡散
        error_spread = VGroup()
        for i in range(8):
            angle = i * PI / 4
            error = Text("ERROR", font_size=16, color=RED)
            error.move_to([4*cos(angle), 4*sin(angle), 0])
            error_spread.add(error)
        
        self.play(
            *[FadeIn(err, scale=3) for err in error_spread],
            *[Create(wave) for wave in expansion_waves[6:]],
            run_time=2
        )
        
        # ∞の宣言
        declaration = Text("「この世界に秩序など不要だ！」", 
                          font_size=28, color=DARK_RED, weight=BOLD)
        self.play(Transform(attack_name, declaration), run_time=1.5)
        
        # 天空が裂け、混沌の嵐
        sky_tear = Line([-8, 4, 0], [8, 4, 0], color=DARK_RED, stroke_width=12)
        chaos_particles = VGroup()
        for _ in range(20):
            particle = Dot(
                [np.random.uniform(-6, 6), np.random.uniform(2, 6), 0],
                color=interpolate_color(RED, YELLOW, np.random.random()),
                radius=0.1
            )
            chaos_particles.add(particle)
        
        self.play(
            Create(sky_tear),
            *[FadeIn(particle, scale=5) for particle in chaos_particles],
            Flash(ORIGIN, color=DARK_RED, flash_radius=12, num_lines=60),
            run_time=3
        )
        
        self.wait(1)
        
        # クリーンアップ
        self.play(
            *[FadeOut(obj) for obj in [formula, error_overlay, error_spread, 
                                       expansion_waves, sky_tear, chaos_particles,
                                       attack_name, scene_title]],
            run_time=1
        )

    def three_constants_assembly(self):
        """Scene 1.4: 三大定数の招集 (45秒)"""
        
        scene_title = Text("Scene 4: 三大定数の招集", font_size=20, color=GRAY)
        scene_title.to_corner(UL)
        self.add(scene_title)
        
        # π宮殿の奥で緊急会議
        meeting_hall = Rectangle(width=8, height=5, fill_color=DARK_BLUE, 
                                fill_opacity=0.3, stroke_color=BLUE, stroke_width=3)
        self.play(FadeIn(meeting_hall), run_time=1)
        
        # 三大定数登場
        pi_hero = Text("π", font_size=48, color=BLUE).move_to([-2, 0, 0])
        e_hero = Text("e", font_size=48, color=GREEN).move_to([0, 0, 0])
        phi_hero = Text("φ", font_size=48, color=GOLD).move_to([2, 0, 0])
        
        self.play(
            FadeIn(pi_hero, scale=2),
            FadeIn(e_hero, scale=2),
            FadeIn(phi_hero, scale=2),
            Flash(ORIGIN, color=WHITE, flash_radius=5, num_lines=30),
            run_time=2
        )
        
        # 各キャラクターのセリフ
        pi_speech = Text("「この危機を止められるのは我々だけだ」", 
                        font_size=18, color=BLUE)
        pi_speech.to_edge(DOWN)
        self.play(Write(pi_speech), run_time=1.5)
        
        e_speech = Text("「∞の力は我々の想像を超えている」", 
                       font_size=18, color=GREEN)
        self.play(Transform(pi_speech, e_speech), run_time=1.5)
        
        phi_speech = Text("「でも、美しい調和を守らねば」", 
                         font_size=18, color=GOLD)
        self.play(Transform(pi_speech, phi_speech), run_time=1.5)
        
        # 三大定数同盟結成の儀式
        alliance_text = Text("三大定数同盟結成！", font_size=24, color=WHITE, weight=BOLD)
        alliance_text.move_to([0, -2, 0])
        
        self.play(
            Write(alliance_text),
            pi_hero.animate.set_color(LIGHT_BLUE),
            e_hero.animate.set_color(LIGHT_GREEN),
            phi_hero.animate.set_color(YELLOW),
            Flash(ORIGIN, color=GOLD, flash_radius=6, num_lines=25),
            run_time=2
        )
        
        # 戦闘準備とパワーアップ
        battle_cry = Text("「数学王国の平和のために！」", 
                         font_size=20, color=WHITE, weight=BOLD)
        self.play(Transform(pi_speech, battle_cry), run_time=1)
        
        # パワーアップエフェクト
        power_auras = VGroup()
        for hero, color in [(pi_hero, BLUE), (e_hero, GREEN), (phi_hero, GOLD)]:
            aura = Circle(radius=1.5, stroke_color=color, stroke_width=6, 
                         fill_color=color, fill_opacity=0.2)
            aura.move_to(hero.get_center())
            power_auras.add(aura)
        
        self.play(
            *[Create(aura) for aura in power_auras],
            *[hero.animate.scale(1.3) for hero in [pi_hero, e_hero, phi_hero]],
            Flash(ORIGIN, color=WHITE, flash_radius=8, num_lines=40),
            run_time=2
        )
        
        self.wait(1)
        
        # 次のACTに向けて準備
        self.heroes = VGroup(pi_hero, e_hero, phi_hero)
        self.hero_auras = power_auras
        
        self.play(
            FadeOut(meeting_hall),
            FadeOut(alliance_text),
            FadeOut(pi_speech),
            FadeOut(scene_title),
            run_time=1
        )

    def act2_great_battle(self):
        """⚔️ ACT II: 激闘編 (4分)"""
        
        # ACT II タイトル
        act2_title = Text("ACT II: 激闘編", font_size=48, color=ORANGE)
        act2_subtitle = Text("THE GREAT BATTLE", font_size=32, color=WHITE)
        act2_subtitle.next_to(act2_title, DOWN, buff=0.5)
        
        self.play(
            Write(act2_title),
            Write(act2_subtitle),
            Flash(ORIGIN, color=ORANGE, flash_radius=10, num_lines=50),
            run_time=2
        )
        self.wait(1)
        self.play(FadeOut(act2_title), FadeOut(act2_subtitle))
        
        # 戦闘シーン
        self.pi_vs_infinity()
        self.e_vs_infinity() 
        self.phi_vs_infinity()
        self.three_constants_defeat()

    def pi_vs_infinity(self):
        """Scene 2.1: π vs ∞ - 円環の決闘 (1分15秒)"""
        
        scene_title = Text("π vs ∞ - 円環の決闘", font_size=20, color=ORANGE)
        scene_title.to_corner(UL)
        self.add(scene_title)
        
        # 決戦の地: 王国中央広場
        arena = Circle(radius=6, stroke_color=WHITE, stroke_width=8, fill_opacity=0.05)
        self.play(Create(arena), run_time=1)
        
        # 戦闘員配置
        pi_fighter = self.heroes[0].copy().move_to([-3, 0, 0]).scale(1.5)
        infinity_fighter = self.infinity.copy().move_to([3, 0, 0])
        
        self.play(
            Transform(self.heroes[0], pi_fighter),
            Transform(self.infinity, infinity_fighter),
            run_time=1
        )
        
        # π登場セリフ
        pi_challenge = Text("「無秩序を許すわけにはいかん！」", 
                          font_size=20, color=BLUE, weight=BOLD)
        pi_challenge.to_edge(DOWN)
        self.play(Write(pi_challenge), run_time=1.5)
        
        # 必殺技合戦開始
        
        # π: 円周波動砲
        attack1_name = Text("「円周波動砲！」", font_size=24, color=BLUE, weight=BOLD)
        self.play(Transform(pi_challenge, attack1_name), run_time=1)
        
        pi_attack_circles = VGroup()
        for i in range(5):
            circle = Circle(radius=1+i*0.5, stroke_color=BLUE, stroke_width=6, fill_opacity=0.1)
            pi_attack_circles.add(circle)
        
        self.play(
            *[Create(circle) for circle in pi_attack_circles],
            Flash(pi_fighter.get_center(), color=BLUE, flash_radius=4, num_lines=20),
            run_time=2
        )
        
        # ∞: 無限拡散破
        infinity_counter = Text("「無限拡散破！」", font_size=24, color=DARK_RED, weight=BOLD)
        self.play(Transform(pi_challenge, infinity_counter), run_time=1)
        
        # 円を無限大に引き伸ばし
        self.play(
            *[circle.animate.scale(3).set_opacity(0) for circle in pi_attack_circles],
            Flash(infinity_fighter.get_center(), color=DARK_RED, flash_radius=4, num_lines=20),
            run_time=2
        )
        
        # π: 3.14159...無限小数連打
        pi_combo = Text("「3.14159...無限小数連打！」", font_size=20, color=BLUE)
        self.play(Transform(pi_challenge, pi_combo), run_time=1)
        
        # 小数攻撃エフェクト
        digits = VGroup()
        pi_digits = "31415926535897932384626433"
        for i, digit in enumerate(pi_digits[:12]):
            d = Text(digit, font_size=20, color=BLUE)
            d.move_to([np.random.uniform(-4, 4), np.random.uniform(-3, 3), 0])
            digits.add(d)
        
        self.play(
            *[FadeIn(digit, scale=3) for digit in digits],
            run_time=1.5
        )
        
        # 数字が∞に向かって飛ぶ
        self.play(
            *[digit.animate.move_to(infinity_fighter.get_center()).set_opacity(0) 
              for digit in digits],
            Flash(infinity_fighter.get_center(), color=BLUE, flash_radius=3, num_lines=15),
            run_time=1.5
        )
        
        # ∞: 発散爆裂
        infinity_blast = Text("「発散爆裂！」", font_size=24, color=DARK_RED, weight=BOLD)
        self.play(Transform(pi_challenge, infinity_blast), run_time=1)
        
        # 発散エフェクト
        divergence_rays = VGroup()
        for i in range(12):
            angle = i * PI / 6
            ray = Line(
                infinity_fighter.get_center(),
                infinity_fighter.get_center() + 4*np.array([cos(angle), sin(angle), 0]),
                color=DARK_RED,
                stroke_width=8
            )
            divergence_rays.add(ray)
        
        self.play(
            *[Create(ray) for ray in divergence_rays],
            Flash(infinity_fighter.get_center(), color=DARK_RED, flash_radius=6, num_lines=30),
            run_time=2
        )
        
        # 互角の戦いで地面が裂ける
        ground_cracks = VGroup()
        for i in range(5):
            crack = Line(
                [np.random.uniform(-5, 5), -4, 0],
                [np.random.uniform(-5, 5), 4, 0],
                color=BROWN,
                stroke_width=6
            )
            ground_cracks.add(crack)
        
        self.play(
            *[Create(crack) for crack in ground_cracks],
            run_time=1.5
        )
        
        # πがダメージを受けて後退
        damage_text = Text("πがダメージを受けた！", font_size=20, color=RED)
        self.play(Transform(pi_challenge, damage_text), run_time=1)
        
        self.play(
            pi_fighter.animate.shift([-2, 0, 0]).set_color(DARK_BLUE).scale(0.8),
            Flash(pi_fighter.get_center(), color=RED, flash_radius=2, num_lines=10),
            run_time=2
        )
        
        self.wait(1)
        
        # クリーンアップ
        self.play(
            *[FadeOut(obj) for obj in [arena, ground_cracks, divergence_rays,
                                       pi_challenge, scene_title]],
            run_time=1
        )
        
        # 状態更新
        self.heroes[0] = pi_fighter
        self.infinity = infinity_fighter

    def e_vs_infinity(self):
        """Scene 2.2: e vs ∞ - 指数の激突 (1分15秒)"""
        
        scene_title = Text("e vs ∞ - 指数の激突", font_size=20, color=ORANGE)
        scene_title.to_corner(UL)
        self.add(scene_title)
        
        # e参戦
        e_fighter = self.heroes[1].copy().move_to([-3, 0, 0]).scale(1.5)
        self.play(
            Transform(self.heroes[1], e_fighter),
            Flash(e_fighter.get_center(), color=GREEN, flash_radius=3, num_lines=15),
            run_time=1
        )
        
        e_entry = Text("「成長こそが宇宙の法則だ！」", font_size=20, color=GREEN, weight=BOLD)
        e_entry.to_edge(DOWN)
        self.play(Write(e_entry), run_time=1.5)
        
        # e: 指数爆発波
        exponential_attack = Text("「指数爆発波！」", font_size=24, color=GREEN, weight=BOLD)
        self.play(Transform(e_entry, exponential_attack), run_time=1)
        
        # 指数成長視覚化
        exp_curves = VGroup()
        for i in range(3):
            curve = ParametricFunction(
                lambda t: np.array([t-2, exp(t*0.5+i*0.3)-2, 0]),
                t_range=[0, 3],
                color=interpolate_color(GREEN, YELLOW, i/2),
                stroke_width=6
            )
            exp_curves.add(curve)
        
        self.play(
            *[Create(curve) for curve in exp_curves],
            Flash(e_fighter.get_center(), color=GREEN, flash_radius=4, num_lines=20),
            run_time=2
        )
        
        # ∞: 無限収束破
        infinity_counter = Text("「無限収束破！」", font_size=24, color=DARK_RED, weight=BOLD)
        self.play(Transform(e_entry, infinity_counter), run_time=1)
        
        # 成長を強制停止
        self.play(
            *[curve.animate.set_color(RED).scale(0.3) for curve in exp_curves],
            Flash(self.infinity.get_center(), color=DARK_RED, flash_radius=4, num_lines=20),
            run_time=2
        )
        
        # e: 自然対数螺旋
        ln_spiral = Text("「自然対数螺旋！」", font_size=20, color=GREEN)
        self.play(Transform(e_entry, ln_spiral), run_time=1)
        
        ln_spiral_curve = ParametricFunction(
            lambda t: np.array([
                log(t+1)*cos(t*2),
                log(t+1)*sin(t*2),
                0
            ]),
            t_range=[0.1, 2*PI],
            color=GREEN,
            stroke_width=8
        )
        
        self.play(
            Create(ln_spiral_curve),
            Flash(e_fighter.get_center(), color=GREEN, flash_radius=3, num_lines=15),
            run_time=2
        )
        
        # ∞: 極限破綻
        limit_break = Text("「極限破綻！」", font_size=24, color=DARK_RED, weight=BOLD)
        self.play(Transform(e_entry, limit_break), run_time=1)
        
        # 極限の破壊エフェクト
        limit_destruction = VGroup()
        for i in range(6):
            fragment = Text("lim", font_size=16, color=RED)
            fragment.move_to([np.random.uniform(-4, 4), np.random.uniform(-2, 2), 0])
            limit_destruction.add(fragment)
        
        self.play(
            *[FadeIn(frag, scale=2) for frag in limit_destruction],
            ln_spiral_curve.animate.set_color(RED),
            Flash(self.infinity.get_center(), color=DARK_RED, flash_radius=5, num_lines=25),
            run_time=2
        )
        
        # eも劣勢に
        defeat_text = Text("「こんなはずでは...」", font_size=20, color=DARK_GREEN)
        self.play(Transform(e_entry, defeat_text), run_time=1)
        
        self.play(
            e_fighter.animate.shift([-2, -1, 0]).set_color(DARK_GREEN).scale(0.7),
            *[frag.animate.set_color(DARK_RED).scale(2) for frag in limit_destruction],
            Flash(e_fighter.get_center(), color=RED, flash_radius=2, num_lines=10),
            run_time=2
        )
        
        self.wait(1)
        
        # クリーンアップ
        self.play(
            *[FadeOut(obj) for obj in [exp_curves, ln_spiral_curve, limit_destruction,
                                       e_entry, scene_title]],
            run_time=1
        )
        
        self.heroes[1] = e_fighter

    def phi_vs_infinity(self):
        """Scene 2.3: φ vs ∞ - 黄金の美学 (1分15秒)"""
        
        scene_title = Text("φ vs ∞ - 黄金の美学", font_size=20, color=ORANGE)
        scene_title.to_corner(UL)
        self.add(scene_title)
        
        # φ最後の希望として参戦
        phi_fighter = self.heroes[2].copy().move_to([-3, 0, 0]).scale(1.5)
        self.play(
            Transform(self.heroes[2], phi_fighter),
            Flash(phi_fighter.get_center(), color=GOLD, flash_radius=3, num_lines=15),
            run_time=1
        )
        
        phi_declaration = Text("「美しさこそが真理の証明！」", 
                              font_size=20, color=GOLD, weight=BOLD)
        phi_declaration.to_edge(DOWN)
        self.play(Write(phi_declaration), run_time=1.5)
        
        # φ: 黄金螺旋砲
        golden_attack = Text("「黄金螺旋砲！」", font_size=24, color=GOLD, weight=BOLD)
        self.play(Transform(phi_declaration, golden_attack), run_time=1)
        
        # フィボナッチ螺旋攻撃
        fibonacci_spiral = ParametricFunction(
            lambda t: np.array([
                exp(t*0.2)*cos(t)*0.8,
                exp(t*0.2)*sin(t)*0.8,
                0
            ]),
            t_range=[0, 4*PI],
            color=GOLD,
            stroke_width=10
        )
        
        self.play(
            Create(fibonacci_spiral),
            Flash(phi_fighter.get_center(), color=GOLD, flash_radius=4, num_lines=20),
            run_time=2
        )
        
        # ∞: 醜悪無限
        ugliness_attack = Text("「醜悪無限！」", font_size=24, color=DARK_RED, weight=BOLD)
        self.play(Transform(phi_declaration, ugliness_attack), run_time=1)
        
        # 美しさを歪める
        self.play(
            fibonacci_spiral.animate.set_color(MAROON).stretch(2, 0).stretch(0.5, 1),
            Flash(self.infinity.get_center(), color=DARK_RED, flash_radius=4, num_lines=20),
            run_time=2
        )
        
        # φ: 完璧比率結界
        ratio_barrier = Text("「完璧比率結界！」", font_size=20, color=GOLD)
        self.play(Transform(phi_declaration, ratio_barrier), run_time=1)
        
        # 1:1.618の黄金比バリア
        golden_rectangles = VGroup()
        phi_value = (1 + sqrt(5)) / 2
        
        for i in range(3):
            rect = Rectangle(
                width=1*phi_value,
                height=1,
                stroke_color=GOLD,
                stroke_width=6,
                fill_opacity=0.2,
                fill_color=GOLD
            )
            rect.scale(1.5-i*0.3).move_to([0, 0, 0])
            golden_rectangles.add(rect)
        
        self.play(
            *[Create(rect) for rect in golden_rectangles],
            fibonacci_spiral.animate.set_color(GOLD),
            run_time=2
        )
        
        # ∞: 比率崩壊
        ratio_destruction = Text("「比率崩壊！」", font_size=24, color=DARK_RED, weight=BOLD)
        self.play(Transform(phi_declaration, ratio_destruction), run_time=1)
        
        # 比率の破壊
        chaos_ratios = VGroup()
        for rect in golden_rectangles:
            # 歪んだ矩形に変換
            distorted = rect.copy()
            distorted.stretch(np.random.uniform(0.3, 3), 0)
            distorted.stretch(np.random.uniform(0.3, 3), 1)
            distorted.set_color(RED)
            chaos_ratios.add(distorted)
        
        self.play(
            *[Transform(rect, chaos) for rect, chaos in zip(golden_rectangles, chaos_ratios)],
            Flash(self.infinity.get_center(), color=DARK_RED, flash_radius=5, num_lines=25),
            run_time=2
        )
        
        # φも敗北寸前
        phi_defeat = Text("φも敗北寸前...", font_size=20, color=DARK_GRAY)
        self.play(Transform(phi_declaration, phi_defeat), run_time=1)
        
        # 血を流す（数学的に）
        blood_drops = VGroup()
        for i in range(5):
            drop = Dot(
                phi_fighter.get_center() + [np.random.uniform(-0.5, 0.5), 
                                           np.random.uniform(-1, 0), 0],
                color=DARK_RED,
                radius=0.1
            )
            blood_drops.add(drop)
        
        self.play(
            phi_fighter.animate.shift([-2, -1, 0]).set_color(ORANGE).scale(0.6),
            *[FadeIn(drop, scale=2) for drop in blood_drops],
            Flash(phi_fighter.get_center(), color=RED, flash_radius=2, num_lines=10),
            run_time=2
        )
        
        self.wait(1)
        
        # クリーンアップ  
        self.play(
            *[FadeOut(obj) for obj in [fibonacci_spiral, golden_rectangles, blood_drops,
                                       phi_declaration, scene_title]],
            run_time=1
        )
        
        self.heroes[2] = phi_fighter

    def three_constants_defeat(self):
        """Scene 2.4: 三大定数の敗北 (15秒)"""
        
        scene_title = Text("三大定数の敗北", font_size=20, color=GRAY)
        scene_title.to_corner(UL)
        self.add(scene_title)
        
        # π、e、φが同時に倒れる
        self.play(
            *[hero.animate.move_to([0, -2, 0]).set_opacity(0.3).scale(0.5) 
              for hero in self.heroes],
            run_time=2
        )
        
        # 敗北のセリフ
        defeat_speech = Text("「我々では...敵わないのか...」", 
                           font_size=20, color=GRAY)
        defeat_speech.to_edge(DOWN)
        self.play(Write(defeat_speech), run_time=1.5)
        
        # ∞の高笑い
        victory_laugh = Text("「ハハハハ！これが現実だ！」", 
                           font_size=28, color=DARK_RED, weight=BOLD)
        self.play(Transform(defeat_speech, victory_laugh), run_time=1.5)
        
        # ∞の勝利ポーズ
        self.play(
            self.infinity.animate.scale(1.5).set_color(RED),
            Flash(self.infinity.get_center(), color=DARK_RED, flash_radius=6, num_lines=30),
            run_time=2
        )
        
        # 絶望の音楽
        despair_music = Text("♫ 絶望の音楽... ♫", font_size=16, color=GRAY)
        despair_music.to_corner(DR)
        self.play(Write(despair_music), run_time=1)
        
        # 暗転
        darkness = Rectangle(width=20, height=12, fill_color=BLACK, 
                           fill_opacity=0.8, stroke_width=0)
        self.play(
            FadeIn(darkness),
            FadeOut(defeat_speech),
            FadeOut(despair_music),
            FadeOut(scene_title),
            run_time=2
        )
        
        self.wait(2)
        self.play(FadeOut(darkness), run_time=1)

    def act3_despair_sacrifice(self):
        """💀 ACT III: 絶望と犠牲 (3分)"""
        
        # ACT III は次のメッセージで実装
        act3_title = Text("ACT III: 絶望と犠牲", font_size=48, color=PURPLE)
        act3_subtitle = Text("DESPAIR AND SACRIFICE", font_size=32, color=WHITE)
        act3_subtitle.next_to(act3_title, DOWN, buff=0.5)
        
        self.play(
            Write(act3_title),
            Write(act3_subtitle),
            Flash(ORIGIN, color=PURPLE, flash_radius=10, num_lines=50),
            run_time=2
        )
        self.wait(1)
        self.play(FadeOut(act3_title), FadeOut(act3_subtitle))
        
        # 続く...
        to_be_continued = Text("To Be Continued...", font_size=32, color=WHITE)
        self.play(Write(to_be_continued), run_time=2)
        self.wait(2)
        self.play(FadeOut(to_be_continued))

    def act4_advent_hope(self):
        """🌟 ACT IV: 希望の降臨 (3分30秒)"""
        pass

    def act5_ultimate_showdown(self):
        """🎆 ACT V: 終極決戦 (3分30秒)"""
        pass

    def finale_rebirth_harmony(self):
        """🌈 FINALE: 新生と調和 (2分30秒)"""
        pass