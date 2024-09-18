---
title: Control Barrier Function
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
$$f:\mathbb{R}^{d} \mapsto \mathbb{R}^{d}$$ and $$g\!:\!\mathbb{R}^{d}\!\mapsto\!\mathbb{R}^{d\times q}$$ are locally Lipschitz continuous.


## Theorem 
(Safety) Considering the safety radius $$R_\mathrm{s}\in\mathbb{R}$$, if we want to ensure that the robots $$i$$ and $$j$$ are not collide with each other, we can define such set as:

$$
h^\mathrm{s}_{i,j}(\mathbf{x}) = ||\mathbf{x}_i -\mathbf{x}_j||^2 -R_\mathrm{s}^2, \forall i>j\\
\mathcal{H}^\mathrm{s}_{i,j} = \{\mathbf{x} \in \mathbb{R}^{dN} | h^\mathrm{s}_{i,j}(\mathbf{x}) \geq 0 \}
$$


Then, we have the following theorem:

**Theorem 1 (Control Barrier Function):** Given a deterministic dynamical system affine in control (i.e., $$\dot{\mathbf{x}}=F(\mathbf{x})+G(\mathbf{x})\mathbf{u}$$) and a desired set $$\mathcal{H}$$ as the 0-super level set of 
a continuously differentiable function $$h: \mathcal{X} \mapsto \mathbb{R}$$, 
the function $h$ is called a control barrier function, if there exists an extended class-$$\mathcal{K}$$ function $$\kappa(\cdot)$$ such that 


$$
\sup_{\mathbf{u}\in\mathcal{U}}\{\dot{h}(\mathbf{x}, \mathbf{u})\}\geq -\kappa(h(\mathbf{x}))
$$

for all $$\mathbf{x}\in\mathcal{X}$$
. 


## Question 1 why this cosntraint can enfore the forward invariance of the set $$\mathcal{H}$$?

Let's make it formal! We can define the problem as:

**Problem 1:** Given the initial time step $$t = 0$$ , $$h(\mathbf{x}(0))\geq0$$ and $$\dot{h}(\mathbf{x})\geq-\alpha(h(\mathbf{x}))$$ holds 
for all $$t\geq0$$, then $$h(\mathbf{x}(t))\geq0$$ for all $$t\geq0$$.

First, let's define an auxiliary function as:

$$
\frac{d}{dt}y(t) = -\alpha(y(t)), \quad y(0) = h(x(0))
$$

An example for such function is that $$y(t) = e^{-\alpha t}y(0)$$. This equation describes an independent system where the rate of the change of $$y(t)$$ is proportional to the value of $$y(t)$$ itself. 

**Definition 1 (Class-$$\mathcal{K}$$ funciton):**
The Class $$\mathcal{K}$$ function is a function $$\alpha: \mathbb{R}_{\geq 0} \mapsto \mathbb{R}_{\geq 0}$$ that is continuous, strictly increasing, and $$\alpha(0) = 0$$. 

Since $$\alpha$$ is a class-$$\mathcal{K}$$ function, we can get 