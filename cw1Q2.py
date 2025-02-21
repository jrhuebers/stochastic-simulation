######
# Q2 #
######

import numpy as np
import matplotlib.pyplot as plt

def sample_exponential(lam):
    # This function uses the inverse transform to sample an exponential distribution
    u = np.random.uniform()
    x = -1/lam * np.log(1-u)
    return x

def p(x, nu):
    return x ** (nu / 2 - 1) * np.exp(-x / 2) / (2 ** (nu / 2) * np.math.factorial(int(nu / 2+0.1) - 1))

def q(x, lam):
    return lam * np.exp(-lam*x)

def sample_chi_squared(nu, return_tries=False):
  lam = 1/nu
  M = np.power((nu/2-1)/(1/2-lam), nu/2-1) * np.exp(1-nu/2) / (np.power(2,nu/2) * np.math.factorial(int(nu/2+0.1-1)) * lam)

  tries = 0
  while True:
    tries += 1
    x = sample_exponential(lam)
    y = np.random.uniform()

    if y <= p(x,nu)/(M*q(x,lam)):
      if return_tries:
        return x, tries
      else:
        return x

w = [0.2, 0.5, 0.3]
nu = [4, 16, 40]

# drawing 100,000 samples
samples = []
for i in range(100000):
    u = np.random.uniform(0,1)
    if u <= w[0]:
        samples.append(sample_chi_squared(nu[0]))
    elif u <= w[0]+w[1]:
        samples.append(sample_chi_squared(nu[1]))
    else:
        samples.append(sample_chi_squared(nu[2]))

def mixture_density (x, w, nu):
  return w[0]*p(x, nu[0]) + w[1]*p(x, nu[1]) + w[2]*p(x, nu[2])

# plots
xx = np.linspace(0, 60 , 1000)
plt.plot(xx , mixture_density(xx , w, nu), color='k', linewidth=2)


plt.hist(samples, bins=100, density=True, alpha=0.5)
plt.show()

