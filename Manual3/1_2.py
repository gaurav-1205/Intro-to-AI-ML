import numpy as np

simlen = int(1e5)

n = np.random.normal(0, 1, simlen)

mean = np.sum(n)/simlen
print(mean)

var = np.sum(np.square(n-mean*np.ones((1, simlen))))/simlen

print(var)