---
title: Recursion in Programming
parent: Data Structure and Algorithm
author: Yupeng
date: 2025-06-26
layout: default
nav_order: 4.1
math: katex
emoji: jemoji
---

# Recursion in Programming

## Overview
This document covers the fundamental concepts of recursion in programming, including what recursion is, base cases, preventing stack overflow, and practical applications. We'll explore how recursion works, when to use it, and how to implement it correctly to avoid common pitfalls.

## What is Recursion?

### Basic Concept
Recursion is a programming technique where a function calls itself to solve a problem. It works by breaking down a complex problem into smaller, similar subproblems until reaching a simple case that can be solved directly.

### Key Principles
- **Divide and Conquer**: Break complex problems into smaller subproblems
- **Self-Similarity**: Subproblems have the same structure as the original problem
- **Termination**: Must have one or more base cases that stop the recursion

### Mathematical Analogy
Recursion mirrors mathematical recurrence relations:
- Fibonacci sequence: F(n) = F(n-1) + F(n-2)
- Factorial: n! = n × (n-1)!
- Sum of array: sum(arr) = arr[0] + sum(arr[1:])

## What is a Base Case?

### Definition
A base case is a condition in a recursive function that can be solved directly without further recursive calls. It serves as the termination condition that prevents infinite recursion.

### Characteristics of Base Cases
- **Simple and Direct**: Can be computed immediately
- **Terminates Recursion**: No further function calls
- **Prevents Infinite Loops**: Ensures recursion eventually stops

### Example: Factorial Function
```java
public int factorial(int n) {
    // Base case
    if (n == 0 || n == 1) {
        return 1;
    }
    // Recursive case
    else {
        return n * factorial(n - 1);
    }
}
```

### Visualization of Factorial Recursion
```
Example: factorial(4)

Call Stack Visualization:
┌─────────────────────────────────────┐
│ factorial(4)                        │
│   return 4 * factorial(3)           │
│   ┌─────────────────────────────────┐│
│   │ factorial(3)                    ││
│   │   return 3 * factorial(2)       ││
│   │   ┌─────────────────────────────┐││
│   │   │ factorial(2)                │││
│   │   │   return 2 * factorial(1)   │││
│   │   │   ┌─────────────────────────┐│││
│   │   │   │ factorial(1)            ││││
│   │   │   │   return 1              ││││
│   │   │   └─────────────────────────┘│││
│   │   └─────────────────────────────┘││
│   └─────────────────────────────────┘│
└─────────────────────────────────────┘

Step-by-Step Execution:
Step 1: factorial(4) called
  - n = 4, not base case
  - return 4 * factorial(3)
  - Wait for factorial(3) result

Step 2: factorial(3) called
  - n = 3, not base case
  - return 3 * factorial(2)
  - Wait for factorial(2) result

Step 3: factorial(2) called
  - n = 2, not base case
  - return 2 * factorial(1)
  - Wait for factorial(1) result

Step 4: factorial(1) called
  - n = 1, base case reached!
  - return 1
  - No more recursive calls

Step 5: Back to factorial(2)
  - factorial(1) returned 1
  - return 2 * 1 = 2

Step 6: Back to factorial(3)
  - factorial(2) returned 2
  - return 3 * 2 = 6

Step 7: Back to factorial(4)
  - factorial(3) returned 6
  - return 4 * 6 = 24

Final Result: 24

Memory Usage Visualization:
┌─────────────────────────────────────┐
│ Call Stack (grows downward)         │
├─────────────────────────────────────┤
│ factorial(4): n=4, waiting for 3!   │
├─────────────────────────────────────┤
│ factorial(3): n=3, waiting for 2!   │
├─────────────────────────────────────┤
│ factorial(2): n=2, waiting for 1!   │
├─────────────────────────────────────┤
│ factorial(1): n=1, returning 1      │ ← Base case
├─────────────────────────────────────┤
│ Stack grows until base case reached │
└─────────────────────────────────────┘

Time Complexity: O(n)
Space Complexity: O(n) - due to call stack depth
```

In this example:
- **Base case**: `n == 0` or `n == 1`, returns 1 directly
- **Recursive case**: `n > 1`, calls `factorial(n - 1)`

### Multiple Base Cases
Some recursive functions may have multiple base cases:
```java
public int fibonacci(int n) {
    // Multiple base cases
    if (n == 0) return 0;
    if (n == 1) return 1;
    
    // Recursive case
    return fibonacci(n - 1) + fibonacci(n - 2);
}
```

## How to Ensure You Approach the Base Case?

### 1. Ensure Recursive Parameters Decrease
Each recursive call should move parameters toward the base case:

