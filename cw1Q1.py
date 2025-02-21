######
# Q1 #
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


# generating 10,000 samples of chi-squared (nu = 4) distribution
samples = []
total_tries = 0
for i in range(10000):
  (x, tries) = sample_chi_squared(4, return_tries=True)
  samples.append(x)
  total_tries += tries


# plot of histogram, p and M*q
xx = np.linspace(0,25,1000)
yy = p(xx, 4)

plt.hist(samples, bins=100, density=True, alpha=0.5)
plt.plot(xx,yy)
plt.show()


# compute acceptance rate and compare with theoretical acceptance rate
a = len(samples)/total_tries
M = np.power((nu/2-1)/(1/2-lam), nu/2-1) * np.exp(1-nu/2) / (np.power(2,nu/2) * np.math.factorial(int(nu/2+0.1-1)) * lam)
a_hat = 1/M

print("acceptance rate  ", a)
print("theor. acc. rate ", a_hat)
#print("deviation from theor. acc. rate", (a-a_hat)/a_hat)

