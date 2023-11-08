import matplotlib.pyplot as plt
import numpy as np

# set radius and theta 
theta = np.linspace(0, np.pi, 200)
radius = 1

a = radius * np.cos( theta )
b = radius * np.sin( theta )

# plot in red color
plt.plot(a, b, color = 'r')

# set aspect ratio
plt.gca().set_aspect('equal')

# set labels
plt.xlabel("X")
plt.ylabel("Y")

# set limits slightly bigger than radius
plt.xlim(-radius - radius/5, radius + radius/5)
plt.ylim(-radius - radius/5, radius + radius/5)

# set title 
plt.title("Semi Circle")
plt.show()