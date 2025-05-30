---
title: Hash Table 
parent: Basic Algorithm
author: Yupeng
date: 2025-05-29
layout: default
nav_order: 2.6
math: katex
emoji: jemoji
---

# Hash Table

A hash table is an efficient data structure that maps keys to storage locations through a hash function, enabling fast data lookup, insertion, and deletion operations.

## 1. Basic Concepts

### 1.1 What is a Hash Table?

A hash table is like an intelligent library system:
- Each book (data) has a unique number (key)
- The librarian (hash function) quickly finds the storage location based on the number
- The bookshelf (array) stores the actual books

![Hash Table Basic Concept](../../assets/image/hash_table_visualization.png)

### 1.2 Core Components

1. **Key**: Unique identifier used for lookup
2. **Value**: Actual stored data
3. **Hash Function**: Function that converts keys to array indices
4. **Array**: Container for storing data

## 2. Working Principle

### 2.1 Hash Function

A hash function converts input of arbitrary size to a fixed-size output (usually an integer). For example: 

```python
# Python Implementation
def simple_hash(key, size):
    return sum(ord(c) for c in str(key)) % size
```

```java
// Java Implementation
public static int simpleHash(Object key, int size) {
    String strKey = key.toString();
    int sum = 0;
    for (int i = 0; i < strKey.length(); i++) {
        sum += (int) strKey.charAt(i);
    }
    return sum % size;
}
```


