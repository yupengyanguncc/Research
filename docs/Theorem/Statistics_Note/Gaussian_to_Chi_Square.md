---
title: Two Gaussian Multiplication
parent: Theorem
author: Yupeng
date: 2024-09-17
layout: default
nav_order: 2.5
math: katex
emoji: jemoji
---


#  Two Gaussian Multiplication

Working on it! :construction:
{: .label .label-blue }

## Gaussian Distribution Preliminaries

The Gaussian distribution material can be easily found in many textbooks. Here we directly
define the random variable $$x$$ and $$y$$ as:

$$
x \sim \mathcal{N}(\mu_x, \Sigma_x)  \tag{1} 
$$

$$
y \sim \mathcal{N}(\mu_y, \Sigma_y)  \tag{2}
$$

where $$\mu_x$$ and $$\mu_y$$ are the mean of the Gaussian distribution, 
and $$\Sigma_x$$ and $$\Sigma_y$$ are the covariance matrix of the
Gaussian distribution.


Here we are interested in the distribution of the random variable $$z$$, which is the multiplication of $$x$$ and $$y$$:

$$
z =xy   \tag{3}
$$

## Question 1: What is the distribution of the random variable $$z$$?

Let's play with the example to visualize the distribution of the random variable $$z$$.

<div align="center">
<img src="../../../assets/image/gxg.png" alt="Example One." width="700">
</div>

It looks like a Gaussian distribution, right? :thinking:

Let's dig into the details! :mag_right:

First, we can use an relative easy way as described in this [link](https://math.stackexchange.com/questions/101062/is-the-product-of-two-gaussian-random-variables-also-a-gaussian):

The basic idea is that:

$$
(x+y)^2 = x^2 + 2xy + y^2
$$

$$
(x-y)^2 = x^2 - 2xy + y^2
$$

So 

$$
xy = \frac{1}{4}[(x+y)^2 - (x-y)^2]
$$

$$  
xy \sim \frac{\mathrm{Var}(x+y)}{4} \mathcal{Q} +
 \frac{\mathrm{Var}(x-y)}{4} \mathcal{R} 
$$

where $$\mathcal{Q}$$ and $$\mathcal{R}$$ are central chi-square distribution.
So the distribution of $$z$$ is a **linear** combination of two central chi-square distribution.

To make it more process, we have
