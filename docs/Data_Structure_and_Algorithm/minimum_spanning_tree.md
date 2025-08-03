---
title: Minimum Spanning Tree
parent: Data Structure and Algorithm
author: Yupeng
date: 2025-08-13
layout: default
nav_order: 6.5
math: katex
emoji: jemoji
---

# Minimum Spanning Tree (MST)

## Overview
This document provides a comprehensive guide to Minimum Spanning Trees, including detailed step-by-step visualizations of Prim's and Kruskal's algorithms. We'll also explore the concept of greedy algorithms and their applications in graph theory.

## What is a Minimum Spanning Tree?

A **Minimum Spanning Tree (MST)** of a connected, undirected, weighted graph is a subset of the graph's edges that:
- Connects all vertices together
- Contains no cycles
- Has the minimum possible total edge weight

### Key Properties
- **Connected**: All vertices are reachable from each other
- **Acyclic**: No cycles in the tree
- **Minimum Weight**: Sum of edge weights is minimized
- **Unique**: If all edge weights are distinct, the MST is unique

## Visual Example

Consider the following weighted undirected graph:

```
        A
       /|\
      2 | 3
     /  |  \
    B---1---C
    |       |
    4       5
    |       |
    D-------E
       6
```

**Weight Matrix:**
```
   A B C D E
A  0 2 3 ∞ ∞
B  2 0 1 4 ∞
C  3 1 0 ∞ 5
D  ∞ 4 ∞ 0 6
E  ∞ ∞ 5 6 0
```

The MST for this graph would be:
```
        A
       /
      2
     /
    B---1---C
    |       |
    4       5
    |       |
    D       E
```

**Total Weight:** 2 + 1 + 4 + 5 = 12

## Greedy Algorithm Concept

### What is a Greedy Algorithm?
A **greedy algorithm** is an algorithmic paradigm that follows the problem-solving heuristic of making the locally optimal choice at each stage with the hope of finding a global optimum.

### Key Characteristics
- **Local Optimization**: Makes the best choice at each step
- **No Backtracking**: Once a choice is made, it's never reconsidered
- **Heuristic Nature**: May not always find the global optimum
- **Efficiency**: Often simple and fast to implement

### Why Greedy Works for MST?
The greedy approach works for MST because of the **cut property**:
- For any cut in the graph, the minimum weight edge crossing the cut must be in the MST
- This allows us to safely add the minimum weight edge at each step

## Prim's Algorithm

### Algorithm Overview
Prim's algorithm grows the MST one vertex at a time, always adding the minimum weight edge that connects a vertex in the MST to a vertex outside it.

### Step-by-Step Visualization

**Initial Graph:**
```
        A(0)
       /|\
      2 | 3
     /  |  \
    B---1---C
    |       |
    4       5
    |       |
    D-------E
       6
```

**Step 1: Start with vertex A**
- Add A to MST
- Update distances: B(2), C(3), D(∞), E(∞)
- Choose minimum: B(2)

```
    A(0)---2---B
```

**Step 2: Add vertex B**
- Add B to MST
- Update distances: C(1), D(4), E(∞)
- Choose minimum: C(1)

```
    A(0)---2---B---1---C
```

**Step 3: Add vertex C**
- Add C to MST
- Update distances: D(∞), E(5)
- Choose minimum: D(4) (from B)

```
    A(0)---2---B---1---C
              |
              4
              |
              D
```

**Step 4: Add vertex D**
- Add D to MST
- Update distances: E(6)
- Choose minimum: E(5) (from C)

```
    A(0)---2---B---1---C---5---E
              |
              4
              |
              D
```

**Final MST:**
```
    A---2---B---1---C---5---E
              |
              4
              |
              D
```

**Total Weight:** 2 + 1 + 4 + 5 = 12

