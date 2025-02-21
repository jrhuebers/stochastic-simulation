import numpy as np
import matplotlib.pyplot as plt

def sample_exponential(lam):
    # This function uses the inverse transform to sample an exponential distribution
    u = np.random.uniform()
    x = -1/lam * np.log(1-u)
    return x

nu = 4
def p(x):
    #return np.power(x, nu/2-1)*np.exp(-x/2) / (np.power(2, nu/2) * np.math.factorial(nu/2 - 1))
    return np.power(x, nu/2-1)*np.exp(-x/2) / (np.power(2, nu/2))

lam = 1/nu
def q(x):
    return lam * np.exp(-lam*x)

#M = np.power((nu/2-1)/(1/2-lam), nu/2-1) * np.exp(1-nu/2) / (np.power(2,nu/2) * np.math.factorial(np.round_(nu/2-1)) * lam)
M = 4/np.e
x_accepted = []
while len(x_accepted) < 10000:
  x = sample_exponential(lam)
  y = np.random.uniform()

  if y <= p(x)/(M*q(x)):
      x_accepted.append(x)
      #print("huzza", len(x_accepted))


xx = np.linspace(0,25,1000)
yy = p(xx)

plt.hist(x_accepted, bins=100, density=True, alpha=0.5)
plt.plot(xx,yy)
plt.show()
