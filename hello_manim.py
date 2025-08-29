from manim import *

class HelloManim(Scene):
    def construct(self):
        # テキストを作成
        text = Text("Hello, Manim!", font_size=48, color=BLUE)
        
        # 別のテキストを作成
        subtitle = Text("uvで環境構築成功！", font_size=32, color=GREEN)
        subtitle.next_to(text, DOWN, buff=1)
        
        # アニメーション
        self.play(Write(text))
        self.wait(1)
        self.play(Write(subtitle))
        self.wait(2)
        
        # 図形を描く
        circle = Circle(radius=2, color=BLUE)
        square = Square(side_length=3, color=RED)
        triangle = Triangle(color=YELLOW)
        
        # 全てをクリアして新しいアニメーション
        self.clear()
        
        # 図形を順番に表示
        self.play(Create(circle))
        self.wait(1)
        self.play(Transform(circle, square))
        self.wait(1)
        self.play(Transform(circle, triangle))
        self.wait(1)
        
        # 回転アニメーション
        self.play(Rotate(circle, angle=2*PI, run_time=3))
        self.wait(1)