---
title: Node and LinkedList Implementation in Java
parent: Data Structure and Algorithm
author: Yupeng
date: 2025-06-25
layout: default
nav_order: 3.5
math: katex
emoji: jemoji
---

# Node and LinkedList Implementation in Java

## Overview
This document covers the implementation of nodes and linked lists in Java, providing a comprehensive understanding of these fundamental data structures. We'll explore how nodes form the building blocks of linked lists and examine practical implementations with real-world examples.

## Node Implementation

### Basic Concept
A node is the fundamental building block of linked data structures. Each node contains data and a reference to the next node (and optionally the previous node for doubly linked lists).

### Java Implementation
```java
// Basic Node for Singly Linked List
class Node {
    int data;
    Node next;
    
    public Node(int data) {
        this.data = data;
        this.next = null;
    }
}

// Node for Doubly Linked List
class DoublyNode {
    int data;
    DoublyNode next;
    DoublyNode prev;
    
    public DoublyNode(int data) {
        this.data = data;
        this.next = null;
        this.prev = null;
    }
}
```

### Visualization
```
Singly Linked Node:
[3] ──▶ [7] ──▶ [12] ──▶ null

Doubly Linked Node:
null ◀──▶ [A] ◀──▶ [B] ◀──▶ [C] ◀──▶ [D] ◀──▶ null
```

## Singly Linked List Implementation

### Java Implementation
```java
class SinglyLinkedList {
    private Node head;
    private int size;
    
    public SinglyLinkedList() {
        head = null;
        size = 0;
    }
    
    // Insert at the beginning
    public void insertAtBeginning(int data) {
        Node newNode = new Node(data);
        newNode.next = head;
        head = newNode;
        size++;
    }
    
    // Insert at the end
    public void insertAtEnd(int data) {
        Node newNode = new Node(data);
        
        if (head == null) {
            head = newNode;
        } else {
            Node current = head;
            while (current.next != null) {
                current = current.next;
            }
            current.next = newNode;
        }
        size++;
    }
    
    // Insert at specific position
    public void insertAtPosition(int data, int position) {
        if (position < 0 || position > size) {
            throw new IllegalArgumentException("Invalid position");
        }
        
        if (position == 0) {
            insertAtBeginning(data);
            return;
        }
        
        Node newNode = new Node(data);
        Node current = head;
        for (int i = 0; i < position - 1; i++) {
            current = current.next;
        }
        
        newNode.next = current.next;
        current.next = newNode;
        size++;
    }
    
    // Delete from beginning
    public int deleteFromBeginning() {
        if (isEmpty()) {
            throw new RuntimeException("List is empty");
        }
        
        int data = head.data;
        head = head.next;
        size--;
        return data;
    }
    
    // Delete from end
    public int deleteFromEnd() {
        if (isEmpty()) {
            throw new RuntimeException("List is empty");
        }
        
        if (size == 1) {
            int data = head.data;
            head = null;
            size--;
            return data;
        }
        
        Node current = head;
        while (current.next.next != null) {
            current = current.next;
        }
        
        int data = current.next.data;
        current.next = null;
        size--;
        return data;
    }
    
    // Search for an element
    public boolean search(int data) {
        Node current = head;
        while (current != null) {
            if (current.data == data) {
                return true;
            }
            current = current.next;
        }
        return false;
    }
    
    // Display the list
    public void display() {
        Node current = head;
        while (current != null) {
            System.out.print(current.data + " -> ");
            current = current.next;
        }
        System.out.println("null");
    }
    
    // Get size
    public int getSize() {
        return size;
    }
    
    // Check if empty
    public boolean isEmpty() {
        return head == null;
    }
}
```

