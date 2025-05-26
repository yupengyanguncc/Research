---
title: BFS Visualization Code
parent: Code
author: Yupeng
date: 2024-09-19
layout: default
nav_order: 2.5
math: katex
emoji: jemoji
---


```julia
%%manim -qm BFSVisualization
from manim import *
import networkx as nx
from collections import deque

class BFSVisualization(Scene):
    """BFS Visualization"""

    # Parameter
    LIST_FONT   = 26
    VALUE_FONT  = 24
    LIST_GAP    = 0.20
    PANEL_SHIFT = RIGHT * 0.7      # contorl the view panel
    HIGHLIGHT   = ORANGE           # Color

    def construct(self):
        # -----------------------------------------------------------
        # Graph
        # -----------------------------------------------------------
        layers        = 3
        total_nodes   = 2 ** layers - 1
        edges_idx     = [(i, 2*i+1) for i in range(total_nodes) if 2*i+1 < total_nodes]
        edges_idx    += [(i, 2*i+2) for i in range(total_nodes) if 2*i+2 < total_nodes]
        G = nx.Graph(edges_idx)

        # -----------------------------------------------------------
        # Position
        # -----------------------------------------------------------
        y0, vgap = 1.5, 1.5
        pos = {}
        for layer in range(layers):
            cnt = 2 ** layer
            y   = y0 - layer * vgap
            x0  = -(cnt - 1) / 2
            for k in range(cnt):
                nid = 2 ** layer - 1 + k
                pos[nid] = [x0 + k, y]

        # -----------------------------------------------------------
        # 3. Edge, node, label
        # -----------------------------------------------------------
        dots   = {v: Dot(radius=0.13).move_to([*pos[v], 0]) for v in G.nodes}
        labels = {v: Text(str(v), font_size=24).next_to(dots[v], DOWN, buff=0.10)
                  for v in G.nodes}
        edge_mob = {(u, v): Line(dots[u].get_center(), dots[v].get_center())
                    for u, v in G.edges}

        # -----------------------------------------------------------
        # Path
        # -----------------------------------------------------------
        path_title = Text("Path:", font_size=32).to_corner(UR).shift(LEFT*0.6)
        self.add(path_title)
        path_lines = []

        def add_path_line(path):
            txt = Text(" → ".join(map(str, path)), font_size=28,
                       t2c={"→": GREY_A})
            anchor = path_lines[-1] if path_lines else path_title
            txt.next_to(anchor, DOWN, aligned_edge=LEFT,
                        buff=0.25 if not path_lines else 0.15)
            path_lines.append(txt)
            self.play(FadeIn(txt), run_time=0.3)

        # -----------------------------------------------------------
        # List
        # -----------------------------------------------------------
        state_title = Text("State:", font_size=32).to_corner(UL).shift(self.PANEL_SHIFT)
        self.add(state_title)

        queue_label = Text("Queue:", font_size=self.LIST_FONT).next_to(
            state_title, DOWN, aligned_edge=LEFT, buff=self.LIST_GAP)
        u_label     = Text("u:",     font_size=self.LIST_FONT).next_to(
            queue_label, DOWN, aligned_edge=LEFT, buff=self.LIST_GAP)
        v_label     = Text("v:",     font_size=self.LIST_FONT).next_to(
            u_label, DOWN, aligned_edge=LEFT, buff=self.LIST_GAP)
        self.add(queue_label, u_label, v_label)

        queue_mob = u_mob = v_mob = None

        def refresh_state(queue, u, v, first=False):
            """refresh"""
            nonlocal queue_mob, u_mob, v_mob
            q_txt = Text(str(list(queue)), font_size=self.VALUE_FONT)
            u_txt = Text(str(u) if u is not None else " ", font_size=self.VALUE_FONT)
            v_txt = Text(str(v) if v is not None else " ", font_size=self.VALUE_FONT)

            q_txt.next_to(queue_label, RIGHT, buff=0.25)
            u_txt.next_to(u_label,     RIGHT, buff=0.25)
            v_txt.next_to(v_label,     RIGHT, buff=0.25)

            if first:
                self.add(q_txt, u_txt, v_txt)
            else:
                self.play(
                    Transform(queue_mob, q_txt,
                              replace_mobject_with_target_in_scene=True),
                    Transform(u_mob,     u_txt,
                              replace_mobject_with_target_in_scene=True),
                    Transform(v_mob,     v_txt,
                              replace_mobject_with_target_in_scene=True),
                    run_time=0.18
                )
            queue_mob, u_mob, v_mob = q_txt, u_txt, v_txt

        # -----------------------------------------------------------
        # 5. graph visualization
        # -----------------------------------------------------------
        for layer in range(layers):
            nodes = [2 ** layer - 1 + k for k in range(2 ** layer)]
            edge_anims = []
            for v in nodes:
                if v == 0:
                    continue
                p = (v - 1) // 2
                edge_anims.append(Create(edge_mob[(p, v)]))
            node_anims = [FadeIn(dots[v]) for v in nodes] + [Write(labels[v]) for v in nodes]
            self.play(*(edge_anims + node_anims), lag_ratio=0.06, run_time=2)

        # -----------------------------------------------------------
        # 6. BFS main
        # -----------------------------------------------------------
        visited, parent = set(), {}
        queue = deque([0])
        refresh_state(queue, u=None, v=None, first=True)
        
        while queue:
        
            u = queue.popleft()
        
   
            if u in visited:
                refresh_state(queue, u=None, v=None)        
                continue
        
    
            visited.add(u)
            refresh_state(queue, u=u, v=None)              
            add_path_line(self._path_to_root(u, parent))    
        
          
            self.play(dots[u].animate.set_color(self.HIGHLIGHT), run_time=0.4)
        
    
            for v in sorted(G.neighbors(u)):
                refresh_state(queue, u=u, v=v)            
        
                if v not in visited:
                  
                    queue.append(v)
                    parent[v] = u
                    edge = edge_mob.get((u, v)) or edge_mob.get((v, u))
                    self.play(Create(edge.copy().set_color(self.HIGHLIGHT)
                                          .set_stroke(width=6)), run_time=0.25)
        
                    refresh_state(queue, u=u, v=v)        
                    self.wait(2)  

    def _path_to_root(self, node, parent):
        p, path = node, []
        while p is not None:
            path.append(p)
            p = parent.get(p)
        return path[::-1]

```