import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch, Ellipse
import os

# 数据
keys = ["Yupeng", "Yiru", "Love", "Rainy"]
values = ["323-3323", "123-1234", "231-3321", "333-3212"]
bucket_count = 8
colors = ["#6c7ae0", "#b085d6", "#ffb366", "#ff6666"]
indices = [4, 6, 7, 6]  # Rainy 和 Yiru 冲突

# 构建哈希表（支持冲突，桶为列表）
table = [[] for _ in range(bucket_count)]
table_color = [[] for _ in range(bucket_count)]
for k, v, c, idx in zip(keys, values, colors, indices):
    table[idx].append((k, v, c))
    table_color[idx].append(c)

fig, ax = plt.subplots(figsize=(15, 6))
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

# 三栏分区
x_keys = 0.17
x_hash = 0.5
x_table = 0.83

# KEYS 区域
ax.text(x_keys, 0.93, "KEYS", fontsize=title_font, fontweight='bold', color='#6c7ae0', ha='center')
key_y = [0.8, 0.65, 0.5, 0.35]
for i, (key, c) in enumerate(zip(keys, colors)):
    ax.add_patch(Rectangle((x_keys-0.09, key_y[i]-0.07), 0.18, 0.14, color=c, alpha=0.85, ec='white', lw=2))
    ax.text(x_keys, key_y[i], key, ha='center', va='center', fontsize=key_font, color='white', fontweight='bold')

# Hash Function 区域
ax.text(x_hash, 0.93, "Hash Function", fontsize=title_font, fontweight='bold', color='#ffd600', ha='center')
ax.text(x_hash, 0.89, "maps a key to an index for storing the key's value", fontsize=subtitle_font, color='#ffd600', ha='center')
ellipse = Ellipse((x_hash, 0.575), 0.18, 0.18, color='#ffe033', ec='black', lw=3, zorder=2)
ax.add_patch(ellipse)
ax.text(x_hash, 0.575, 'Hash\nFunction', fontsize=key_font, ha='center', va='center', fontweight='bold', color='#222')

# Hash Table 区域
ax.text(x_table, 0.93, 'HASH TABLE', fontsize=title_font, fontweight='bold', color='#6c7ae0', ha='center', alpha=0.8)
ax.text(x_table-0.09, 0.87, 'Index', fontsize=cell_font, fontweight='bold', color='#6c7ae0', ha='center')
ax.text(x_table, 0.87, 'Key', fontsize=cell_font, fontweight='bold', color='#6c7ae0', ha='center')
ax.text(x_table+0.09, 0.87, 'Value', fontsize=cell_font, fontweight='bold', color='#6c7ae0', ha='center')
table_y = [0.8 - i * 0.08 for i in range(bucket_count)]
for i in range(bucket_count):
    y = table_y[i]
    # index色块
    ax.add_patch(Rectangle((x_table-0.13, y-0.035), 0.08, 0.07, color='#e3eaff', alpha=0.8, ec='white', lw=1))
    ax.text(x_table-0.09, y, f"{i:03}", va='center', ha='center', fontsize=cell_font, color='#6c7ae0', fontweight='bold')
    # key-value色块
    if table[i]:
        for j, (k, v, c) in enumerate(table[i]):
            y_offset = y + (j-0.5*(len(table[i])-1))*0.04  # 多个冲突时上下错开
            ax.add_patch(Rectangle((x_table-0.05, y_offset-0.02), 0.09, 0.04, color=c, alpha=0.18, ec=None))
            ax.add_patch(Rectangle((x_table+0.04, y_offset-0.02), 0.09, 0.04, color=c, alpha=0.18, ec=None))
            ax.text(x_table, y_offset, k, va='center', ha='center', fontsize=cell_font, color='#222', fontweight='bold')
            ax.text(x_table+0.09, y_offset, v, va='center', ha='center', fontsize=cell_font, color='#222', fontweight='bold')
        # 如果有冲突（entry数大于1），加红色边框
        if len(table[i]) > 1:
            y_offsets = [y + (j-0.5*(len(table[i])-1))*0.04 for j in range(len(table[i]))]
            y_top = max(y_offsets) + 0.02
            y_bot = min(y_offsets) - 0.02
            ax.add_patch(Rectangle((x_table-0.05, y_bot), 0.18, y_top-y_bot, fill=False, ec='red', lw=2, zorder=10))
    else:
        ax.add_patch(Rectangle((x_table-0.05, y-0.035), 0.18, 0.07, color='#f7fafc', alpha=0.5, ec=None))

# 箭头参数
arrow_params = dict(arrowstyle='simple', lw=4)
for i, (c, idx) in enumerate(zip(colors, indices)):
    # key -> hash function
    ax.add_patch(FancyArrowPatch((x_keys+0.09, key_y[i]), (x_hash-0.09, 0.575), color=c, **arrow_params))
    # hash function -> table
    y_table = table_y[idx]
    ax.add_patch(FancyArrowPatch((x_hash+0.09, 0.575), (x_table-0.13, y_table), color=c, **arrow_params))

os.makedirs('assets/image', exist_ok=True)
plt.savefig('assets/image/hash_table_collision.png', bbox_inches='tight', dpi=300)
plt.close()
