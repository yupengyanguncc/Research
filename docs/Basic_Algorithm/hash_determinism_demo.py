"""
Demonstration of the Determinism Property of a Hash Function
----------------------------------------------------------
A hash function is deterministic if the same input always produces the same output. This property is crucial because it ensures that data can be reliably retrieved from a hash table: the key will always map to the same location.
"""

def simple_hash(key, size):
    return sum(ord(c) for c in str(key)) % size

keys = ["apple", "banana", "orange", "grape", "melon", "berry", "peach", "plum", "kiwi", "pear"]
size = 10

hashes_first = [simple_hash(k, size) for k in keys]
hashes_second = [simple_hash(k, size) for k in keys]

print("First run: ", hashes_first)
print("Second run:", hashes_second)
print("Are both runs identical?", hashes_first == hashes_second) 