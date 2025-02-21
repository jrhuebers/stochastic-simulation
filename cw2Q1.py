import numpy as np
import matplotlib.pyplot as plt

def phi(x):
    y = 9
    return 1/np.sqrt(2*np.pi) * np.exp(-((y-x)**2)/2)

def p(x):
    return 1/np.sqrt(2*np.pi) * np.exp(-1/2 * x**2)

def q(x):
    return 1/np.sqrt(2*np.pi) * np.exp(-1/2 * (x-6)**2)

phi_bar = 1/(2*np.sqrt(np.pi) * np.exp(81/4))
MC_estimates = []
MC_RAE = []
IC_estimates = []
IC_RAE = []
samples = np.random.normal(0,1,100000)
samples2 = np.random.normal(6,1,N)
for N in [10,100,1000,10000,100000]:
    estimate_MC = np.sum(phi(samples[0:N]))/N
    MC_estimates.append(estimate_MC)
    MC_RAE.append(abs(estimate_MC-phi_bar)/abs(phi_bar))
    
    estimate_IC = np.sum((p(samples2)/q(samples2)*phi(samples2))[0:N])/N
    IC_estimates.append(estimate_IC)
    IC_RAE.append(abs(estimate_IC-phi_bar)/abs(phi_bar))

print("phi_bar =", phi_bar)
print()

print("Monte Carlo")
print(MC_estimates)
print(MC_RAE)
print()

print("Importance sampling")
print(IC_estimates)
print(IC_RAE)

# plots
plt.plot([10,100,1000,10000,100000],MC_RAE)
plt.loglog()
plt.xlabel("N")
plt.ylabel("RAE")
plt.title("Relative absolute error for Monte Carlo")
plt.show()

plt.plot([10,100,1000,10000,100000],IC_RAE)
plt.loglog()
plt.xlabel("N")
plt.ylabel("RAE")
plt.title("Relative absolute error for importance sampling")
plt.show()

plt.plot([10,100,1000,10000,100000],MC_RAE,label="Monte Carlo")
plt.plot([10,100,1000,10000,100000],IC_RAE,label="Importance sampling")
plt.loglog()
plt.xlabel("N")
plt.ylabel("RAE")
plt.legend()
plt.show()