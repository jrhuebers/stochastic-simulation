import numpy as np
import matplotlib.pyplot as plt

def alpha(x,x_prime):
    sigma_y = 1
    mu_x = 0
    sigma_x = 10
    y = [4.44, 2.51, 0.73]
    s = [-1, 2, 5]
    
    sum = 0
    for i in range(3):
        sum += ((y[i]-abs(x-s[i]))**2 - (y[i]-abs(x_prime-s[i]))**2)/(2*sigma_y**2)
    return np.exp(((x-mu_x)**2 - (x_prime-mu_x)**2) / (2*sigma_x**2) + sum)

x_true = 4
N = 1000000
for sigma_q in [0.1,0.01]:
    x_0 = 10
    x_list = [x_0]
    
    burnin = -1
    for n in range(N):
        x = x_list[n]
        x_prime = np.random.normal(x,sigma_q)

        if x_prime < 4 and burnin == -1:
            print(n)
            burnin = n

        if alpha(x,x_prime) >= np.random.uniform():
            x_list.append(x_prime)
        else:
            x_list.append(x)
    
    plt.clf()
    plt.axvline (x_true, color='k', label='true value ', linewidth=2)
    plt.hist(x_list[burnin:N], bins=50 , density=True , label='posterior ', alpha=0.5, color=[0.8, 0, 0])
    plt.legend()
    plt.title("$\sigma_q$ = "+str(sigma_q))
    plt.show()