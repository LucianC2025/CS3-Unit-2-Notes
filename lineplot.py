import matplotlib.pyplot as plt
import numpy as np


# Set Style for Charts
plt.style.use('seaborn-v0_8-pastel')
# print(plt.style.available) # Get the available color schemes

#  ***************** CHART 1 ***************** 

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

# Close old plot before making new one
plt.close()


#  ***************** CHART 2 ***************** 

# Alternatively, set up a figure OBJECT
fig = plt.figure() # NOTE: figure is a container that contains all the objects representing axes, graphics, text, and labels
ax = plt.axes() # NOTE: axes is a bounding box with ticks, grids, and labels 

# Plot a funciton on the Axes object instance
ax.plot(x_vals, 2*(x_vals), color = 'pink')
ax.plot(x_vals, 3*(x_vals), color ='#91EF9F', linestyle='dashed')
ax.plot(x_vals, 4*(x_vals), color = '#7678ed', linestyle='dashdot')
ax.plot(x_vals, 5*(x_vals), color ='#e63946', linestyle='dotted')
ax.plot(x_vals, np.tan(x_vals), color = '#e9ff70')

# You can use shortcut to define color & style
ax.plot(x_vals, 1.5*(x_vals), '-m')
fig.savefig('lineplot2.png')
plt.close() # clear the plot before making another


#  ***************** CHART 3 ***************** 

# Demo on custimization
plt.plot(x_vals, np.sin(x_vals), '-.m', label="sin(x)")
plt.xlim(-1,11)
plt.ylim(-1.5, 1.5)
# Set axis to tight to fit your plot better
plt.axis('tight') # zooms in, makes sure the axis aren't longer than neccessary and added ticks, the entire set of data gets plotted in a tighter box. less white space
# other options: 'equal' OR 'image' OR etc

# Add TITLES / LABELS
plt.title('A Sine Wave')
plt.xlabel('x')
plt.ylabel('sin(x)')
# Add LEGEND
plt.legend()

plt.savefig('lineplot3.png')
plt.close()


#  ***************** CHART 4 ***************** 

