---
title: Stack and Queue Implementation with Arrays
parent: Data Structure and Algorithm
author: Yupeng
date: 2025-06-15
layout: default
nav_order: 3.2
math: katex
emoji: jemoji
---

# Stack and Queue Implementation with Arrays

## Overview
This document covers the implementation of stacks and queues using arrays, suitable for a 15-minute discussion. We'll explore how these fundamental data structures can be efficiently implemented using arrays and understand their practical applications.

## Stack Implementation Using Array

### Basic Concept
A stack follows LIFO (Last In, First Out) principle and can be implemented using an array with a single pointer.

### Java Implementation
```java
class ArrayStack {
    private int[] array;
    private int top;
    private int capacity;
    
    public ArrayStack(int size) {
        array = new int[size];
        top = -1;
        capacity = size;
    }
    
    public void push(int value) {
        if (isFull()) {
            throw new RuntimeException("Stack is full");
        }
        array[++top] = value;
    }
    
    public int pop() {
        if (isEmpty()) {
            throw new RuntimeException("Stack is empty");
        }
        return array[top--];
    }
    
    public int peek() {
        if (isEmpty()) {
            throw new RuntimeException("Stack is empty");
        }
        return array[top];
    }
    
    public boolean isEmpty() {
        return top == -1;
    }
    
    public boolean isFull() {
        return top == capacity - 1;
    }
}
```

### Visualization
```
Initial State: top = -1
[ ][ ][ ][ ][ ]

Push(5): top = 0
[5][ ][ ][ ][ ]

Push(2): top = 1
[5][2][ ][ ][ ]

Push(8): top = 2
[5][2][8][ ][ ]

Pop(): returns 8, top = 1
[5][2][ ][ ][ ]

Push(1): top = 2
[5][2][1][ ][ ]
```

### Key Points
- **Single Pointer**: Only need `top` pointer
- **O(1) Operations**: Push, pop, and peek are all constant time
- **Simple Implementation**: Easy to understand and implement

## Queue Implementation Using Array

### Basic Concept
A queue follows FIFO (First In, First Out) principle and requires two pointers for efficient implementation.

### Java Implementation
```java
class ArrayQueue {
    private int[] array;
    private int front;
    private int rear;
    private int size;
    private int capacity;
    
    public ArrayQueue(int size) {
        array = new int[size];
        front = 0;
        rear = -1;
        size = 0;
        capacity = size;
    }
    
    public void enqueue(int value) {
        if (isFull()) {
            throw new RuntimeException("Queue is full");
        }
        rear = (rear + 1) % capacity;  // Circular array
        array[rear] = value;
        size++;
    }
    
    public int dequeue() {
        if (isEmpty()) {
            throw new RuntimeException("Queue is empty");
        }
        int value = array[front];
        front = (front + 1) % capacity;  // Circular array
        size--;
        return value;
    }
    
    public int front() {
        if (isEmpty()) {
            throw new RuntimeException("Queue is empty");
        }
        return array[front];
    }
    
    public boolean isEmpty() {
        return size == 0;
    }
    
    public boolean isFull() {
        return size == capacity;
    }
}
```

### Visualization
```
Initial: front = 0, rear = -1, size = 0
[ ][ ][ ][ ][ ]

Enqueue(5): front = 0, rear = 0, size = 1
[5][ ][ ][ ][ ]

Enqueue(2): front = 0, rear = 1, size = 2
[5][2][ ][ ][ ]

Enqueue(8): front = 0, rear = 2, size = 3
[5][2][8][ ][ ]

Dequeue(): returns 5, front = 1, rear = 2, size = 2
[ ][2][8][ ][ ]

Enqueue(1): front = 1, rear = 3, size = 3
[ ][2][8][1][ ]

Circular Wraparound Example:
[1][2][8][1][2]  <- rear wraps around to beginning
```

### Key Points
- **Two Pointers**: `front` and `rear` pointers
- **Circular Array**: Uses modulo operation for wraparound
- **O(1) Operations**: Enqueue, dequeue, and front are all constant time

## Discussion Points 

### 1. Why Use Arrays?
- **Memory Efficiency**: Contiguous memory allocation
- **Cache Performance**: Better cache locality
- **Predictable Performance**: No dynamic allocation overhead
- **Simple Implementation**: Easy to understand and debug

### 2. Circular Array Concept 
- **Problem**: Without circular array, space gets wasted
- **Solution**: Modulo operation for wraparound
- **Benefits**: Reuses freed space efficiently
- **Implementation**: `(index + 1) % capacity`

### 3. Trade-offs and Considerations 
- **Fixed Size**: Need to know maximum capacity
- **Memory Usage**: Arrays vs linked lists
- **Performance**: Cache-friendly vs dynamic allocation
- **Complexity**: Simple vs more complex implementations

