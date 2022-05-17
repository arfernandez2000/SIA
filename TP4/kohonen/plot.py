import numpy as np
import seaborn as sns
import matplotlib.pylab as plt

def plot_map(data,ylabels="auto",xlabels="auto"):
    ax = sns.heatmap(data, linewidth=1, cbar=True, robust=True, yticklabels=ylabels, xticklabels=xlabels)
    plt.show()