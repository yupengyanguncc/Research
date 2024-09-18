---
title: control barrier function
parent: Theorem
date: 2024-09-17
layout: default
nav_order: 2
math: katex
---

# Control Barrier Function

Working on this 
{: .label .label-green }

Consider a contol-affine dynamical system defined as:
$$
\dot{\mathbf{x}} = f(\mathbf{x}) + g(\mathbf{x})u
$$

where $$\mathbf{x}\in\mathcal{X}\in\mathbb{R}^{d}$$ $$\mathbf{u}_\!\in\!\mathcal{U}\!\subset\!\mathbb{R}^{q}$$ denotes the control input. $$F:\mathbb{R}^{d} \mapsto \mathbb{R}^{d}$$ and $$G\!:\!\mathbb{R}^{d}\!\mapsto\!\mathbb{R}^{d\times q}$$ are locally Lipschitz continuous.

$$
h(\mathbf{x}) = \frac{1}{2} \mathbf{x}^T P \mathbf{x}
$$