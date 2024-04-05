import numpy as np
import matplotlib.pyplot as plt

x=np.array([1.0,2.0,3.0,4.0,2.0,1.0])
y= np.loadtxt('y_n_output.txt',dtype='double')

plt.stem(range(0,6),x)
plt.ylabel('$x(n)$')
plt.grid()
plt.savefig("Plot_xn.png")
