import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random

words = ['"hello"', '"bye"', '"world"']
ascii_lists = [
    [104, 101, 108, 108, 111],
    [98, 121, 101],
    [119, 111, 114, 108, 100]
]
sums = [sum(lst) for lst in ascii_lists]
mod = 7
modded = [v % mod for v in sums]
counts = [random.randint(1, 5) for _ in words]

fig, ax = plt.subplots(figsize=(10, 5))
ax.axis('off')

y_start = 2.2
y_gap = 0.9
box_w = 0.7
box_h = 0.5

# Draw hash calculation for each word
for idx, (word, ascii_vals, total, mod_val, count) in enumerate(zip(words, ascii_lists, sums, modded, counts)):
    y = y_start - idx * y_gap
    # Draw character boxes and ASCII values
    for i, (c, v) in enumerate(zip(word.replace('"', ''), ascii_vals)):
        rect = patches.FancyBboxPatch(
            (i * (box_w + 0.1), y), box_w, box_h,
            boxstyle="round,pad=0.05", edgecolor='#FFA726', facecolor='white', lw=2
        )
        ax.add_patch(rect)
        ax.text(i * (box_w + 0.1) + box_w/2, y + box_h*0.65, c, ha='center', va='center', fontsize=14)
        ax.text(i * (box_w + 0.1) + box_w/2, y + box_h*0.18, str(v), ha='center', va='center', fontsize=9, color='gray')
    # Draw sum and mod result
    x_sum = len(word.replace('"', '')) * (box_w + 0.1) - 0.1
    ax.text(x_sum + 0.5, y + box_h*0.65, f"SUM = {total}", fontsize=12, color='#D32F2F', va='center', fontweight='bold')
    ax.text(x_sum + 2.0, y + box_h*0.65, f"SUM % {mod} = {mod_val}", fontsize=12, color='#388E3C', va='center', fontweight='bold')

# Title
ax.text(0, y_start + 0.6, f"Hash Function with Modulo {mod} (Prime)", fontsize=15, fontweight='bold')

# Code block at the bottom
code = (
    f"int h(String k, int size) {{\n"
    f"    int total = 0;\n"
    f"    for (int i = 0; i < k.length(); i++)\n"
    f"        total += (int)k.charAt(i);\n"
    f"    return total % {mod};\n"
    f"}}"
)
code_y = -0.2
ax.text(0, code_y, code, fontsize=10, family='monospace', va='top', bbox=dict(facecolor='#F5F5F5', edgecolor='#BDBDBD', boxstyle='round,pad=0.3'))

# Draw the hash table array well below the code block
array_y = code_y - 3 # Move array further down
slot_w = 1.2
slot_h = 0.7
for i in range(mod):
    rect = patches.FancyBboxPatch((i * (slot_w + 0.1), array_y), slot_w, slot_h,
                                  boxstyle="round,pad=0.05", edgecolor='#1976D2', facecolor='white', lw=2)
    ax.add_patch(rect)
    ax.text(i * (slot_w + 0.1) + slot_w/2, array_y + slot_h + 0.05, str(i), ha='center', va='bottom', fontsize=12, color='#1976D2')

# Place each word in its slot with count, using a line between key and value
for word, mod_val, count in zip(words, modded, counts):
    x = mod_val * (slot_w + 0.1) + slot_w/2
    # Draw a horizontal line between key and value
    ax.text(x, array_y + slot_h*0.65, word, ha='center', va='center', fontsize=12, color='#388E3C', fontweight='bold')
    ax.plot([x-0.35, x+0.35], [array_y + slot_h*0.5, array_y + slot_h*0.5], color='#BDBDBD', lw=1)
    ax.text(x, array_y + slot_h*0.35, f"{count}", ha='center', va='center', fontsize=12, color='#D32F2F', fontweight='bold')

#ax.text(0, array_y + slot_h + 0.5, "Hash Table (Array): Each slot shows key — value", fontsize=12, color='#1976D2')

plt.xlim(-0.5, mod * (slot_w + 0.1) + 1)
plt.ylim(array_y - 1.2, y_start + 1)
plt.tight_layout()
plt.savefig('hash_function_mod_visual.png', dpi=180)
plt.show()