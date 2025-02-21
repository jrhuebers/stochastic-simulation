import numpy as np
import matplotlib.pyplot as plt

A1 = np.matrix([[0.4, -0.3733],[0.06, 0.6]])
A2 = np.matrix([[-0.8, -0.1867],[0.1371, 0.8]])

b1 = np.array([[0.3533,0.0]]).T
b2 = np.array([[1.1,0.1]]).T

def f(i,x):
    if i == 1:
        return A1 @ x + b1
    elif i == 2:
        return A2 @ x + b2

x = [np.array([[0,0]]).T]
for n in range(1,10001):
    i_n = np.random.choice([1, 2], p=[0.2993, 0.7007])
    x.append(f(i_n,x[-1]))

x = np.array(x)

plt.scatter(x[20:,0], x[20:,1], s=0.1, color=[0.8, 0, 0])
plt.gca().spines['top'].set_visible (False)
plt.gca().spines['right'].set_visible (False)
plt.gca().spines['bottom'].set_visible (False)
plt.gca().spines['left'].set_visible (False)
plt.gca().set_xticks ([])
plt.gca().set_yticks ([])
plt.gca().set_xlim(0, 1.05)
plt.gca().set_ylim(0, 1)
plt.show()