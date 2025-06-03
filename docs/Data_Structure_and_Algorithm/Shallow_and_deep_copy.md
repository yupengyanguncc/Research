---
title: Shallow and Deep Copy
parent: Data Structure and Algorithm
author: Yupeng
date: 2025-06-03
layout: default
nav_order: 2.81
math: katex
emoji: jemoji
---

# Shallow Copy vs Deep Copy

Code used in this material [Code](Copy.java) :cool:

## Basic Concept

In Java, there are two ways to copy objects: shallow copy and deep copy. Let's understand the difference with a concrete example.

```java
// Example classes
class Address {
    String street;
    String city;
    
    public Address(String street, String city) {
        this.street = street;
        this.city = city;
    }
}

class Person {
    String name;
    Address address;
    
    public Person(String name, Address address) {
        this.name = name;
        this.address = address;
    }
}
```

## Shallow Copy

A shallow copy creates a new object but shares the internal objects with the original object.

### Characteristics:
- Only copies object references
- New object shares internal objects with original
- Modifying internal objects affects both copies

### Example:
```java
// Shallow copy example
Person person1 = new Person("John", new Address("123 Main St", "New York"));
Person person2 = person1;  // Shallow copy

// Modifying person2's address affects person1
person2.address.city = "Boston";
System.out.println(person1.address.city);  // Prints "Boston"
```

## Deep Copy

A deep copy creates a completely independent copy of an object and all its internal objects.

### Characteristics:
- Creates completely independent copies
- New object has its own internal objects
- Modifying internal objects doesn't affect original

### Example:
```java
// Deep copy example
Person person3 = new Person("John", new Address("123 Main St", "New York"));
Person person4 = new Person(
    person3.name,
    new Address(person3.address.street, person3.address.city)
);  // Deep copy

// Modifying person4's address doesn't affect person3
person4.address.city = "Boston";
System.out.println(person3.address.city);  // Still prints "New York"
```

## Visual Representation

```
Shallow Copy (Shared Memory Address):
person1 ─────┐
             ├──> Address object (Memory Address: 0x1234)
person2 ─────┘

Deep Copy (Independent Memory Addresses):
person3 ────> Address object 1 (Memory Address: 0x5678)
person4 ────> Address object 2 (Memory Address: 0x9ABC)
```

## When to Use Each

### Use Deep Copy when:
- You need completely independent objects
- Data integrity is critical
- Modifications to the copy shouldn't affect the original

### Use Shallow Copy when:
- You only need to share data
- Memory efficiency is important
- You're aware of the shared references

### Considerations:
- Deep copy is more resource-intensive but ensures data independence
- Shallow copy is more efficient but requires careful handling of shared data
- Choose based on your specific requirements for data independence and resource usage


