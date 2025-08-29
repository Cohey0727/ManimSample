from manim import *
import numpy as np
from math import *

class GenesisAndApocalypse(Scene):
    def construct(self):
        # 創世記 - 無から有へ
        self.big_bang_genesis()
        
        # 生命の誕生と進化
        self.evolution_of_life()
        
        # 文明の興隆
        self.rise_of_civilization()
        
        # 終末と再生の無限サイクル
        self.apocalypse_and_rebirth()

    def big_bang_genesis(self):
        # 完全な闇から始まる
        self.camera.background_color = BLACK
        
        # 最初の一点（特異点）
        singularity = Dot(ORIGIN, radius=0.001, color=WHITE)
        self.add(singularity)
        self.wait(2)  # 静寂の時間
        
        # ビッグバン爆発！
        big_bang_title = Text("創世 - GENESIS", font_size=24, color=WHITE)
        big_bang_title.to_edge(UP).set_opacity(0.3)
        self.add(big_bang_title)
        
        # エネルギーの波動
        energy_waves = VGroup()
        for i in range(50):
            wave = Circle(
                radius=0.1 + i * 0.3,
                stroke_color=interpolate_color(WHITE, GOLD, i/50),
                stroke_width=8 - i * 0.15,
                fill_opacity=0
            )
            energy_waves.add(wave)
        
        # 爆発アニメーション
        self.play(
            singularity.animate.scale(1000).set_opacity(0),
            *[Create(wave) for wave in energy_waves[:10]],
            Flash(ORIGIN, color=WHITE, flash_radius=20, num_lines=100),
            run_time=3
        )
        
        # 素粒子の誕生
        particles = VGroup(*[
            Dot(
                [np.random.uniform(-6, 6), np.random.uniform(-4, 4), 0],
                color=interpolate_color(BLUE, RED, np.random.random()),
                radius=np.random.uniform(0.02, 0.1)
            )
            for _ in range(200)
        ])
        
        self.play(
            *[FadeIn(p, scale=10, shift=p.get_center()) for p in particles[::5]],
            *[FadeOut(wave) for wave in energy_waves],
            run_time=2
        )
        
        # 重力による集合
        self.play(
            *[p.animate.move_to(
                p.get_center() * 0.3 + 
                0.7 * np.array([sin(i*0.3), cos(i*0.7), 0])
            ) for i, p in enumerate(particles)],
            run_time=3
        )
        
        self.play(FadeOut(particles), FadeOut(big_bang_title))

    def evolution_of_life(self):
        life_title = Text("進化 - EVOLUTION", font_size=24, color=GREEN)
        life_title.to_edge(UP).set_opacity(0.7)
        self.add(life_title)
        
        # 原始海洋
        ocean = Rectangle(
            width=14, height=8,
            fill_color=BLUE,
            fill_opacity=0.3,
            stroke_color=BLUE_C,
            stroke_width=3
        )
        self.play(FadeIn(ocean))
        
        # DNAヘリックス構造の生成
        def dna_helix(t, strand=0):
            radius = 1.5
            height_factor = 0.5
            spiral_offset = strand * PI
            
            return np.array([
                radius * cos(t + spiral_offset),
                height_factor * t,
                radius * sin(t + spiral_offset) * 0.3
            ])
        
        # 2本のDNA鎖
        dna_strand1 = ParametricFunction(
            lambda t: dna_helix(t, 0),
            t_range=[-6, 6],
            color=GREEN,
            stroke_width=6
        )
        
        dna_strand2 = ParametricFunction(
            lambda t: dna_helix(t, 1),
            t_range=[-6, 6],
            color=YELLOW,
            stroke_width=6
        )
        
        # DNA塩基対（横の結合）
        base_pairs = VGroup()
        for t in np.arange(-5, 6, 0.5):
            p1 = dna_helix(t, 0)
            p2 = dna_helix(t, 1)
            line = Line(p1, p2, color=WHITE, stroke_width=2)
            base_pairs.add(line)
        
        dna = VGroup(dna_strand1, dna_strand2, base_pairs)
        dna.scale(0.5).move_to(ORIGIN)
        
        # DNA誕生アニメーション
        self.play(
            Create(dna_strand1),
            Create(dna_strand2),
            run_time=3
        )
        
        self.play(
            *[Create(pair) for pair in base_pairs],
            run_time=2
        )
        
        # DNA複製アニメーション（自己増殖）
        dna_copy = dna.copy().shift(RIGHT * 4)
        self.play(
            Transform(dna.copy(), dna_copy),
            dna.animate.shift(LEFT * 4),
            run_time=2
        )
        
        # 細胞分裂
        cells = VGroup()
        for i in range(8):
            cell = Circle(
                radius=0.5,
                color=interpolate_color(GREEN, BLUE, i/8),
                fill_opacity=0.5
            )
            angle = i * PI / 4
            cell.move_to([2 * cos(angle), 2 * sin(angle), 0])
            cells.add(cell)
        
        self.play(
            Transform(dna, cells),
            Transform(dna_copy, cells.copy().shift(UP)),
            FadeOut(ocean),
            run_time=3
        )
        
        # 多細胞生物への進化（フラクタル樹状構造）
        def create_tree(depth, pos, angle, length, color_factor):
            if depth == 0:
                return VGroup()
            
            branch = Line(
                pos,
                pos + length * np.array([cos(angle), sin(angle), 0]),
                color=interpolate_color(BROWN, GREEN, color_factor),
                stroke_width=depth * 2
            )
            
            tree = VGroup(branch)
            end_pos = pos + length * np.array([cos(angle), sin(angle), 0])
            
            # 左右の枝
            left_tree = create_tree(depth-1, end_pos, angle + PI/6, length*0.7, color_factor + 0.2)
            right_tree = create_tree(depth-1, end_pos, angle - PI/6, length*0.7, color_factor + 0.2)
            
            tree.add(left_tree, right_tree)
            return tree
        
        life_tree = create_tree(5, DOWN * 3, PI/2, 2, 0)
        
        self.play(
            Transform(cells, life_tree),
            run_time=4
        )
        
        self.wait(1)
        self.play(FadeOut(cells), FadeOut(life_title))

    def rise_of_civilization(self):
        civilization_title = Text("文明 - CIVILIZATION", font_size=24, color=GOLD)
        civilization_title.to_edge(UP).set_opacity(0.7)
        self.add(civilization_title)
        
        # 都市の建設（幾何学的構造の成長）
        buildings = VGroup()
        for i in range(20):
            height = np.random.uniform(1, 4)
            building = Rectangle(
                width=0.8,
                height=height,
                fill_color=interpolate_color(GRAY, YELLOW, height/4),
                fill_opacity=0.7,
                stroke_color=WHITE,
                stroke_width=2
            )
            building.move_to([i - 10, -2 + height/2, 0])
            buildings.add(building)
        
        # 建物が下から成長
        self.play(
            *[GrowFromEdge(building, DOWN) for building in buildings],
            run_time=3
        )
        
        # 電気システム（ネットワーク）
        network = VGroup()
        nodes = []
        for building in buildings[::2]:  # 2つおきに
            node = Dot(building.get_top(), color=YELLOW, radius=0.1)
            nodes.append(node)
            network.add(node)
        
        # ネットワークの接続線
        for i in range(len(nodes)-1):
            connection = Line(
                nodes[i].get_center(),
                nodes[i+1].get_center(),
                color=YELLOW,
                stroke_width=3
            )
            network.add(connection)
        
        self.play(Create(network), run_time=2)
        
        # データの流れ（パーティクルがネットワークを流れる）
        data_particles = VGroup(*[
            Dot(color=CYAN, radius=0.05)
            for _ in range(30)
        ])
        
        for particle in data_particles:
            particle.move_to(nodes[0].get_center())
        
        # パーティクルがネットワーク上を移動
        self.play(
            *[particle.animate.move_to(nodes[-1].get_center()) 
              for particle in data_particles],
            run_time=3
        )
        
        # 文明の絶頂 - 黄金時代
        golden_light = Rectangle(
            width=20, height=12,
            fill_color=GOLD,
            fill_opacity=0.2,
            stroke_width=0
        )
        
        self.play(
            FadeIn(golden_light),
            buildings.animate.set_color(GOLD),
            network.animate.set_color(GOLD),
            run_time=2
        )
        
        self.wait(1)
        
        # 文明の衰退の兆し
        self.play(
            golden_light.animate.set_opacity(0.05),
            buildings.animate.set_color(GRAY),
            *[FadeOut(particle) for particle in data_particles],
            run_time=2
        )
        
        self.play(
            FadeOut(buildings),
            FadeOut(network),
            FadeOut(golden_light),
            FadeOut(civilization_title)
        )

    def apocalypse_and_rebirth(self):
        # 終末
        apocalypse_title = Text("終末 - APOCALYPSE", font_size=24, color=RED)
        apocalypse_title.to_edge(UP)
        self.add(apocalypse_title)
        
        # 破滅の兆候（カオス的な動き）
        chaos_particles = VGroup(*[
            Dot(
                [np.random.uniform(-8, 8), np.random.uniform(-4, 4), 0],
                color=interpolate_color(RED, BLACK, np.random.random()),
                radius=np.random.uniform(0.05, 0.3)
            )
            for _ in range(100)
        ])
        
        self.play(
            *[FadeIn(p, scale=5) for p in chaos_particles],
            run_time=2
        )
        
        # カオス的運動
        for _ in range(3):
            self.play(
                *[p.animate.move_to([
                    np.random.uniform(-8, 8),
                    np.random.uniform(-4, 4),
                    0
                ]).set_color(interpolate_color(RED, YELLOW, np.random.random()))
                for p in chaos_particles],
                run_time=1.5
            )
        
        # 最終的崩壊（ブラックホール）
        black_hole = Circle(
            radius=0.1,
            fill_color=BLACK,
            fill_opacity=1,
            stroke_color=PURPLE,
            stroke_width=5
        )
        
        self.play(Create(black_hole))
        
        # 全てがブラックホールに吸い込まれる
        self.play(
            *[p.animate.move_to(ORIGIN).scale(0.01) for p in chaos_particles],
            black_hole.animate.scale(20).set_opacity(0.9),
            apocalypse_title.animate.set_color(BLACK),
            run_time=4
        )
        
        # 完全な闇
        self.play(FadeOut(black_hole))
        self.wait(2)
        
        # 再生 - REBIRTH
        rebirth_title = Text("再生 - REBIRTH", font_size=24, color=WHITE)
        rebirth_title.to_edge(UP)
        
        # 新たな光（希望）
        new_light = Dot(ORIGIN, color=WHITE, radius=0.01)
        
        self.play(
            Write(rebirth_title),
            GrowFromCenter(new_light),
            run_time=2
        )
        
        # 無限サイクルの象徴（ウロボロス - 永遠の輪廻）
        ouroboros = Circle(
            radius=3,
            color=GOLD,
            stroke_width=8
        )
        
        # 円周上の装飾（生命のシンボル）
        life_symbols = VGroup()
        for i in range(12):
            angle = i * 2 * PI / 12
            symbol = Dot(
                [3 * cos(angle), 3 * sin(angle), 0],
                color=interpolate_color(GREEN, BLUE, i/12),
                radius=0.15
            )
            life_symbols.add(symbol)
        
        self.play(
            Transform(new_light, ouroboros),
            Create(life_symbols),
            run_time=3
        )
        
        # 永遠の回転（輪廻転生）
        eternal_group = VGroup(new_light, life_symbols, rebirth_title)
        self.play(
            Rotating(eternal_group, angle=4*PI),
            eternal_group.animate.set_opacity(0.7),
            run_time=6
        )
        
        # 最終メッセージ
        final_message = VGroup(
            Text("全ては循環する", font_size=32, color=WHITE),
            Text("Everything is Cyclical", font_size=24, color=GRAY),
            Text("∞", font_size=80, color=GOLD)
        )
        
        final_message[0].move_to(UP * 1)
        final_message[1].move_to(ORIGIN)
        final_message[2].move_to(DOWN * 1.5)
        
        self.play(
            Transform(eternal_group, final_message),
            run_time=3
        )
        
        self.wait(3)
        
        # 美しい消失
        self.play(
            final_message.animate.scale(0.1).set_opacity(0),
            run_time=3
        )