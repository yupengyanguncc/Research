---
title: Linear Data Structure
parent: Data Structure and Algorithm
author: Yupeng
date: 2025-06-15
layout: default
nav_order: 3.1
math: katex
emoji: jemoji
---

# Linear Data Structure

A linear data structure is a type of data structure where data elements are arranged in a sequential manner, with each element having at most one predecessor and one successor.

## Main Types

### 1. Array
- Contiguous memory space
- Fixed size
- Direct access through index
- Time complexity:
  - Access: O(1)
  - Insert/Delete: O(n)

Visualization:
```
Memory Layout:
[0] [1] [2] [3] [4]  <- Indices
 5   2   8   1   9   <- Values
```

### 2. Linked List
- Non-contiguous memory space
- Dynamic size
- Connected through pointers
- Time complexity:
  - Access: O(n)
  - Insert/Delete: O(1)

#### Types of Linked Lists

1. Singly Linked List:
```
[5] -> [2] -> [8] -> [1] -> [9] -> null
```

2. Doubly Linked List:
```
null <- [5] <-> [2] <-> [8] <-> [1] <-> [9] -> null
```

3. Circular Linked List:
```
[5] -> [2] -> [8] -> [1] -> [9] -┐
^                                |
└────────────────────────────────┘
```

### 3. Stack
- Last In First Out (LIFO)
- Main operations:
  - Push
  - Pop
  - Peek
- Time complexity: O(1)

Visualization:
```
    [9]  <- Top (Last In)
    [1]
    [8]
    [2]
    [5]  <- Bottom (First In)
```


### 4. Queue
- First In First Out (FIFO)
- Main operations:
  - Enqueue
  - Dequeue
  - Front
- Time complexity: O(1)

Visualization:
```
Front -> [5] [2] [8] [1] [9] <- Rear
```


## Applications

1. Array:
   - Random access required
   - Fixed data size
   - Memory efficiency needed

2. Linked List:
   - Frequent insertions and deletions
   - Unknown data size
   - No random access needed

3. Stack:
   - Function calls
   - Expression evaluation
   - Parenthesis matching

4. Queue:
   - Task scheduling
   - Message queues
   - Breadth-first search

## Implementation Examples

### Array Implementation
```java
// Array example
int[] array = new int[]{1, 2, 3, 4, 5};
System.out.println(array[0]);  // Access element

// Dynamic array (ArrayList)
ArrayList<Integer> dynamicArray = new ArrayList<>();
dynamicArray.add(1);
dynamicArray.add(2);
dynamicArray.add(3);
```

### Linked List Implementation
```java
// Node definition
class ListNode {
    int value;
    ListNode next;
    
    public ListNode(int value) {
        this.value = value;
        this.next = null;
    }
}

// Linked List implementation
class LinkedList {
    private ListNode head;
    
    public LinkedList() {
        head = null;
    }
    
    public void add(int value) {
        ListNode newNode = new ListNode(value);
        if (head == null) {
            head = newNode;
            return;
        }
        ListNode current = head;
        while (current.next != null) {
            current = current.next;
        }
        current.next = newNode;
    }
}
```

### Stack Implementation
```java
class Stack {
    private ArrayList<Integer> elements;
    
    public Stack() {
        elements = new ArrayList<>();
    }
    
    public void push(int value) {
        elements.add(value);
    }
    
    public int pop() {
        if (isEmpty()) {
            throw new RuntimeException("Stack is empty");
        }
        return elements.remove(elements.size() - 1);
    }
    
    public int peek() {
        if (isEmpty()) {
            throw new RuntimeException("Stack is empty");
        }
        return elements.get(elements.size() - 1);
    }
    
    public boolean isEmpty() {
        return elements.isEmpty();
    }
}
```

### Queue Implementation
```java
class Queue {
    private ArrayList<Integer> elements;
    
    public Queue() {
        elements = new ArrayList<>();
    }
    
    public void enqueue(int value) {
        elements.add(value);
    }
    
    public int dequeue() {
        if (isEmpty()) {
            throw new RuntimeException("Queue is empty");
        }
        return elements.remove(0);
    }
    
    public int front() {
        if (isEmpty()) {
            throw new RuntimeException("Queue is empty");
        }
        return elements.get(0);
    }
    
    public boolean isEmpty() {
        return elements.isEmpty();
    }
}

// Using Java's built-in Queue interface
Queue<Integer> builtInQueue = new LinkedList<>();
builtInQueue.offer(1);  // Enqueue
builtInQueue.poll();    // Dequeue
builtInQueue.peek();    // Front
```

## Summary

Linear data structures are fundamental in computer science, each with its own characteristics and use cases. Choosing the appropriate linear data structure is crucial for program efficiency and performance. In Java, we can use built-in collection frameworks (such as ArrayList, LinkedList) or implement these data structures ourselves.

## Array vs Linked List: Key Differences

### Memory Allocation
```
Array: Contiguous Memory Space
[0x1000][0x1004][0x1008][0x1012][0x1016]  <- Contiguous Memory Addresses
  5      2      8      1      9

Linked List: Non-contiguous Memory Space
[0x2000] -> [0x3000] -> [0x4000] -> [0x5000] -> [0x6000]
   5           2           8           1           9
```