### Java Implementation (Prim's Algorithm)
```java
import java.util.*;

class PrimMST {
    private int V;
    private int[][] graph;
    
    public PrimMST(int V) {
        this.V = V;
        graph = new int[V][V];
    }
    
    public void addEdge(int u, int v, int weight) {
        graph[u][v] = weight;
        graph[v][u] = weight;
    }
    
    public void primMST() {
        // Array to store constructed MST
        int[] parent = new int[V];
        
        // Key values used to pick minimum weight edge
        int[] key = new int[V];
        
        // To represent set of vertices included in MST
        boolean[] mstSet = new boolean[V];
        
        // Initialize all keys as INFINITE
        Arrays.fill(key, Integer.MAX_VALUE);
        
        // Always include first vertex in MST
        key[0] = 0;
        parent[0] = -1;
        
        for (int count = 0; count < V - 1; count++) {
            // Pick the minimum key vertex from the set of vertices
            // not yet included in MST
            int u = minKey(key, mstSet);
            
            // Add the picked vertex to the MST Set
            mstSet[u] = true;
            
            // Update key value and parent index of the adjacent
            // vertices of the picked vertex
            for (int v = 0; v < V; v++) {
                if (graph[u][v] != 0 && !mstSet[v] && 
                    graph[u][v] < key[v]) {
                    parent[v] = u;
                    key[v] = graph[u][v];
                }
            }
        }
        
        printMST(parent);
    }
    
    private int minKey(int[] key, boolean[] mstSet) {
        int min = Integer.MAX_VALUE, minIndex = -1;
        
        for (int v = 0; v < V; v++) {
            if (!mstSet[v] && key[v] < min) {
                min = key[v];
                minIndex = v;
            }
        }
        
        return minIndex;
    }
    
    private void printMST(int[] parent) {
        System.out.println("Edge \tWeight");
        for (int i = 1; i < V; i++) {
            System.out.println(parent[i] + " - " + i + "\t" + 
                             graph[i][parent[i]]);
        }
    }
}
```

## Kruskal's Algorithm

### Algorithm Overview
Kruskal's algorithm sorts all edges by weight and adds them to the MST in ascending order, avoiding cycles using a disjoint-set data structure.

### Step-by-Step Visualization

**Initial Graph (same as before):**
```
        A
       /|\
      2 | 3
     /  |  \
    B---1---C
    |       |
    4       5
    |       |
    D-------E
       6
```

**Step 1: Sort edges by weight**
- B-C: 1
- A-B: 2
- A-C: 3
- B-D: 4
- C-E: 5
- D-E: 6

**Step 2: Add edge B-C (weight 1)**
- No cycle formed
- Add to MST

```
    B---1---C
```

**Step 3: Add edge A-B (weight 2)**
- No cycle formed
- Add to MST

```
    A---2---B---1---C
```

**Step 4: Add edge A-C (weight 3)**
- Would form cycle A-B-C-A
- Skip this edge

**Step 5: Add edge B-D (weight 4)**
- No cycle formed
- Add to MST

```
    A---2---B---1---C
              |
              4
              |
              D
```

**Step 6: Add edge C-E (weight 5)**
- No cycle formed
- Add to MST

```
    A---2---B---1---C---5---E
              |
              4
              |
              D
```

**Step 7: Add edge D-E (weight 6)**
- Would form cycle D-B-C-E-D
- Skip this edge

**Final MST:**
```
    A---2---B---1---C---5---E
              |
              4
              |
              D
```

**Total Weight:** 1 + 2 + 4 + 5 = 12

### Java Implementation (Kruskal's Algorithm)
```java
import java.util.*;

class Edge implements Comparable<Edge> {
    int src, dest, weight;
    
    public Edge(int src, int dest, int weight) {
        this.src = src;
        this.dest = dest;
        this.weight = weight;
    }
    
    @Override
    public int compareTo(Edge other) {
        return this.weight - other.weight;
    }
}

class KruskalMST {
    private int V, E;
    private Edge[] edges;
    
    public KruskalMST(int V, int E) {
        this.V = V;
        this.E = E;
        edges = new Edge[E];
    }
    
    public void addEdge(int index, int src, int dest, int weight) {
        edges[index] = new Edge(src, dest, weight);
    }
    
    // Find set of an element i (uses path compression)
    private int find(int[] parent, int i) {
        if (parent[i] != i) {
            parent[i] = find(parent, parent[i]);
        }
        return parent[i];
    }
    
    // Union of two sets (uses union by rank)
    private void union(int[] parent, int[] rank, int x, int y) {
        int xRoot = find(parent, x);
        int yRoot = find(parent, y);
        
        if (rank[xRoot] < rank[yRoot]) {
            parent[xRoot] = yRoot;
        } else if (rank[xRoot] > rank[yRoot]) {
            parent[yRoot] = xRoot;
        } else {
            parent[yRoot] = xRoot;
            rank[xRoot]++;
        }
    }
    
    public void kruskalMST() {
        Edge[] result = new Edge[V - 1];
        int e = 0; // Index for result[]
        int i = 0; // Index for sorted edges
        
        // Sort edges by weight
        Arrays.sort(edges);
        
        // Allocate memory for creating V subsets
        int[] parent = new int[V];
        int[] rank = new int[V];
        
        // Create V subsets with single elements
        for (int v = 0; v < V; v++) {
            parent[v] = v;
            rank[v] = 0;
        }
        
        while (e < V - 1 && i < E) {
            Edge nextEdge = edges[i++];
            
            int x = find(parent, nextEdge.src);
            int y = find(parent, nextEdge.dest);
            
            // If including this edge doesn't cause cycle
            if (x != y) {
                result[e++] = nextEdge;
                union(parent, rank, x, y);
            }
        }
        
        printMST(result);
    }
    
    private void printMST(Edge[] result) {
        System.out.println("Edge \tWeight");
        for (int i = 0; i < V - 1; i++) {
            System.out.println(result[i].src + " - " + result[i].dest + 
                             "\t" + result[i].weight);
        }
    }
}
```