### Visualization of Operations
```
Initial State:
head = null, size = 0

Insert 5 at beginning:
head ──▶ [5] ──▶ null
size = 1

Insert 2 at end:
head ──▶ [5] ──▶ [2] ──▶ null
size = 2

Insert 8 at position 1:
Step 1: Find node at position 0 (before insertion point)
        current = head (points to node 5)
Step 2: Create new node [8]
Step 3: newNode.next = current.next;  // [8].next = [2]
Step 4: current.next = newNode;       // [5].next = [8]
Result: head ──▶ [5] ──▶ [8] ──▶ [2] ──▶ null
size = 3

Delete from beginning:
Step 1: Save head.data = 5
Step 2: head = head.next;  // head now points to [8]
Result: head ──▶ [8] ──▶ [2] ──▶ null
size = 2

Delete from end:
Step 1: Find second-to-last node
        current = head (points to [8])
        current.next.next = null, so stop here
Step 2: Save current.next.data = 2
Step 3: current.next = null;  // Remove last node
Result: head ──▶ [8] ──▶ null
size = 1

Search for value 8:
Step 1: current = head (points to [8])
Step 2: current.data == 8? Yes! Return true

Search for value 5:
Step 1: current = head (points to [8])
Step 2: current.data == 5? No, move to next
Step 3: current = current.next (points to null)
Step 4: current == null? Yes, return false
```

## Doubly Linked List Implementation

### Java Implementation
```java
class DoublyLinkedList {
    private DoublyNode head;
    private DoublyNode tail;
    private int size;
    
    public DoublyLinkedList() {
        head = null;
        tail = null;
        size = 0;
    }
    
    // Insert at the beginning
    public void insertAtBeginning(int data) {
        DoublyNode newNode = new DoublyNode(data);
        
        if (isEmpty()) {
            head = tail = newNode;
        } else {
            newNode.next = head;
            head.prev = newNode;
            head = newNode;
        }
        size++;
    }
    
    // Insert at the end
    public void insertAtEnd(int data) {
        DoublyNode newNode = new DoublyNode(data);
        
        if (isEmpty()) {
            head = tail = newNode;
        } else {
            newNode.prev = tail;
            tail.next = newNode;
            tail = newNode;
        }
        size++;
    }
    
    // Delete from beginning
    public int deleteFromBeginning() {
        if (isEmpty()) {
            throw new RuntimeException("List is empty");
        }
        
        int data = head.data;
        
        if (size == 1) {
            head = tail = null;
        } else {
            head = head.next;
            head.prev = null;
        }
        size--;
        return data;
    }
    
    // Delete from end
    public int deleteFromEnd() {
        if (isEmpty()) {
            throw new RuntimeException("List is empty");
        }
        
        int data = tail.data;
        
        if (size == 1) {
            head = tail = null;
        } else {
            tail = tail.prev;
            tail.next = null;
        }
        size--;
        return data;
    }
    
    // Display forward
    public void displayForward() {
        DoublyNode current = head;
        while (current != null) {
            System.out.print(current.data + " <-> ");
            current = current.next;
        }
        System.out.println("null");
    }
    
    // Display backward
    public void displayBackward() {
        DoublyNode current = tail;
        while (current != null) {
            System.out.print(current.data + " <-> ");
            current = current.prev;
        }
        System.out.println("null");
    }
    
    // Get size
    public int getSize() {
        return size;
    }
    
    // Check if empty
    public boolean isEmpty() {
        return head == null;
    }
}
```

### Visualization
```
null ◀── [prev|data:5|next] ◀──▶ [prev|data:8|next] ◀──▶ [prev|data:2|next] ◀──▶ null
         ▲         ▲         ▲
         │         │         │
       head    middle node   tail

Each node has two pointers:
- prev points to the previous node
- next points to the next node

Both prev and next need to be maintained during insert/delete operations.
```

## Practical Examples

### Example 1: Browser History Management
```java
class BrowserHistory {
    private DoublyLinkedList history;
    private DoublyNode currentPage;
    
    public BrowserHistory(String homepage) {
        history = new DoublyLinkedList();
        history.insertAtEnd(homepage.hashCode()); // Using hash for simplicity
        currentPage = history.head;
    }
    
    public void visit(String url) {
        // Remove all pages after current page
        while (currentPage.next != null) {
            history.deleteFromEnd();
        }
        
        // Add new page
        history.insertAtEnd(url.hashCode());
        currentPage = currentPage.next;
    }
    
    public String back(int steps) {
        for (int i = 0; i < steps && currentPage.prev != null; i++) {
            currentPage = currentPage.prev;
        }
        return "Page: " + currentPage.data;
    }
    
    public String forward(int steps) {
        for (int i = 0; i < steps && currentPage.next != null; i++) {
            currentPage = currentPage.next;
        }
        return "Page: " + currentPage.data;
    }
    
    public void displayHistory() {
        System.out.println("Browser History:");
        history.displayForward();
    }
}

// Usage Example
public class BrowserExample {
    public static void main(String[] args) {
        BrowserHistory browser = new BrowserHistory("google.com");
        
        browser.visit("facebook.com");
        browser.visit("twitter.com");
        browser.visit("linkedin.com");
        
        System.out.println("Current: " + browser.forward(0));
        System.out.println("Back 2: " + browser.back(2));
        System.out.println("Forward 1: " + browser.forward(1));
        
        browser.displayHistory();
    }
}
```