### Key Advantages of Linked Lists

1. Dynamic Size
   - Array: Fixed size at creation, requires reallocation for expansion
   - Linked List: Can grow dynamically, no need for pre-allocation

2. Insertion and Deletion Efficiency
   - Array: Requires shifting elements for middle insertions/deletions
   ```
   Array Insertion Example:
   [5][2][8][1][9]  -> Insert 7 at position 2
   [5][2][7][8][1][9]  -> Need to shift 8,1,9
   ```
   - Linked List: Only needs to change pointers
   ```
   Linked List Insertion Example:
   [5] -> [2] -> [8] -> [1] -> [9]
   [5] -> [2] -> [7] -> [8] -> [1] -> [9]  -> Only two pointer changes needed
   ```

3. Memory Utilization
   - Array: Must allocate full size even if partially used
   - Linked List: Allocates only what's needed, no memory waste

### Real-world Applications

1. Text Editor
   - Uses linked list to store text for easy character insertion/deletion
   - Each character as a node allows easy editing at any position

2. Music Player
   - Playlist implementation using linked list
   - Easy to add, remove, and reorder songs
   - Supports loop playback (using circular linked list)

3. Undo Functionality
   - Implements undo stack using linked list
   - Each operation as a node
   - Easy to backtrack to previous states

4. Memory Management
   - Operating systems use linked lists to manage free memory blocks
   - Efficient memory allocation and deallocation

5. Graph Algorithms
   - Adjacency lists use linked lists to store graph edges
   - Space-efficient for sparse graphs

### When to Choose Array?

1. Random Access Needed
   - Array: O(1) time access to any element
   - Linked List: O(n) time access to any element

2. Fixed Size Data
   - Array: More memory efficient
   - Linked List: Has additional pointer overhead

3. Cache-friendly
   - Array: Contiguous memory, high cache hit rate
   - Linked List: Non-contiguous memory, low cache hit rate

### Practical Java Example

```java
public class ArrayVsLinkedList {
    public static void main(String[] args) {
        // 1. Array Example
        System.out.println("Array Operations:");
        int[] array = new int[5];
        array[0] = 5;
        array[1] = 2;
        array[2] = 8;
        array[3] = 1;
        array[4] = 9;
        
        // Inserting in the middle of array (inefficient)
        int[] newArray = new int[6];
        System.arraycopy(array, 0, newArray, 0, 2);  // Copy first 2 elements
        newArray[2] = 7;                             // Insert new element
        System.arraycopy(array, 2, newArray, 3, 3);  // Copy remaining elements
        array = newArray;
        
        // 2. LinkedList Example
        System.out.println("\nLinkedList Operations:");
        LinkedList<Integer> linkedList = new LinkedList<>();
        linkedList.add(5);
        linkedList.add(2);
        linkedList.add(8);
        linkedList.add(1);
        linkedList.add(9);
        
        // Inserting in the middle of linked list (efficient)
        linkedList.add(2, 7);  // Insert 7 at index 2
        
        // 3. Performance Comparison
        System.out.println("\nPerformance Comparison:");
        
        // Array access time
        long startTime = System.nanoTime();
        int element = array[3];  // Random access
        long endTime = System.nanoTime();
        System.out.println("Array random access time: " + (endTime - startTime) + " ns");
        
        // LinkedList access time
        startTime = System.nanoTime();
        element = linkedList.get(3);  // Sequential access
        endTime = System.nanoTime();
        System.out.println("LinkedList access time: " + (endTime - startTime) + " ns");
        
        // 4. Memory Usage
        System.out.println("\nMemory Usage:");
        System.out.println("Array size: " + array.length + " elements");
        System.out.println("LinkedList size: " + linkedList.size() + " elements");
        
        // 5. Real-world Example: Text Editor
        System.out.println("\nText Editor Example:");
        LinkedList<Character> textBuffer = new LinkedList<>();
        
        // Simulating text insertion
        String text = "Hello";
        for (char c : text.toCharArray()) {
            textBuffer.add(c);
        }
        
        // Inserting text in the middle
        textBuffer.add(2, 'X');
        
        // Displaying the result
        System.out.print("Text after insertion: ");
        for (char c : textBuffer) {
            System.out.print(c);
        }
        System.out.println();  // Output: HeXllo
    }
}
```

This example demonstrates:

1. Array Operations:
   - Fixed size initialization
   - Inefficient middle insertion (requires array copying)
   - Fast random access

2. LinkedList Operations:
   - Dynamic size
   - Efficient middle insertion
   - Sequential access

3. Performance Comparison:
   - Measures access time for both structures
   - Shows the trade-off between random and sequential access

4. Memory Usage:
   - Shows the size difference between array and linked list

5. Real-world Application:
   - Simulates a simple text editor using linked list
   - Demonstrates efficient text insertion

The output will show the performance differences and practical usage of both data structures. This helps understand when to use each structure in real applications.