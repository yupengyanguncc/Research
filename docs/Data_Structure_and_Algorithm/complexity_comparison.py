import matplotlib.pyplot as plt
import numpy as np
import math

# Set up the plotting style
plt.style.use('seaborn-v0_8')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 12
# Use a font that supports subscript characters
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['mathtext.fontset'] = 'dejavusans'

# Create data points
n_values = np.linspace(1, 1000, 1000)
linear_values = n_values
log_values = np.log2(n_values)  # log base 2
log10_values = np.log10(n_values)  # log base 10
ln_values = np.log(n_values)  # natural log

# Create the main comparison plot
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))

# Plot 1: Linear vs Log2
ax1.plot(n_values, linear_values, 'b-', linewidth=2, label='Linear: O(n)', alpha=0.8)
ax1.plot(n_values, log_values, 'r-', linewidth=2, label='Logarithmic: O(logn)', alpha=0.8)
ax1.set_xlabel('Input Size (n)')
ax1.set_ylabel('Time Complexity')
ax1.set_title('Linear vs Logarithmic Growth')
ax1.legend()
ax1.grid(True, alpha=0.3)
ax1.set_xlim(0, 1000)
ax1.set_ylim(0, 1000)

# Add annotations
ax1.annotate('Linear grows\nsteadily', xy=(500, 500), xytext=(300, 700),
            arrowprops=dict(arrowstyle='->', color='blue', alpha=0.7),
            fontsize=10, color='blue')
ax1.annotate('Logarithmic\ngrows slowly', xy=(500, 9), xytext=(700, 50),
            arrowprops=dict(arrowstyle='->', color='red', alpha=0.7),
            fontsize=10, color='red')

# Plot 2: Different log bases comparison
ax2.plot(n_values, log_values, 'r-', linewidth=2, label='log₂(n)', alpha=0.8)
ax2.plot(n_values, log10_values, 'g-', linewidth=2, label='log₁₀(n)', alpha=0.8)
ax2.plot(n_values, ln_values, 'orange', linewidth=2, label='ln(n)', alpha=0.8)
ax2.set_xlabel('Input Size (n)')
ax2.set_ylabel('Logarithmic Values')
ax2.set_title('Different Logarithm Bases')
ax2.legend()
ax2.grid(True, alpha=0.3)
ax2.set_xlim(0, 1000)

# Plot 3: Large scale comparison (up to 1 million)
n_large = np.linspace(1, 1000000, 1000)
linear_large = n_large
log2_large = np.log2(n_large)

ax3.plot(n_large, linear_large, 'b-', linewidth=2, label='Linear: O(n)', alpha=0.8)
ax3.plot(n_large, log2_large, 'r-', linewidth=2, label='Logarithmic: O(log₂n)', alpha=0.8)
ax3.set_xlabel('Input Size (n)')
ax3.set_ylabel('Time Complexity')
ax3.set_title('Large Scale: Linear vs Logarithmic (up to 1M)')
ax3.legend()
ax3.grid(True, alpha=0.3)
ax3.set_xscale('log')  # Log scale for x-axis only
# Remove y-scale log to show the dramatic difference better

# Add performance comparison annotations
ax3.annotate('n=1M: Linear=1M\nlog₂n ≈ 20', xy=(1000000, 20), xytext=(100000, 100),
            arrowprops=dict(arrowstyle='->', color='red', alpha=0.7),
            fontsize=10, color='red', bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8))

# Plot 4: Performance ratio
ratio = linear_large / log2_large
ax4.plot(n_large, ratio, 'purple', linewidth=2, label='Linear/Logarithmic Ratio', alpha=0.8)
ax4.set_xlabel('Input Size (n)')
ax4.set_ylabel('Performance Ratio (Linear/Log)')
ax4.set_title('How Much Faster is Logarithmic?')
ax4.legend()
ax4.grid(True, alpha=0.3)
ax4.set_xscale('log')
ax4.set_yscale('log')

# Add ratio annotations
ax4.annotate('n=1K: ~50x faster', xy=(1000, 50), xytext=(100, 200),
            arrowprops=dict(arrowstyle='->', color='purple', alpha=0.7),
            fontsize=10, color='purple')
ax4.annotate('n=1M: ~50,000x faster', xy=(1000000, 50000), xytext=(10000, 100000),
            arrowprops=dict(arrowstyle='->', color='purple', alpha=0.7),
            fontsize=10, color='purple')

plt.tight_layout()
# Save the figure
plt.savefig('assets/image/complexity_comparison.png', dpi=300, bbox_inches='tight')
plt.show()

# Create a detailed comparison table
print("\n" + "="*80)
print("PERFORMANCE COMPARISON: LINEAR vs LOGARITHMIC")
print("="*80)

sizes = [10, 100, 1000, 10000, 100000, 1000000]
print(f"{'Input Size':<12} {'Linear O(n)':<15} {'Log₂(n)':<12} {'Ratio':<15} {'Speedup'}")
print("-" * 80)

for size in sizes:
    linear = size
    log2 = math.log2(size)
    ratio = linear / log2
    print(f"{size:<12} {linear:<15} {log2:<12.2f} {ratio:<15.2f} {ratio:.0f}x faster")

print("\n" + "="*80)
print("KEY INSIGHTS:")
print("="*80)
print("1. Linear growth: Time increases proportionally with input size")
print("2. Logarithmic growth: Time increases very slowly with input size")
print("3. For large datasets, logarithmic algorithms are dramatically faster")
print("4. Binary trees provide O(log n) search, making them ideal for large datasets")
print("5. The performance gap widens exponentially as data size increases")

# Create a practical example
print("\n" + "="*80)
print("PRACTICAL EXAMPLE: SEARCHING 1 MILLION RECORDS")
print("="*80)

million = 1000000
linear_steps = million
log2_steps = math.log2(million)

print(f"Linear Search (Array/Linked List):")
print(f"  - Average steps needed: {linear_steps:,}")
print(f"  - Time estimate: ~{linear_steps/1000:.0f} seconds")

print(f"\nBinary Tree Search:")
print(f"  - Average steps needed: {log2_steps:.0f}")
print(f"  - Time estimate: ~{log2_steps/1000:.3f} seconds")

speedup = linear_steps / log2_steps
print(f"\nBinary Tree is {speedup:.0f}x faster!")

print(f"\nReal-world impact:")
print(f"  - Linear search: 16+ minutes")
print(f"  - Binary tree search: 0.02 seconds")
print(f"  - Difference: {speedup:.0f}x faster") 