from manim import *
import numpy as np

class MegaMathBattle(Scene):
    def construct(self):
        # 🔥 超絶テンション爆上げ数学バトル！ 🔥
        
        # 開幕大爆発！
        self.camera.background_color = BLACK
        
        # 超ド派手タイトル
        title = Text("🔥 MEGA MATH BATTLE 🔥", 
                    font_size=48, color=GOLD, weight=BOLD)
        
        # 5連続爆発でオープニング
        self.play(
            Write(title),
            Flash(ORIGIN, color=RED, flash_radius=15, num_lines=100),
            run_time=1
        )
        self.play(Flash(ORIGIN, color=GOLD, flash_radius=12, num_lines=80), run_time=0.3)
        self.play(Flash(ORIGIN, color=WHITE, flash_radius=10, num_lines=60), run_time=0.3)
        self.play(Flash(ORIGIN, color=BLUE, flash_radius=8, num_lines=40), run_time=0.3)
        self.play(Flash(ORIGIN, color=GREEN, flash_radius=6, num_lines=30), run_time=0.3)
        
        # タイトル爆発消失
        self.play(
            title.animate.scale(8).set_opacity(0),
            Flash(ORIGIN, color=GOLD, flash_radius=20, num_lines=120),
            run_time=1
        )
        
        # 🎆 キャラクター超ド派手登場
        
        # 悪役∞登場
        infinity = Text("∞", font_size=100, color=RED, weight=BOLD)
        villain_text = Text("「俺が全てを支配する！」", font_size=24, color=RED, weight=BOLD)
        villain_text.to_edge(DOWN)
        
        self.play(
            GrowFromCenter(infinity),
            Write(villain_text),
            Flash(ORIGIN, color=RED, flash_radius=10, num_lines=60),
            run_time=2
        )
        
        # ヒーロー軍団登場！
        pi_hero = Text("π", font_size=80, color=BLUE, weight=BOLD).move_to([-3, -1, 0])
        e_hero = Text("e", font_size=80, color=GREEN, weight=BOLD).move_to([-1, -1, 0])
        phi_hero = Text("φ", font_size=80, color=GOLD, weight=BOLD).move_to([1, -1, 0])
        i_hero = Text("i", font_size=80, color=PURPLE, weight=BOLD).move_to([3, -1, 0])
        
        hero_text = Text("「数学の平和を守る！」", font_size=24, color=WHITE, weight=BOLD)
        
        self.play(
            Transform(villain_text, hero_text),
            GrowFromCenter(pi_hero),
            GrowFromCenter(e_hero),
            GrowFromCenter(phi_hero),
            GrowFromCenter(i_hero),
            Flash(pi_hero.get_center(), color=BLUE, flash_radius=5, num_lines=25),
            Flash(e_hero.get_center(), color=GREEN, flash_radius=5, num_lines=25),
            Flash(phi_hero.get_center(), color=GOLD, flash_radius=5, num_lines=25),
            Flash(i_hero.get_center(), color=PURPLE, flash_radius=5, num_lines=25),
            run_time=2
        )
        
        # 🌪️ 超高速バトルシーケンス
        
        heroes = [pi_hero, e_hero, phi_hero, i_hero]
        attack_names = [
            "円周波動砲！", "指数爆発波！", "黄金螺旋砲！", "虚数次元砲！"
        ]
        
        battle_text = Text("バトル開始！", font_size=32, color=WHITE, weight=BOLD)
        self.play(Transform(villain_text, battle_text), run_time=0.5)
        
        # 10連続攻撃！
        for round_num in range(10):
            # ランダムヒーローが攻撃
            attacker = np.random.choice(heroes)
            attack_idx = heroes.index(attacker)
            attack_name = attack_names[attack_idx]
            
            # 攻撃テキスト
            attack_text = Text(f"「{attack_name}」", 
                             font_size=20, color=attacker.color, weight=BOLD)
            attack_text.to_edge(DOWN)
            
            # 攻撃エフェクト
            self.play(
                Transform(villain_text, attack_text),
                Flash(attacker.get_center(), color=attacker.color, 
                      flash_radius=4, num_lines=20),
                Flash(infinity.get_center(), color=WHITE, 
                      flash_radius=3, num_lines=15),
                attacker.animate.scale(1.2),
                infinity.animate.rotate(PI/6),
                run_time=0.4
            )
            
            # ∞の反撃
            counter_attacks = [
                "無限拡散破！", "発散爆裂！", "極限崩壊！", "次元破綻！", "無限連射！"
            ]
            counter_name = np.random.choice(counter_attacks)
            counter_text = Text(f"「{counter_name}」", 
                               font_size=20, color=RED, weight=BOLD)
            counter_text.to_edge(DOWN)
            
            self.play(
                Transform(villain_text, counter_text),
                Flash(infinity.get_center(), color=RED, 
                      flash_radius=5, num_lines=25),
                Flash(attacker.get_center(), color=ORANGE,
                      flash_radius=2, num_lines=10),
                infinity.animate.scale(1.1),
                attacker.animate.scale(1/1.2),
                run_time=0.4
            )
            
            # リセット
            self.play(infinity.animate.scale(1/1.1), run_time=0.1)
        
        # 🎯 決定的瞬間！
        
        crisis_text = Text("ピンチ！ヒーロー劣勢！", font_size=28, color=ORANGE, weight=BOLD)
        self.play(Transform(villain_text, crisis_text), run_time=0.8)
        
        # ヒーローたちがダメージ
        self.play(
            *[hero.animate.set_opacity(0.5).scale(0.8) for hero in heroes],
            Flash(ORIGIN, color=RED, flash_radius=8, num_lines=40),
            run_time=1
        )
        
        # 合体技の時間！
        unity_text = Text("「みんなで力を合わせよう！」", font_size=24, color=CYAN, weight=BOLD)
        self.play(Transform(villain_text, unity_text), run_time=1)
        
        # ヒーローたち復活＆パワーアップ
        self.play(
            *[hero.animate.set_opacity(1).scale(1.5/0.8).set_color(WHITE) 
              for hero in heroes],
            Flash(ORIGIN, color=WHITE, flash_radius=12, num_lines=80),
            run_time=2
        )
        
        # 究極合体技発動！
        ultimate_text = Text("「究極合体技発動！」", font_size=32, color=GOLD, weight=BOLD)
        self.play(Transform(villain_text, ultimate_text), run_time=1)
        
        # オイラーの公式
        euler = Text("e^(iπ) + 1 = 0", font_size=48, color=GOLD, weight=BOLD)
        euler.set_stroke(WHITE, width=3)
        
        self.play(
            Write(euler),
            Flash(ORIGIN, color=GOLD, flash_radius=15, num_lines=100),
            run_time=2
        )
        
        # 最終決戦！
        final_battle_text = Text("「これで決着だ！」", font_size=28, color=WHITE, weight=BOLD)
        self.play(Transform(villain_text, final_battle_text), run_time=0.8)
        
        # 連続大爆発！
        for explosion_round in range(8):
            colors = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE, PINK, WHITE]
            self.play(
                Flash(ORIGIN, color=colors[explosion_round], 
                      flash_radius=15-explosion_round, num_lines=80-explosion_round*5),
                infinity.animate.rotate(PI/4).scale(0.95),
                run_time=0.3
            )
        
        # ∞の改心
        redemption_text = Text("「俺も...仲間になりたかった...」", 
                              font_size=24, color=LIGHT_BLUE, weight=BOLD)
        self.play(Transform(villain_text, redemption_text), run_time=1.5)
        
        self.play(
            infinity.animate.set_color(LIGHT_BLUE).scale(0.8),
            Flash(infinity.get_center(), color=LIGHT_BLUE, flash_radius=6, num_lines=30),
            run_time=2
        )
        
        # 🌈 感動のフィナーレ
        
        friendship_text = Text("「みんな友達だ！」", font_size=32, color=PINK, weight=BOLD)
        self.play(Transform(villain_text, friendship_text), run_time=1)
        
        # 全員集合！
        all_characters = heroes + [infinity]
        positions = [
            [2.5*np.cos(i*2*PI/5 - PI/2), 2.5*np.sin(i*2*PI/5 - PI/2), 0]
            for i in range(5)
        ]
        
        self.play(
            *[char.animate.move_to(pos).set_color(interpolate_color(RED, BLUE, i/5))
              for i, (char, pos) in enumerate(zip(all_characters, positions))],
            FadeOut(euler),
            run_time=2
        )
        
        # 友情の回転ダンス
        for dance_round in range(4):
            self.play(
                Rotating(VGroup(*all_characters), angle=PI/2, about_point=ORIGIN),
                *[char.animate.rotate(PI/2) for char in all_characters],
                Flash(ORIGIN, color=interpolate_color(RED, BLUE, dance_round/4), 
                      flash_radius=6, num_lines=30),
                run_time=0.8
            )
        
        # 最終メッセージ
        self.play(
            FadeOut(VGroup(*all_characters)),
            FadeOut(villain_text),
            run_time=1
        )
        
        final_message = VGroup(
            Text("🔥 数学は友情だ！ 🔥", font_size=40, color=GOLD, weight=BOLD),
            Text("MATH IS FRIENDSHIP!", font_size=28, color=WHITE),
            Text("π + e + φ + i + ∞ = ❤", font_size=32, color=PINK)
        )
        final_message.arrange(DOWN, buff=0.5)
        
        self.play(
            Write(final_message),
            Flash(ORIGIN, color=PINK, flash_radius=12, num_lines=80),
            run_time=2
        )
        
        # ラストスパート大爆発祭り！
        for final_round in range(6):
            colors = [RED, GOLD, WHITE, BLUE, GREEN, PURPLE]
            self.play(
                Flash(ORIGIN, color=colors[final_round], 
                      flash_radius=18-final_round*2, num_lines=100-final_round*10),
                final_message.animate.scale(1.1).rotate(PI/12),
                run_time=0.4
            )
            self.play(
                final_message.animate.scale(1/1.1).rotate(-PI/12),
                run_time=0.2
            )
        
        # THE END爆発
        the_end = Text("🔥 THE END 🔥", font_size=60, color=GOLD, weight=BOLD)
        the_end.set_stroke(RED, width=4)
        
        self.play(
            Write(the_end),
            FadeOut(final_message),
            Flash(ORIGIN, color=GOLD, flash_radius=25, num_lines=150),
            Flash([-6, 0, 0], color=RED, flash_radius=10, num_lines=50),
            Flash([6, 0, 0], color=BLUE, flash_radius=10, num_lines=50),
            Flash([0, 4, 0], color=GREEN, flash_radius=10, num_lines=50),
            Flash([0, -4, 0], color=PURPLE, flash_radius=10, num_lines=50),
            run_time=3
        )
        
        self.wait(2)