```java
public void countdown(int n) {
    // Base case
    if (n <= 0) {
        System.out.println("Blast off!");
        return;
    }
    // Recursive case - n decreases
    System.out.println(n);
    countdown(n - 1);  // n decreases by 1 each time
}
```

### 2. Ensure Problem Size Reduces
The recursive call should handle a smaller problem:

```java
public int sumArray(int[] arr, int index) {
    // Base case
    if (index >= arr.length) {
        return 0;
    }
    // Recursive case - problem size reduces
    return arr[index] + sumArray(arr, index + 1);
}
```

### 3. Checklist for Preventing Infinite Recursion
- [ ] Every recursive branch has a clear base case
- [ ] Recursive parameters move monotonically toward base case
- [ ] Problem size decreases with each recursive call
- [ ] Base case will eventually be reached

### 4. Common Patterns for Approaching Base Case

#### Pattern 1: Decreasing Integer
```java
public void printNumbers(int n) {
    if (n <= 0) return;  // Base case
    System.out.println(n);
    printNumbers(n - 1);  // Decrease n
}
```

#### Pattern 2: Reducing Array Size
```java
public int arraySum(int[] arr, int start) {
    if (start >= arr.length) return 0;  // Base case
    return arr[start] + arraySum(arr, start + 1);  // Increase start
}
```

#### Pattern 3: Dividing Problem Size
```java
public int binarySearch(int[] arr, int target, int left, int right) {
    if (left > right) return -1;  // Base case
    
    int mid = (left + right) / 2;
    if (arr[mid] == target) return mid;  // Base case
    
    if (arr[mid] > target) {
        return binarySearch(arr, target, left, mid - 1);  // Reduce right half
    } else {
        return binarySearch(arr, target, mid + 1, right);  // Reduce left half
    }
}
```

## What is Stack Overflow and What Causes It?

### Definition
Stack overflow occurs when a program runs out of stack memory due to excessive recursive function calls. Each function call consumes stack space, and when the stack is exhausted, the program crashes.

### Causes of Stack Overflow

#### 1. Missing Base Case
```java
public void infiniteRecursion() {
    // No base case!
    infiniteRecursion();  // Calls itself forever
}
```

#### 2. Base Case Never Reached
```java
public int badFactorial(int n) {
    if (n == 0) return 1;
    // Error: n doesn't decrease
    return n * badFactorial(n);  // Always calls factorial(n)
}
```

#### 3. Excessive Recursion Depth
```java
public int deepRecursion(int n) {
    if (n <= 0) return 0;
    // For very large n, causes stack overflow
    return 1 + deepRecursion(n - 1);
}

// Calling deepRecursion(10000) may cause stack overflow
```

#### 4. Complex Recursive Calls
```java
public int fibonacciNaive(int n) {
    if (n <= 1) return n;
    // Exponential number of calls
    return fibonacciNaive(n - 1) + fibonacciNaive(n - 2);
}
```

### Visualization of Fibonacci Recursion
```
Example: fibonacciNaive(5)

Call Tree Visualization:
                    fib(5)
                   /      \
              fib(4)      fib(3)
             /      \     /      \
        fib(3)    fib(2) fib(2)  fib(1)
       /      \   /    \  /    \
   fib(2) fib(1) fib(1) fib(0) fib(1) fib(0)
   /    \
fib(1) fib(0)

Total function calls: 15

Step-by-Step Analysis:
- fib(5) calls fib(4) and fib(3)
- fib(4) calls fib(3) and fib(2)  
- fib(3) calls fib(2) and fib(1)
- fib(2) calls fib(1) and fib(0)
- fib(1) and fib(0) are base cases

Repeated Calculations:
- fib(3) is calculated 2 times
- fib(2) is calculated 3 times
- fib(1) is calculated 5 times  
- fib(0) is calculated 3 times

Time Complexity: O(2^n) - exponential growth
Space Complexity: O(n) - maximum recursion depth
```

### Symptoms of Stack Overflow
- Program crashes with "StackOverflowError"
- High memory usage
- Program becomes unresponsive
- Exception stack trace shows deep recursion

### Preventing Stack Overflow

#### 1. Use Tail Recursion
```java
public int factorialTailRecursive(int n, int accumulator) {
    if (n <= 1) {
        return accumulator;
    }
    return factorialTailRecursive(n - 1, n * accumulator);
}

// Initial call: factorialTailRecursive(n, 1)
```

#### 2. Convert to Iteration
```java
public int factorialIterative(int n) {
    int result = 1;
    for (int i = 1; i <= n; i++) {
        result *= i;
    }
    return result;
}
```