### Example 2: Task Scheduler with Priority
```java
class Task {
    String name;
    int priority;
    String description;
    
    public Task(String name, int priority, String description) {
        this.name = name;
        this.priority = priority;
        this.description = description;
    }
    
    @Override
    public String toString() {
        return name + " (Priority: " + priority + ")";
    }
}

class TaskScheduler {
    private SinglyLinkedList highPriority;
    private SinglyLinkedList mediumPriority;
    private SinglyLinkedList lowPriority;
    
    public TaskScheduler() {
        highPriority = new SinglyLinkedList();
        mediumPriority = new SinglyLinkedList();
        lowPriority = new SinglyLinkedList();
    }
    
    public void addTask(Task task) {
        switch (task.priority) {
            case 1:
                highPriority.insertAtEnd(task.hashCode());
                break;
            case 2:
                mediumPriority.insertAtEnd(task.hashCode());
                break;
            case 3:
                lowPriority.insertAtEnd(task.hashCode());
                break;
            default:
                System.out.println("Invalid priority level");
        }
    }
    
    public Task getNextTask() {
        // First check high priority
        if (!highPriority.isEmpty()) {
            return new Task("High Priority Task", 1, "Task ID: " + highPriority.deleteFromBeginning());
        }
        // Then medium priority
        else if (!mediumPriority.isEmpty()) {
            return new Task("Medium Priority Task", 2, "Task ID: " + mediumPriority.deleteFromBeginning());
        }
        // Finally low priority
        else if (!lowPriority.isEmpty()) {
            return new Task("Low Priority Task", 3, "Task ID: " + lowPriority.deleteFromBeginning());
        }
        else {
            return null;
        }
    }
    
    public void displayAllTasks() {
        System.out.println("High Priority Tasks:");
        highPriority.display();
        System.out.println("Medium Priority Tasks:");
        mediumPriority.display();
        System.out.println("Low Priority Tasks:");
        lowPriority.display();
    }
}

// Usage Example
public class TaskSchedulerExample {
    public static void main(String[] args) {
        TaskScheduler scheduler = new TaskScheduler();
        
        scheduler.addTask(new Task("Fix critical bug", 1, "Urgent fix needed"));
        scheduler.addTask(new Task("Code review", 2, "Review pull request"));
        scheduler.addTask(new Task("Update documentation", 3, "Non-urgent"));
        scheduler.addTask(new Task("Security patch", 1, "High security priority"));
        
        System.out.println("All tasks:");
        scheduler.displayAllTasks();
        
        System.out.println("\nProcessing tasks:");
        Task task;
        while ((task = scheduler.getNextTask()) != null) {
            System.out.println("Processing: " + task);
        }
    }
}
```

## Discussion Points

### 1. Singly vs Doubly Linked Lists
- **Singly Linked List**:
  - Simpler implementation
  - Less memory overhead
  - Can only traverse forward
  - Good for simple sequential access

- **Doubly Linked List**:
  - Can traverse both directions
  - Easier deletion operations
  - More memory overhead
  - Better for complex operations

### 2. Time Complexity Analysis
| Operation | Singly Linked List | Doubly Linked List |
|-----------|-------------------|-------------------|
| Insert at beginning | O(1) | O(1) |
| Insert at end | O(n) | O(1) |
| Delete from beginning | O(1) | O(1) |
| Delete from end | O(n) | O(1) |
| Search | O(n) | O(n) |
| Access by index | O(n) | O(n) |

