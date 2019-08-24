import numpy as np
import matplotlib.pyplot as plt
import subprocess
import shlex

#Plotting log(x)
x = np.linspace(-4,4,50)#points on the x axis
# f=np.log(x)#Objective function
f=x**2#Objective function
plt.plot(x,f,color=(1,0,1))
plt.grid()
plt.xlabel('$x$')
plt.ylabel('$\ln x$')

#Convexity/Concavity
a = -3
b = 4
lamda = 0.3
c = lamda *a + (1-lamda)*b
f_a = a**2
f_b = b**2

f_c = c**2
f_c_hat = lamda *f_a + (1-lamda)*f_b

#Plot commands
plt.plot([a,a],[0,f_a],color=(1,0,0),marker='o',label="$f(a)$")
plt.plot([b,b],[0,f_b],color=(0,1,0),marker='o',label="$f(b)$")
plt.plot([c,c],[0,f_c],color=(0,0,1),marker='o',label="$f(\lambda a + (1-\lambda)b)$")
plt.plot([c,c],[0,f_c_hat],color=(1/2,2/3,3/4),marker='o',label="$\lambda f(a) + (1-\lambda)f(b)$")
plt.plot([a,b],[f_a,f_b],color=(0,1,1))
plt.legend(loc=2)


plt.show()#Reveals the plot