#### 3. Use Memoization
```java
public int fibonacciMemo(int n, Map<Integer, Integer> memo) {
    if (memo.containsKey(n)) {
        return memo.get(n);
    }
    if (n <= 1) {
        return n;
    }
    int result = fibonacciMemo(n - 1, memo) + fibonacciMemo(n - 2, memo);
    memo.put(n, result);
    return result;
}
```

#### 4. Limit Recursion Depth
```java
public int safeRecursion(int n, int depth) {
    if (depth > 1000) {
        throw new RuntimeException("Recursion depth limit exceeded");
    }
    if (n <= 0) return 0;
    return 1 + safeRecursion(n - 1, depth + 1);
}
```

## Practical Examples

### Example 1: Directory Tree Traversal
```java
import java.io.File;

class DirectoryTraversal {
    public void traverseDirectory(File directory, int depth) {
        // Base case: not a directory or depth limit reached
        if (!directory.isDirectory() || depth > 10) {
            return;
        }
        
        // Print current directory
        String indent = "  ".repeat(depth);
        System.out.println(indent + "📁 " + directory.getName());
        
        // Recursive case: traverse subdirectories
        File[] files = directory.listFiles();
        if (files != null) {
            for (File file : files) {
                if (file.isDirectory()) {
                    traverseDirectory(file, depth + 1);
                } else {
                    System.out.println(indent + "  📄 " + file.getName());
                }
            }
        }
    }
}

// Usage Example
public class DirectoryExample {
    public static void main(String[] args) {
        DirectoryTraversal traversal = new DirectoryTraversal();
        File root = new File("C:/Users/Documents");
        traversal.traverseDirectory(root, 0);
    }
}
```

### Example 2: Tower of Hanoi
```java
class TowerOfHanoi {
    public void solveHanoi(int n, char source, char auxiliary, char destination) {
        // Base case: only one disk
        if (n == 1) {
            System.out.println("Move disk 1 from " + source + " to " + destination);
            return;
        }
        
        // Recursive case: move n-1 disks
        solveHanoi(n - 1, source, destination, auxiliary);
        System.out.println("Move disk " + n + " from " + source + " to " + destination);
        solveHanoi(n - 1, auxiliary, source, destination);
    }
    
    public void solve(int n) {
        System.out.println("Tower of Hanoi solution for " + n + " disks:");
        solveHanoi(n, 'A', 'B', 'C');
    }
}

// Usage Example
public class HanoiExample {
    public static void main(String[] args) {
        TowerOfHanoi hanoi = new TowerOfHanoi();
        hanoi.solve(3);
    }
}
```

### Example 3: Binary Tree Traversal
```java
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    
    public TreeNode(int val) {
        this.val = val;
        this.left = null;
        this.right = null;
    }
}

class BinaryTreeTraversal {
    // Inorder traversal (Left -> Root -> Right)
    public void inorderTraversal(TreeNode root) {
        if (root == null) return;  // Base case
        
        inorderTraversal(root.left);   // Recursive case
        System.out.print(root.val + " ");
        inorderTraversal(root.right);  // Recursive case
    }
    
    // Preorder traversal (Root -> Left -> Right)
    public void preorderTraversal(TreeNode root) {
        if (root == null) return;  // Base case
        
        System.out.print(root.val + " ");
        preorderTraversal(root.left);   // Recursive case
        preorderTraversal(root.right);  // Recursive case
    }
    
    // Postorder traversal (Left -> Right -> Root)
    public void postorderTraversal(TreeNode root) {
        if (root == null) return;  // Base case
        
        postorderTraversal(root.left);   // Recursive case
        postorderTraversal(root.right);  // Recursive case
        System.out.print(root.val + " ");
    }
}

// Usage Example
public class TreeTraversalExample {
    public static void main(String[] args) {
        // Create a simple binary tree
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.left.left = new TreeNode(4);
        root.left.right = new TreeNode(5);
        
        BinaryTreeTraversal traversal = new BinaryTreeTraversal();
        
        System.out.print("Inorder: ");
        traversal.inorderTraversal(root);
        System.out.println();
        
        System.out.print("Preorder: ");
        traversal.preorderTraversal(root);
        System.out.println();
        
        System.out.print("Postorder: ");
        traversal.postorderTraversal(root);
        System.out.println();
    }
}
```

## Discussion Points

### 1. Recursion vs Iteration
- **Recursion**:
  - More elegant for certain problems
  - Easier to understand for complex logic
  - Higher memory overhead
  - Risk of stack overflow

- **Iteration**:
  - More efficient memory usage
  - Better performance
  - No stack overflow risk
  - Can be more complex for some problems

### 2. Time Complexity Analysis