This is the [ASCII Table](https://www.ascii-code.com/). We will introduce the Hash Function in detail [here](Hash_Function.html).


### 2.2 Storage Process

![Hash Table Storage Process](../../assets/image/hash_table_storage_process.png)

### 2.3 Search Process

![Hash Table Search Process](../../assets/image/hash_table_search_process.png)


## 3. Collision Handling

### 3.1 What is a Hash Collision?

A collision occurs when two different keys map to the same index through the hash function.

![Hash Collision Illustration](../../assets/image/hash_table_collision.png)

### 3.2 Methods to Handle Collisions

1. **Separate Chaining**
   - Uses linked lists to store colliding elements
   ![Separate Chaining Illustration](../../assets/image/hash_table_chaining.png)

2. **Open Addressing**
   - Linear Probing
   - Quadratic Probing
   - Double Hashing

## 4. Performance Analysis

### 4.1 Properties of Good Hash Functions

A good hash function should have the following properties:

- **Deterministic**: Same input always produces the same output
- **Uniform Distribution**: Outputs should be evenly distributed across the range
- **Avalanche Effect**: Small changes in input should cause large changes in output
- **Efficiency**: Should be computationally efficient

### 4.2 Why Hash Function Properties Matter

#### **Deterministic**
A hash function must be deterministic so that the same key always maps to the same slot. If not, you would not be able to reliably find or update data in the hash table.

**Example (What goes wrong if not deterministic):**

Suppose we use a bad hash function that returns a random slot each time:

```python
import random

def bad_hash(key, size):
    return random.randint(0, size-1)  # Not deterministic!

size = 10
hash_table = [[] for _ in range(size)]

# Insert a key-value pair
key = "apple"
value = 1
slot = bad_hash(key, size)
hash_table[slot].append((key, value))

# Try to search for the same key
search_slot = bad_hash(key, size)
found = any(k == key for k, v in hash_table[search_slot])
print("Found?", found)  # Most likely False!
```

```java
import java.util.*;

public class BadHashDemo {
    public static int badHash(String key, int size) {
        Random rand = new Random();
        return rand.nextInt(size); // Not deterministic!
    }

    public static void main(String[] args) {
        int size = 10;
        List<List<Map.Entry<String, Integer>>> hashTable = new ArrayList<>();
        for (int i = 0; i < size; i++) {
            hashTable.add(new ArrayList<>());
        }

        // Insert a key-value pair
        String key = "apple";
        int value = 1;
        int slot = badHash(key, size);
        hashTable.get(slot).add(new AbstractMap.SimpleEntry<>(key, value));

        // Try to search for the same key
        int searchSlot = badHash(key, size);
        boolean found = false;
        for (Map.Entry<String, Integer> entry : hashTable.get(searchSlot)) {
            if (entry.getKey().equals(key)) {
                found = true;
                break;
            }
        }
        System.out.println("Found? " + found); // Most likely false!
    }
}
```

A visualization of the failuare case is provided in ![Separate Chaining Illustration](../../assets/image/bad_hash_search_result.png)

**Explanation:**
- When inserting, the key "apple" is placed in a random slot.
- When searching, "apple" is looked up in a different random slot, so the search almost always fails.
- This demonstrates that a non-deterministic hash function makes the hash table unusable.

#### **Uniform Distribution**
Uniform distribution ensures that hash values are spread evenly across all slots. This minimizes collisions (multiple keys mapping to the same slot), which is crucial for maintaining fast lookup, insertion, and deletion times.

If a hash function is not uniform, some slots will be crowded (many keys), while others are empty. This leads to more collisions and degrades performance.

Here is the visualization for the Uniform Distribution:
![Uniform Distribution](../../assets/image/hash_slot_distribution.png)



**Example:**
Suppose you have 10 slots and 1000 elements. Ideally, each slot has 100 elements. If you use separate chaining (linked lists in each slot), the average number of comparisons to find an existing element is about 100/2 = 50 (since on average, the element is in the middle of the list). If the distribution is uneven, some slots may have 300 elements, and searching in those slots could take up to 150 comparisons on average, making the hash table much slower.

**Tips:**
- For a slot with $$n$$ elements (using chaining):
    - Average comparisons for a successful search: $$n/2$$

**Summary:**
- Determinism guarantees correctness.
- Uniform distribution guarantees efficiency.


### 4.3 Time Complexity

| Operation | Average Case | Worst Case |
|-----------|--------------|------------|
| Search    | O(1)         | O(n)       |
| Insert    | O(1)         | O(n)       |
| Delete    | O(1)         | O(n)       |

### 4.4 Space Complexity
- Space Complexity: O(n), where n is the number of stored elements

## 5. Applications

1. **Database Indexing**
2. **Cache Systems**
3. **Dictionary Implementation**
4. **Compiler Symbol Tables**
5. **Routing Tables**

## 6. Code Examples

### 6.1 Implementation

```python
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def hash_function(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        index = self.hash_function(key)
        self.table[index].append((key, value))
    
    def search(self, key):
        index = self.hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None
```

```java
// Java Implementation
import java.util.LinkedList;

class HashTable<K, V> {
    private class Entry {
        K key;
        V value;
        Entry(K key, V value) {
            this.key = key;
            this.value = value;
        }
    }

    private LinkedList<Entry>[] table;
    private int size;

    public HashTable(int size) {
        this.size = size;
        table = new LinkedList[size];
        for (int i = 0; i < size; i++) {
            table[i] = new LinkedList<>();
        }
    }

    private int hashFunction(K key) {
        return Math.abs(key.hashCode()) % size;
    }

    public void insert(K key, V value) {
        int index = hashFunction(key);
        table[index].add(new Entry(key, value));
    }

    public V search(K key) {
        int index = hashFunction(key);
        for (Entry entry : table[index]) {
            if (entry.key.equals(key)) {
                return entry.value;
            }
        }
        return null;
    }
}
```

### 6.3 Usage Example 

```python
# Create hash table
ht = HashTable(10)

# Insert data
ht.insert("apple", 1)
ht.insert("banana", 2)
ht.insert("orange", 3)

# Search data
print(ht.search("apple"))  # Output: 1
print(ht.search("banana")) # Output: 2
```

```java
// Usage Example (Java)
public class Main {
    public static void main(String[] args) {
        HashTable<String, Integer> ht = new HashTable<>(10);
        ht.insert("apple", 1);
        ht.insert("banana", 2);
        ht.insert("orange", 3);

        System.out.println(ht.search("apple"));   // Output: 1
        System.out.println(ht.search("banana"));  // Output: 2
        System.out.println(ht.search("grape"));   // Output: null
    }
}
```

## 7. Best Practices

1. **Choose Appropriate Hash Function**
   - Uniform distribution
   - Fast computation
   - Minimal collisions

2. **Set Initial Size Appropriately**
   - Avoid frequent resizing
   - Control load factor

3. **Handle Collisions**
   - Choose collision handling method based on requirements
   - Monitor collision rate

## 8. Common Questions

1. **How to Choose a Hash Function?**
   - Consider data characteristics
   - Test distribution uniformity
   - Evaluate computation efficiency

2. **How to Handle Hash Table Resizing?**
   - Set appropriate resize threshold
   - Rehash all elements
   - Maintain data consistency

3. **How to Optimize Performance?**
   - Use appropriate collision handling method
   - Regularly clean up unused data
   - Monitor performance metrics 

## 9. References

- Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein. "Introduction to Algorithms", 3rd Edition, MIT Press, Chapter 11.
- Wikipedia contributors, "Hash table", Wikipedia, The Free Encyclopedia. [Link](https://en.wikipedia.org/wiki/Hash_table)
- Donald E. Knuth, "The Art of Computer Programming, Volume 3: Sorting and Searching", Addison-Wesley. 