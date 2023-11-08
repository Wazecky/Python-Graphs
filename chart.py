import matplotlib.pyplot as plt
import numpy as np

# set num of steps
num_steps = 16

# set num of lines
num_lines = 8

# set line width
line_width = 2

# set angle
angle = 45

# set colors
colors = plt.cm.viridis(np.linspace(0, 1, num_lines))

# set figure size
plt.figure(figsize=(10, 6))

# set anchor point
anchor_point = (0.5, 0.5)

# create steps
steps = np.linspace(0, 1, num_steps)

# create lines
for i in range(num_lines):
    # create line data
    x = anchor_point[0] + steps * np.cos(angle * np.pi / 180)
    y = anchor_point[1] + steps * np.sin(angle * np.pi / 180)

    # plot line
    plt.plot(x, y, color=colors[i], linewidth=line_width)

# set limits slightly bigger than anchor point
plt.xlim([-0.1 + anchor_point[0], 1.1 + anchor_point[0]])
plt.ylim([-0.1 + anchor_point[1], 1.1 + anchor_point[1]])

# set axes
plt.xlabel("X")
plt.ylabel("Y")

# set title
plt.title(f"{num_lines} Lines, {num_steps} Steps, {angle}° Angle")

# show plot
plt.show()