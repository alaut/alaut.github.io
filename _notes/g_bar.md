---
layout: post
date: October 28, 2021
title: $\bar{g}$
author: Alexander Laut
---

## The Effective Geometry Factor

The induced wakefield voltage for a particle traveling within a longitudinal bunch $\lambda(\tau)$ influenced by a longitudinal impedance $Z/n$ is given by

$$V_{W} = -\frac{1}{\omega}\frac{Z}{n}\frac{d\lambda}{d\tau},$$

where the space-charge impedance is defined by

$$\frac{Z}{n} = -j\frac{Z_0}{\beta \gamma^2}g,$$

and geometry factor $g$ for a particle within a long round bunch of radius $a$ within a conductive beam pipe of radius $b$ is given by:

$$g = \frac{1}{2} + \ln\frac{b}{a}-\frac{1}{2}\frac{r^2}{a^2}$$

Typically in longitudinal trackers, the maximum geometry factor is applied homogeneously to all particle's tracked in a bunch. Realistically the incurred space-charge for an individual particle will vary based on it's transverse emittance $\epsilon$ and momentum-spread $\delta$.

## Analysis

Integrated around the ring, the effective geometry factor $\bar{g}$ can be computed by

$$\bar{g} = \frac{1}{2} + \ln\frac{b}{\bar{a}} -\frac{\overline{r^2}}{\bar{a}^2}$$

where:

$$\overline{r^2} = \frac{\beta}{2}(\epsilon_x+\epsilon_y)+D^2\delta^2$$

<details>

---

A particle's transverse position around a ring defined by optics $\beta(s) \approx \beta$ and $D(s) \approx D$ is given by

$$\begin{aligned}
x &= \sqrt{\beta \epsilon_x}\cos\phi_x+D\delta \cr
y &= \sqrt{\beta\epsilon_y}\cos\phi_y
\end{aligned}$$

where the betatron phase advance is given by:

$$\phi = \frac{s}{\beta} + \phi_0.$$

A particles transverse position is given by $r^2 = x^2 = y^2$ therefore

$$r^2 = \beta\epsilon_x\cos^2\phi_x + \beta\epsilon_y\cos^2\phi_y + D^2\delta^2 + 2 \sqrt{\beta\epsilon_x}\cos\phi_x D\delta.$$

Because the betatron tune $Q_x$ and $Q_y$ are large, the variation due to phase-advance averages out to zero and accordingly:

$$\overline{r^2} = \frac{1}{C}\oint r^2 ds $$
since
$$\overline{\cos^2x} =\lim_{x\to\infty} \frac{1}{x}\int_0^x \cos^2x'dx' = \frac{1}{2}$$
and 
$$\overline{\cos x} = \lim_{x\to\infty} \int_0^x \cos x' dx' = 0$$

$$\boxed{\overline{r^2} = \frac{\beta}{2}(\epsilon_x+\epsilon_y)+D^2\delta^2}$$

---

</details>

and

$$\bar{a}=2\sqrt[4]{(\beta\sigma_\epsilon+D^2\sigma_\delta^2)(\beta\sigma_\epsilon)}$$

<details>

---

For the beam width $a$, if the beta function is approximated as constant throughout the ring, the beam radius is given by:

$$a = \sqrt{a_y a_y} = 2\sqrt{\sigma_x\sigma_y}$$

where:

$$\begin{aligned}
\sigma_x^2 &=\beta\sigma_\epsilon + D^2\sigma_\delta^2\cr
\sigma_y^2 &= \beta\sigma_\epsilon
\end{aligned}$$

Because the optics optics are assumed invariant along the ring, the beam width is constant nd so accordingly

$$\boxed{\bar{a} = 2\sqrt[4]{(\beta\sigma_\epsilon+D^2\sigma_\delta^2)(\beta\sigma_\epsilon)}}$$

---

</details>

For fringe particles where $\overline{r^2} \geq \bar{a}^2$, the geometry factor is given by:

$$\bar{g} = \overline{\ln \frac{b}{r}} = \ln b - \overline{\ln r}$$

where:

$$\overline{\ln r} = ?$$

<details>

---

Because $\overline{\ln r} = \frac{1}{2}\overline{\ln r^2}$ and that:

$$\begin{aligned}
\overline{\ln r^2} &= \frac{1}{2\pi}\oint \ln r^2d \theta\cr
&= \frac{1}{2\pi}\oint_0^{2\pi} \ln\left(\beta(\epsilon_x\cos^2\phi_x + \epsilon_y\cos^2\phi_y)+D^2\delta^2+2\sqrt{\beta\epsilon_x}\cos\phi_xD\delta\right)d\theta
\end{aligned}$$

where:

$$\phi = \frac{R\theta}{\beta}+ \phi_0$$

---