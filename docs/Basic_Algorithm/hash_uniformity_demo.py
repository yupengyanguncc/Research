"""
Demonstration of the Uniform Distribution Property of a Hash Function
--------------------------------------------------------------------
A good hash function should distribute keys uniformly across the available slots. Uniform distribution minimizes collisions and ensures efficient use of the hash table. This script shows that the simple_hash function does not guarantee uniform distribution.
"""

import random
import string
import matplotlib.pyplot as plt

def simple_hash(key, size):
    return sum(ord(c) for c in str(key)) % size

def random_string(length=6):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

size = 10
num_samples = 1000
hash_counts = [0] * size

for _ in range(num_samples):
    key = random_string()
    h = simple_hash(key, size)
    hash_counts[h] += 1

plt.bar(range(size), hash_counts)
plt.xlabel("Hash Value")
plt.ylabel("Count")
plt.title("Distribution of simple_hash outputs (size=10)")
plt.show() 