import matplotlib.pyplot as plt
import numpy as np
from config_loader import max_gens

plt.style.use('default')

def draw(y_data: list, weight, benefit):
    fig, ax = plt.subplots()
    plt.title('Weight: {w}, Benefit: {b}'.format(w = weight, b = benefit))
    plt.xlabel('Generaciones')
    plt.ylabel('Fitness')
    len_y = len(y_data)
    x_data = np.arange(0,max_gens)
    y = np.zeros(max_gens)
    y[:len_y] = y_data
    ax.plot(x_data, y, linewidth=2.0)

    plt.xlim(0,len_y)
    plt.ylim(0,10000)
    ax.locator_params("y", nbins = 10)
    ax.locator_params("x", nbins=10)
    
    plt.show()