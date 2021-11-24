---
layout: post
title: SC
author: Alexander J. Laut
---

## Space Charge

A __wake potential__ $V_W$ is defined by:

$$\mathcal{E} _{ind} = -\nabla V_W \rightarrow \Delta V_W = -\int_L\mathcal{E} _{ind}\cdot dl$$

The __wakefunction__ is defined as the wake field gain per unit charge:

$$W(\tau) = \frac{\Delta V_w}{q} = -\frac{1}{q}\int_0^{l_{ind}} \vec{\mathcal{E}}_{ind}(s)\cdot \vec{ds}$$

The particle's energy gain due to the experienced wake potential is given by:

$$U = \Delta E = q \Delta V_W = q^2 W$$

where:

$$t = \frac{s}{\beta c}-\tau$$

and our normalized charge density function is defined as:

$$Q = \int_{-\infty}^{\infty}\lambda(\tau)d\tau  = qN_b$$

In a bunch distribution, we must convolute our charge density to yield the total induced wake potential for a particle from all other particles:

$$V_{ind}(\tau) = -\int_{-\infty}^{\infty}\lambda(\tau')W(\tau-\tau')d\tau' = (\lambda * W)(\tau) $$

Our charge density $\lambda(\tau)$ and wake function $\mathcal{W}(\tau)$ can be re-written in frequency domain as bunch spectrum $S(f)$ and impedance $Z(f)$:

$$S(f) = \mathcal{F}\{\lambda(\tau)\} = \int_{-\infty}^{\infty}\lambda(\tau)e^{-i\omega\tau}d\tau \\
Z(f) = \mathcal{F}\{W(\tau)\} = \int_{-\infty}^{\infty}W(\tau)e^{-i\omega\tau}d\tau$$

Using fourier properties, our induced voltage in the frequency domain is:

$$V_{ind}(\tau) = \mathcal{F}^{-1}\{S(f)Z(f)\} = -\int_{-\infty}^{\infty} S(f) Z(f) e^{i2\pi f \tau} df$$

For harmonics $n = f/f_{rev}$:

$$V_{ind}(\tau) = -f_{rev}\sum_{n=-\infty}^\infty S(nf_{rev})\mathcal{Z}(nf_{rev})e^{i2\pi f_{rev}\tau}$$

# Small Amplitude Oscillations

As a reminder, in normal synchrotron oscillations, we have that the particles within a bunch make quasi-elliptical orbits at the synchrotron frequency $\Omega_s = \omega_s$ in ($\Delta E- \Delta t$) phase space according to the following:

$$\begin{aligned}
\Delta t &= \Delta t_0\cos(\omega_s t)\cr\cr
\Delta E &= \Delta E_0 \sin(\omega_s t)
\end{aligned}$$

To model this motion as an induced voltage, we require the spectrum and impedance:

$$V_{ind} = -qN_b\int_{-\infty}^\infty S(f)Z(f)e^{i\omega \tau}df$$

Using the [Jacobi-Anger expansion](https://en.wikipedia.org/wiki/Jacobi%E2%80%93Anger_expansion):

$$e^{i z\cos\theta}=J_0(z)+2\sum_{n=1}^\infty i^nJ_n(z)\cos(n\theta)$$

and that [the Bessel functions](https://en.wikipedia.org/wiki/Bessel_function#Bessel_functions_of_the_first_kind) can be approximated for $0<z<<\sqrt{a+1}$:

$$J_a(z) \approx \frac{1}{\Gamma(a+1)}\left(\frac{z}{2}\right)^a$$

Where:

$$\Gamma(n) = (n-1)!$$

Therefore for small z:

$$e^{i z \cos \theta} \approx J_0(z)+2iJ_1(z)\cos(\theta) \approx1 + i z \cos \theta$$

Replacing for:

$$z = 2\pi f \tau_0 \quad\theta = \omega_s t \quad \omega = 2\pi f \quad\tau = \tau_0 \cos(\omega_s t)$$

We then get:

$$e^{i 2\pi f\tau_0\cos(\omega_s t)} = 1 + i 2\pi f\tau_0\cos(\omega_st)$$

Or:

$$\boxed{e^{i\omega\tau} = 1 + i\omega \tau}$$

Re-substituting into our equation for induced voltage yields:

$$V_{ind} = -qN_b\int_{-\infty}^\infty S(f)Z(f)(1+i\omega\tau )df$$


Defining:

$$\begin{aligned}
Z_0 &= \int_{-\infty}^\infty S(f) Z(f) df = \int_{-\infty}^\infty S(f) R(f) df\cr
Z_1 &= \int_{-\infty}^\infty S(f) Z(f) i \omega df = 2\pi\int_{-\infty}^{\infty}S(f)X(f)fdf
\end{aligned}$$

Our expression simplifies to:

$$\boxed{V_{ind} = -qN_b(Z_0 + \tau Z_1 + ...)}$$

For an impedance defined by:

$$Z(f) = R(f) + j X(f)$$

As it is defined by the fourier transform of the real wake potential, it is hermitian (as is the spectrum) if it is hermitian, $R(f)$ is even and $X(f)$ is odd:

# Equations of Motion

If we now recite our equation of motion:

$$\ddot{\phi}+\frac{h\omega_s^2\eta}{2\pi\beta_s^2E_s}\left(qV_g g(\phi)+qV_{ind}\right)=0$$

Or equivalently:


$$\ddot{\tau} + \frac{\eta}{\beta_s^2E_sT_{rev}}q\left(V_g g(h\omega_s\tau)+V_{ind}(\tau)\right) = 0$$

Which substitutes to:

$$\ddot{\phi}+\frac{\Omega_s^2}{\cos\varphi_s}g(\phi)=\frac{\Omega_s^2}{\cos\varphi_s}\frac{q N_b}{V_g}\left(Z_0+Z_1(\frac{\phi}{h\omega_s})\right)$$

or more consicely:

$$\boxed{\ddot{\phi}+\frac{\Omega_s^2}{\cos\varphi_s}\left(g(\phi)+\frac{q N_b}{V_g}\left( Z_0+Z_1 \frac{\phi}{h\omega_s}\right) \right) = 0}$$