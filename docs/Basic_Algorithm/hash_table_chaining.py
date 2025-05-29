import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch, Ellipse
import os

# 数据
keys = ["Yupeng", "Yiru", "Love", "Rainy"]
values = ["323-3323", "123-1234", "231-3321", "333-3212"]
bucket_count = 8
colors = ["#6c7ae0", "#b085d6", "#ffb366", "#ff6666"]
indices = [4, 6, 7, 6]  # Rainy 和 Yiru 冲突

# 构建哈希表（链地址法，桶为链表/列表）
table = [[] for _ in range(bucket_count)]
for k, v, c, idx in zip(keys, values, colors, indices):
    table[idx].append((k, v, c))

fig, ax = plt.subplots(figsize=(18, 6))
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
x_chain = 0.82

# KEYS 区域
ax.text(x_keys, 0.93, "KEYS", fontsize=title_font, fontweight='bold', color='#6c7ae0', ha='center')
key_y = [0.8, 0.65, 0.5, 0.35]
for i, (key, c, idx) in enumerate(zip(keys, colors, indices)):
    is_conflict = (idx == conflict_idx)
    color = c if is_conflict else '#cccccc'
    alpha = 0.85 if is_conflict else 0.18
    text_color = 'white' if is_conflict else '#888888'
    text_alpha = 1 if is_conflict else 0.5
    ax.add_patch(Rectangle((x_keys-0.09, key_y[i]-0.07), 0.18, 0.14, color=color, alpha=alpha, ec='white', lw=2, zorder=2))
    ax.text(x_keys, key_y[i], key, ha='center', va='center', fontsize=key_font, color=text_color, fontweight='bold', alpha=text_alpha, zorder=3)

# Hash Function 区域
ax.text(x_hash, 0.93, "Hash Function", fontsize=title_font, fontweight='bold', color='#ffd600', ha='center')
ellipse = Ellipse((x_hash, 0.575), 0.18, 0.18, color='#ffe033', ec='black', lw=3, zorder=2, alpha=1)
ax.add_patch(ellipse)
ax.text(x_hash, 0.575, 'Hash\nFunction', fontsize=key_font, ha='center', va='center', fontweight='bold', color='#222')

# Hash Table 区域
ax.text(x_table, 0.93, 'HASH TABLE', fontsize=title_font, fontweight='bold', color='#6c7ae0', ha='center', alpha=0.8)
ax.text(x_table-0.09, 0.87, 'Index', fontsize=cell_font, fontweight='bold', color='#6c7ae0', ha='center')
ax.text(x_table, 0.87, 'Key', fontsize=cell_font, fontweight='bold', color='#6c7ae0', ha='center')
ax.text(x_table+0.09, 0.87, 'Value', fontsize=cell_font, fontweight='bold', color='#6c7ae0', ha='center')
table_y = [0.8 - i * 0.08 for i in range(bucket_count)]
# 先找到冲突桶的索引，供后续高亮判断使用
detected_conflict_idx = None
for i in range(bucket_count):
    if len(table[i]) > 1:
        detected_conflict_idx = i
        break
conflict_idx = detected_conflict_idx
for i in range(bucket_count):
    y = table_y[i]
    ax.add_patch(Rectangle((x_table-0.13, y-0.035), 0.08, 0.07, color='#e3eaff', alpha=0.8, ec='white', lw=1))
    ax.text(x_table-0.09, y, f"{i:03}", va='center', ha='center', fontsize=cell_font, color='#6c7ae0', fontweight='bold')
    if table[i]:
        if len(table[i]) > 1:
            ax.add_patch(Rectangle((x_table-0.05, y-0.02), 0.18, 0.04, fill=False, ec='red', lw=4, zorder=20))
        else:
            k, v, c = table[i][0]
            is_conflict = (i == conflict_idx)
            color = c if is_conflict else '#cccccc'
            alpha = 0.18 if is_conflict else 0.10
            text_color = '#222' if is_conflict else '#888888'
            text_alpha = 1 if is_conflict else 0.5
            ax.add_patch(Rectangle((x_table-0.05, y-0.02), 0.09, 0.04, color=color, alpha=alpha, ec=None, zorder=2))
            ax.add_patch(Rectangle((x_table+0.04, y-0.02), 0.09, 0.04, color=color, alpha=alpha, ec=None, zorder=2))
            ax.text(x_table, y, k, va='center', ha='center', fontsize=cell_font, color=text_color, fontweight='bold', alpha=text_alpha, zorder=3)
            ax.text(x_table+0.09, y, v, va='center', ha='center', fontsize=cell_font, color=text_color, fontweight='bold', alpha=text_alpha, zorder=3)
    else:
        ax.add_patch(Rectangle((x_table-0.05, y-0.035), 0.18, 0.07, color='#f7fafc', alpha=0.5, ec=None))

# 恢复 KEYS 到 Hash Function、Hash Function 到 Hash Table 的三条彩色线，但只高亮冲突相关，其余虚化
arrow_params = dict(arrowstyle='simple', lw=4)
for i, (c, idx) in enumerate(zip(colors, indices)):
    is_conflict = (idx == conflict_idx)
    color = c if is_conflict else '#cccccc'
    alpha = 1 if is_conflict else 0.18
    ax.add_patch(FancyArrowPatch((x_keys+0.09, key_y[i]), (x_hash-0.09, 0.575), color=color, alpha=alpha, **arrow_params))
    y_table = table_y[idx]
    ax.add_patch(FancyArrowPatch((x_hash+0.09, 0.575), (x_table-0.13, y_table), color=color, alpha=alpha, **arrow_params))

# LINKED CHAIN 区域
ax.text(x_chain, 0.93, 'LINKED CHAIN', fontsize=title_font, fontweight='bold', color='#ff6666', ha='center')
if conflict_idx is not None:
    y = table_y[conflict_idx]
    node_width = 0.10
    node_height = 0.12  # 表格更高
    node_gap = 0.055  # 更紧凑
    chain_node_count = len(table[conflict_idx])
    chain_total_width = node_width * chain_node_count + node_gap * (chain_node_count - 1)
    chain_x_start = x_table - 0.05 + 0.18 + 0.03  # 红框最右端+一点间隔
    # 灰色线从红框最右端到第一个链表节点最左侧
    arrow_start = x_table - 0.05 + 0.18
    arrow_end = chain_x_start
    ax.add_patch(FancyArrowPatch((arrow_start, y), (arrow_end, y), color='#888', arrowstyle='->', lw=2.5, zorder=19))
    for j, (k, v, c) in enumerate(table[conflict_idx]):
        x_node = chain_x_start + j*(node_width + node_gap)
        ax.add_patch(Rectangle((x_node, y-node_height/2), node_width, node_height, color=c, alpha=0.18, ec=c, lw=2, zorder=10))
        ax.plot([x_node, x_node+node_width], [y, y], color='#888', lw=1.5, zorder=11)
        ax.text(x_node+node_width/2, y+node_height/4, k, va='center', ha='center', fontsize=cell_font, color='#222', fontweight='bold', zorder=12)
        ax.text(x_node+node_width/2, y-node_height/4, v, va='center', ha='center', fontsize=cell_font-2, color='#444', zorder=12)
        if j < len(table[conflict_idx])-1:
            ax.add_patch(FancyArrowPatch((x_node+node_width, y), (x_node+node_width+node_gap, y), color='#888', arrowstyle='->', lw=2, zorder=11))

os.makedirs('assets/image', exist_ok=True)
plt.savefig('assets/image/hash_table_chaining.png', bbox_inches='tight', dpi=300)
plt.close()
