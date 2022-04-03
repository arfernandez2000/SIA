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

    max_y = np.amax(y_data)
    step_y = round(max_y / 10)
    step_x = round(len_y / 10)
    ax.set(xlim=(0, len_y), xticks=np.arange(1, len_y, step_x),
        ylim=(0, max_y+300), yticks=np.arange(1, max_y+10, step_y))
    
    plt.show()