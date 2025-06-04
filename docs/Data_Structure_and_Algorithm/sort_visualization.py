%%manim -qm BubbleSortScene
from manim import *

"""Bubble Sort Visualization  ✨ (digits of 19970923)
Quick preview:
    manim -pql bubble_sort_animation.py BubbleSortScene
"""

class BubbleSortScene(Scene):
    def construct(self):
        # ─────────────────────────────────────────
        # 1.  Data setup (8 digits of 19970923)
        # ─────────────────────────────────────────
        values = [1, 9, 9, 7, 0, 9, 2, 3]  # eight numbers to sort

        # Create squares with centered digits
        boxes = VGroup()
        for v in values:
            square = Square(side_length=1.2, color=BLUE_A)
            label = Text(str(v)).move_to(square)
            boxes.add(VGroup(square, label))

        boxes.arrange(RIGHT, buff=0.4).to_edge(UP)
        self.play(LaggedStart(*[FadeIn(b) for b in boxes], lag_ratio=0.05))
        self.wait(0.3)

        # ─────────────────────────────────────────
        # 2.  Pointers and labels
        # ─────────────────────────────────────────
        i_ptr = Text("i", color=YELLOW).scale(0.7)
        j_ptr = Text("j", color=GREEN).scale(0.7)
        i_ptr.next_to(boxes[0], DOWN)
        j_ptr.next_to(boxes[0], DOWN)
        self.play(FadeIn(i_ptr, j_ptr))

        pass_label = Text("Pass 1").to_corner(DOWN + LEFT)
        bound_label = Text(f"n - 1 - i = {len(values) - 1}").scale(0.5)
        bound_label.next_to(boxes, UP)
        self.play(Write(pass_label), Write(bound_label))
        self.wait(0.3)

        # ─────────────────────────────────────────
        # 3.  Bubble‑sort animation
        # ─────────────────────────────────────────
        n = len(values)
        for i in range(n):
            if i > 0:
                # Move i‑pointer right each pass
                self.play(i_ptr.animate.next_to(boxes[i], DOWN), run_time=0.3)
                self.play(
                    Transform(pass_label, Text(f"Pass {i+1}").to_corner(DOWN + LEFT)),
                    Transform(bound_label, Text(f"n - 1 - i = {n - 1 - i}").scale(0.5).next_to(boxes, UP)),
                )

            # Reset j‑pointer
            self.play(j_ptr.animate.next_to(boxes[0], DOWN), run_time=0.2)

            for j in range(n - 1 - i):
                self.play(j_ptr.animate.next_to(boxes[j], DOWN), run_time=0.15)
                self.play(Indicate(boxes[j]), Indicate(boxes[j + 1]), run_time=0.25)

                if values[j] > values[j + 1]:
                    # Swap animation
                    self.play(
                        boxes[j].animate.shift(RIGHT * 1.4),
                        boxes[j + 1].animate.shift(LEFT * 1.4),
                        run_time=0.35,
                    )
                    boxes[j], boxes[j + 1] = boxes[j + 1], boxes[j]
                    values[j], values[j + 1] = values[j + 1], values[j]
                    self.play(boxes.animate.arrange(RIGHT, buff=0.4), run_time=0.2)

            # Grey out sorted element
            boxes[n - 1 - i].set_color(GREY_B)

        # ─────────────────────────────────────────
        # 4.  Completion banner
        # ─────────────────────────────────────────
        self.play(Write(Text("Sorted!", color=GREEN).next_to(boxes, DOWN)))
        self.wait(2)

