%%manim -qm BinarySearchScene
from manim import *

# ---------- helper ---------- #
def make_box(val, side=1):
    box = Square(side_length=side, color=WHITE)
    txt = Text(str(val), font_size=32)
    txt.move_to(box.get_center())
    return VGroup(box, txt)

# ---------- constants ---------- #
CLR_LOW   = BLUE
CLR_HIGH  = YELLOW
CLR_MID   = RED
CLR_FOUND = GREEN

class BinarySearchScene(Scene):
    def construct(self):
        # Sorted array (digits of 19970923)
        values = [0, 1, 2, 3, 4,5,7, 9, 9, 9]
        target = 2

        boxes = VGroup(*[make_box(v) for v in values])
        boxes.arrange(RIGHT, buff=0.35)
        boxes.to_edge(UP, buff=1.5)
        self.play(LaggedStart(*[FadeIn(b) for b in boxes], lag_ratio=0.05))
        self.wait(0.3)

        # Search caption
        caption = Text(f"Looking for {target}", font_size=28)
        caption.to_corner(DOWN + LEFT)
        self.play(Write(caption))

        # Pointer labels
        low_lbl  = Text("low",  color=CLR_LOW  ).scale(0.6)
        high_lbl = Text("high", color=CLR_HIGH ).scale(0.6)
        mid_lbl  = Text("mid",  color=CLR_MID  ).scale(0.6)

        self.add(low_lbl, high_lbl, mid_lbl)

        # Initial positions
        low, high = 0, len(values) - 1
        low_lbl.next_to(boxes[low],  DOWN)
        high_lbl.next_to(boxes[high], DOWN)
        mid = (low + high) // 2
        mid_lbl.next_to(boxes[mid],  DOWN)
        self.play(FadeIn(low_lbl), FadeIn(high_lbl), FadeIn(mid_lbl))

        while low <= high:
            mid = (low + high) // 2
            # Move mid pointer
            self.play(mid_lbl.animate.next_to(boxes[mid], DOWN), run_time=0.3)
            self.play(Indicate(boxes[mid]), run_time=0.4)

            if values[mid] == target:
                boxes[mid].set_color(CLR_FOUND)
                found_text = Text(f"Found {target} at index {mid}", color=CLR_FOUND).scale(0.8)
                found_text.next_to(boxes, DOWN, buff=0.9)
                self.play(Write(found_text))
                break
            elif values[mid] < target:
                low = mid + 1
                self.play(low_lbl.animate.next_to(boxes[low], DOWN), run_time=0.3)
            else:
                high = mid - 1
                self.play(high_lbl.animate.next_to(boxes[high], DOWN), run_time=0.3)

        # Clean-up pointers
        self.play(FadeOut(low_lbl), FadeOut(high_lbl), FadeOut(mid_lbl))
        self.wait(2)