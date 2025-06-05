# %%manim -qm BubbleSortScene
from manim import *

#Bubble Sort Visualization  ✨ (digits of 19970923)

def make_box(value: int) -> VGroup:
    square = Square(side_length=1.0, color=BLUE_A)
    label = Text(str(value)).scale(0.7).move_to(square)
    return VGroup(square, label)


class BubbleSortScene(Scene):
    def construct(self):
        # ─────────────────────────────────────────
        # 1.  Data setup
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

class ImprovedBubbleSortScene(Scene):

    # Helper to create a square with a centred digit
    @staticmethod
    def _make_box(value: int) -> VGroup:
        square = Square(side_length=1.0, color=BLUE_A)
        label = Text(str(value)).scale(0.7).move_to(square)
        return VGroup(square, label)

    def construct(self):
        # Data setup ------------------------------------------------------
        values = [1, 9, 9, 7, 0, 9, 2, 3]
        boxes = VGroup(*[self._make_box(v) for v in values])
        boxes.arrange(RIGHT, buff=0.35).to_edge(UP, buff=0.5)
        self.play(LaggedStart(*[FadeIn(b) for b in boxes], lag_ratio=0.05))
        self.wait(0.3)

        #  Pointers and static labels -------------------------------------
        i_ptr = Text("i", color=YELLOW).scale(0.7)
        j_ptr = Text("j", color=GREEN).scale(0.7)
        i_ptr.next_to(boxes[0], DOWN)
        j_ptr.next_to(boxes[0], DOWN)
        self.play(FadeIn(i_ptr, j_ptr))

        pass_label = Text("Pass 1").scale(0.6).to_corner(DOWN + LEFT)
        bound_label = Text(f"n - 1 - i = {len(values) - 1}").scale(0.45)
        bound_label.next_to(boxes, UP, buff=0.25)
        self.play(Write(pass_label), Write(bound_label))
        self.wait(0.3)

        #  Bubble‑sort animation -----------------------------------------
        n = len(values)
        swap_banner = None  # yellow banner shown on first swap of a pass

        for i in range(n):
            if i > 0:
                # Start new pass → move i‑pointer & refresh labels
                self.play(i_ptr.animate.next_to(boxes[i], DOWN), run_time=0.3)
                self.play(
                    Transform(pass_label, Text(f"Pass {i+1}").scale(0.6).to_corner(DOWN + LEFT)),
                    Transform(bound_label, Text(f"n - 1 - i = {n - 1 - i}").scale(0.45).next_to(boxes, UP, buff=0.25)),
                )
                # Fade out previous pass's banner (if any)
                if swap_banner:
                    self.play(FadeOut(swap_banner))
                    swap_banner = None

            # Reset j‑pointer for this pass
            self.play(j_ptr.animate.next_to(boxes[0], DOWN), run_time=0.2)

            swapped = False  # tracks if *any* swap occurred this pass
            for j in range(n - 1 - i):
                self.play(j_ptr.animate.next_to(boxes[j], DOWN), run_time=0.15)
                self.play(Indicate(boxes[j]), Indicate(boxes[j + 1]), run_time=0.25)

                if values[j] > values[j + 1]:
                    # FIRST swap in this pass? show banner once
                    if not swapped:
                        swap_banner = Text("Swap happens", color=YELLOW_E).scale(0.8)
                        swap_banner.to_edge(DOWN, buff=0.3)
                        self.play(Write(swap_banner))
                    swapped = True
                    # Visual swap (direct exchange)
                    pos_a, pos_b = boxes[j].get_center(), boxes[j + 1].get_center()
                    self.play(
                        boxes[j].animate.move_to(pos_b),
                        boxes[j + 1].animate.move_to(pos_a),
                        run_time=0.3,
                    )
                    # Update references
                    boxes[j], boxes[j + 1] = boxes[j + 1], boxes[j]
                    values[j], values[j + 1] = values[j + 1], values[j]

            # Grey out element that’s now in final position
            boxes[n - 1 - i].set_color(GREY_B)

            # Early‑exit check: no swaps in this entire pass
            if not swapped:
                # Remove any lingering swap banner
                if swap_banner:
                    self.play(FadeOut(swap_banner))
                    swap_banner = None
                exit_msg = Text("No swaps → Already sorted!", color=GREEN).scale(0.8)
                exit_msg.to_edge(DOWN, buff=0.3)
                self.play(Write(exit_msg))
                self.wait(0.8)
                self.play(FadeOut(exit_msg))
                break

        # Final "Sorted!" banner ---------------------------------------
        if swap_banner:
            self.play(FadeOut(swap_banner))

        sorted_banner = Text("Sorted!", color=GREEN).scale(1.1)
        sorted_banner.to_edge(DOWN, buff=0.2)
        self.play(Write(sorted_banner))
        self.wait(2)




