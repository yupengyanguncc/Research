---
title: DFS Visualization Code
parent: Code
author: Yupeng
date: 2024-09-19
layout: default
nav_order: 2.2
math: katex
emoji: jemoji
---

This is the code using [manim](https://www.manim.community/plugin/manim-onlinetex/), which is one of my favorite algorithm visualization library :grin:. I am still wokring on familar with it.

```julia
%%manim -qm DFSVisualization
from manim import *
import networkx as nx

class DFSVisualization(Scene):
    """DFS on a 5‑layer pyramid with a live cumulative path panel."""

    def construct(self):
        # ---------------------------------------------------------------
        # 1. Build perfect binary tree (5 layers → 31 nodes)
        # ---------------------------------------------------------------
        num_layers = 3
        total_nodes = 2 ** num_layers - 1
        edges = [(i, 2 * i + 1) for i in range(total_nodes) if 2 * i + 1 < total_nodes]
        edges += [(i, 2 * i + 2) for i in range(total_nodes) if 2 * i + 2 < total_nodes]
        G = nx.Graph(edges)

        # ---------------------------------------------------------------
        # 2. Layout (root lifted so bottom row is visible)
        # ---------------------------------------------------------------
        vertical_gap = 1.5
        y_offset = vertical_gap
        pos = {}
        for layer in range(num_layers):
            nodes_in_layer = 2 ** layer
            y = y_offset - layer * vertical_gap
            x_offset = -(nodes_in_layer - 1) / 2
            for k in range(nodes_in_layer):
                node_id = 2 ** layer - 1 + k
                pos[node_id] = [x_offset + k, y]

        # ---------------------------------------------------------------
        # 3. Manim mobjects
        # ---------------------------------------------------------------
        dots = {v: Dot(radius=0.13).move_to([pos[v][0], pos[v][1], 0])
                for v in G.nodes}
        labels = {v: Text(str(v), font_size=24).next_to(dots[v], DOWN, buff=0.10)
                  for v in G.nodes}
        edge_lines = {(u, v): Line(dots[u].get_center(), dots[v].get_center())
                      for u, v in G.edges}

        # ---------------------------------------------------------------
        # 4. Right‑hand path panel – one cumulative path per line
        # ---------------------------------------------------------------
        panel_title = Text("Path:", font_size=32).to_corner(UR).shift(LEFT * 0.6)
        self.add(panel_title)
        path_mobs = []
        def add_path_line(path_list):
            txt = Text(" → ".join(map(str, path_list)), font_size=28, t2c={"→": GREY_A})
            if path_mobs:
                txt.next_to(path_mobs[-1], DOWN, aligned_edge=LEFT, buff=0.15)
            else:
                txt.next_to(panel_title, DOWN, aligned_edge=LEFT, buff=0.25)
            path_mobs.append(txt)
            self.play(FadeIn(txt), run_time=0.3)

        # ---------------------------------------------------------------
        # 5. Reveal graph layer‑by‑layer (edges, then nodes)
        # ---------------------------------------------------------------
        for layer in range(num_layers):
            layer_nodes = [2 ** layer - 1 + k for k in range(2 ** layer)]
            edge_anims = []
            for v in layer_nodes:
                if v == 0:
                    continue
                p = (v - 1) // 2
                edge_anims.append(Create(edge_lines[(p, v)]))
            node_anims = [FadeIn(dots[v]) for v in layer_nodes] + [Write(labels[v]) for v in layer_nodes]
            self.play(*(edge_anims + node_anims), lag_ratio=0.06, run_time=2)
            self.wait(0.15)

        # ---------------------------------------------------------------
        # 6. DFS traversal (explicit stack) with live path updates
        # ---------------------------------------------------------------
        highlight_col = ORANGE
        visited = set()
        stack = [(0, None)]  # (node, parent)
        parent_map = {}

        while stack:
            u, parent = stack.pop()  # LIFO for DFS
            if u in visited:
                continue
            visited.add(u)
            # Highlight vertex and edge that led here
            if parent is not None:
                edge = edge_lines.get((u, parent)) or edge_lines.get((parent, u))
                self.play(Create(edge.copy().set_color(highlight_col).set_stroke(width=6)), run_time=0.35)
            self.play(dots[u].animate.set_color(highlight_col), run_time=0.45)

            # Store parent for path reconstruction
            parent_map[u] = parent
            # Build and display current cumulative path from root to u
            cu_path = self._reconstruct_path(u, parent_map)
            add_path_line(cu_path)

            # Push children (reverse order so left child explored first)
            for v in sorted(G.neighbors(u), reverse=True):
                if v not in visited:
                    stack.append((v, u))
            self.wait(2)

        

    # -----------------------------------------------------------
    # Helper to backtrack parents to root (0) and return list
    # -----------------------------------------------------------
    def _reconstruct_path(self, node, parent_map):
        current = node
        path = []
        while current is not None:
            path.append(current)
            current = parent_map.get(current)
        return path[::-1]
```