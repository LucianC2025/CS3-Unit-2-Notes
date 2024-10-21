import matplotlib.pyplot as plt
import numpy as np

# Set Style for Charts
plt.style.use('seaborn-v0_8-pastel')
# print(plt.style.available) # Get the available color schemes

# Create a sample set of data
# Remember that X is for the independent variable
# NOTE: .linspace creates a linear space of points
x_vals = np.linspace(0, 10, 100) # 0 is the starting point, 10 is the stop point, 100 is the number of samples to generate

# LINE PLOTS are good when graphing FUNCTIONS
# Use .plot Function
plt.plot(x_vals, np.sin(x_vals))
plt.plot(x_vals, np.cos(x_vals))

# Show figure 
#plt.show()

# Save Figure as PNG in current directory (The folder that we are in) 
plt.savefig('lineplot.png') # x-values are from 0 to 10, y-values are from -1 to 1


# Alternatively, set up a figure OBJECT
fig = plt.figure() # NOTE: figure is a container that contains all the objects representing axes, graphics, text, and labels
ax = plt.axes() # NOTE: axes is a bounding box with ticks, grids, and labels 

# Plot a funciton on the Axes object instance
ax.plot(x_vals, 2*(x_vals), color = 'pink')
ax.plot(x_vals, np.tan(x_vals), color = 'dodgerblue')
fig.savefig('lineplot2.png')
