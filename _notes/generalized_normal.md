---
title: Generalized Normal Distribution
author: Alexander Laut
date: November 26, 2021
layout: post
permalink: distributions
---

A normal distribution is commonly defined by

$$f(x) = \frac{1}{\sqrt{2\pi\sigma^2}}\exp\left[-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2\right].$$

Approximating that

$$\exp x = \lim_{n\to\infty}\left(1+\frac{x}{n}\right)^n,$$

one can define a uniform $(k=0)$, parabolic $(k=1)$, and gaussian $(k=\infty)$ distribution profile.

The generalized distribution is given by 

$$f(x; m) = \frac{2\Gamma(3/2+m)}{L\sqrt{\pi}\Gamma(1+m)}\left[1-4\left(\frac{x-\mu}{L}\right)^2\right]^m,$$

where

$$\sigma^2 = \frac{L^2}{4}\frac{1}{3+2m}.$$

![Binomial Functions](../assets/binomial.0.svg)

The derivative is therefore given by

$$f'(x;m) = -\frac{16m( x-\mu) \Gamma(m+3/2)}{\sqrt{\pi}L^3\Gamma(m+1)} \left[1-4\left(\frac{x-\mu}{L}\right)^2\right]^{m-1}.$$

![Binomial Der](../assets/binomial.1.svg)
