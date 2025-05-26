---
title: Breadth First Search (BFS)
parent: Basic Algorithm
author: Yupeng
date: 2025-05-25
layout: default
nav_order: 2
math: katex
emoji: jemoji
---

# Breadth First Search (BFS)

## What is BFS

Breadth‑First Search (BFS) is a graph‑traversal algorithm that explores a graph level by level. Starting from a source vertex, it first visits all immediate neighbours (distance 1), then all vertices at distance 2, and so on until every reachable vertex has been discovered.

### 1.1 Algorithm (pseudocode)

```julia

BFS(G, s):
    create an empty queue Q
    mark s as visited and enqueue s  ➜  Q ← [s]
    while Q is not empty:
        u ← dequeue(Q)
        for each neighbour v of u in G:
            if v is unvisited:
                mark v as visited
                enqueue v  ➜  Q ← Q ∪ {v}
```

**Time complexity**: $$\mathcal{O}(|\mathcal{V}|+|\mathcal{E}|)$$
**Space complexity**: $$\mathcal{O}(|\mathcal{V}|)$$ (It uses a queue to keep track of the vertices that need to be visited.)
**Usage** - shortest path in unweighted graphs, connectivity checks, level ordering, bipartite testing, etc.

## Visualization
The animation below is generated with Manim. It shows BFS expanding a queue and colouring vertices/edges in the order they are discovered.

<div align="center">
<img src="../../assets/image/bfs.gif" alt="BFS Example" width="700" title="Example Video.">
</div>

Plus 🛠️:

You can also add the list veiw of each round for example the neighbour and not visting list vs. visiting list.