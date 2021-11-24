---
layout: post
title: TBD
author: Alexander Laut
---

## Transverse Beam Dynamics

The sollutions of the Hill's equations are generalized as follows:

$$\begin{aligned}
u &= \sqrt{\epsilon\beta}\cos\phi\\
u' &=-\sqrt{\frac{\epsilon}{\beta}}(\alpha\cos\phi+\sin\phi)
\end{aligned}$$

Where:

$$\phi = \mu + \mu_0$$

$$\alpha = -\frac{1}{2}\beta'$$

$$\gamma = \frac{1+\alpha^2}{\beta}$$

$$\mu = \int_{0}^s \frac{ds}{\beta} \to \phi' = \frac{1}{\beta}$$

If we include dispersion we have:

$$\begin{aligned}
u &= \sqrt{\epsilon \beta} \cos \phi + D\delta\\
u' &= \sqrt{\frac{\epsilon}{\beta}}(\alpha\cos\phi+\sin\phi) + D'\delta + D\dot{\delta}
\end{aligned}$$

# Bunch Distributions

## Elliptical Distributions

An ellipse with semi-axes __a__, __b__ and area $A=\pi a b$ is defined by:

$$\begin{aligned}
x(\varphi) &= a\cos\varphi\\
y(\varphi) &= b \sin\varphi
\end{aligned}$$

Upon rotation by angle $\phi$ our equations yield:

$$\begin{aligned}
x(\varphi) &= a\cos\varphi\cos\phi-b\sin\varphi\sin\phi\\
y(\varphi) &= a\cos\varphi\sin\phi+b\sin\varphi\cos\phi
\end{aligned}$$

<!-- Our semi-axis are equivalently defined by:

$$\begin{aligned}
a^2 &= x(\phi)^2+y(\phi)^2\\
b^2 &= x(\phi+\pi/2)^2+y(\phi+\pi/2)^2
\end{aligned}$$

For __a__:

$$\begin{aligned}
x(\phi) &= a\cos\phi\cos\phi-b\sin\phi\sin\phi &= a\cos^2\phi-b\sin^2\phi\\
y(\phi) &= a\cos\phi\sin\phi+b\sin\phi\cos\phi &= (a+b)\cos\phi\sin\phi
\end{aligned}$$

so:

$$a^2 = a\cos^2\phi+b\sin^2\phi = x(\phi)+2b\sin^2\phi$$ -->

## Transforming Offset Elliptical Phase-Space Distributions

We can generate our elliptical distributions by defining the following covariance matrix:

$$\Sigma=\epsilon\Omega = \epsilon\begin{bmatrix}\beta & -\alpha \\ -\alpha & \gamma\end{bmatrix}$$

This distribution follows such that:

$$\epsilon = \sqrt{\det{\Sigma}}$$

