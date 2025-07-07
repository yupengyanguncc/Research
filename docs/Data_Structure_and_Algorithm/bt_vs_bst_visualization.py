import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
import math

# Set up the plotting style
plt.style.use('seaborn-v0_8')
plt.rcParams['figure.figsize'] = (16, 12)
plt.rcParams['font.size'] = 12
plt.rcParams['font.family'] = 'DejaVu Sans'

# Create the main figure with subplots
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))

# ============================================================================
# Plot 1: Binary Tree Structure Visualization
# ============================================================================
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)
ax1.set_aspect('equal')
ax1.set_title('Binary Tree Structure', fontsize=14, fontweight='bold')

# Define node positions for Binary Tree
bt_nodes = {
    '5': (5, 8),
    '8': (3, 6),
    '3': (7, 6),
    '1': (2, 4),
    '9': (4, 4),
    '7': (8, 4),
    '2': (3, 2)
}

# Draw nodes
for value, (x, y) in bt_nodes.items():
    circle = plt.Circle((x, y), 0.4, color='lightblue', ec='black', linewidth=2)
    ax1.add_patch(circle)
    ax1.text(x, y, value, ha='center', va='center', fontsize=12, fontweight='bold')

# Draw edges
bt_edges = [
    ((5, 8), (3, 6)),  # 5 -> 8
    ((5, 8), (7, 6)),  # 5 -> 3
    ((3, 6), (2, 4)),  # 8 -> 1
    ((3, 6), (4, 4)),  # 8 -> 9
    ((7, 6), (8, 4)),  # 3 -> 7
    ((4, 4), (3, 2))   # 9 -> 2
]

for (x1, y1), (x2, y2) in bt_edges:
    ax1.plot([x1, x2], [y1, y2], 'k-', linewidth=2)

# Add characteristics text
ax1.text(0.5, 9.5, 'Characteristics:', fontsize=10, fontweight='bold')
ax1.text(0.5, 9.2, '• No ordering rules', fontsize=9)
ax1.text(0.5, 8.9, '• Left child can be > parent', fontsize=9)
ax1.text(0.5, 8.6, '• Right child can be < parent', fontsize=9)
ax1.text(0.5, 8.3, '• Structure depends on insertion order', fontsize=9)

ax1.set_xticks([])
ax1.set_yticks([])

# ============================================================================
# Plot 2: Binary Search Tree Structure Visualization
# ============================================================================
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)
ax2.set_aspect('equal')
ax2.set_title('Binary Search Tree Structure', fontsize=14, fontweight='bold')

# Define node positions for BST
bst_nodes = {
    '5': (5, 8),
    '3': (3, 6),
    '8': (7, 6),
    '1': (2, 4),
    '4': (4, 4),
    '9': (8, 4),
    '6': (6, 2)
}

# Draw nodes
for value, (x, y) in bst_nodes.items():
    circle = plt.Circle((x, y), 0.4, color='lightgreen', ec='black', linewidth=2)
    ax2.add_patch(circle)
    ax2.text(x, y, value, ha='center', va='center', fontsize=12, fontweight='bold')

# Draw edges
bst_edges = [
    ((5, 8), (3, 6)),  # 5 -> 3
    ((5, 8), (7, 6)),  # 5 -> 8
    ((3, 6), (2, 4)),  # 3 -> 1
    ((3, 6), (4, 4)),  # 3 -> 4
    ((7, 6), (8, 4)),  # 8 -> 9
    ((4, 4), (6, 2))   # 4 -> 6
]

for (x1, y1), (x2, y2) in bst_edges:
    ax2.plot([x1, x2], [y1, y2], 'k-', linewidth=2)

# Add characteristics text
ax2.text(0.5, 9.5, 'Characteristics:', fontsize=10, fontweight='bold')
ax2.text(0.5, 9.2, '• Strict ordering: left < root < right', fontsize=9)
ax2.text(0.5, 8.9, '• Left subtree: all values < root', fontsize=9)
ax2.text(0.5, 8.6, '• Right subtree: all values > root', fontsize=9)
ax2.text(0.5, 8.3, '• Maintains sorted order', fontsize=9)

ax2.set_xticks([])
ax2.set_yticks([])

# ============================================================================
# Plot 3: Search Performance Comparison
# ============================================================================
# Create data for performance comparison
n_values = np.linspace(1, 1000, 1000)
bt_search = n_values  # O(n)
bst_search = np.log2(n_values)  # O(log n)

