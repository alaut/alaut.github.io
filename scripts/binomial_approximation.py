import matplotlib.pyplot as plt
import numpy as np

from sylt.functions import binomial, binomial_der

profiles = {
    r"$f(x; \mu)$": binomial,
    r"$f'(x; \mu)$": binomial_der,
}

sig = 1
mu = np.arange(4)
L = sig*2*np.sqrt(3+2*mu)
x = np.linspace(-L/2, L/2, 999)

for i, (YLABEL, fun) in enumerate(profiles.items()):
    fig, ax = plt.subplots(constrained_layout=True)

    ax.plot(x/sig, fun(x, L, mu=mu), label=mu)

    ax.legend()
    ax.set_xlabel(r"$x$ ($\sigma$)")
    ax.set_ylabel(YLABEL)

    fig.savefig(f'./assets/binomial.{i}.svg')

plt.show()
