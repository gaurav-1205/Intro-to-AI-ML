import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-4, 4, 300)

simlen = int(1e5)

err = []

n = np.random.normal(0, 1, simlen)
# print(n)

mean = np.sum(n)/simlen
# print(mean)

var = np.sum(np.square(n-mean*np.ones((1, simlen))))/simlen



for i in range(0,30):
	err_ind = np.nonzero(n < x[i])
	err_n = np.size(err_ind)
	err.append(err_n/(simlen*1.0)) 


Px = (1/np.sqrt(2*np.pi*var)*np.exp((-(x-mean)**2)/(2*var)))

# print(err)

plt.plot(x.T, Px)
plt.grid()
plt.xlabel('$x$')
plt.xlabel('$y$')
plt.show()