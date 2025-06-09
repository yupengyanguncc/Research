---
title: Binary Search
parent: Data Structure and Algorithm
author: Yupeng
date: 2025-06-08
layout: default
nav_order: 2.31
math: katex
emoji: jemoji
---

# Binary Search

**Binary Search** is an efficient algorithm for finding an element in a sorted array. It works by repeatedly dividing the search interval in half.

**Key Points:**
- Array must be **sorted** before searching
- Time complexity: O(log n)
- Space complexity: O(1) for iterative, O(log n) for recursive
- Compare target with middle element
- If not found, eliminate half of the array

**Example Table: Binary Search Process**

| Step | Left | Right | Mid | Array[mid] | Action |
|------|------|-------|-----|------------|--------|
| 1    | 0    | 7     | 3   | 7          | 7 > 5, search left |
| 2    | 0    | 2     | 1   | 3          | 3 < 5, search right |
| 3    | 2    | 2     | 2   | 5          | Found! |

**Visualization:**
![Binary Search](../../assets/image/BinarySearch.gif)

```
Array: [1, 3, 5, 7, 9, 11, 13, 15]
Target: 5

Step 1: [1, 3, 5, 7, 9, 11, 13, 15]
         ↑        ↑              ↑
         L        M              R

Step 2: [1, 3, 5, 7, 9, 11, 13, 15]
         ↑  ↑  ↑
         L  M  R

Step 3: [1, 3, 5, 7, 9, 11, 13, 15]
               ↑
               L，R
               M
```

# Iterative Binary Search

**Iterative Binary Search** uses a loop to implement the binary search algorithm. It's more space-efficient than the recursive version.

**How it works:**
1. Initialize left and right pointers
2. While left <= right:
   - Calculate middle index
   - Compare target with middle element
   - Adjust search range accordingly
3. Return result

**Java Implementation:**

```java
public class BinarySearchDemo {
    public static int binarySearch(int[] arr, int target) {
        int left = 0;
        int right = arr.length - 1;
        
        while (left <= right) {
            int mid = left + (right - left) / 2;
            
            if (arr[mid] == target) {
                return mid;
            }
            
            if (arr[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        
        return -1; // Element not found
    }

    public static void main(String[] args) {
        int[] arr = {1, 3, 5, 7, 9, 11, 13, 15};
        int target = 5;
        int result = binarySearch(arr, target);
        System.out.println("Element found at index: " + result);
        // Output: Element found at index: 2
    }
}
```


# Binary Search Variations

## 1. First Occurrence

Find the first occurrence of a target element in a sorted array that may contain duplicates.

```java
public static int firstOccurrence(int[] arr, int target) {
    int left = 0;
    int right = arr.length - 1;
    int result = -1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        
        if (arr[mid] == target) {
            result = mid;
            right = mid - 1; // Continue searching left
        } else if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    
    return result;
}
```

## 2. Last Occurrence

Find the last occurrence of a target element in a sorted array that may contain duplicates.

```java
public static int lastOccurrence(int[] arr, int target) {
    int left = 0;
    int right = arr.length - 1;
    int result = -1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        
        if (arr[mid] == target) {
            result = mid;
            left = mid + 1; // Continue searching right
        } else if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    
    return result;
}
```

## 3. Ceiling of a Number

Find the smallest element in the array that is greater than or equal to the target.

```java
public static int ceiling(int[] arr, int target) {
    int left = 0;
    int right = arr.length - 1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        
        if (arr[mid] == target) {
            return mid;
        }
        
        if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    
    return left; // Return the insertion point
}
```

## 4. Floor of a Number

Find the largest element in the array that is less than or equal to the target.

```java
public static int floor(int[] arr, int target) {
    int left = 0;
    int right = arr.length - 1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        
        if (arr[mid] == target) {
            return mid;
        }
        
        if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    
    return right; // Return the largest element less than target
}
```

# Time Complexity Analysis

**Best Case:** O(1)
- Target element is found at the middle of the array

**Worst Case:** O(log n)
- Target element is not in the array
- Need to search until the array is empty

**Average Case:** O(log n)
- On average, we need to search half of the remaining elements


# Common Mistakes and Tips

1. **Integer Overflow**
   - Wrong: `mid = (left + right) / 2`
   - Correct: `mid = left + (right - left) / 2`
   
   **Why?**
   
   ```
   Example with large numbers:
   left = 2^30 (1073741824)
   right = 2^30 (1073741824)
   
   Wrong way:
   mid = (left + right) / 2
       = (2^30 + 2^30) / 2
       = 2^31 / 2
       = 2^30
   But left + right = 2^31 overflows!
   (int max value is 2^31 - 1 = 2147483647)
   
   Correct way:
   mid = left + (right - left) / 2
       = 2^30 + (2^30 - 2^30) / 2
       = 2^30 + 0 / 2
       = 2^30
   No overflow because:
   - right - left is always < right
   - division by 2 makes it even smaller
   - adding left at the end is safe
   ```

2. **Loop Termination Condition**
   - Wrong: `while (left < right)`
   - Correct: `while (left <= right)`

   **Why?**
   - When `left == right`, the position might contain the target value
   - Using `<` will skip checking this position
   - This may cause the algorithm to return incorrect results or miss the target value
   - Therefore, in binary search, we should use `while (left <= right)` to ensure we check all possible element positions

   **Problem Summary:**
   - Using `while (left < right)` will cause early termination
   - When the search range narrows down to a single element (`left == right`), the loop exits prematurely
   - This leads to missing the potential target value at that position
   - The correct approach is to use `while (left <= right)` to properly handle the case when `left == right`
   - This ensures the algorithm checks all possible positions before terminating



