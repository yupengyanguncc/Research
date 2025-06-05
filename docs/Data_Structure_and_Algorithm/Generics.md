---
title: Generics
parent: Data Structure and Algorithm
author: Yupeng
date: 2025-06-01
layout: default
nav_order: 2.14
math: katex
emoji: jemoji
---

# Generics in Java

Generics is a feature in Java that allows you to write classes, interfaces, and methods that can work with different data types while maintaining type safety. It enables you to create type-safe collections and eliminate the need for type casting. Code used in this material [Code](GenericSearch.java) :cool:

## Why Use Generics?

1. **Type Safety**: Catch type errors at compile time rather than runtime
2. **Eliminate Type Casting**: No need to cast objects when retrieving from collections
3. **Code Reusability**: Write one class/method that works with multiple types
4. **Better Code Organization**: Create more flexible and reusable code

## Basic Syntax

### Generic Class
```java
public class Box<T> {
    private T content;  

    public Box(){
        this.content = null;

    }
    public Box(T content){
        this.content = content;
    }

    public void set(T content) {
        this.content = content;
    }
    
    public T get() {
        return content;
    }
}
```

#### Type Parameter Naming
- Any valid identifier can be used as a type parameter name
- Standard naming conventions:
  - `T` - Type
  - `E` - Element
  - `K` - Key
  - `V` - Value
  - `N` - Number
- While custom names (like `Yupeng`) are allowed, it's recommended to follow standard conventions for better code readability （<span style="color: red">Not recommend</span> )

Like this :fireworks:
```java
    public static class Box<Yupeng> {
        private Yupeng content;
        public void set(Yupeng content) {
            this.content = content;
        }
        public Yupeng get() {
            return content;
        }
    }
```



#### Constructors and Setters
1. **Parameterized Constructor**:
```java
public Box(T content) {
    this.content = content;
}
```
- Requires an initial value when creating an object
- Ensures the object has a value from creation

2. **Default Constructor**:
```java
public Box() {
    // Can set default value, e.g., null
}
```
- Allows creating empty objects
- Values can be set later using setter

3. **Setter Method**:
```java
public void set(T content) {
    this.content = content;
}
```
- Allows changing the value after object creation
- Can be called multiple times to update the value
- Provides flexibility in modifying object state
- Example usage:
  ```java
  Box<String> box = new Box<>();  // Create empty box
  box.set("Hello");               // Set initial value
  box.set("World");               // Update value later
  ```

4. **Constructor Overloading**:
- Multiple constructors can coexist
- The appropriate constructor is called based on whether parameters are provided
- Provides flexible object creation options

#### Usage Example
```java
// Using parameterized constructor
Box<String> box1 = new Box<>("Hello");  // Must provide initial value

// Using default constructor
Box<String> box2 = new Box<>();         // Can create empty object
box2.set("Hello");                      // Set value later
```

## Comparison: Generic Method vs Generic Class Implementation of Linear Search

### Generic Method Implementation
```java
public class GenericLinearSearch {
    public static <T> int linearSearch(T[] arr, T target) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i].equals(target)) {
                return i;
            }
        }
        return -1;
    }
}
```
- **Scope**: Type parameter `<T>` is only used within the method
- **Usage**: Can be called directly without creating an instance
- **Flexibility**: Can search different array types in different calls
- **Example Usage**:
  ```java
  linearSearch(array1, target1);  // Search integer array
  linearSearch(array2, target2);  // Search string array
  linearSearch(array3, target3);  // Search any other type array
  ```

### Generic Class Implementation
```java
public class GenericLinearSearch<T> {
    private T[] array;

    public GenericLinearSearch(T[] array) {
        this.array = array;
    }

    public int linearSearch(T target) {
        for (int i = 0; i < array.length; i++) {
            if (array[i].equals(target)) {
                return i;
            }
        }
        return -1;
    }
}
```
- **Scope**: Type parameter `<T>` is used throughout the class
- **Usage**: Requires creating an instance with a specific array type
- **Flexibility**: Once created, can only search arrays of the same type
- **Example Usage**:
  ```java
  GenericLinearSearch<Integer> search = new GenericLinearSearch<>(array1);
  search.linearSearch(target2);  // Can only search integer arrays
  ```

### Key Differences
1. **Type Binding**:
   - Generic Method: Type is determined at each method call
   - Generic Class: Type is fixed when the instance is created

2. **Memory Usage**:
   - Generic Method: No instance needed, more memory efficient
   - Generic Class: Requires instance creation, stores array reference

3. **Reusability**:
   - Generic Method: Can search different array types in different calls
   - Generic Class: Can only search arrays of the type specified at creation

4. **Use Case Preference**:
   - Generic Method: Better for one-time searches on different array types
   - Generic Class: Better when you need to perform multiple searches on the same array