### 4. Real-world Applications 
- **Stack Applications**:
  - Function call stack
  - Undo operations in text editors
  - Expression evaluation
  - Browser back button

- **Queue Applications**:
  - Print spooling
  - Task scheduling
  - Breadth-first search
  - Message queues

## Practice Questions

1. **Stack**: What happens if you try to pop from an empty stack?
2. **Queue**: How does the circular array prevent space waste?
3. **Comparison**: When would you choose array implementation over linked list?
4. **Application**: How would you implement an undo feature using a stack?

### Answers

1. **Stack Pop from Empty Stack**:
   - The operation will throw a `RuntimeException` with message "Stack is empty"
   - This prevents accessing invalid memory locations
   - Always check `isEmpty()` before popping
   ```java
   if (isEmpty()) {
       throw new RuntimeException("Stack is empty");
   }
   ```

2. **Circular Array Space Efficiency**:
   - Without circular array: After dequeueing elements, front space becomes unusable
   - With circular array: Uses modulo operation `(index + 1) % capacity` to wrap around
   - Example: When rear reaches end, it wraps to index 0, reusing freed space
   - This allows the queue to use the full array capacity efficiently

3. **Array vs Linked List Choice**:
   - **Choose Array when**:
     - You know the maximum size in advance
     - You need random access to elements
     - Memory efficiency is critical
     - Cache performance is important
   - **Choose Linked List when**:
     - Size is unknown or highly variable
     - Frequent insertions/deletions in middle
     - Memory allocation overhead is acceptable

4. **Undo Feature Implementation**:
   ```java
   class UndoManager {
       private Stack<String> undoStack = new Stack<>();
       
       public void performAction(String action) {
           // Save current state before action
           undoStack.push(getCurrentState());
           // Execute the action
           executeAction(action);
       }
       
       public void undo() {
           if (!undoStack.isEmpty()) {
               String previousState = undoStack.pop();
               restoreState(previousState);
           }
       }
   }
   ```
   - Each action pushes the previous state onto the stack
   - Undo pops the last state and restores it
   - LIFO nature ensures correct undo order

## Summary

- **Stack**: Single pointer, LIFO, simple implementation
- **Queue**: Two pointers, FIFO, circular array for efficiency
- **Arrays**: Memory efficient, cache-friendly, predictable performance
- **Applications**: Both structures have numerous real-world uses

This implementation approach provides a solid foundation for understanding how fundamental data structures can be efficiently implemented using basic array operations.

## LeetCode-Style Problem: Valid Parentheses

### Problem Description
Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

### Examples
```
Input: s = "()"
Output: true

Input: s = "()[]{}"
Output: true

Input: s = "(]"
Output: false

Input: s = "([)]"
Output: false

Input: s = "{[]}"
Output: true
```

### Solution Using Stack
```java
class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        
        for (char c : s.toCharArray()) {
            // If it's an opening bracket, push to stack
            if (c == '(' || c == '{' || c == '[') {
                stack.push(c);
            }
            // If it's a closing bracket
            else {
                // If stack is empty, no matching opening bracket
                if (stack.isEmpty()) {
                    return false;
                }
                
                // Check if the top of stack matches the closing bracket
                char top = stack.pop();
                if ((c == ')' && top != '(') ||
                    (c == '}' && top != '{') ||
                    (c == ']' && top != '[')) {
                    return false;
                }
            }
        }
        
        // Stack should be empty if all brackets are properly matched
        return stack.isEmpty();
    }
}
```

### Step-by-Step Execution
```
Input: "([)]"

Step 1: '[' -> stack: ['[']
Step 2: '(' -> stack: ['[', '(']
Step 3: ')' -> pop '(' from stack, matches ✓
        stack: ['[']
Step 4: ']' -> pop '[' from stack, matches ✓
        stack: []
Result: true (stack is empty)

Input: "([)]"

Step 1: '(' -> stack: ['(']
Step 2: '[' -> stack: ['(', '[']
Step 3: ')' -> pop '[' from stack, doesn't match '('
Result: false
```

### Time and Space Complexity
- **Time Complexity**: O(n) where n is the length of the string
- **Space Complexity**: O(n) for the stack in worst case

### Key Insights
1. **Stack Property**: LIFO nature perfectly matches bracket matching
2. **Opening Brackets**: Always push to stack
3. **Closing Brackets**: Must match the most recent opening bracket (top of stack)
4. **Validation**: Stack must be empty at the end

### Common Mistakes to Avoid
1. Not checking if stack is empty before popping
2. Not checking if stack is empty at the end
3. Incorrect bracket matching logic
4. Using wrong data structure (queue instead of stack)

This problem demonstrates how the LIFO property of stacks naturally solves bracket matching problems, making it a classic example of stack applications in algorithm problems. 