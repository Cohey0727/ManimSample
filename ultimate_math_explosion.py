from manim import *
import numpy as np

class UltimateMathExplosion(Scene):
    def construct(self):
        # 🔥 究極のテンション爆上げ数学バトル！ 🔥
        
        # 開幕から爆発！
        self.camera.background_color = BLACK
        
        # 超ド派手オープニング
        mega_title = Text("🔥 ULTIMATE MATH EXPLOSION 🔥", 
                         font_size=48, color=GOLD, weight=BOLD)
        mega_title.set_stroke(RED, width=4)
        
        # 画面全体を埋め尽くす爆発
        self.play(
            Write(mega_title),
            Flash(ORIGIN, color=RED, flash_radius=15, num_lines=100),
            Flash(ORIGIN, color=GOLD, flash_radius=12, num_lines=80),
            Flash(ORIGIN, color=WHITE, flash_radius=10, num_lines=60),
            Flash(ORIGIN, color=BLUE, flash_radius=8, num_lines=40),
            run_time=1
        )
        self.wait(0.5)
        
        # タイトルが爆発して消える
        self.play(
            mega_title.animate.scale(5).set_opacity(0),
            Flash(ORIGIN, color=GOLD, flash_radius=20, num_lines=150),
            run_time=1
        )
        
        # 🌟 超高速数学要素大乱舞！
        
        # 数字軍団が画面を埋め尽くす
        number_army = VGroup()
        for i in range(50):
            num = Text(str(np.random.randint(0, 10)), 
                      font_size=np.random.randint(20, 60),
                      color=interpolate_color(RED, BLUE, np.random.random()))
            num.move_to([
                np.random.uniform(-8, 8),
                np.random.uniform(-4, 4),
                0
            ])
            number_army.add(num)
        
        # 数字軍団大進撃！
        self.play(
            *[FadeIn(num, scale=np.random.uniform(3, 8), 
                    shift=[np.random.uniform(-2, 2), np.random.uniform(-2, 2), 0]) 
              for num in number_army],
            run_time=2
        )
        
        # 数字たちがカオス的に動き回る
        for chaos_round in range(5):
            self.play(
                *[num.animate.move_to([
                    np.random.uniform(-8, 8),
                    np.random.uniform(-4, 4),
                    0
                ]).set_color(interpolate_color(RED, YELLOW, np.random.random()))
                .rotate(np.random.uniform(-PI, PI))
                for num in number_army],
                run_time=0.3
            )
        
        # 💥 大爆発で数字軍団消滅！
        self.play(
            *[FadeOut(num, scale=10) for num in number_army],
            Flash(ORIGIN, color=WHITE, flash_radius=25, num_lines=200),
            Flash([-4, 0, 0], color=RED, flash_radius=8, num_lines=50),
            Flash([4, 0, 0], color=BLUE, flash_radius=8, num_lines=50),
            Flash([0, 3, 0], color=GREEN, flash_radius=8, num_lines=50),
            Flash([0, -3, 0], color=YELLOW, flash_radius=8, num_lines=50),
            run_time=1
        )
        
        # 🎆 超巨大数学記号バトルロイヤル！
        
        # 主要キャラクター超デカサイズで登場
        infinity = Text("∞", font_size=120, color=RED, weight=BOLD)
        pi = Text("π", font_size=100, color=BLUE, weight=BOLD)
        e_char = Text("e", font_size=100, color=GREEN, weight=BOLD)
        phi = Text("φ", font_size=100, color=GOLD, weight=BOLD)
        i_char = Text("i", font_size=100, color=PURPLE, weight=BOLD)
        
        # 配置
        infinity.move_to([0, 0, 0])
        pi.move_to([-4, 2, 0])
        e_char.move_to([4, 2, 0])
        phi.move_to([-4, -2, 0])
        i_char.move_to([4, -2, 0])
        
        # 全員同時に超ド派手登場！
        self.play(
            GrowFromCenter(infinity),
            GrowFromCenter(pi),
            GrowFromCenter(e_char),
            GrowFromCenter(phi),
            GrowFromCenter(i_char),
            Flash(infinity.get_center(), color=RED, flash_radius=10, num_lines=60),
            Flash(pi.get_center(), color=BLUE, flash_radius=6, num_lines=30),
            Flash(e_char.get_center(), color=GREEN, flash_radius=6, num_lines=30),
            Flash(phi.get_center(), color=GOLD, flash_radius=6, num_lines=30),
            Flash(i_char.get_center(), color=PURPLE, flash_radius=6, num_lines=30),
            run_time=2
        )
        
        # 超高速セリフラッシュ
        battle_text = Text("数学最終決戦開始！", font_size=36, color=WHITE, weight=BOLD)
        battle_text.to_edge(DOWN)
        self.play(Write(battle_text), run_time=0.5)
        
        # 🌪️ 超絶怒涛のバトルシーケンス！
        
        for battle_round in range(8):
            # ランダムな攻撃エフェクト
            attacker = np.random.choice([pi, e_char, phi, i_char])
            target = infinity
            
            # 攻撃エフェクト（レーザービーム）
            laser = Line(attacker.get_center(), target.get_center(),
                        color=attacker.color, stroke_width=20)
            
            # 攻撃名表示
            attack_names = [
                "円周波動砲！", "指数爆発！", "黄金螺旋！", "虚数次元斬！",
                "無限連射！", "極限突破！", "調和爆裂！", "複素融合！"
            ]
            attack_name = Text(f"「{np.random.choice(attack_names)}」",
                             font_size=24, color=attacker.color, weight=BOLD)
            attack_name.to_edge(DOWN)
            
            self.play(
                Create(laser),
                Transform(battle_text, attack_name),
                Flash(attacker.get_center(), color=attacker.color, 
                      flash_radius=5, num_lines=25),
                Flash(target.get_center(), color=WHITE, 
                      flash_radius=4, num_lines=20),
                run_time=0.4
            )
            
            # ∞の反撃
            counter_laser = Line(target.get_center(), attacker.get_center(),
                               color=RED, stroke_width=25)
            
            counter_names = [
                "無限拡散破！", "発散爆裂！", "極限崩壊！", "次元破綻！"
            ]
            counter_name = Text(f"「{np.random.choice(counter_names)}」",
                               font_size=24, color=RED, weight=BOLD)
            counter_name.to_edge(DOWN)
            
            self.play(
                Transform(laser, counter_laser),
                Transform(battle_text, counter_name),
                Flash(target.get_center(), color=RED, 
                      flash_radius=6, num_lines=30),
                Flash(attacker.get_center(), color=ORANGE,
                      flash_radius=3, num_lines=15),
                run_time=0.4
            )
            
            # 爆発消失
            self.play(
                FadeOut(laser, scale=5),
                Flash(ORIGIN, color=YELLOW, flash_radius=8, num_lines=40),
                run_time=0.2
            )
            
            # キャラクターがダメージで点滅
            self.play(
                attacker.animate.set_opacity(0.3).scale(0.9),
                run_time=0.1
            )
            self.play(
                attacker.animate.set_opacity(1).scale(1/0.9),
                run_time=0.1
            )
        
        # 🎯 究極のクライマックス！
        
        climax_text = Text("究極合体技発動！", font_size=40, color=GOLD, weight=BOLD)
        self.play(Transform(battle_text, climax_text), run_time=0.5)
        
        # 四大数が合体陣形
        self.play(
            pi.animate.move_to([-2, 1, 0]),
            e_char.animate.move_to([2, 1, 0]),
            phi.animate.move_to([-2, -1, 0]),
            i_char.animate.move_to([2, -1, 0]),
            run_time=1
        )
        
        # オイラーの公式発動！
        euler_formula = Text("e^(iπ) + 1 = 0", font_size=48, color=GOLD, weight=BOLD)
        euler_formula.set_stroke(WHITE, width=3)
        
        self.play(
            Write(euler_formula),
            Flash(ORIGIN, color=GOLD, flash_radius=12, num_lines=80),
            run_time=2
        )
        
        # 宇宙規模の大爆発！
        mega_explosion = VGroup()
        for i in range(30):
            explosion_circle = Circle(
                radius=0.5 + i*0.8,
                stroke_color=interpolate_color(GOLD, RED, i/30),
                stroke_width=10 - i*0.3,
                fill_opacity=0
            )
            mega_explosion.add(explosion_circle)
        
        self.play(
            *[Create(circle) for circle in mega_explosion[:10]],
            Flash(ORIGIN, color=WHITE, flash_radius=30, num_lines=300),
            Flash([-5, 0, 0], color=RED, flash_radius=15, num_lines=100),
            Flash([5, 0, 0], color=BLUE, flash_radius=15, num_lines=100),
            Flash([0, 4, 0], color=GREEN, flash_radius=15, num_lines=100),
            Flash([0, -4, 0], color=YELLOW, flash_radius=15, num_lines=100),
            run_time=1
        )
        
        self.play(
            *[Create(circle) for circle in mega_explosion[10:20]],
            Flash(ORIGIN, color=GOLD, flash_radius=25, num_lines=200),
            run_time=1
        )
        
        self.play(
            *[Create(circle) for circle in mega_explosion[20:]],
            Flash(ORIGIN, color=PURPLE, flash_radius=20, num_lines=150),
            run_time=1
        )
        
        # ∞が浄化される
        purification_text = Text("無限大が浄化された！", font_size=32, color=CYAN, weight=BOLD)
        self.play(Transform(battle_text, purification_text), run_time=1)
        
        self.play(
            infinity.animate.set_color(LIGHT_BLUE).scale(0.8),
            Flash(infinity.get_center(), color=LIGHT_BLUE, flash_radius=8, num_lines=50),
            run_time=2
        )
        
        # 🌈 超感動フィナーレ！
        
        # 全員が友達になる
        friendship_text = Text("みんな友達だ！", font_size=36, color=PINK, weight=BOLD)
        self.play(Transform(battle_text, friendship_text), run_time=1)
        
        # みんなで輪になって踊る
        dance_positions = [
            [3*np.cos(i*2*PI/5), 3*np.sin(i*2*PI/5), 0] 
            for i in range(5)
        ]
        
        characters = [infinity, pi, e_char, phi, i_char]
        
        self.play(
            *[char.animate.move_to(pos) for char, pos in zip(characters, dance_positions)],
            run_time=2
        )
        
        # 回転ダンス
        for dance_round in range(3):
            self.play(
                *[char.animate.rotate(2*PI/3) for char in characters],
                Rotating(VGroup(*characters), angle=2*PI/3, about_point=ORIGIN),
                run_time=1
            )
        
        # 虹色のハートが降る
        hearts = VGroup()
        for i in range(20):
            heart = Text("❤", font_size=30, 
                        color=interpolate_color(RED, PURPLE, i/20))
            heart.move_to([
                np.random.uniform(-6, 6),
                6,
                0
            ])
            hearts.add(heart)
        
        self.play(
            *[heart.animate.move_to([
                heart.get_x(),
                -6,
                0
            ]) for heart in hearts],
            run_time=3
        )
        
        # 最終メッセージ
        final_message = VGroup(
            Text("数学は愛だ！", font_size=48, color=PINK, weight=BOLD),
            Text("MATHEMATICS IS LOVE!", font_size=32, color=WHITE),
            Text("∞ + π + e + φ + i = ❤", font_size=36, color=GOLD)
        )
        final_message.arrange(DOWN, buff=0.5)
        
        # 全てをクリアして最終メッセージ
        self.play(
            FadeOut(VGroup(*characters)),
            FadeOut(euler_formula),
            FadeOut(mega_explosion),
            FadeOut(hearts),
            FadeOut(battle_text),
            run_time=1
        )
        
        self.play(
            Write(final_message),
            Flash(ORIGIN, color=PINK, flash_radius=15, num_lines=100),
            run_time=3
        )
        
        # 最後の最後に超ド派手爆発
        for final_explosion in range(5):
            self.play(
                Flash(ORIGIN, color=interpolate_color(RED, GOLD, final_explosion/5), 
                      flash_radius=20-final_explosion*2, num_lines=80-final_explosion*10),
                final_message.animate.scale(1.1),
                run_time=0.5
            )
            self.play(
                final_message.animate.scale(1/1.1),
                run_time=0.5
            )
        
        # スーパー最終爆発！
        self.play(
            Flash(ORIGIN, color=WHITE, flash_radius=50, num_lines=500),
            Flash(ORIGIN, color=GOLD, flash_radius=40, num_lines=400),
            Flash(ORIGIN, color=RED, flash_radius=30, num_lines=300),
            Flash(ORIGIN, color=BLUE, flash_radius=20, num_lines=200),
            final_message.animate.scale(2).set_opacity(0.8),
            run_time=2
        )
        
        self.wait(3)
        
        # THE END
        the_end = Text("🔥 THE END 🔥", font_size=60, color=GOLD, weight=BOLD)
        the_end.set_stroke(RED, width=4)
        
        self.play(
            Write(the_end),
            FadeOut(final_message),
            Flash(ORIGIN, color=GOLD, flash_radius=25, num_lines=150),
            run_time=2
        )
        
        self.wait(2)