Said particle will normally follow an elliptical trajectory in $(u, u')$ phase-space given by:

$$\boxed{\epsilon = \gamma u^2 + 2\alpha u u' + \beta u'^2}$$

We can further deduce from $\beta(s)$, given by our optics, the following:

$$\alpha(s) = -\frac{1}{2}\beta'(s)\\
\gamma(s) = \frac{1+\alpha(s)^2}{\beta(s)}$$

This elliptical distribution appears rotated by $\phi$ as defined by:

$$\tan(2\phi) = \frac{-2\alpha(s)}{\beta(s) -\gamma(s)}$$

Particles $(\epsilon, \varphi)$ injected with an offset $\Delta u$ will follow enlarged elliptical trajectories given by a transformation $\varphi\to\tilde{\varphi}$ and emittance $\epsilon\to\tilde{\epsilon}$ transform.

<!-- ![](../figs/offset_distribution.drawio.svg) -->

From:

$$\begin{aligned}
u = r\cos\varphi\\
u' = r\sin\varphi
\end{aligned}$$

Substituing this into our ellipse equation gives:

$$\epsilon = r^2\left(\gamma\cos^2\varphi+2\alpha\cos\varphi\sin\varphi+\beta\sin^2\varphi\right)$$

Our particle's radial position is therefore defined via $\epsilon$, $\varphi$, and it's optics $\alpha, \beta, \gamma$:

$$\boxed{r^2 = \frac{\epsilon}{\gamma\cos^2\varphi+2\alpha\cos\varphi\sin\varphi+\beta\sin^2\varphi}}$$

To transform from $u\to\tilde{u}$ we solve the __SAS__ triangle first by __law of cosines__:

$$\boxed{\tilde{r}^2=\Delta u^2 + r^2 - 2\Delta u r \cos(\pi-\varphi)}$$

We solve for $\tilde{\varphi}$ using __law of sines__:

$$\frac{\sin\tilde{\varphi}}{r} = \frac{\sin(\pi-\varphi)}{\tilde{r}}$$

Alternatively:

$$\boxed{\tilde{\varphi} = \arcsin\left(\frac{r\sin(\pi-\varphi)}{\tilde{r}}\right)}$$

Considering that:

$$\begin{aligned}
\tilde{u} &= \tilde{r}\cos\tilde{\varphi}\\
\tilde{u}' &= \tilde{r}\sin\tilde{\varphi}
\end{aligned}$$

Then from the new phase-space trajectory defined by:

$$\begin{aligned}
\tilde{\epsilon} &= \gamma \tilde{u}^2+2\alpha\tilde{u}\tilde{u}'+\beta\tilde{u^2}\\
&=\tilde{r}^2\left(\gamma\cos^2\tilde{\varphi}+2\alpha\cos\tilde{\varphi}\sin\tilde{\varphi}+\beta\sin^2\tilde{\varphi}\right)
\end{aligned}$$

Particle emittance $\tilde{\epsilon}$ will increase and phase $\tilde{\varphi}$ shift when offset in phase-space by $\Delta u$. These new coordinates will follow standard betatron motion as defined by:

$$\boxed{\tilde{u}(s) = \sqrt{\tilde{\epsilon}\beta(s)}\cos\tilde{\varphi}(s)}$$

## Compute semi-axes

For a rotated ellipse by $\phi$ we have:

$$\begin{aligned}
1 &= \frac{(u\cos\phi-u'\sin\phi)^2}{a^2}+\frac{(u\sin\phi+u'\cos\phi)^2}{b^2}\\
&=\frac{c^2u^2-2uu'cs+s^2u'^2}{a^2}+\frac{s^2u^2+2uu'cs+c^2u'^2}{b^2}\\
&= \left(\frac{c^2}{a^2}+\frac{s^2}{b^2}\right)u^2+2cs\left(\frac{1}{b^2}-\frac{1}{a^2}\right)uu'+\left(\frac{s^2}{a^2}+\frac{c^2}{b^2}\right)u'^2
\end{aligned}$$

Where:

$$\begin{aligned}
s = \sin\phi\\
c = \cos\phi\\
t = \tan\phi
\end{aligned}$$

Considering the area of an ellipse is defined by:

$$A = \pi a b = \pi \epsilon \to \epsilon = ab$$

We can derive our twiss parameters as:

$$\begin{aligned}
\gamma &= \epsilon \left(\frac{c^2}{a^2}+\frac{s^2}{b^2}\right) &=&\frac{1}{\epsilon} (s^2a^2+c^2b^2)\\
\alpha &= \epsilon \left(\frac{1}{b^2}-\frac{1}{a^2}\right)cs &=&\frac{cs}{\epsilon}(a^2-b^2) \\
\beta &= \epsilon \left(\frac{s^2}{a^2}+\frac{c^2}{b^2}\right) &=&\frac{1}{\epsilon}(c^2a^2+s^2b^2)
\end{aligned}$$

Yielding the familiar:

$$\epsilon = \gamma u^2 + 2\alpha u u' + \beta u'^2$$

Therefore:

$$\begin{bmatrix}s^2& c^2 \\ cs &-cs \\ c^2& s^2 \end{bmatrix} \begin{bmatrix}a^2\\b^2\end{bmatrix}=\epsilon\begin{bmatrix}
\gamma \\ \alpha \\ \beta    
\end{bmatrix}$$

Which simplifies yielding:

$$\boxed{\begin{aligned}
a^2 &= \epsilon(\alpha t+\beta)\\ b^2 &= \epsilon(\alpha t+\gamma)
\end{aligned}}$$

## Polar to Phase
Our polar angle $\theta$ in phase-space given by $\tan\theta=\frac{x'}{x}$ requires transformation to yield the phase advance $\varphi$

We have:

$$\begin{aligned}
u &= \sqrt{\beta\epsilon}\cos\phi\\
u'&=-\sqrt{\frac{\epsilon}{\beta}}(\alpha\cos\phi+\sin\phi)
\end{aligned}$$

Accordingly we can generate:

$$\frac{u'}{u} = -\frac{1}{\beta}(\alpha+\tan\varphi)$$

Therefore:

$$\boxed{\varphi = \arctan\left(-\beta\frac{u'}{u}-\alpha\right)}$$

Our __polar angle__ $\theta$ in u-u' phase-space is therefore is transformed to phase advance $\varphi$ via:

$$\boxed{\tan\varphi + \alpha + \beta\tan\theta = 0}$$ 