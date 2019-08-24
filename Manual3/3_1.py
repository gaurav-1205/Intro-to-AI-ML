import numpy as np
import matplotlib.pyplot as plt

def coin(x):
	return 2*np.random.randint(2, size=x)-1

simlen = int(1e5)

N = np.random.normal(0,1,simlen)

S = coin(simlen)
A=4
X = A*S+N
print()
print(X.shape)
print(X.min())
print(X.max())
x = np.linspace(-10, 10, int(1e5))
plt.scatter(x,X)
plt.show()