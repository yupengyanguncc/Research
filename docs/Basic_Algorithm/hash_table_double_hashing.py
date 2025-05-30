import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch, Ellipse
import os
import random

# 自动生成数据
names = ["Alice", "Bob", "Carol", "David", "Eve", "Frank"]
keys = names
values = [f"{random.randint(100,999)}-{random.randint(1000,9999)}" for _ in names]
bucket_count = 8
colors = ["#6c7ae0", "#b085d6", "#ffb366", "#ff6666", "#4ecdc4", "#f7b32b"]
hash_values = [hash(k) for k in keys]
initial_indices = [hv % bucket_count for hv in hash_values]

def hash2(key):
    # 第二哈希函数，返回与表长互质的正整数
    return 5 + (abs(hash(key)) % (bucket_count - 1))  # 保证与8互质，结果为5~12

# 构建哈希表（使用双重哈希）
table = [None for _ in range(bucket_count)]
table_color = [None for _ in range(bucket_count)]
probe_paths = []
probe_steps = []

for i, (k, v, c, idx, hv) in enumerate(zip(keys, values, colors, initial_indices, hash_values)):
    h2v = hash2(k)
    probe_count = 0
    current_idx = (hv + probe_count * h2v) % bucket_count
    probe_path = [current_idx]
    steps = [f"hash({k}) = {hv}", f"hash2({k}) = {h2v}", f"h({k}) = hash({k}) % {bucket_count} = {hv} % {bucket_count} = {idx}"]
    while table[current_idx] is not None:
        probe_count += 1
        current_idx = (hv + probe_count * h2v) % bucket_count
        probe_path.append(current_idx)
        calc = f"(hash({k}) + {probe_count}*hash2({k})) % {bucket_count} = ({hv} + {probe_count}*{h2v}) % {bucket_count} = {current_idx}"
        steps.append(f"Step {probe_count}: {calc}")
    table[current_idx] = (k, v, c)
    table_color[current_idx] = c
    probe_paths.append(probe_path)
    probe_steps.append(steps)

fig, ax = plt.subplots(figsize=(15, 12))
ax.set_facecolor("white")
plt.xlim(0, 1)
plt.ylim(0, 1)
ax.axis('off')

# 字体设置
font_delta = 3
base_title_font = 14
base_subtitle_font = 10
base_cell_font = 8
base_key_font = 8

title_font = base_title_font + font_delta
subtitle_font = base_subtitle_font + font_delta
cell_font = base_cell_font + font_delta
key_font = base_key_font + font_delta

# 四栏分区
x_keys = 0.13
x_hash = 0.36
x_table = 0.59
x_steps = 0.82

# KEYS 区域
ax.text(x_keys, 0.93, "KEYS", fontsize=title_font, fontweight='bold', color='#6c7ae0', ha='center')
key_y = [0.85 - i*0.12 for i in range(len(keys))]
for i, (key, c) in enumerate(zip(keys, colors)):
    ax.add_patch(Rectangle((x_keys-0.09, key_y[i]-0.07), 0.18, 0.14, color=c, alpha=0.85, ec='white', lw=2))
    ax.text(x_keys, key_y[i], key, ha='center', va='center', fontsize=key_font, color='white', fontweight='bold')

# Hash Function 区域
ax.text(x_hash, 0.93, "Hash Function", fontsize=title_font, fontweight='bold', color='#ffd600', ha='center')
ax.text(x_hash, 0.89, "h(k) = hash(key) % 8, hash2(key)", fontsize=subtitle_font, color='#ffd600', ha='center')
ellipse = Ellipse((x_hash, 0.575), 0.18, 0.18, color='#ffe033', ec='black', lw=3, zorder=2)
ax.add_patch(ellipse)
ax.text(x_hash, 0.575, 'Hash\nFunction', fontsize=key_font, ha='center', va='center', fontweight='bold', color='#222')

# Hash Table 区域
ax.text(x_table, 0.93, 'HASH TABLE', fontsize=title_font, fontweight='bold', color='#6c7ae0', ha='center', alpha=0.8)
ax.text(x_table-0.09, 0.87, 'Index', fontsize=cell_font, fontweight='bold', color='#6c7ae0', ha='center')
ax.text(x_table, 0.87, 'Key', fontsize=cell_font, fontweight='bold', color='#6c7ae0', ha='center')
ax.text(x_table+0.09, 0.87, 'Value', fontsize=cell_font, fontweight='bold', color='#6c7ae0', ha='center')
table_y = [0.85 - i * 0.08 for i in range(bucket_count)]

# 绘制哈希表
for i in range(bucket_count):
    y = table_y[i]
    ax.add_patch(Rectangle((x_table-0.13, y-0.035), 0.08, 0.07, color='#e3eaff', alpha=0.8, ec='white', lw=1))
    ax.text(x_table-0.09, y, f"{i:03}", va='center', ha='center', fontsize=cell_font, color='#6c7ae0', fontweight='bold')
    if table[i]:
        c = table_color[i]
        ax.add_patch(Rectangle((x_table-0.05, y-0.035), 0.09, 0.07, color=c, alpha=0.18, ec=None))
        ax.add_patch(Rectangle((x_table+0.04, y-0.035), 0.09, 0.07, color=c, alpha=0.18, ec=None))
        ax.text(x_table, y, table[i][0], va='center', ha='center', fontsize=cell_font, color='#222', fontweight='bold')
        ax.text(x_table+0.09, y, table[i][1], va='center', ha='center', fontsize=cell_font, color='#222', fontweight='bold')
    else:
        ax.add_patch(Rectangle((x_table-0.05, y-0.035), 0.18, 0.07, color='#f7fafc', alpha=0.5, ec=None))

# 探测步骤说明区域
ax.text(x_steps, 0.93, 'PROBING STEPS', fontsize=title_font, fontweight='bold', color='#ff6666', ha='center')
step_y = [0.85 - i*0.12 for i in range(len(keys))]
for i, (key, c, steps) in enumerate(zip(keys, colors, probe_steps)):
    steps_text = f"Step {i+1}: {key}\n"
    for s in steps:
        steps_text += f"  {s}\n"
    ax.text(x_steps, step_y[i], steps_text, fontsize=cell_font, color='#222', va='top', family='monospace')

# 绘制探测路径
arrow_params = dict(arrowstyle='->', lw=2, color='#888', alpha=0.6)
for i, (key, c, path) in enumerate(zip(keys, colors, probe_paths)):
    ax.add_patch(FancyArrowPatch((x_keys+0.09, key_y[i]), (x_hash-0.09, 0.575), color=c, arrowstyle='simple', lw=4))
    ax.add_patch(FancyArrowPatch((x_hash+0.09, 0.575), (x_table-0.13, table_y[path[0]]), color=c, arrowstyle='simple', lw=4))
    for j in range(len(path)-1):
        start_y = table_y[path[j]]
        end_y = table_y[path[j+1]]
        ax.add_patch(FancyArrowPatch((x_table-0.13, start_y), (x_table-0.13, end_y), **arrow_params))

os.makedirs('assets/image', exist_ok=True)
plt.savefig('assets/image/hash_table_double_hashing.png', bbox_inches='tight', dpi=300)
plt.close() 