## Algorithm Comparison

| Aspect              | Prim's Algorithm        | Kruskal's Algorithm     |
|---------------------|------------------------|-------------------------|
| **Approach**        | Vertex-based            | Edge-based              |
| **Data Structure**  | Priority Queue          | Disjoint Set            |
| **Time Complexity** | O(E log V)              | O(E log E)              |
| **Space Complexity**| O(V)                    | O(E)                    |
| **Best For**        | Dense graphs            | Sparse graphs           |
| **Implementation**  | More complex            | Simpler                 |

## Mathematical Foundation

### Cut Property
For any cut in the graph, the minimum weight edge crossing the cut must be in the MST.

### Cycle Property
For any cycle in the graph, the maximum weight edge in the cycle is not in the MST.

### Proof of Correctness
Both algorithms work because they respect the cut property:
- **Prim's**: Always adds the minimum weight edge crossing the cut between MST and non-MST vertices
- **Kruskal's**: Always adds the minimum weight edge that doesn't create a cycle

## Applications

### Real-World Applications
1. **Network Design**: Connecting cities with minimum cable cost
2. **Clustering**: Grouping similar data points
3. **Image Segmentation**: Connecting pixels with similar properties
4. **Circuit Design**: Minimizing wire length
5. **Water Supply**: Connecting water sources to consumers

### LeetCode Problems
- **1584. Min Cost to Connect All Points**: Direct MST application
- **1135. Connecting Cities With Minimum Cost**: MST with custom weights
- **1489. Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree**: Advanced MST concepts

## Example: LeetCode 1584

### Problem
Given an array of points where `points[i] = [xi, yi]` represents a point on the X-Y plane, return the minimum cost to make all points connected.

### Solution using Prim's Algorithm
```java
class Solution {
    public int minCostConnectPoints(int[][] points) {
        int n = points.length;
        boolean[] visited = new boolean[n];
        int[] minDist = new int[n];
        Arrays.fill(minDist, Integer.MAX_VALUE);
        
        minDist[0] = 0;
        int totalCost = 0;
        
        for (int i = 0; i < n; i++) {
            // Find unvisited vertex with minimum distance
            int u = -1;
            int min = Integer.MAX_VALUE;
            for (int j = 0; j < n; j++) {
                if (!visited[j] && minDist[j] < min) {
                    min = minDist[j];
                    u = j;
                }
            }
            
            visited[u] = true;
            totalCost += min;
            
            // Update distances to unvisited neighbors
            for (int v = 0; v < n; v++) {
                if (!visited[v]) {
                    int dist = Math.abs(points[u][0] - points[v][0]) + 
                              Math.abs(points[u][1] - points[v][1]);
                    if (dist < minDist[v]) {
                        minDist[v] = dist;
                    }
                }
            }
        }
        
        return totalCost;
    }
}
```

## Summary Table

| Algorithm    | Time Complexity | Space Complexity | Approach    | Best For      |
|--------------|-----------------|------------------|-------------|---------------|
| Prim's       | O(E log V)      | O(V)             | Vertex-based| Dense graphs  |
| Kruskal's    | O(E log E)      | O(E)             | Edge-based  | Sparse graphs |
| Borůvka's    | O(E log V)      | O(V)             | Component   | Parallel      |

## Key Takeaways

1. **Greedy Nature**: Both algorithms make locally optimal choices that lead to globally optimal solutions
2. **Cut Property**: The mathematical foundation that makes greedy approach work
3. **Implementation Choice**: 
   - Use Prim's for dense graphs (E ≈ V²)
   - Use Kruskal's for sparse graphs (E << V²)
4. **Disjoint Set**: Essential data structure for Kruskal's algorithm
5. **Priority Queue**: Essential data structure for Prim's algorithm
6. **Applications**: Network design, clustering, and optimization problems

## Advanced Topics

### Multiple MSTs
When edge weights are not unique, there may be multiple MSTs with the same total weight.

### Second Best MST
Finding the second minimum spanning tree using edge replacement.

### Dynamic MST
Maintaining MST under edge insertions and deletions.

### Parallel MST Algorithms
Borůvka's algorithm is naturally parallelizable and used in distributed systems. 