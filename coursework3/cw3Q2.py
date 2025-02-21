import numpy as np
import matplotlib.pyplot as plt

# Logarithm of volatility is initially 1
x = [1]
# Observed returns start at 0
y = [0]

for n in range(1,1001):
    x.append(np.random.normal(1+0.98*(x[-1]-1), 0.1))
    y.append(np.random.normal(0, np.exp(x[-1])))

plt.plot(range(1001), np.exp(x), color="red", label="x")
plt.show()
plt.plot(range(1001), y, color="blue", label="y")
plt.show()
