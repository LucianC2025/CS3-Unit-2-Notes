import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# NOTE: if something is depracated it means that in a new version it's been updated, so there is a new way to say something
# NOTE: Data Structures: Data Frames & Series

sns.set_theme(style='ticks', palette='bright') # seaborn's method to set its chart style
# style: darkgrid, whitegrid, dark, white, ticks
# palette: deep, muted, bright, pastel, dark, colorblind

# Matplotlib histogram
# NOTE: Histograms show distribution of values
    # - Each column is a bin
data = np.random.multivariate_normal([0,0], [[5,2], [2,2]], size =2000)
data = pd.DataFrame(data, columns=['x','y'])
for col in 'xy':
    plt.hist(data[col], density = True, alpha = 0.5)
plt.savefig('sns-hist.png', bbox_inches='tight')
plt.close()


# Seaborn KDE
# KDE (kernel density estimation) gives a smooth estimate of distribution of values
sns.kdeplot(data=data, fill=True)
plt.savefig('sns-kdeplot.png', bbox_inches='tight')
plt.close()

# Load a built-in data set 
# Gets stored as a data frame
iris = sns.load_dataset("iris")
print(iris.head())

# NOTE: PAIR PLOT: visualize multi-dimensional data
# hue is the coloring, each species is given its own color
# when its a variable against itself, it generates a histogram
# when its a variable against another variable it generates a scatter plot
sns.pairplot(iris, hue='species', height = 2.5)
plt.savefig('sns-pairplot.png', bbox_inches='tight')
plt.close()