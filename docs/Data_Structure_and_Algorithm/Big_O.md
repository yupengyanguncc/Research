---
title: Big O
parent: Data Structure and Algorithm
author: Yupeng
date: 2025-06-02
layout: default
nav_order: 2.93
math: katex
emoji: jemoji
---

# Big O Notation

Big O notation is a mathematical notation used to describe the performance or complexity of an algorithm. It helps us understand how the runtime or space requirements of an algorithm grow as the input size increases.

## Why Big O?

1. **Algorithm Comparison**: Helps compare different algorithms and choose the most efficient one
2. **Performance Prediction**: Allows us to predict how an algorithm will perform with larger inputs
3. **Resource Planning**: Helps in planning system resources and understanding scalability
4. **Code Optimization**: Guides us in writing more efficient code

## Common Time Complexities

- **O(1)** - Constant time
  - Example: Accessing an array element by index
  - Performance remains the same regardless of input size

- **O(log n)** - Logarithmic time
  - Example: Binary search
  - Performance improves as input size increases

- **O(n)** - Linear time
  - Example: Linear search
  - Performance scales linearly with input size

- **O(n log n)** - Linearithmic time
  - Example: Merge sort, Quick sort
  - Common in efficient sorting algorithms

- **O(n²)** - Quadratic time
  - Example: Bubble sort, Selection sort
  - Performance degrades quickly with larger inputs

- **O(2^n)** - Exponential time
  - Example: Recursive Fibonacci
  - Performance degrades very quickly with larger inputs

## Space Complexity

Big O notation is also used to describe space complexity - how much additional memory an algorithm needs relative to the input size.

## Best, Worst, and Average Cases

- **Best Case**: Minimum time/space required
- **Worst Case**: Maximum time/space required
- **Average Case**: Expected time/space required

## Rules of Big O

1. **Drop Constants**: O(2n) → O(n)
2. **Drop Non-Dominant Terms**: O(n² + n) → O(n²)
3. **Different Inputs**: Different variables for different inputs
4. **Nested Loops**: Multiply the complexities

## Example

```java
// O(n) - Linear time
for (int i = 0; i < n; i++) {
    // do something
}

// O(n²) - Quadratic time
for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
        // do something
    }
}
```

## Common Misconceptions

1. **Big O is not about speed**: It's about growth rate
2. **Constants matter in real life**: Big O ignores constants, but they can be important
3. **Not all O(n) algorithms are equal**: Different algorithms with same Big O can have different performance
4. **Big O is not always the best metric**: Sometimes other factors like memory usage or code readability are more important

## When to Use Big O

1. **Algorithm Design**: When designing new algorithms
2. **Code Review**: When reviewing code for performance
3. **System Design**: When designing scalable systems
4. **Interview Preparation**: When preparing for technical interviews

## Conclusion

Understanding Big O notation is crucial for writing efficient code and making informed decisions about algorithm selection. It provides a common language for discussing algorithm performance and helps us write more scalable applications.