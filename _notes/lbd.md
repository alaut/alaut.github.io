---
layout: post
title: LBD
author: Alexander Laut
---

## Longitudinal Beam Dynamics

# Time Energy Coordaintes

Noting:

$$\tau = t-t_s \qquad \phi = \varphi - \varphi_s \qquad \delta = \frac{p-p_s}{p_s} \qquad w = W-W_s$$

From panofsky equation, we have the discrete energy gain per turn defined by the gap voltage and RF phase:

$$\Delta W = qV_g\cos\varphi$$

In relative coordinates we accordingly have:

$$\Delta w = \Delta W - \Delta W_s = qV_g(\sin\varphi-\sin\varphi_s)=qV_g g(\phi)$$

From $\Delta w/\Delta t \approx \dot{w}$ and letting $g(\phi) = \sin\varphi-\sin\varphi_s$:

$$\dot{w} = \frac{qV_g}{T_s}g(\phi)$$

Changing variables from $\phi = h\omega_s\tau$, we can write:

$$\boxed{\dot{\tau} = \kappa w \qquad \dot{w} = \frac{qV(\tau)}{T_s}}$$

Where:

$$\kappa = \frac{\eta}{\beta_s^2E_s} \qquad V(\tau) = V_g g(h\omega_s \tau)$$

And in discretized form we have:

$$\boxed{\Delta w = qV(\tau) \qquad \Delta\tau = \kappa T_s w}$$

We can derive our __EOM__ from the following hamiltonion:

$$\boxed{H = \frac{1}{2}\kappa w^2-\frac{q}{T_s}\int V(\tau)d\tau}$$

For an RF voltage source(s) of harmonic $h$ and gap voltage $V_h$, we have:

$$V(\tau) = \sum V_h g_h(\tau)$$

Where:

$$\begin{aligned}
g(\phi) &= \sin\varphi-\sin\varphi_s\cr
&=\sin(\phi+\varphi_s)-\sin\varphi_s\cr
&= \sin\phi\sin\varphi_s+\cos\phi\cos\varphi_s-\sin\varphi_s\cr
&= \sin\varphi_s(\sin\phi-1)+\cos\varphi_s\cos\phi
\end{aligned}$$

Therefore:

$$G(\phi) = \int g(\phi) d\phi = -\sin\varphi_s(\cos\phi+\phi)+\cos\varphi_s\sin\phi$$

So our hamiltonion simplifies to:

$$H = \frac{1}{2}\kappa w^2 - \frac{q}{T_s}G(\tau)$$

For small $\phi$ and $\phi = h\omega_s\tau$:

$$g(\phi) \approx \cos\varphi_s\phi$$

Therefore:

$$\ddot{\tau} - \frac{\eta}{\beta_s^2E_s}\frac{qV_g}{T_s}\cos\varphi_sh\omega_s \tau = 0$$

Or:

$$\ddot{\tau}+\Omega_s^2\tau=0 \qquad \ddot{w}+\Omega_s^2w=0$$

where:

$$\boxed{\Omega_s^2 = -\frac{h\omega_s^2\eta}{\beta_s^2E_s} \frac{qV_h}{2\pi}\cos\varphi_s}$$