### 3. Memory Considerations
- **Node Overhead**: Each node requires extra memory for references
- **Cache Performance**: Poor cache locality compared to arrays
- **Memory Fragmentation**: Dynamic allocation can cause fragmentation

### 4. When to Use Linked Lists
- **Use when**:
  - Frequent insertions/deletions at beginning
  - Unknown size requirements
  - No random access needed
  - Implementing stacks/queues

- **Avoid when**:
  - Random access is frequent
  - Memory efficiency is critical
  - Cache performance is important

## Practice Questions

1. **Node Creation**: How would you create a node that can store any data type?
2. **Cycle Detection**: How can you detect if a linked list has a cycle?
3. **Reversal**: How would you reverse a singly linked list?
4. **Merge**: How would you merge two sorted linked lists?

### Answers

1. **Generic Node**:
```java
class GenericNode<T> {
    T data;
    GenericNode<T> next;
    
    public GenericNode(T data) {
        this.data = data;
        this.next = null;
    }
}
```

2. **Cycle Detection (Floyd's Algorithm)**:
```java
public boolean hasCycle(Node head) {
    if (head == null || head.next == null) return false;
    
    Node slow = head;
    Node fast = head.next;
    
    while (slow != fast) {
        if (fast == null || fast.next == null) return false;
        slow = slow.next;
        fast = fast.next.next;
    }
    return true;
}
```

3. **List Reversal**:
```java
public Node reverse(Node head) {
    Node prev = null;
    Node current = head;
    Node next = null;
    
    while (current != null) {
        next = current.next;
        current.next = prev;
        prev = current;
        current = next;
    }
    return prev;
}
```

4. **Merge Sorted Lists**:
```java
public Node mergeSortedLists(Node l1, Node l2) {
    if (l1 == null) return l2;
    if (l2 == null) return l1;
    
    Node result;
    if (l1.data <= l2.data) {
        result = l1;
        result.next = mergeSortedLists(l1.next, l2);
    } else {
        result = l2;
        result.next = mergeSortedLists(l1, l2.next);
    }
    return result;
}
```

## Summary

- **Nodes**: Fundamental building blocks with data and references
- **Singly Linked Lists**: Simple, forward-only traversal
- **Doubly Linked Lists**: Bidirectional traversal, easier deletions
- **Applications**: Browser history, task scheduling, undo systems
- **Trade-offs**: Flexibility vs memory overhead, cache performance

This implementation approach provides a solid foundation for understanding linked data structures and their practical applications in software development.

## Problem: Remove Nth Node From End

### Problem Description
Given the head of a linked list, remove the nth node from the end of the list and return its head.

### Examples
```
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Input: head = [1], n = 1
Output: []

Input: head = [1,2], n = 1
Output: [1]
```

### Solution Using Two Pointers
```java
class Solution {
    public Node removeNthFromEnd(Node head, int n) {
        Node dummy = new Node(0);
        dummy.next = head;
        
        Node first = dummy;
        Node second = dummy;
        
        // Move first pointer n+1 steps ahead
        for (int i = 0; i <= n; i++) {
            first = first.next;
        }
        
        // Move both pointers until first reaches end
        while (first != null) {
            first = first.next;
            second = second.next;
        }
        
        // Remove the nth node from end
        second.next = second.next.next;
        
        return dummy.next;
    }
}
```

### Step-by-Step Execution
```
Input: [1,2,3,4,5], n = 2

Step 1: Create dummy node
dummy -> [1] -> [2] -> [3] -> [4] -> [5] -> null

Step 2: Move first pointer n+1 steps (3 steps)
first: [4], second: dummy

Step 3: Move both pointers until first reaches end
first: null, second: [3]

Step 4: Remove nth node from end
[3].next = [5], result: [1,2,3,5]
```

### Key Insights
1. **Two Pointer Technique**: Use two pointers with n steps difference
2. **Dummy Node**: Helps handle edge cases (removing head)
3. **Single Pass**: O(n) time complexity with O(1) space
4. **Boundary Conditions**: Handle cases where n equals list length

This problem demonstrates the power of the two-pointer technique in linked list manipulation, a common pattern in linked list problems. 