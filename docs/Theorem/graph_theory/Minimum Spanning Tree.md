---
title: Minimum Spanning Tree
parent: Theorem
author: Yupeng
date: 2024-09-17
layout: default
nav_order: 2.4
math: katex
emoji: jemoji
---
Working on it! :construction:
{: .label .label-blue }

# Minimum Spanning Tree

We are interested in finding a minimum spanning tree of a connected, undirected graph. A minimum spanning tree is a subgraph of the original graph that is a tree and connects all the vertices together with the minimum possible total edge weight.
Given a connected, undirected graph $$\mathcal{G} = (\mathcal{V},\mathcal{E}) $$, where $$ \mathcal{V} $$ is the set of vertices and $$ \mathcal{E}$$ denotes the set of edges.
Each edge $$ e \in \mathcal{E} $$ has a weight $$ w(e) $$ associated with it. 

## Spanning Tree
A spanning tree contains a subset of edges $$\mathcal{E}'\subseteq\mathcal{E}$$ with the following properties:
1. The subset contains exactly $$n-1$$ edges, where $$n$$ is the number of vertices in the graph.
2. The subset $$\mathcal{E}'$$ connects all the vertices in the graph.

We seek to find the particular **spanning tree** that has the minimum total edge weight. This tree is called the minimum spanning tree. With this,
we can formally define the problem as:

\begin{equation}
 MST = \arg\min_{\mathcal{E}'\subseteq \mathcal{E}} \sum w(e)
\end{equation}

There are two most popular algorithms to construct a minimum spanning tree:

1. Kruskal's algorithm
2. Prim's algorithm

## Kruskal's algorithm
