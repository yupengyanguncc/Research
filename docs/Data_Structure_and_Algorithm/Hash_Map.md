---
title: Hash Map
parent: Data Structure and Algorithm
author: Yupeng
date: 2025-06-01
layout: default
nav_order: 2.8
math: katex
emoji: jemoji
---

# HashMap in Java

HashMap is a fundamental data structure in Java that implements the Map interface. It stores data in key-value pairs and provides efficient operations for storing, retrieving, and manipulating data.

## Key Characteristics

- **Generic Class**: HashMap<K,V> where:
  - K: the type of keys maintained by the map
  - V: the type of mapped values
- **Key-Value Storage**: Each element is stored as a key-value pair
- **No Duplicate Keys**: Each key must be unique

## Basic Operations

### 1. Creating a HashMap
```java
HashMap<String, Integer> studentScores = new HashMap<>();
```

HashMap can be created in several different ways, each with its specific purpose:

1. **Default Constructor**:
```java
HashMap<String, Integer> studentScores = new HashMap<>();
// Default initial capacity: 16
// Default load factor: 0.75f
```

2. **Specifying Initial Capacity**:
```java
HashMap<String, Integer> studentScores = new HashMap<>(100);
// Initial capacity: 100
// Default load factor: 0.75f
```

3. **Specifying Initial Capacity and Load Factor**:
```java
HashMap<String, Integer> studentScores = new HashMap<>(100, 0.5f);
// Initial capacity: 100
// Load factor: 0.5f
```

4. **Creating from Another Map**:
   
```java
HashMap<String, Integer> existingMap = new HashMap<>();
existingMap.put("A", 1);
existingMap.put("B", 2);

HashMap<String, Integer> map4 = new HashMap<>(existingMap);
// Creates a new HashMap containing all elements from existingMap
```

**Parameter Explanation**:
- **Initial Capacity**: The initial size of the internal array
  - Default value: 16
  - Recommendation: Specify initial capacity if you know the approximate number of elements to avoid frequent resizing

- **Load Factor**: Determines when the HashMap will resize
  - Default value: 0.75f (float type, 'f' indicates float)
  - Formula: resize when (number of elements / capacity) > load factor
  - Lower load factor: fewer collisions but more space required
  - Higher load factor: less space but more potential collisions

### 2. Adding Elements
- `put(key, value)`: Adds a new key-value pair
- Returns the previous value if key exists, null if it's a new key
```java
studentScores.put("Alice", 95);  // Add new entry
studentScores.put("Bob", 88);
Integer oldValue = studentScores.put("Alice", 97);  // Updates existing entry
```

### 3. Checking Elements
- `containsKey(key)`: Checks if a key exists
- `get(key)`: Retrieves value for a given key
```java
String checkName = "Charlie";
if (studentScores.containsKey(checkName)) {
    System.out.println(checkName + " exists in the map");
} else {
    System.out.println(checkName + " does not exist in the map");
}
```

### 4. Replacing Elements
- `replace(key, oldValue, newValue)`: Replaces value only if key exists and current value matches
- `replace(key, newValue)`: Simple value replacement
```java
boolean replaced = studentScores.replace("Bob", 88, 90);  // Conditional replace
boolean notReplaced = studentScores.replace("Charlie", 85, 90);  // Try to replace non-existent key
studentScores.replace("Alice", 100);  // Simple replace
```

### 5. Iterating Through HashMap
Three common methods to iterate:

#### 1. Using for-each loop with keySet:
```java
// keySet(): returns a Set of all keys in the HashMap
Set<String> keys = studentScores.keySet();
for (String key : keys) {
    System.out.println(key + ": " + studentScores.get(key));
}
```

#### 2. Using forEach with lambda:
```java
// Lambda Expression: parameter -> expression
// - parameter: input parameter 
// - -> : arrow operator
// - expression: code to execute
keys.forEach(key -> System.out.println(key + ": " + studentScores.get(key)));
```

Lambda expressions, introduced in Java 8, provide a concise way to write anonymous functions. They are particularly useful with HashMap's forEach method:

**Lambda Syntax**:
   
```java
// Single parameter
key -> System.out.println(key)

// Multiple parameters
(key, value) -> System.out.println(key + ": " + value)

// Multiple lines
key -> {
    System.out.println("Processing: " + key);
    System.out.println("Value: " + studentScores.get(key));
}
```

```java
// Iterate with lambda
studentScores.forEach((key, value) -> 
    System.out.println(key + ": " + value)
);

```

#### 3. Using iterator:
   
```java
// Iterator: An object that enables you to traverse through a collection
// - hasNext(): checks if there are more elements
// - next(): returns the next element
// - remove(): removes the last element returned by next()
var iterator = keys.iterator();
while (iterator.hasNext()) {
    String key = iterator.next();
    System.out.println(key + ": " + studentScores.get(key));
}
```

### 6. Clearing HashMap
- `clear()`: Removes all mappings
```java
studentScores.clear();
System.out.println("Number of students after clearing: " + studentScores.size());
```

## Related Files
- [HashMapDemo.java](../Data_Structure_and_Algorithm/HashMapDemo.java) - Complete example demonstrating HashMap operations 