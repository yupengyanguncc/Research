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
def simple_hash(key, size):
    return sum(ord(c) for c in str(key)) % size
```

Let's break down how this simple hash function works:

1. **Step-by-Step Example**:
   Let's calculate the hash value for the string "Hello" with size = 10:
   ```
   Input: key = "Hello", size = 10
   
   Step 1: Convert each character to its ASCII value
   'H' -> ord('H') = 72
   'e' -> ord('e') = 101
   'l' -> ord('l') = 108
   'l' -> ord('l') = 108
   'o' -> ord('o') = 111
   
   Step 2: Sum all ASCII values
   72 + 101 + 108 + 108 + 111 = 500
   
   Step 3: Take modulo with size
   500 % 10 = 0
   
   Final result: simple_hash("Hello", 10) = 0
   ```

2. **More Examples**:
   ```python
   # Example 1: Different strings
   print(simple_hash("Hello", 10))    # 0
   print(simple_hash("World", 10))    # 5
   print(simple_hash("Python", 10))   # 8
   
   # Example 2: Same string, different size
   print(simple_hash("Hello", 5))     # 0
   print(simple_hash("Hello", 7))     # 3
   print(simple_hash("Hello", 13))    # 6
   
   # Example 3: Numbers (converted to strings)
   print(simple_hash(123, 10))        # 6
   print(simple_hash("123", 10))      # 6
   ```

3. **Properties of this Hash Function**:
   - **Deterministic**: Same input always produces same output
   - **Uniform Distribution**: Not guaranteed
   - **Collision Prone**: Different inputs can produce same output
   - **Example of Collision**:
     ```python
     # These different strings produce the same hash value
     print(simple_hash("ab", 10))     # 3
     print(simple_hash("ba", 10))     # 3
     ```

4. **Limitations**:
   - Not cryptographically secure
   - Prone to collisions
   - Distribution depends on input patterns
   - ASCII sum can overflow for long strings

5. **When to Use**:
   - Simple applications
   - Small datasets
   - Non-critical systems
   - Learning purposes

6. **When Not to Use**:
   - Security applications
   - Large datasets
   - Systems requiring uniform distribution
   - Applications sensitive to collisions

### 2.2 Storage Process

![Hash Table Storage Process](../../assets/image/hash_table_storage_process.png)

### 2.3 Search Process

![Hash Table Search Process](../../assets/image/hash_table_search_process.png)

## 3. Hash Functions in Detail

### 3.1 Properties of Good Hash Functions

A good hash function should have the following properties:

- **Deterministic**: Same input always produces the same output
- **Uniform Distribution**: Outputs should be evenly distributed across the range
- **Avalanche Effect**: Small changes in input should cause large changes in output
- **Efficiency**: Should be computationally efficient

### 3.2 Common Hash Functions

#### 3.2.1 MD5 (Message-Digest Algorithm 5)
- Output length: 128 bits (16 bytes)
- Mathematical expression: $$ H(x) = f(x) \mod 2^{128} $$
- **Detailed Process**:
  1. **Padding**: 
     - Append a single '1' bit
     - Append '0' bits until length is 448 bits (mod 512)
     - Append 64-bit original length
  2. **Initialize Variables**:
     ```
     A = 0x67452301
     B = 0xefcdab89
     C = 0x98badcfe
     D = 0x10325476
     ```
  3. **Main Loop**:
     - Process data in 512-bit blocks
     - 64 rounds of operations
     - Each round uses different bit operations and constants

- **Step-by-Step Example**:
  Let's calculate MD5 for the string "Hello":
  1. **Convert to bytes**:
     ```
     "Hello" -> [72, 101, 108, 108, 111]
     Binary: 01001000 01100101 01101100 01101100 01101111
     ```
  2. **Add padding**:
     ```
     Original length: 40 bits
     Add '1' bit: 01001000 01100101 01101100 01101100 01101111 1
     Add '0' bits until 448 bits: ...0000
     Add length (40 bits): ...00101000
     ```
  3. **Process in blocks**:
     ```
     Block 1: [72, 101, 108, 108, 111, 128, 0, 0, ..., 40]
     ```
  4. **Final result**:
     ```
     MD5("Hello") = 8b1a9953c4611296a827abf8c47804d7
     ```

- **Example with Different Inputs**:
  ```python
  import hashlib
  
  # Same input always gives same output
  text1 = "Hello"
  text2 = "Hello"
  print(hashlib.md5(text1.encode()).hexdigest())  # 8b1a9953c4611296a827abf8c47804d7
  print(hashlib.md5(text2.encode()).hexdigest())  # 8b1a9953c4611296a827abf8c47804d7
  
  # Small change in input causes big change in output
  text3 = "Hello!"
  print(hashlib.md5(text3.encode()).hexdigest())  # f7ff9e8b7bb2e09b70935a5d785e0cc5d9d0abf0
  ```

#### 3.2.2 SHA-256 (Secure Hash Algorithm 256)
- Output length: 256 bits (32 bytes)
- Mathematical expression: $$ H(x) = f(x) \mod 2^{256} $$
- **Detailed Process**:
  1. **Padding**:
     - Similar to MD5 but with 512-bit block size
     - More complex padding rules
  2. **Initialize Variables**:
     ```
     h0 = 0x6a09e667
     h1 = 0xbb67ae85
     h2 = 0x3c6ef372
     h3 = 0xa54ff53a
     h4 = 0x510e527f
     h5 = 0x9b05688c
     h6 = 0x1f83d9ab
     h7 = 0x5be0cd19
     ```
  3. **Main Loop**:
     - 64 rounds of operations
     - More complex bit operations than MD5
     - Uses different constants for each round

- **Step-by-Step Example**:
  Let's calculate SHA-256 for the string "Hello":
  1. **Convert to bytes**:
     ```
     "Hello" -> [72, 101, 108, 108, 111]
     Binary: 01001000 01100101 01101100 01101100 01101111
     ```
  2. **Add padding**:
     ```
     Original length: 40 bits
     Add '1' bit: 01001000 01100101 01101100 01101100 01101111 1
     Add '0' bits until 448 bits: ...0000
     Add length (40 bits): ...00101000
     ```
  3. **Process in blocks**:
     ```
     Block 1: [72, 101, 108, 108, 111, 128, 0, 0, ..., 40]
     ```
  4. **Final result**:
     ```
     SHA-256("Hello") = 185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969
     ```

- **Example with Different Inputs**:
  ```python
  import hashlib
  
  # Same input always gives same output
  text1 = "Hello"
  text2 = "Hello"
  print(hashlib.sha256(text1.encode()).hexdigest())
  # 185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969
  print(hashlib.sha256(text2.encode()).hexdigest())
  # 185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969
  
  # Small change in input causes big change in output
  text3 = "Hello!"
  print(hashlib.sha256(text3.encode()).hexdigest())
  # 334d016f755cd6dc58c53a86e183882f8ec14f52fb05345887c8a5edd42c87b7
  ```

#### 3.2.3 MurmurHash
- Output length: 32 or 64 bits
- Mathematical expression: $$ H(x) = (x \cdot c_1) \oplus ((x \cdot c_1) \gg r_1) $$
- **Detailed Process**:
  1. **Key Mixing**:
     - Multiply key by a constant
     - Rotate the result
     - XOR with the result
  2. **Final Mixing**:
     - Additional mixing steps
     - Final XOR operations

- **Step-by-Step Example**:
  Let's calculate MurmurHash3 for the string "Hello":
  1. **Convert to bytes**:
     ```
     "Hello" -> [72, 101, 108, 108, 111]
     ```
  2. **Process in 4-byte blocks**:
     ```
     Block 1: [72, 101, 108, 108] -> 0x48656c6c
     Block 2: [111, 0, 0, 0] -> 0x6f000000
     ```
  3. **Apply mixing function**:
     ```
     k1 = 0x48656c6c
     k1 *= 0xcc9e2d51
     k1 = (k1 << 15) | (k1 >> 17)
     k1 *= 0x1b873593
     ```
  4. **Final result**:
     ```
     MurmurHash3("Hello") = 316307400
     ```

- **Example with Different Inputs**:
  ```python
  import mmh3
  
  # Same input always gives same output
  text1 = "Hello"
  text2 = "Hello"
  print(mmh3.hash(text1))  # 316307400
  print(mmh3.hash(text2))  # 316307400
  
  # Small change in input causes different output
  text3 = "Hello!"
  print(mmh3.hash(text3))  # -1327161286
  ```

### 3.3 Hash Function Comparison

#### 3.3.1 Distribution Analysis
The following visualization shows the distribution of hash values for different algorithms:

![Hash Distribution Comparison](../../assets/image/hash_functions_comparison.png)

- **MD5**: Shows good distribution but with some clustering
- **SHA-256**: Exhibits excellent uniform distribution
- **MurmurHash**: Shows good distribution for non-cryptographic use

#### 3.3.2 Performance Comparison

| Metric | MD5 | SHA-256 | MurmurHash |
|--------|-----|----------|------------|
| Speed | Fast | Slow | Very Fast |
| Security | Low | High | Low |
| Memory Usage | Low | High | Low |
| Collision Resistance | Weak | Strong | Moderate |

#### 3.3.3 Use Case Recommendations

1. **Security Applications**:
   - Use SHA-256 for:
     - Password hashing
     - Digital signatures
     - Blockchain
     - File integrity verification

2. **General Purpose**:
   - Use MD5 for:
     - File checksums
     - Non-critical data deduplication
     - Quick data validation

3. **High Performance**:
   - Use MurmurHash for:
     - Hash tables
     - Bloom filters
     - Cache keys
     - Load balancing

## 4. Collision Handling

### 4.1 What is a Hash Collision?

A collision occurs when two different keys map to the same index through the hash function.

![Hash Collision Illustration](../../assets/image/hash_table_collision.png)

### 4.2 Methods to Handle Collisions

1. **Separate Chaining**
   - Uses linked lists to store colliding elements
   ![Separate Chaining Illustration](../../assets/image/hash_table_chaining.png)

2. **Open Addressing**
   - Linear Probing
   - Quadratic Probing
   - Double Hashing

## 5. Performance Analysis

### 5.1 Time Complexity

| Operation | Average Case | Worst Case |
|-----------|--------------|------------|
| Search    | O(1)         | O(n)       |
| Insert    | O(1)         | O(n)       |
| Delete    | O(1)         | O(n)       |

### 5.2 Space Complexity
- Space Complexity: O(n), where n is the number of stored elements

## 6. Applications

1. **Database Indexing**
2. **Cache Systems**
3. **Dictionary Implementation**
4. **Compiler Symbol Tables**
5. **Routing Tables**

## 7. Code Examples

### 7.1 Python Implementation

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

### 7.2 Java Implementation

```java
import java.util.LinkedList;

public class HashTable<K, V> {
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

    private int hash(K key) {
        return Math.abs(key.hashCode()) % size;
    }

    public void put(K key, V value) {
        int idx = hash(key);
        for (Entry entry : table[idx]) {
            if (entry.key.equals(key)) {
                entry.value = value;
                return;
            }
        }
        table[idx].add(new Entry(key, value));
    }

    public V get(K key) {
        int idx = hash(key);
        for (Entry entry : table[idx]) {
            if (entry.key.equals(key)) {
                return entry.value;
            }
        }
        return null;
    }

    public boolean remove(K key) {
        int idx = hash(key);
        return table[idx].removeIf(entry -> entry.key.equals(key));
    }
}
```

### 7.3 Usage Example (Python)

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

### 7.4 Usage Example (Java)

```java
public class Main {
    public static void main(String[] args) {
        HashTable<String, Integer> ht = new HashTable<>(10);
        ht.put("apple", 1);
        ht.put("banana", 2);
        ht.put("orange", 3);

        System.out.println(ht.get("apple"));   // Output: 1
        System.out.println(ht.get("banana"));  // Output: 2
        System.out.println(ht.get("grape"));   // Output: null
    }
}
```

## 8. Best Practices

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

## 9. Common Questions

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