| Problem | Recursive Approach | Time Complexity | Space Complexity |
|---------|-------------------|-----------------|------------------|
| Factorial | Simple recursion | O(n) | O(n) |
| Fibonacci | Naive recursion | O(2^n) | O(n) |
| Fibonacci | Memoization | O(n) | O(n) |
| Binary Search | Recursive | O(log n) | O(log n) |
| Tree Traversal | Recursive | O(n) | O(h) |

### 3. Memory Considerations
- **Stack Space**: Each recursive call uses stack memory
- **Call Stack**: Function parameters and local variables
- **Depth Limit**: Maximum recursion depth varies by system
- **Optimization**: Tail recursion can be optimized by compiler

### 4. When to Use Recursion
- **Use when**:
  - Problem naturally divides into subproblems
  - Tree/graph traversal
  - Backtracking algorithms
  - Mathematical problems with recurrence relations

- **Avoid when**:
  - Simple loops suffice
  - Memory is limited
  - Performance is critical
  - Deep recursion is expected

## Practice Questions

1. **Factorial with Tail Recursion**: Implement factorial using tail recursion
2. **Reverse String**: Write a recursive function to reverse a string
3. **Palindrome Check**: Check if a string is palindrome using recursion
4. **Power Function**: Implement power function using recursion

### Answers

1. **Tail Recursive Factorial**:
```java
public int factorialTail(int n, int accumulator) {
    if (n <= 1) return accumulator;
    return factorialTail(n - 1, n * accumulator);
}

public int factorial(int n) {
    return factorialTail(n, 1);
}
```

2. **Reverse String**:
```java
public String reverseString(String str) {
    if (str.length() <= 1) return str;
    return reverseString(str.substring(1)) + str.charAt(0);
}
```

3. **Palindrome Check**:
```java
public boolean isPalindrome(String str) {
    if (str.length() <= 1) return true;
    if (str.charAt(0) != str.charAt(str.length() - 1)) return false;
    return isPalindrome(str.substring(1, str.length() - 1));
}
```

4. **Power Function**:
```java
public double power(double base, int exponent) {
    if (exponent == 0) return 1;
    if (exponent < 0) return 1 / power(base, -exponent);
    if (exponent % 2 == 0) {
        double half = power(base, exponent / 2);
        return half * half;
    }
    return base * power(base, exponent - 1);
}
```

## Summary

- **Recursion**: Function calling itself to solve problems
- **Base Case**: Termination condition preventing infinite recursion
- **Approaching Base Case**: Ensure parameters decrease or problem size reduces
- **Stack Overflow**: Caused by excessive recursion depth
- **Prevention**: Use tail recursion, iteration, or memoization
- **Applications**: Tree traversal, mathematical problems, backtracking

This comprehensive understanding of recursion provides a solid foundation for implementing recursive algorithms and avoiding common pitfalls in programming.

## Problem: Merge Two Sorted Lists

### Problem Description
Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

### Examples
```
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

Input: l1 = [], l2 = []
Output: []

Input: l1 = [], l2 = [0]
Output: [0]
```

### Recursive Solution
```java
class Solution {
    public Node mergeTwoLists(Node l1, Node l2) {
        // Base cases
        if (l1 == null) return l2;
        if (l2 == null) return l1;
        
        // Recursive case
        if (l1.data <= l2.data) {
            l1.next = mergeTwoLists(l1.next, l2);
            return l1;
        } else {
            l2.next = mergeTwoLists(l1, l2.next);
            return l2;
        }
    }
}
```

### Step-by-Step Execution
```
Input: l1 = [1,2,4], l2 = [1,3,4]

Step 1: l1.data(1) <= l2.data(1), so l1.next = mergeTwoLists([2,4], [1,3,4])
Step 2: l1.data(2) > l2.data(1), so l2.next = mergeTwoLists([2,4], [3,4])
Step 3: l1.data(2) <= l2.data(3), so l1.next = mergeTwoLists([4], [3,4])
Step 4: l1.data(4) > l2.data(3), so l2.next = mergeTwoLists([4], [4])
Step 5: l1.data(4) <= l2.data(4), so l1.next = mergeTwoLists(null, [4])
Step 6: Base case: return [4]
Result: [1,1,2,3,4,4]
```

### Key Insights
1. **Base Cases**: Handle null lists
2. **Recursive Logic**: Compare heads and merge remaining lists
3. **In-Place Merging**: Modify existing nodes rather than creating new ones
4. **Efficiency**: O(n + m) time complexity where n, m are list lengths

This problem demonstrates how recursion can elegantly solve linked list manipulation problems by breaking them down into smaller subproblems. 