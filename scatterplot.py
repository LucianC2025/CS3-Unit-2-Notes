import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_iris


plt.style.use('seaborn-v0_8-pastel')

# Generate data points
rng = np.random.default_rng(0)
x = rng.normal(size=250)
y = rng.normal(size=250)
# NOTE: .random() function is a part of the random object in the numpy library
colors = rng.random(250)
sizes = 1000 * rng.random(250)

# Scatterplot Function
# NOTE: .scatter() is a Function
# NOTE: # alpha sets the opacity (transparency) of the point
plt.scatter(x, y, c=colors, s=sizes, alpha=0.3) 
plt.colorbar() # show color scale
# Save figure
plt.savefig('scatterplot.png')
plt.close()




#  ***************** CHART 2: IRIS DATA SET ***************** 

# Scatter plot from Iris Data
iris = load_iris()
features = iris.data.T # NOTE: T Transposes the data (switch rows & columns)

plt.scatter(features[0], features[1], alpha = 0.4, s=100*features[3], c=iris.target, cmap = 'viridis') # (row, col)
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
plt.savefig('iris-scatter.png')

# 4 different properties observed
# 1. length (position on x axis) - related to sepal length
# 2. Width (position on y axis - related to sepal width
# 3. Size (dot size) - related to the petal width
# 4. Species (color) - related to Iris species