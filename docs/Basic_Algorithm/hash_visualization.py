import hashlib
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

def generate_hash_values(data, hash_func):
    """Generate hash values for the input data"""
    return [hash_func(d.encode()).hexdigest() for d in data]

def plot_comparison(test_data, hash_functions):
    """Create comparison plots for all hash functions"""
    # Create figure with subplots
    fig = plt.figure(figsize=(15, 10))
    
    # Distribution plots
    plt.subplot(2, 1, 1)
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c']  # Blue, Orange, Green
    for (name, func), color in zip(hash_functions.items(), colors):
        hash_values = generate_hash_values(test_data, func)
        hash_ints = [int(h[:8], 16) for h in hash_values]
        plt.hist(hash_ints, bins=50, alpha=0.5, label=name, color=color)
    
    plt.title('Hash Value Distribution Comparison', fontsize=14, pad=20)
    plt.xlabel('Hash Value', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.3)
    
    # Avalanche effect plots
    plt.subplot(2, 1, 2)
    base_input = "Hello, World!"
    
    for (name, func), color in zip(hash_functions.items(), colors):
        changes = []
        hash_diffs = []
        
        for i in range(len(base_input)):
            # Modify one character
            modified = list(base_input)
            modified[i] = chr(ord(modified[i]) + 1)
            modified = ''.join(modified)
            
            # Calculate original and modified hashes
            original_hash = int(func(base_input.encode()).hexdigest()[:8], 16)
            modified_hash = int(func(modified.encode()).hexdigest()[:8], 16)
            
            # Calculate difference in bits
            diff = bin(original_hash ^ modified_hash).count('1')
            changes.append(i)
            hash_diffs.append(diff)
        
        plt.plot(changes, hash_diffs, 'o-', label=name, color=color, alpha=0.7)
    
    plt.title('Avalanche Effect Comparison', fontsize=14, pad=20)
    plt.xlabel('Modified Character Position', fontsize=12)
    plt.ylabel('Number of Different Bits', fontsize=12)
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.3)
    
    # Add overall title
    plt.suptitle('Hash Function Analysis', fontsize=16, y=0.95)
    
    # Adjust layout and save
    plt.tight_layout()
    plt.savefig('hash_functions_comparison.png', dpi=300, bbox_inches='tight')
    plt.close()

def main():
    # Generate test data
    test_data = [f"test{i}" for i in range(1000)]
    
    # Test different hash functions
    hash_functions = {
        'MD5': hashlib.md5,
        'SHA-256': hashlib.sha256,
        'SHA-1': hashlib.sha1
    }
    
    # Generate comparison plots
    plot_comparison(test_data, hash_functions)
    
    # Calculate and print collision rates
    print("\nCollision Rate Analysis:")
    print("-" * 30)
    for name, func in hash_functions.items():
        hash_values = generate_hash_values(test_data, func)
        counter = Counter(hash_values)
        collisions = sum(count - 1 for count in counter.values())
        collision_rate = collisions / len(test_data)
        print(f"{name:8} Collision Rate: {collision_rate:.4f}")

if __name__ == "__main__":
    main() 