ax3.plot(n_values, bt_search, 'b-', linewidth=2, label='Binary Tree: O(n)', alpha=0.8)
ax3.plot(n_values, bst_search, 'r-', linewidth=2, label='Binary Search Tree: O(log n)', alpha=0.8)
ax3.set_xlabel('Number of Nodes (n)')
ax3.set_ylabel('Search Time Complexity')
ax3.set_title('Search Performance Comparison')
ax3.legend()
ax3.grid(True, alpha=0.3)
ax3.set_xlim(0, 1000)
ax3.set_ylim(0, 1000)

# Add performance annotations
ax3.annotate('BT: Must check all nodes', xy=(500, 500), xytext=(300, 700),
            arrowprops=dict(arrowstyle='->', color='blue', alpha=0.7),
            fontsize=10, color='blue')
ax3.annotate('BST: Use ordering to eliminate half', xy=(500, 9), xytext=(700, 50),
            arrowprops=dict(arrowstyle='->', color='red', alpha=0.7),
            fontsize=10, color='red')

# ============================================================================
# Plot 4: Insertion Performance Comparison
# ============================================================================
# Create data for insertion comparison
bt_insert = n_values  # O(n) - simple insertion
bst_insert = np.log2(n_values)  # O(log n) - maintain order

ax4.plot(n_values, bt_insert, 'b-', linewidth=2, label='Binary Tree: O(n)', alpha=0.8)
ax4.plot(n_values, bst_insert, 'r-', linewidth=2, label='Binary Search Tree: O(log n)', alpha=0.8)
ax4.set_xlabel('Number of Nodes (n)')
ax4.set_ylabel('Insertion Time Complexity')
ax4.set_title('Insertion Performance Comparison')
ax4.legend()
ax4.grid(True, alpha=0.3)
ax4.set_xlim(0, 1000)
ax4.set_ylim(0, 1000)

# Add insertion annotations
ax4.annotate('BT: Simple placement', xy=(500, 500), xytext=(300, 700),
            arrowprops=dict(arrowstyle='->', color='blue', alpha=0.7),
            fontsize=10, color='blue')
ax4.annotate('BST: Maintain ordering', xy=(500, 9), xytext=(700, 50),
            arrowprops=dict(arrowstyle='->', color='red', alpha=0.7),
            fontsize=10, color='red')

plt.tight_layout()

# Save the figure
plt.savefig('assets/image/bt_vs_bst_comparison.png', dpi=300, bbox_inches='tight')
plt.show()

# Print detailed comparison table
print("\n" + "="*80)
print("BINARY TREE vs BINARY SEARCH TREE COMPARISON")
print("="*80)

print("\nSTRUCTURAL DIFFERENCES:")
print("-" * 50)
print("Binary Tree:")
print("  • No ordering constraints")
print("  • Left child can be > parent")
print("  • Right child can be < parent")
print("  • Structure depends on insertion order")
print("  • Simple to implement")

print("\nBinary Search Tree:")
print("  • Strict ordering: left < root < right")
print("  • Left subtree: all values < root")
print("  • Right subtree: all values > root")
print("  • Maintains sorted order")
print("  • More complex but efficient")

print("\nPERFORMANCE COMPARISON:")
print("-" * 50)
sizes = [10, 100, 1000, 10000]
print(f"{'Size':<8} {'BT Search':<12} {'BST Search':<12} {'BT Insert':<12} {'BST Insert':<12}")
print("-" * 60)

for size in sizes:
    bt_search_steps = size
    bst_search_steps = math.log2(size)
    bt_insert_steps = size
    bst_insert_steps = math.log2(size)
    
    print(f"{size:<8} {bt_search_steps:<12.0f} {bst_search_steps:<12.2f} {bt_insert_steps:<12.0f} {bst_insert_steps:<12.2f}")

print("\nAPPLICATION SCENARIOS:")
print("-" * 50)
print("Choose Binary Tree when:")
print("  • No ordering requirements")
print("  • Hierarchical data representation")
print("  • Expression evaluation")
print("  • File system modeling")
print("  • Decision tree algorithms")

print("\nChoose Binary Search Tree when:")
print("  • Sorted data requirements")
print("  • Fast search operations")
print("  • Database indexing")
print("  • Dictionary implementation")
print("  • Priority queue")

print("\n" + "="*80)
print("KEY INSIGHT: BST provides O(log n) search/insert vs O(n) for BT")
print("="*80) 