# ──────────────────────────────────────────────────────────────────────────────
# Exchange Sort Scene
# ──────────────────────────────────────────────────────────────────────────────

class ExchangeSortScene(Scene):

    def construct(self):
        # 1️⃣  Data setup
        values = [1, 9, 9, 7, 0, 9, 2, 3]
        boxes = VGroup(*[make_box(v) for v in values])
        boxes.arrange(RIGHT, buff=0.35).to_edge(UP, buff=0.5)
        self.play(LaggedStart(*[FadeIn(b) for b in boxes], lag_ratio=0.05))
        self.wait(0.3)

        # 2️⃣  Pointers
        i_ptr = Text("i", color=YELLOW).scale(0.7)
        j_ptr = Text("j", color=GREEN).scale(0.7)
        i_ptr.next_to(boxes[0], DOWN)
        j_ptr.next_to(boxes[1], DOWN)
        self.play(FadeIn(i_ptr, j_ptr))

        pass_label = Text("i = 0").scale(0.6).to_corner(DOWN + LEFT)
        self.play(Write(pass_label))
        self.wait(0.3)

        # 3️⃣  Exchange sort animation
        n = len(values)
        for i in range(n - 1):
            if i > 0:
                self.play(i_ptr.animate.next_to(boxes[i], DOWN), run_time=0.3)
                self.play(Transform(pass_label, Text(f"i = {i}").scale(0.6).to_corner(DOWN + LEFT)))

            # Reset j pointer to i+1
            self.play(j_ptr.animate.next_to(boxes[i + 1], DOWN), run_time=0.2)
            for j in range(i + 1, n):
                self.play(j_ptr.animate.next_to(boxes[j], DOWN), run_time=0.15)
                self.play(Indicate(boxes[i]), Indicate(boxes[j]), run_time=0.25)
                if values[i] > values[j]:
                    # Visual swap
                    pos_a, pos_b = boxes[i].get_center(), boxes[j].get_center()
                    self.play(
                        boxes[i].animate.move_to(pos_b), boxes[j].animate.move_to(pos_a), run_time=0.3
                    )
                    boxes[i], boxes[j] = boxes[j], boxes[i]
                    values[i], values[j] = values[j], values[i]

            # Grey out element at i (now in final position)
            boxes[i].set_color(GREY_B)

        # Last element sorted
        boxes[-1].set_color(GREY_B)

        # 4️⃣  Completion banner
        sorted_banner = Text("Sorted!", color=GREEN).scale(1.1)
        sorted_banner.to_edge(DOWN, buff=0.2)
        self.play(Write(sorted_banner))
        self.wait(2)


class InsertionSortScene(Scene):

    def construct(self):
        values = [1, 9, 9, 7, 0, 9, 2, 3]
        boxes = VGroup(*[make_box(v) for v in values])
        boxes.arrange(RIGHT, buff=0.35).to_edge(UP, buff=0.5)
        self.play(LaggedStart(*[FadeIn(b) for b in boxes], lag_ratio=0.05))
        self.wait(0.3)

        i_ptr = Text("i", color=YELLOW).scale(0.7)
        j_ptr = Text("j", color=GREEN).scale(0.7)
        i_ptr.next_to(boxes[1], DOWN)
        j_ptr.next_to(boxes[0], DOWN)
        self.play(FadeIn(i_ptr, j_ptr))

        pass_label = Text("i = 1").scale(0.6).to_corner(DOWN + LEFT)
        self.play(Write(pass_label))
        self.wait(0.3)

        n = len(values)
        for i in range(1, n):
            # Update i pointer and label
            if i > 1:
                self.play(i_ptr.animate.next_to(boxes[i], DOWN), run_time=0.3)
                self.play(Transform(pass_label, Text(f"i = {i}").scale(0.6).to_corner(DOWN + LEFT)))

            # Highlight the key element
            self.play(Indicate(boxes[i]), run_time=0.4)

            j = i - 1
            self.play(j_ptr.animate.next_to(boxes[j], DOWN), run_time=0.2)

            while j >= 0 and values[j] > values[j + 1]:
                # Swap boxes[j] and boxes[j+1]
                pos_a, pos_b = boxes[j].get_center(), boxes[j + 1].get_center()
                self.play(
                    boxes[j].animate.move_to(pos_b), boxes[j + 1].animate.move_to(pos_a), run_time=0.3
                )
                boxes[j], boxes[j + 1] = boxes[j + 1], boxes[j]
                values[j], values[j + 1] = values[j + 1], values[j]
                j -= 1
                if j >= 0:
                    self.play(j_ptr.animate.next_to(boxes[j], DOWN), run_time=0.2)

            # Grey out sorted prefix up to i
            for k in range(i + 1):
                boxes[k].set_color(GREY_B)