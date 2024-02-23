import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define a grid of points in x and y
x = np.linspace(0, 5, 100)
y = np.linspace(0, 5, 100)

# Create a meshgrid from x and y
X, Y = np.meshgrid(x, y)

# Define the equation of the plane z = 1
Z = np.ones_like(X)

# Create a 3D plot
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='3d')

# Plot the plane
ax.plot_surface(X, Y, Z, alpha=0.5, rstride=100, cstride=100, color='red')
ax.plot_surface(X, X, Y, alpha=0.5, rstride=100, cstride=100, color='green')
# Set axis labels
ax.set_xlabel('a')
ax.set_ylabel('b')
ax.set_zlabel('n')

# Set the title
ax.set_title('solution of n using 3d plot')

# Show the plot
plt.show()

