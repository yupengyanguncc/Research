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

where $$\mathbf{x}\in\mathcal{X}\sub\mathbb{R}^{d}$$, $$\mathbf{u}\in\mathcal{U}\sub\mathbb{R}^{q}$$ denotes the control input. 
$$F:\mathbb{R}^{d} \mapsto \mathbb{R}^{d}$$ and $$G\!:\!\mathbb{R}^{d}\!\mapsto\!\mathbb{R}^{d\times q}$$ are locally Lipschitz continuous.

(Safety) Considering the safety radius $$R_\mathrm{s}\in\mathbb{R}$$, if we want to ensure that the robots $$i$$ and $$j$$ are not collide with each other, we can define such set as:

$$
h^\mathrm{s}_{i,j}(\mathbf{x}) = ||\mathbf{x}_i -\mathbf{x}_j||^2 -R_\mathrm{s}^2, \forall i>j\\
\mathcal{H}^\mathrm{s}_{i,j} = \{\mathbf{x} \in \mathbb{R}^{dN} | h^\mathrm{s}_{i,j}(\mathbf{x}) \geq 0 \}
$$

Then, we have the following theorem:

```angular2html
Theorem 1 (Control Barrier Function):Given a deterministic dynamical system affine in control (i.e., $\dot{\mathbf{x}}=F(\mathbf{x})+G(\mathbf{x})\mathbf{u}$) and a desired set $\mathcal{H}$ as the 0-super level set of a continuously differentiable function $h: \mathcal{X} \mapsto \mathbb{R}$, the function $h$ is called a control barrier function, if there exists an extended class-$\mathcal{K}$ function\footnote{In the rest of this paper, we select the particular choice of $\kappa(h(\mathbf{x}))=\gamma h(\mathbf{x})$ with $\gamma$ as a user-defined parameter \cite{ames2019control}.}  $\kappa(\cdot)$ such that 
$\sup_{\mathbf{u}\in\mathcal{U}}\{\dot{h}(\mathbf{x}, \mathbf{u})\}\geq -\kappa(h(\mathbf{x}))$ for all $\mathbf{x}\in\mathcal{X}$. 
```