from manim import *
import numpy as np

class WarfareTest(Scene):
    def construct(self):
        # タイトル
        title = Text("MATHEMATICAL WARFARE", font_size=60, color=GOLD)
        subtitle = Text("THE EPIC SAGA", font_size=36, color=WHITE)
        subtitle.next_to(title, DOWN, buff=0.5)
        
        self.play(
            Write(title),
            Flash(ORIGIN, color=GOLD, flash_radius=8, num_lines=50),
            run_time=2
        )
        self.play(Write(subtitle), run_time=1)
        self.wait(1)
        self.play(FadeOut(title), FadeOut(subtitle))
        
        # 無限大の覚醒
        infinity = Text("∞", font_size=80, color=RED)
        
        awakening_text = Text("「俺の時代が来た！」", 
                            font_size=32, color=RED)
        awakening_text.to_edge(DOWN)
        
        self.play(
            GrowFromCenter(infinity),
            Write(awakening_text),
            Flash(ORIGIN, color=RED, flash_radius=6, num_lines=30),
            run_time=3
        )
        
        # 三大定数登場
        pi_hero = Text("π", font_size=48, color=BLUE).move_to([-2, -1, 0])
        e_hero = Text("e", font_size=48, color=GREEN).move_to([0, -1, 0])  
        phi_hero = Text("φ", font_size=48, color=GOLD).move_to([2, -1, 0])
        
        heroes_text = Text("三大定数同盟結成！", font_size=24, color=WHITE)
        heroes_text.to_edge(DOWN)
        
        self.play(
            Transform(awakening_text, heroes_text),
            FadeIn(pi_hero, scale=2),
            FadeIn(e_hero, scale=2), 
            FadeIn(phi_hero, scale=2),
            Flash(ORIGIN, color=WHITE, flash_radius=5, num_lines=25),
            run_time=2
        )
        
        # 戦闘開始
        battle_text = Text("「数学王国の平和のために！」", 
                          font_size=20, color=WHITE)
        self.play(Transform(awakening_text, battle_text), run_time=1)
        
        # 爆発エフェクト
        self.play(
            Flash(pi_hero.get_center(), color=BLUE, flash_radius=3, num_lines=15),
            Flash(e_hero.get_center(), color=GREEN, flash_radius=3, num_lines=15),
            Flash(phi_hero.get_center(), color=GOLD, flash_radius=3, num_lines=15),
            Flash(infinity.get_center(), color=RED, flash_radius=4, num_lines=20),
            run_time=2
        )
        
        # 結果
        result_text = Text("激戦が続く...", font_size=32, color=WHITE)
        self.play(Transform(awakening_text, result_text), run_time=1)
        self.wait(2)
        
        # To Be Continued
        tbc = Text("To Be Continued...", font_size=36, color=GOLD)
        self.play(
            Write(tbc),
            FadeOut(infinity),
            FadeOut(pi_hero),
            FadeOut(e_hero),
            FadeOut(phi_hero),
            FadeOut(awakening_text),
            run_time=2
        )
        self.wait(2)